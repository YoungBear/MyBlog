#常见内存泄漏

1. 使用ApplicationContext
2. onDestroy中，remove掉数据源的数据
3. AsyncTask，使用静态内部类，使用WeakReference来保存当前Activity的实例
4. Handler，在onDestroy中，remove掉CallBacks
5. 不要使用静态的Activity或静态View
6. 观察者模式，退出时，remove掉所有Linstener
7. 在onDestroy中remove掉listener

#Dalvik与ART的区别
art上应用启动快，运行快，但是耗费更多存储空间，安装时间长，总的来说ART的功效就是”空间换时间”。

ART: Ahead of Time
Dalvik: Just in Time

什么是Dalvik：Dalvik是Google公司自己设计用于Android平台的Java虚拟机。Dalvik虚拟机是Google等厂商合作开发的Android移动设备平台的核心组成部分之一，它可以支持已转换为.dex(即Dalvik Executable)格式的Java应用程序的运行，.dex格式是专为Dalvik应用设计的一种压缩格式，适合内存和处理器速度有限的系统。Dalvik经过优化，允许在有限的内存中同时运行多个虚拟机的实例，并且每一个Dalvik应用作为独立的Linux进程执行。独立的进程可以防止在虚拟机崩溃的时候所有程序都被关闭。

什么是ART:Android操作系统已经成熟，Google的Android团队开始将注意力转向一些底层组件，其中之一是负责应用程序运行的Dalvik运行时。Google开发者已经花了两年时间开发更快执行效率更高更省电的替代ART运行时。ART代表Android Runtime,其处理应用程序执行的方式完全不同于Dalvik，Dalvik是依靠一个Just-In-Time(JIT)编译器去解释字节码。开发者编译后的应用代码需要通过一个解释器在用户的设备上运行，这一机制并不高效，但让应用能更容易在不同硬件和架构上运行。ART则完全改变了这套做法，在应用安装的时候就预编译字节码到机器语言，这一机制叫Ahead-Of-Time(AOT)编译。在移除解释代码这一过程后，应用程序执行将更有效率，启动更快。

ART优点：

系统性能的显著提升
应用启动更快、运行更快、体验更流畅、触感反馈更及时。
更长的电池续航能力
支持更低的硬件

ART缺点：
更大的存储空间占用，可能会增加10%-20%
更长的应用安装时间


#Android的Pid和Uid
Pid：进程ID。程序一运行系统就会自动分配给进程一个独一无二的PID。进程中止后PID被系统回收，可能会被继续分配给新运行的程序，但是在android系统中一般不会把已经kill掉的进程ID重新分配给新的进程，新产生进程的进程号，一般比产生之前所有的进程号都要大。

Uid：用户ID。只是Android和计算机不一样，计算机每个用户都具有一个Uid，哪个用户start的程序，这个程序的Uid就是那个用户，而Android中每个程序都有一个Uid，默认情况下，Android会给每个程序分配一个普通级别互不相同的 Uid，如果用互相调用，只能是Uid相同才行，这就使得共享数据具有了一定安全性，每个软件之间是不能随意获得数据的。而同一个application 只有一个Uid，所以application下的Activity之间不存在访问权限的问题。

#拷贝文件
```
    public static void copyFile(File source, File dest)
            throws IOException {

        InputStream in = null;
        OutputStream out = null;
        try {
            in = new FileInputStream(source);
            out = new FileOutputStream(dest);
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = in.read(buffer)) != -1) {
                out.write(buffer, 0, bytesRead);
            }
        } finally {
            if (in != null) {
                in.close();
            }
            if (out != null) {
                out.close();
            }
        }
    }
```

#inputStream 转换为String
```
    public static String inputStream2String(InputStream input)
            throws IOException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        int bytesRead;
        while ((bytesRead = input.read()) != -1) {
            baos.write(bytesRead);
        }
        return baos.toString(HTTP.UTF - 8);
    }
```

#格式化日期
```
    public static void formatDate() {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        Date currentDate = new Date();
        String dateString = sdf.format(currentDate);
    }
```

#ListView的优化方案
1. **convertView的复用：**
在getView()方法中，系统就为我们提供了一个复用view的历史缓存对象convertView，当显示第一屏的时候，每一个item都会新创建一个view对象，这些view都是可以被复用的；如果每次显示一个view都要创建一个，是非常耗费内存的；所以为了节约内存，可以在convertView不为null的时候，对其进行复用
2. **缓存item条目的引用——ViewHolder：** 
使用ViewHolder的原因是findViewById方法耗时较大，如果控件个数过多，会严重影响性能，而使用ViewHolder主要是为了可以省去这个时间。通过setTag，getTag直接获取View
3. **ListView中数据的分批及分页加载：**
4. **减少Item View的布局层级**
5. **adapter中的getView方法尽量少使用逻辑**
6. **adapter中的getView方法尽量少做耗时操作**
7. **adapter中的getView方法避免创建大量对象**

#Android常用布局
- LinearLayout
- RelativeLayout
- FrameLayout
- AbsoluteLayout
- TableLayout

#Android四大组件
- **Activity：**一个Activity通常就是一个单独的屏幕
- **Service：** 一个Service 是一段长生命周期的，没有用户界面的程序(start和bind)
- **Broadcast Receiver：**广播接收者(静态注册和动态注册)
- **ContentProvider：**不同程序间共享数据。

#Android数据存储方式
1. 文件
2. SharedPreference
3. SQLite数据库

#Android动画分类
1. **View动画**，也称Tween(补间)动画。可以在一个视图容器内执行一系列简单变换（位置、大小、旋转、透明度）
2. **Frame动画**，即逐帧动画
3. **Property动画**，即属性动画。Android 3.0（API 11）以后才有。

#Android解析XML
1. **SAX解析：** SAX(Simple API for XML) 使用流式处理的方式，它并不记录所读内容的相关信息。它是一种以事件为驱动的XML API，解析速度快，占用内存少。使用回调函数来实现。 缺点是不能倒退。
2. **DOM解析：** DOM(Document Object Model) 是一种用于XML文档的对象模型，可用于直接访问XML文档的各个部分。它是一次性全部将内容加载在内存中，生成一个树状结构,它没有涉及回调和复杂的状态管理。 缺点是加载大文档时效率低下。
3. **使用Pull解析XML：** Pull内置于Android系统中。也是官方解析布局文件所使用的方式。Pull与SAX有点类似，都提供了类似的事件，如开始元素和结束元素。不同的是，SAX的事件驱动是回调相应方法，需要提供回调的方法，而后在SAX内部自动调用相应的方法。而Pull解析器并没有强制要求提供触发的方法。因为他触发的事件不是一个方法，而是一个数字。它使用方便，效率高。

**SAX、DOM、Pull的比较:**

内存占用：SAX、Pull比DOM要好；

编程方式：SAX采用事件驱动，在相应事件触发的时候，会调用用户编好的方法，也即每解析一类XML，就要编写一个新的适合该类XML的处理类。DOM是W3C的规范，Pull简洁。

访问与修改:SAX采用流式解析，DOM随机访问。

访问方式:SAX，Pull解析的方式是同步的，DOM逐字逐句。

#Android MVC模式
[参考](http://www.cnblogs.com/liqw/p/4175325.html)

MVC即Model-View-Controller。M：逻辑模型，V：视图模型，C：控制器。

　　MVC模式下，系统框架的类库被划分为3种：模型（Model）、视图（View）、控制器（Controller）。模型对象负责建立数据结构和相应的行为操作处理。视图对象负责在屏幕上渲染出相应的图形信息展示给用户看。控制器对象负责截获用户的按键和屏幕触摸等事件，协调Model对象和View对象。

　　用户与视图交互，视图接收并反馈用户的动作；视图把用户的请求传给相应的控制器，由控制器决定调用哪个模型，然后由模型调用相应的业务逻辑对用户请求进行加工处理，如果需要返回数据，模型会把相应的数据返回给控制器，由控制器调用相应的视图，最终由视图格式化和渲染返回的数据，对于返回的数据完全可以增加用户体验效果展现给用户。
