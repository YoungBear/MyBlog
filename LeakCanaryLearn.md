#使用LeakCanary源代码检测内存泄漏

square公司出品的Android内存泄漏检测工具[LeakCanary](https://github.com/square/leakcanary)，真的是非常好用，该库已经放在了JCenter上面，在Android Studio下，可以在build.gradle下添加依赖，就可以使用：

```
dependencies {
    ...
    debugCompile 'com.squareup.leakcanary:leakcanary-android:1.5'
    releaseCompile 'com.squareup.leakcanary:leakcanary-android-no-op:1.5'
    testCompile 'com.squareup.leakcanary:leakcanary-android-no-op:1.5'
    ...
}
```

然后，在Application的onCreate()方法中，添加下列代码，就可以使用了：

```
public class MemLeakApplication extends Application {

    @Override
    public void onCreate() {
        super.onCreate();
        if (LeakCanary.isInAnalyzerProcess(this)) {
            // This process is dedicated to LeakCanary for heap analysis.
            // You should not init your app in this process.
            return;
        }
        LeakCanary.install(this);
    }
}
```

在该demo程序中，在Activity中，调用Handler的post方法，延迟执行一个任务，模拟内存泄漏。这样，当退出Activity时，由于匿名内部类Runnable还未执行完，它持有一个MainActivity的强引用，导致MainActivity生命周期已经结束，但是资源不能释放，造成了内存泄漏。

```
public class MainActivity extends Activity {

    private static final String TAG = MainActivity.class.getSimpleName();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // 延迟执行，模拟内存泄漏
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                Log.d(TAG, "Hello");
            }
        }, 60 * 1000);
    }
}
```

当发生内存泄漏的时候，会弹出Dialog，LeakCanary工具会在/storage/sdcard/Download/<package-name>/目录下生成对应的xxxpending.hprof的pending文件，工具会对内存泄漏进行分析，分析成功后，会在通知栏弹出消息，这时候，对应目录下会变成xxx.hprof文件和xxx.hprof.result文件。可以点击Leaks图标或者使用adb shell命令查看具体分析情况。

`adb shell am start -n <package-name>/com.squareup.leakcanary.internal.DisplayLeakActivity`

![这里写图片描述](http://img.blog.csdn.net/20170125172843602?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

但是，有的时候，我们需要对LeakCanary工具的源代码进行修改，以满足我们的需求，所以，接下来，就学习下在已有的AS工程使用LeakCanary工具源代码进行内存泄漏检测分析。

第一步，将LeakCanary源代码clone下来:

`git clone git@github.com:square/leakcanary.git`

第二步，进入leakcanary目录：`cd leakcanary`，然后将应用放在该目录下，本例以我平常的练习应用[Hello](https://github.com/YoungBear/Hello)为例：`git clone https://github.com/YoungBear/Hello.git`。

第三步，修改leakcanary的`settings.gradle`，即`Project Settings`，将`include ':leakcanary-sample'`注释掉，然后添加`include ':Hello:app'`。由于Hello还有一个库mylibrary，所以将`include 'Hello:mylibrary'`也添加到settings文件中。

```
//leakcanary/settings.gradle
include ':leakcanary-watcher'
include ':leakcanary-analyzer'
include ':leakcanary-android'
include ':leakcanary-android-no-op'
include 'Hello:mylibrary'
include ':Hello:app'
//include ':leakcanary-sample'
```
这时候，可以在leakcancary目录下的.gitignore文件中，添加Hello目录，即git忽略Hello目录下的所有文件，这样的话，我们就可以自己修改leakcanary库的源代码了，并且可以提交到远程库。

```
//leakcanary/.gitignore
...
# Hello
Hello
```

第四步，由于mylibrary在工程中的路径变化了，所以需要将`leakcanary/Hello/app/build.gradle`中的dependencies依赖`compile project(':mylibrary')`<font color=red>**改为**</font>`compile project(':Hello:mylibrary')`。

第五步，在`leakcanary/Hello/app/build.gradle`添加dependencies依赖：`compile project(':leakcanary-android')`。

第五步，使用Android Studio，File->New->Import Project...，选择leakcanary目录下的build.gradle文件，点击OK。顺利的话，会导入成功。

![这里写图片描述](http://img.blog.csdn.net/20170125172746351?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

接下来，就和使用jCenter时候一样了，修改Application即可。

另外，可以通过monkey test来指定包名做测试：

`adb shell monkey -p com.example.hello -s 500 -v 100000`

该命令会每隔500ms执行一个随机动作，共执行10万次。在实际的项目中，这个数量可以更大。当monkey结束后，可以查看内存泄漏情况。

`adb shell am start -n com.example.hello/com.squareup.leakcanary.internal.DisplayLeakActivity`

我将Hello工程的memory leak 学习上传到github上了，可以clone下来，然后切换到br_leakcanary_source_learn分支：

`https://github.com/YoungBear/Hello.git`

`git checkout remotes/origin/br_leakcanary_source_learn`

至此，我们就可以根据需要，修改leakcanary的源代码了，也可以学习其原理。

todo：

专门用一个project，来分析常见的内存泄漏情况。





