##StrictMode

Android 2.3(API Level 9) 提供了一个称为严苛模式(StrictMode)的调试特性，Google称该特性已经使数百个Android上的Google应用程序受益。那它都做了什么呢？它将报告与线程与虚拟机相关的策略违例。一旦检测到策略违例(policy violation)，你将获得警告，其包含了一个栈trace显示你的应用在何处发生违例。你可以强制用警告代替崩溃(crash)，也可以仅将警告计入日志，让你的应用继续执行。

官方文档：https://developer.android.com/reference/android/os/StrictMode.html

StrictMode is a developer tool which detects things you might be doing by accident and brings them to your attention so you can fix them.

StrictMode意思为严格模式，是用来检测程序中违例情况的开发者工具。

StrictMode is most commonly used to catch accidental disk or network on the application's main thread, where UI operations are received and animations take place.

最常用的场景就是检测主线程中本地磁盘和网络读写等耗时的操作。

Keeping disk and network operations off the main thread makes for much smoother, more responsive applications. By keeping your application's main thread responsive, you also prevent ANR dialogs from being shown to users.

在子线程做磁盘和网络操作，可以让应用更加平滑，及时响应。这样也可以避免ANR。



用严格模式，系统检测出主线程违例的情况会做出相应的反应，如日志打印，弹出对话框亦或者崩溃等。换言之，严格模式会将应用的违例细节暴露给开发者方便优化与改善。

注意：我们只需要在app的开发版本下使用 StrictMode，线上版本避免使用 StrictMode，随意需要通过 诸如 DEVELOPER_MODE 这样的配置变量来进行控制。

StrictMode通过策略方式来让你自定义需要检查哪方面的问题。主要有两种策略：

###两种策略
1. 线程策略(ThreadPolicy)
2. 虚拟机策略(VMPolicy)

####ThreadPolicy
线程策略检测的内容有：

- 自定义的耗时调用，使用detectCustomSlowCalls()开启
- 磁盘读取操作，使用detectDiskReads()开启
- 磁盘写入操作，使用detectDiskWrites()开启
- 网络操作，使用detectNetwork()开启

####VMPolicy
虚拟机策略检测的内容有：

- Activity泄漏，使用detectActivityLeaks()开启
- 未关闭的Closable对象泄漏，使用detectLeakedClosableObjects()开启
- 泄露的Sqlite对象，使用detectLeakedSqlLiteObjects()开启
- 检测实例数量，使用setClassInstanceLimit()开启

###如何使用StrictMode

严格模式的开启可以放在Application或者Activity以及其他组件的onCreate方法。为了更好地分析应用中的问题，建议放在Application的onCreate方法中。

```
    if (IS_DEBUG && SDK_INT >= GINGERBREAD) {
      StrictMode.setThreadPolicy(new StrictMode.ThreadPolicy.Builder() //
              .detectAll() //
              .penaltyLog() //
              .penaltyDeath() //
              .build());

      StrictMode.setVmPolicy(new StrictMode.VmPolicy.Builder()
              .detectAll()
              .penaltyLog()
              .build());
    }

```

严格模式需要在debug模式开启，不要在release版本中启用。

同时，严格模式自API 9 开始引入，某些API方法也从 API 11 引入。使用时应该注意 API 级别。

如有需要，也可以开启部分的严格模式。

###查看结果

严格模式有很多种报告违例的形式，但是想要分析具体违例情况，还是需要查看日志，终端下过滤StrictMode就能得到违例的具体stacktrace信息。

`adb logcat | grep StrictMode`


###**检测内存泄漏**

通常情况下，检测内存泄露，我们需要使用MAT对heap dump 文件进行分析，这种操作不困难，但也不容易。使用严格模式，只需要过滤日志就能发现内存泄露。

这里以Activity为例说明，首先我们需要开启对检测Activity泄露的违例检测。使用上面的detectAll或者detectActivityLeaks()均可。其次写一段能够产生Activity泄露的代码。

```
public class LeakyActivity extends Activity{
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        MyApplication.sLeakyActivities.add(this);
    }
}
```
MyApplication中关于sLeakyActivities的部分实现

```
public class MyApplication extends Application {
  public static final boolean IS_DEBUG = true;
    public static ArrayList<Activity> sLeakyActivities = new ArrayList<Activity>();

}
```

当我们反复进入LeakyActivity再退出，过滤StrictMode就会得到这样的日志

```
E/StrictMode( 2622): class com.example.strictmodedemo.LeakyActivity; instances=2; limit=1
E/StrictMode( 2622): android.os.StrictMode$InstanceCountViolation: class com.example.strictmodedemo.LeakyActivity; instances=2; limit=1
E/StrictMode( 2622):    at android.os.StrictMode.setClassInstanceLimit(StrictMode.java:1)

```

在我的demo中，使用[LeakCanary](https://github.com/square/leakcanary "")官方的内存泄漏sample，即在Activity的onCreate方法中，使用匿名内部类，启动一个AsyncTask任务，这样，当Activity执行到onDestry的时候，该任务并没有停止，并且保存着一个该Activity的强引用，这样就会导致内存泄漏。

```
    private void startAsyncTask() {
        // This async task is an anonymous class and therefore has a hidden reference to the outer
        // class MainActivity. If the activity gets destroyed before the task finishes (e.g. rotation),
        // the activity instance will leak.
        new AsyncTask<Void, Void, Void>() {
            @Override protected Void doInBackground(Void... params) {
                // Do some slow work in background
                SystemClock.sleep(20000);
                return null;
            }
        }.execute();
    }
```

```
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_strict_mode);
        ButterKnife.bind(this);

        enabledStrictMode();
    }

    private void enabledStrictMode() {
        if (IS_DEBUG && SDK_INT >= GINGERBREAD) {
            StrictMode.setThreadPolicy(new StrictMode.ThreadPolicy.Builder() //
                    .detectAll() //
                    .penaltyLog() //
                    .penaltyDeath() //
                    .build());

            StrictMode.setVmPolicy(new StrictMode.VmPolicy.Builder()
                    .detectAll()
                    .penaltyLog()
                    .build());
        }
    }

    @OnClick(R.id.async_task)
    public void onClick() {
        startAsyncTask();
    }
```

操作：进入StrictModeActivity中，点击按钮，然后在旋转屏幕，这时候Activity会重启，onDestroy方法执行了，但是由于匿名内部类仍然保留着Activity的一个强引用，导致资源不能释放，就多了一个Activity实例，造成了内存泄漏。通过`adb logcat | grep StrictMode`，可以得到相关的log：

```
01-10 17:16:35.501 3778-3778/com.example.hello E/StrictMode: class com.example.hello.activity.StrictModeActivity; instances=2; limit=1
        android.os.StrictMode$InstanceCountViolation: class com.example.hello.activity.StrictModeActivity; instances=2; limit=1
        at android.os.StrictMode.setClassInstanceLimit(StrictMode.java:1)

```

这样，开发者就可以定位到这个Activity,去优化或者解决内存泄漏的问题。

Demo地址：

https://github.com/YoungBear/Hello/blob/master/app/src/main/java/com/example/hello/activity/StrictModeActivity.java

参考：

http://droidyue.com/blog/2015/09/26/android-tuning-tool-strictmode/
http://blog.csdn.net/brokge/article/details/8543145