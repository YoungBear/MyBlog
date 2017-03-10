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
````

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






















