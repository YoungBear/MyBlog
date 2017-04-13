#App研发录 读书笔记

##Activity的onCreate()方法中做以下三件事情：

1. initVariables 初始化变量
2. initViews 初始化组件
3. loadDatas 加载数据


##6.1 Java语法相关异常
###6.1.1 空指针 NullPointException

###6.1.2 角标越界
关键字：

1. indexOutOfBoundsException
2. StringIndexOutOfBoundsException
3. ArrayIndexOutOfBoundsException

###6.1.3 试图调用一个空对象的方法
关键字：

Attempt to invoke virtual method on a null object reference

###6.1.4 类型转换异常
关键字：

ClassCastException: classA cannot be cast to classB

这类Crash都是由于强制类型转换导致的，如下所示：

```
Object x = new Integer(0);
String str = (String) x;
```

折就会抛出ClassCastException的异常了。

解决方案是，使用安全类型转换函数，参见本书第1章中1.6节介绍的类型安全安全转换函数。在把字符串转换为整数、小数或布尔类型时，我们要为其制定<font color=red>转换失败时的默认值。</font>否则，就会得到一个空值，放到哪里使用都会崩溃。

Tips: from 阿里巴巴JAVA开发手册

ArrayList的subList结果不可强转成ArrayList，否则会抛出ClassCastException异常: java.util.RandomAccessSubList cannot be cast to java.util.ArrayList;

<font color=red>说明</font>：subList返回的是ArrayList的内部类SubList，并不是ArrayList，而是ArrayList的一个视图，对于SubList子列表的所有操作最终会反映到原列表上。

在subList场景中，**高度注意**对原集合元素个数的修改，会导致子列表的遍历、增加、删除均产生ConcurrentModificationException 异常。


###6.1.5 数字转换错误

NumberFormatException

在数据类型转换过程中，如果转换不成功，一般抛出ClassCastException的异常。只有一个例外情况，当字符型转换为数字失败时，Android系统会抛出NumberFormatException异常，如下所示：

```
String abc = "123xxx45";
int result = Integer.parseInt(abc);
```

这种情况多发生在服务器返回数据，没有按照约定返回整数而是字符串，客户端必须事先考虑到这种情况，如果转换失败，必须有默认值而不是直接就崩溃了。

###6.1.6 声明数组时长度为-1

NegativeArraySizeException

eg.

```
String[] arg1 = new String[args.length - 1];
```
当args数组中没有元素时，就会出现int[-1]的场景。

###6.1.7 遍历集合同时删除其中元素

ConcurrentModificationException

```
        HashMap<Integer, String> map = new HashMap<>();
        for (int i = 0; i < 10; i++) {
            map.put(i, "value " + i);
        }
        for (Map.Entry<Integer, String> entry : map.entrySet()) {
            Integer key = entry.getKey();
            if (key % 2 == 0) {
                map.remove(key);
            }
        }
```

遍历一个集合时不能删除该集合中的元素。

解决方案，需要再定义一个列表集合delList，用来保存需要删除的对象。

```
    public static void concurrent1() {
        HashMap<Integer, String> map = new HashMap<>();
        for (int i = 0; i < 10; i++) {
            map.put(i, "value " + i);
        }

        List delList = new ArrayList<Integer>();

        for (Map.Entry<Integer, String> entry : map.entrySet()) {
            Integer key = entry.getKey();
            if (key % 2 == 0) {
                delList.add(key);
            }
        }

        for (int i = 0; i < delList.size(); i++) {
            map.remove(delList.get(i));
        }

    }
```

还有另一种产生这种崩溃的情况，那就是在多个线程中删除同一个集合中的元素。

如下列代码所示，vector是一个集合，我们建立了两个线程，线程1对其进行遍历，线程2对其进行插入操作。由于这两个线程同时在执行，所以就会产生ConcurrentModificationException的异常了:

```
    static ArrayList<Integer> list = new ArrayList<>();

    public static void testScenario2() {
        for (int i = 0; i < 100; i++) {
            list.add(i);
        }

        Thread1 thread1 = new Thread1();
        thread1.start();

        Thread2 thread2 = new Thread2();
        thread2.start();

    }

    static class Thread1 extends Thread {
        @Override
        public void run() {
            while (true) {
                Iterator<Integer> iterator = list.iterator();
                while (iterator.hasNext()) {
                    System.out.println(iterator.next());
                }
            }
        }
    }

    static class Thread2 extends Thread {
        @Override
        public void run() {
            while (true) {
                for (int j = 101; j < 200; j++) {
                    list.add(j);
                }
            }
        }
    }
```

ArrayList继承自AbstractList，这是一个迭代器，所有继承自AbstractList的集合类，都是线程不安全的。

相应的解决方案是，将ArrayList换为CopyOnWriteArrayList，这是一个线程安全的集合类。

Tips：

不要在foreach循环里进行元素的remove/add操作。remove元素请使用Iterator方式，如果并发操作，需要对Iterator对象加锁。

###6.1.8 比较器使用不当

Comparison method violates its general contract!

<font color=red>没有处理相等的情况</font>，实际使用中可能会出现异常：

```
    public static void comparatorTest() {
        new Comparator<Student>() {
            @Override
            public int compare(Student o1, Student o2) {
                return o1.getId() > o2.getId() ? 1 : -1;
            }
        };
    }
```

方案，加上相等情况的处理。

```
    public static void comparatorTest() {
        new Comparator<Student>() {
            @Override
            public int compare(Student o1, Student o2) {
                int id1 = o1.getId();
                int id2 = o2.getId();
                if (id1 < id2) {
                    return -1;
                } else if (id1 > id2) {
                    return 1;
                } else {
                    return 0;
                }
            }
        };
    }
```

Tips: from 阿里巴巴JAVA开发手册

在JDK7版本以上，Comparator要满足<font color=red>自反性，传递性，对称性</font>，不然Arrays.sort，Collection.sort会报IllegalArgumentException异常。

说明：

1. 自反性：x，y的比较结果和y，x的比较结果相反。
2. 传递性：如果x>y，y>z，则x>z。
3. 对称性：如果x=y，则x，z的比较结果和y，z的比较结果相同。

###6.1.9 当除数为0

java.lang.ArithmeticException:divide by zero

场景：一般在处理视频、音频的duration的时候，获取到duration为0，导致除数为0。

###6.1.10 不能随便使用asList

使用工具类Arrays.asList()把数组转换成集合时，不能使用其修改集合相关的方法，它的add/remove/clear方法会抛出java.lang.UnsupportedOperationException异常。

Arrays.asList()的返回值是java.util.Arrays$ArrayList，是Arrays的一个内部类，而不是java.util.ArrayList。只有java.util.ArrayList实现了add和remove方法，而Arrays$ArrayList并没有实现这两个方法，而直接抛出了UnsupportedOperationException异常。

eg. 导致异常的代码：

```
        String str = "1,2,3,4,5";
        String[] arrayString = str.split(",");
        List<String> testList = Arrays.asList(arrayString);
        testList.remove("1");
```

解决方案：将java.util.Arrays$ArrayList转换成java.util.ArrayList，如下所示：

```
        String str = "1,2,3,4,5";
        String[] arrayString = str.split(",");
        List<String> testList = Arrays.asList(arrayString);
        List<String> arrayList = new ArrayList<>(testList);
        arrayList.remove("1");
```

<font color=red>说明</font>：asList的返回对象是一个Arrays内部类，并没有实现集合的修改方法。Arrays.asList体现的是适配器模式，只是转换接口，后台的数据仍是数组。

```
    public static void arraysTest() {
        String[] str = new String[] {"a", "b"};
        List<String> list = Arrays.asList(str);
//        str[0] = "c";
//        list.add("c");
        for (String element : list) {
            System.out.println(element);
        }
    }
```

第一种情况: `list.add("c");` 运行时异常 UnsupportedOperationException
第二种情况: `str[0] = "c";` str[0]变了，那么list.get(0)也会随之改变。

###6.1.11 ClassNotFoundException

场景：

```
Class.forName("com.company.package.class");
ClassLoader..loadClass("com.company.package.class")
```

//todo 分析具体产生ClassNotFoundExcaption的情况，如Proguard会把一些类混淆了，但是Class.forName()中的参数并没有改变。

###6.1.12 NoClassDefFoundError

当我们在B类中声明一个A类的实例，如下所示：

`ClassA obj = new ClassA();`

但是打包时B和A分别位于不同的dex中，这是如果在A所在的dex中把A类删除了，那么在运行时执行到这句话就会抛出NoClassDefFoundError的异常信息。

通常插件化编程的时候会牵扯出这个异常，因为要使用到DelClassLoader。也许你的项目中没有用到插件化编程但是也有类似的问题，那么就看一下你所使用的第三方SDK吧。

##6.2 Activity相关的异常

###6.2.1 找不到Activity

android.content.ActivityNotFoundException:No Activity found to handle Intent{...}

场景：

URL不是以http开头，代码就会报出异常：

```
Uri uri = Uri.parse("www.baidu.com");
Intent intent = new Intent(Intent.ACTION_VIEW, uri);
startActivity(intent);
```

这类Crash还有一种发生的场景是，当我们要打开SD卡上的一个HTML页面时，没有为Intent指定打开该HTML页面所需要的浏览器，如下所示：

```
Intent intent = new Intent(Intent.ACTION_VIEW,
        Uri.parse("file://sdcard/101.html"));

//此处指定系统自带的浏览器包名和Activity名称
//intent.setClassName("com.android.browser",
         "com.android.browser.BrowserActivity");
startActivity(intent);
```
就是因为指定浏览器的语句被注释了，所以就崩溃了。

还有一个原因，如果是调用百度地图的openBaiduMapNavi方法导致的Crash，有可能是手机没有安装百度地图的客户端，而这个方法就是要打开这个客户端。

解决方案： 判断其是否安装了，没有的话就提示用户有问题要么就干脆不显示。

###6.2.2 不能实例化Activity

java.lang.RuntimeException:Unable to instantiate activity ComponentInfo

这种Crash，通常是因为没有在AndroidManifest.xml清单中注册该Activity，或者在创建完Activity后，修改了包名或者Activity的类名，而配置清单没有修改，造成不能实例化。

如果还不能解决问题，有可能是系统处于异常状态(关机，内存不足)等，导致部件初始化失败。

###6.2.3 找不到Service

java.lang.RuntimeException:Unable to instantiate service

原因：AndroidManifest.xml文件中没有注册，或者有Class.forName("Class1")这样的语句，对于此，ProGuard会将Class1混淆，从而就是找不到Class1这个类。

###6.2.4 不能启动BroadcastReceiver

Unable to start receiver

情形：从Receiver启动一个Activity，必须指定Intent.FLAG_ACTIVITY_NEW_TASK，不过不建议这么做。

###6.2.5 startActivityForResult 不能回传

Failure delivering result ResultInfo

这类问题是startActivityForResult导致的。就是说传回来的key是A，但是却按照B这个key来取值。

###6.2.6 猴急的Fragment

Fragment not attached to Activity

发生这个异常，是因为Fragment在还没有Attach到Activity时，调用了诸如getResource()这样的方法。

解决方案：在获取资源前，先使用isAdded()方法进行判断。isAdded()方法是Android系统提供的，它只有在Fragment被添加到所属的Activity后才会返回true。

##6.3 序列化相关的异常

###6.3.1 实体对象不支持序列化

Paracelable encountered IOException writing serializable object(name=xxx)...

###6.3.2 序列化时未指定ClassLoader

BadParcelableException: ClassNotFoundException when unmarshalling...

###6.3.3 反序列化时发现类找不到：被ProGuard混淆导致的崩溃

Parcelable encountered ClassNotFoundException reading a Serializable object...

ProGuard对于Class.forName(className)中的class是无能为力的，它会将这个class混淆得面目全非，于是在反序列化这个类的时候却发现找不到这个类了，自然就会抛出这种异常信息了。相应的解决方案是，<font color=red>在ProGuard文件中keep这个类</font>。

###6.3.4 反序列化时发现类找不到：传入畸形数据

Parcelable encountered ClassNotFoundException reading a Serializable object(name=xxx)

这是一个最近发现的安全漏洞。

由于在App中使用了getSerializableExtra()的API，App开发人员没有对传入的数据做异常判断，别有企图的人可以通过传入畸形数据，导致本地拒绝服务。

###6.3.5 反序列化时出错

Could not read input channel file descriptors from parcel...

出现这个异常，一般是因为Intent传递的数据太大了。

##6.4 列表相关的异常

###6.4.1 Adapter数据源变化但是没通知ListView
异常中的关键字：

The content of the adapter has changed but ListView did not receive a notification. Make sure the content of your adapter is not modified from a background thread, but only from the UI thread.

上述异常信息的大体意思是，adapter的内容变化了，但是相应的ListView并不知情。请保证adapter的数据在主线程中进行修改！

无论何时何地，只要修改了adapter中集合数据的值，就要马上调用notifyDataSetChanged方法，以确保列表同步更新。

###6.4.2 ListView滚动时点击刷新按钮后崩溃

IndexOutOfBoundException:Invalid index 30, size is 1 at...

ListView滚动的时候，表示它已经获取了adapter的getCounts()，可能是30，也可能更大。回调用getView()，这个时候将数据clear掉了。当然会报IndexOutOfBoundException:Invalid index 30, size is 1。这个1是那个header，因为我们使用的是HeaderViewListAdapter。

这种Crash的解决方案是，ListView滚动的时候，将刷新按钮设置为不可点击。

###6.4.3 AbsListView的obtainView返回空指针

java.lang.NullPointerException at android.widget.AbsListView.obtainView...

导致空指针的罪魁祸首是AbsListView的obtainView方法获取不到View，究竟原因是getView方法在某些时候返回null。

解决方案很简单，getView的第二个参数convertView是不会为null的，在getView返回值的时候，判断一下是否为null，如果为null，则返回convertView。

###6.4.4 Adapter数据源变化但是没有调用notifyDataSetChanged

The application's PagerAdapter changed the adapter's contents without calling PagerAdapter#notifyDataSetChanged

PagerAdapter对于nofifyDataSetChanged()和getCount()的执行顺序是非常严格的，系统跟踪count的值，如果这个值和getCount返回的值不一致，就会抛出这个异常。所以为了保证getCount总是返回一个正确的值，那么在初始化ViewPager时，应先给adapter初始化内容后再将该adapter传给ViewPager，如果不这样处理，在更新adapter的内容后，应该调用一下Adapter的notifyDataSetChanged方法。

##6.5 窗体相关的异常

###6.5.1 窗口句柄泄漏

android.view.WindowLeaked:Activity xxx has leaked window com.android.internal.policy.impl.PhoneWindow$DecorView{xxxx} that was originally added here.

Activity已经销毁，但是在它基础上创建的Dialog对话框还在，窗口句柄泄漏，未能及时销毁。

解决方案：重写Activity的onDestroy方法，在方法中调用dismiss来解除对Dialog等的引用。

###6.5.2 View not atached to window manager

java.lang.IllegalArgumentException:View not attached to window manager at.

场景：在一个耗时的线程任务，在任务开始的时候显示一个对话框，然后当任务完成了再销毁对话框，在此期间如果Activity因为某种原因被杀掉且又重新启动了，那么当Dialog调用dismiss方法的时候WindowManager检查发现Dialog所属的Activity已经不存在了，所以会报View not attached to window manager。

###6.5.3 窗体在不恰当的时候获取了焦点

java.lang.NullPointerException:android.widget.PopupWindow$PopupViewContainer dispatchKeyEvent.

这个问题是因为在PopupWindow显示之前，就把焦点赋予了它，结果当然会Crash了。

###6.5.4 token null is not for an application

android.view.WindowManager$BadTokenException: Unable to add window -- token null is not for an application

原因：创建Dialog的时候，使用的Context不对，不能接受ApplicationContext，只有一个Activity才能添加一个窗体。

###6.5.5 permission denied for this window type

Android.view.WindowManager$BadTokenException:Unable to add window android.view.ViewRootImpl$W@411da608 -- permission denied for this window type

在使用WindowManager.LayoutParams.TYPE_SYSTEM_ALERT 涉及window type 权限问题。

需要添加权限：

```
<uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />
<uses-permission android:name="android.permission.SYSTEM_OVERLAT_WINDOW" />
```

前者允许应用使用TYPE_SYSTEM_ALERT来打开窗口，并将窗口显示于其他应用的顶端；后者允许使用窗体覆盖在window上。

###6.5.6 is your activity running

###6.5.7 添加窗体失败

Adding window failed at...

###6.5.8 AlertDialog.resolveDialogTheme

###6.5.9 The specified child already has a parent

The specified child already has parent. You must call removeView() on the child's parent first.

###6.5.10 子线程不能修改UI

android.view.ViewRootImpl$CalledFromWrongThreadException: Only the original thread that created a view hierarchy can touch its views...

###6.5.11 不能在子线程操作AlertDialog 和 Toast

Can't create handler inside thread that has not called Looper.prepare()

##6.6 资源相关的异常

###6.6.1 Resources$NotFoundException

###6.6.2 StackOverflowError

发生这种事情，主要是因为Layout布局结构嵌套层次太深。

###6.6.3 UnsatisfiedLinkError

java.lang.UnsatisfiedLinkError:dalvik.system.PathClassLoader[DexPathList[...]]

遇到这个Crash，肯定是so格式的文件没有加载到。

###6.6.4 InflateException 之 FileNotFoundException

资源没有回收，建议手动回收。

###6.6.5 InflateException 之缺少构造器

自定义View的时候，没有重写两个参数的构造函数。

###6.6.6 InflateException 之 style 与 android:textStyle 的区别

### 6.6.7 TransactionTooLargeException

不要将大量数据传入Binder。

##6.7 系统碎片化相关的异常

这类Crash由两部分组成：

1. Android系统版本不同
2. ROM不同

###6.7.1 NoSuchMethodError

java.lang.NoSuchMethodError

一般查看下不同版本的方法有什么不同。

###6.7.2 RemoteViews

android.widget.RemoteViews$RefiectionAction.writeToParcel(RemoteViews.java :763)

###6.7.3 pointerIndex out of range

###6.7.4 SecurityException之一：Intent中图片太大

在跳转Activity的过程中携带的extras中有Bitmap，应尽量减少要传输的图片的体积，或者通过保存图片到SD卡中或者通过URI方式传递图片参数；否则，图片太大，就会报上述的异常信息。

###6.7.5 SecurityException 之二：动态加载其他apk的Activity

###6.7.6 SecurityException 之三：No permission to modify thread

动态获取权限

###6.7.7 view的getDrawingCache()返回null

当背景图太大，超过了屏幕的大小，就会导致getDrawingCache()返回的结果为null，从未抛出NullPointException的异常。

###6.7.8 DeadObjectException

###6.7.9 Android 2.1 不支持SSL

Android 2.1版本不支持SSL，所以发起https的请求会导致崩溃。解决方案是，在调用https请求的时候，要实现判断Android系统的版本，版本过低要提示用户不能进行操作。

###6.7.10 ViewFlipper 引发的血案

在Activity中使用ViewFlipper控件，进行横竖屏切换操作时，就会发生这种异常。这是由于onDetachedFromWindow()在onAttachedToWindow()之前被调用所致。

解决方案：重写ViewFlipper的onDetachedFromWindow()方法。

###6.7.11 ActivityNotFoundException

Android 4.0以上把原来的打开网络设置方式舍弃了。

###6.7.12 Android 2.2 不支持xlargeScreens

###6.7.13 Package manager has died

解决方案：每次获取PakcageManager的时候用try...catch...捕获。

###6.7.14 SpannableString与富文本字符串

try -- catch

###6.7.15 Can not perform this action after onSaveInstanceState

###6.7.16 Service Intent must be explicit

Android在升级到5.0系统后会产生这样的崩溃。直接通过action启动Service，就会导致这个问题，所以我们必须指定component或package才能避免这类问题。(建议使用显式的方法启动Service)。

##6.8 SQLite相关的异常

###6.8.1 No transaction is active

在事务中，逐条循环插入大量数据时会导致这类崩溃。Android中在SQLite插入数据的时候默认一条语句就是一个事务，有多少条数据就有多少次磁盘操作，而且不能保证所有数据都能同时插入。

解决方案：使用SQLite提供的批量插入语法，一次性地把这些数据都插入到数据库中。

###6.8.2 Cursor没有关闭

android.database.CursorWindowAllocationException:Cursor window allocation of 2048kb failed.

###6.8.3 数据库被锁定

android.database.sqlite.SQLiteDatabaseLockedException:database is locked

在多个线程中创建多个连接时，就会抛出这个异常。

###6.8.4 试图再打开已经关闭的对象

java.lang.IllegalStateException:attempt to re-open an already closed object

###6.8.5 文件加密了或者无数据库

SQLiteDatabaseCorruptException:file is encrypted or is not a database

###6.8.6 WebView 中SQLite缓存导致的崩溃

###6.8.7 磁盘读写错误

android.database.sqlite.SQLiteDiskIOException:disk I/O error

dbHelper 只有在创建数据库、进行事务处理时才会锁住数据库。默认情况下dbHelper会缓存DB实例，执行类似于getWritableDatabase的操作是立即返回的，并不会上锁。

disk I/O error 这类异常的抛出，是因为多线程修改DB，比如一个线程在写数据，另一个线程却在删除数据。

###6.8.8 android_metadata 表不存在

###6.8.9 android_metadata表中的locale字段

###6.8.10 数据库或磁盘满了

##6.9 不明觉厉的异常

###6.9.1 内存溢出

OutOfMemoryException

方案：

1. largeHeap
2. 解决内存泄漏问题

###6.9.2 Verify Failed

##6.10 其他情况的异常

###6.10.1 TimeoutException

###6.10.2 JSON解析异常

###6.10.3 JSONArray 在初始化时为空

###6.10.4 第三方SDK抛出的Crash

###6.10.5 两个不同类型的View有相同的id

在Activity中，确定要保存/恢复一个View的状态的时候，一定要保证它们有唯一的id，因为Android内部使用id作为保存、恢复状态时使用的key，否则就会发生一个覆盖另一个的悲剧。

###6.10.6 LayoutInflater.from().inflate()使用不当导致的崩溃

###6.10.7 ViewGroup中的玄机

###6.10.8 Monkey点击过快导致的崩溃

###6.10.9 图片缩放很多倍

###6.10.10 图片宽高为0

###6.10.11 不能重复添加组件

#ProGuard

##7.3 如何写一个ProGuard文件

###7.3.1 基本混淆

**ProGuard常用语法:**

- `-keep` 不混淆某些类
- `-keepclassmember` 不混淆类的成员
- `-keepclasseswithmembers` 不混淆类及其成员
- `-keepnames` 不混淆类及其成员名
- `-keepclassmembernames` 不混淆类的成员名
- `-keepclasseswithmembernames` 不混淆类及其成员名
- `-dontwarn` 不提示warning

**Android的混淆原则：**

- 反射用到的类不混淆
- JNI方法不混淆
- AndroidManifest中的类不混淆，四大组件和Application层下所有的类默认不会进行混淆
- Parcelable的子类和Creator静态成员变量不混淆，否则会产生android.os.BadParcelableException异常
- 使用Gson，fastjson等框架时，所写的JSON对象类不混淆，否则无法将JSON解析成对应的对象
- 使用第三方开源库或者引用其他第三方的SDK包时，需要在混淆文件中加入对应的混淆规则
- 有用到WebView的JS调用也需要保证写的接口方法不混淆

1. 基本指令

先看看google默认混淆文件: \sdk\tools\proguard\proguard-android.txt

```
# \sdk\tools\proguard\proguard-android.txt
# \sdk\tools\proguard\proguard-android-optimize.txt
# This is a configuration file for ProGuard.
# http://proguard.sourceforge.net/index.html#manual/usage.html

# 指定混淆时使用的算法，后面的参数是一个过滤器
# 这个过滤器是谷歌推荐的算法，一般不改变
-optimizations !code/simplification/arithmetic,!code/simplification/cast,!field/*,!class/merging/*
# 代码混淆压缩比，在0-7之间，默认为5，一般不需要改
-optimizationpasses 5
# 优化时允许访问并修改有修饰符的类和类的成员
# 这项配置是设置是否允许改变作用域的。使用这项配置之后可以提高优化的效果。
# 但是，如果你的代码是一个库的话，最好不要配置这个选项，因为它可能会导致一些private变量被改成public
-allowaccessmodification

# 混淆时不使用大小写混合，混淆后的类名为小写
-dontusemixedcaseclassnames
# 指定不去忽略非公共的库的类
-dontskipnonpubliclibraryclasses
# 输入混淆日志
-verbose

# Optimization is turned off by default. Dex does not like code run
# through the ProGuard optimize and preverify steps (and performs some
# of these optimizations on its own).
# 不进行优化
-dontoptimize
# 不进行预检验
-dontpreverify
# Note that if you want to enable optimization, you cannot just
# include optimization flags in your own project configuration file;
# instead you will need to point to the
# "proguard-android-optimize.txt" file instead of this one from your
# project.properties file.

# 不混淆注解（注解不能被混淆）
-keepattributes *Annotation*
# 不混淆指定类
-keep public class com.google.vending.licensing.ILicensingService
-keep public class com.android.vending.licensing.ILicensingService

# For native methods, see http://proguard.sourceforge.net/manual/examples.html#native
# 保留所有的本地native方法不被混淆
-keepclasseswithmembernames class * {
    native <methods>;
}

# keep setters in Views so that animations can still work.
# see http://proguard.sourceforge.net/manual/examples.html#beans
# 不混淆继承View的所有类的set和get方法
-keepclassmembers public class * extends android.view.View {
   void set*(***);
   *** get*();
}

# We want to keep methods in Activity that could be used in the XML attribute onClick
# 不混淆继承Activity的所有类的中的参数类型为View的方法，从而在layout里面编写onClick就不会被影响
-keepclassmembers class * extends android.app.Activity {
   public void *(android.view.View);
}

# For enumeration classes, see http://proguard.sourceforge.net/manual/examples.html#enumerations
# 不混淆枚举类型的values和valueOf方法
-keepclassmembers enum * {
    public static **[] values();
    public static ** valueOf(java.lang.String);
}

# 不混淆继承Parcelable的所有类的CREATOR，保留Parcelable序列化的类不被混淆
-keepclassmembers class * implements android.os.Parcelable {
  public static final android.os.Parcelable$Creator CREATOR;
}

# 不混淆R类中所有static字段
-keepclassmembers class **.R$* {
    public static <fields>;
}

# The support library contains references to newer platform versions.
# Don't warn about those in case this app is linking against an older
# platform version.  We know about them, and they are safe.
# 忽略兼容库的所有警告
-dontwarn android.support.**

# Understand the @Keep support annotation.
# 不混淆指定的类及其类成员
-keep class android.support.annotation.Keep

# 不混淆使用注解的类及其类成员
-keep @android.support.annotation.Keep class * {*;}

# 不混淆所有类及其类成员中的使用注解的方法
-keepclasseswithmembers class * {
    @android.support.annotation.Keep <methods>;
}

# 不混淆所有类及其类成员中的使用注解的字段
-keepclasseswithmembers class * {
    @android.support.annotation.Keep <fields>;
}

# 不混淆所有类及其类成员中的使用注解的初始化方法
-keepclasseswithmembers class * {
    @android.support.annotation.Keep <init>(...);
}
```

针对Android的混淆原则，分别给出下面的混淆规则：
```
# 代码中使用了反射，需要保证类名，方法不变， 不然混淆后， 就反射不了
-keepattributes Signature
-keepattributes EnclosingMethod

# 使用GSON、fastjson等JSON解析框架所生成的对象类
# 生成的bean实体对象,内部大多是通过反射来生成, 不能混淆
# 不混淆所有的com.clock.bean包下的类和这些类的所有成员变量
-keep class com.clock.bean.**{*;}

# AndroidManifest中的类不混淆，四大组件和Application层下所有的类默认不会进行混淆
-keep public class * extends android.app.Activity
-keep public class * extends android.view.View
-keep public class * extends android.app.Application
-keep public class * extends android.app.Service
-keep public class * extends android.content.BroadcastReceiver

# 不混淆Serializable接口的子类中指定的某些成员变量和方法
-keepclassmembers class * implements java.io.Serializable {
    static final long serialVersionUID;
    private static final java.io.ObjectStreamField[] serialPersistentFields;
    private void writeObject(java.io.ObjectOutputStream);
    private void readObject(java.io.ObjectInputStream);
    java.lang.Object writeReplace();
    java.lang.Object readResolve();
}

# 引用了第三方开源框架或继承第三方SDK情况比较复杂，
# 开发过程中使用了知名成熟的开发框架都会有给出它的混淆规则，
# 第三方的SDK也一样。这里以okhttp框架和百度地图sdk为例
#okhttp框架的混淆
-dontwarn com.squareup.okhttp.internal.http.*
-dontwarn org.codehaus.mojo.animal_sniffer.IgnoreJRERequirement
-keepnames class com.levelup.http.okhttp.** { *; }
-keepnames interface com.levelup.http.okhttp.** { *; }
-keepnames class com.squareup.okhttp.** { *; }
-keepnames interface com.squareup.okhttp.** { *; }

#百度sdk的混淆
-keep class com.baidu.** {*;}
-keep class vi.com.** {*;}
-dontwarn com.baidu.**

# 有用到WEBView的JS调用接口，需加入如下规则
-keepclassmembers class fqcn.of.javascript.interface.for.webview {
   public *;
}
# //保持WEB接口不被混淆 此处xxx.xxx是自己接口的包名
-keep class com.xxx.xxx.** { *; }
```

##12.7 Android应用开发人员所需要精通的20个技能点：

1. Activity相关。App应用开发，以Activity使用最多，涉及LaunchMode，onSaveInstanceState，生命周期等技术。
2. Fragment相关技术。
3. 序列化技术。有Parcelable和Serializable两种。前者是基于Service的，后者是基于Bundle的，二者的实现原理不同，但是达到的效果差不多。
4. ImageLoader的原理和使用。了解多个开源库如UIL,Glide,Picasso,Fresco
5. fastJSON或GSON的使用。
6. 多线程相关。包括Handler,Looper,ExecutorService等。
7. Adapter和ListView。
8. 用户Cookie设计。需要把登录机制彻底搞清楚，包括在HttpRequest头中夹带Cookie来进行用户身份验证的技术。
9. 网络请求封装。volley,okhttp的二次封装。
10. Android和HTML5的交互。
11. 代码混淆。ProGuard。
12. Android打包机制。Ant,Gradle或者Maven。
13. 线上Crash分析并修复。要具备通过分析Crash信息修复线上Crash的能力。
14. 内存泄漏。包括内存优化、内存泄漏的场景，MAT工具的使用。使用开源工具LeakCanary。
15. 调试工具。包括DDMS、Eclipse或AndroidStudio的调试功能。
16. Monkey机制。
17. 单元测试。
18. Git的高级功能。
19. 插件化编程。
20. 设计模式。对常见的设计模式如工厂，生成器，适配器，代理，策略模式耳熟能详。














