# Android面试题整理



## 1. Android

### 1.1 Android四大组件
[参考](http://www.cnblogs.com/bravestarrhu/archive/2012/05/02/2479461.html)

Android四大基本组件分别是

1. Activity，
2. Service 服务
3. BroadcastReceiver 广播接收器
4. Content Provider 内容提供者


**Activity:**
应用程序中，一个Activity通常就是**一个单独的屏幕**，它上面可以显示一些控件也可以监听并处理用户的事件做出响应。


**Service:** 
一个Service 是一段长生命周期的，**没有用户界面**的程序，可以用来开发如监控类程序。

**BroadcastReceive:**
你的应用可以使用它对外部事件进行过滤只对感兴趣的外部事件(如当电话呼入时，或者数据网络可用时)进行接收并做出响应。广播接收器没有用户界面。

**Content Provider:**
android平台提供了Content Provider使一个应用程序的指定数据集提供给其他应用程序。这些数据可以存储在文件系统中、在一个SQLite数据库、或以任何其他合理的方式。

### 1.2 Activity生命周期
[参考](http://blog.csdn.net/woshimalingyi/article/details/50961380)

![Activity生命周期](http://img.blog.csdn.net/20160323111932870)

`onCreate()->onStart()->onResume()->onPause()->onStop()->onDestroy()`

### 1.3 Service
[参考](http://blog.csdn.net/javazejian/article/details/52709857)
Service的两种方式：

**start**和**bind**。

**startService:**


当其他组件调用startService()方法请求启动Service时，该方法被回调。一旦Service启动，它会在后台独立运行。当Service执行完以后，需调用stopSelf() 或 stopService()方法停止Service。

这种启动的生命周期为：

`onCreate()->onStartCommand()->onDestroy()`

**bindService:**

某个组件通过调用bindService()绑定了Service（系统不会回调onStartCommand()方法），只要该组件与Service处于绑定状态，Service就会一直运行，当Service不再与组件绑定时，该Service将被destroy。

这种的生命周期为：

`onCreate()->onBind()->onUnbind()->onDestroy()`

**什么是IntentService?**

1. IntentService 是继承自 Service 并处理异步请求的一个类，在 IntentService 内有一个工作线程来处理耗时操作。
2. 当任务执行完后，IntentService 会自动停止，不需要我们去手动结束。
3. 如果启动 IntentService多次，那么每一个耗时操作会以工作队列的方式在 IntentService 的 onHandleIntent回调方法中执行，依次去执行，使用串行的方式，执行完自动结束。

### 1.4 Activity 的启动模式LaunchMode
[参考](https://blog.csdn.net/u011959433/article/details/50946544)

**1. standard**
默认启动模式
不管当前栈顶有没有实例，都会新建一个新的实例，将Activity放在栈顶。

**2. singleTop**

**栈顶复用**模式

如果当前栈顶元素是我们需要启动的Activity的一个实例，则这个Activity不会再次被创建，而是先调用onPause()方法，然后再调用onNewIntent方法，onResume(),即onPause()->onNewIntent()->onResume()。

如果当前栈顶没有该Activity的实例，则新建一个实例放在栈顶。

**3. singleTask**

**栈内复用**模式

　　以singleTask模式启动的Activity首先就会寻找自己需要的任务栈，如果没有，就会创建一个，然后把自己给放进栈里面。要是有发现自己需要的任务栈，就会看里面有没有这个Activity的实例，没有的话就在栈顶加入新创的实例，要是有的话就会弹出该实例上面的所有元素，即它上面所有元素都出栈，从而把所需求的实例给推到栈顶。

**4. singleInstance**

**单实例**模式

　　它具备上一个singleTask的所有属性，其次，它只能独自的存在于一个单独的任务栈。即这个task只有这个实例，不允许有别的Activity存在。


### 1.5 Handler机制
[参考](https://blog.csdn.net/guolin_blog/article/details/9991569)

Android UI是线程不安全的，即只能在主线程(UI线程)对UI进行操作。一般的做法是，创建一个Message对象，使用Handler发送出去，然后在Handler的handleMessage()方法中获取刚才发送的Message对象，在这里进行UI操作。这就是Android的异步消息处理机制。

　　异步消息处理线程启动后，会进入一个无限的循环体中，每循环一次，从其内部的消息队列中取出一个消息，然后回调相应的消息处理函数，执行完一个消息后则继续训话。若消息队列为空，线程则会阻塞等待。

　　Android 中**Handler、Message、Looper和MessageQueue**的关系：

　　Looper负责创建一个MessageQueue,然后进入一个无限循环体中不断从该MessageQueue中读取消息，而消息的创建者就是一个或者多个Handler。

**可以在子线程new一个Handler吗？**

不能。

在子线程中创建的Handler是会导致程序崩溃的，提示的错误信息为 `Can't create handler inside thread that has not called Looper.prepare()` 。

因为在Activity的启动代码中，已经在当前UI线程调用了Looper.prepare()和Looper.loop()方法。如果在子线程中实现Handler，则必须手动调用Looper.prepare()和Looper.loop()方法，才能实现异步消息处理。

### 1.6 使用到什么框架

网络访问：okhttp,volley

JSON解析：Gson，fastjson

图片加载：Glide，Picasso，Universal-Image-Loader

### 1.7 了解设计模式吗，项目中用到哪些？

单例模式，观察者模式，工厂模式，策略模式等。

各模式的特点。

单例模式的特点（构造函数私有化，静态的getInstance()方法），手写单例模式(饿汉，懒汉，Double Check，静态内部类)。[参考](https://blog.csdn.net/next_second/article/details/52549953)

### 1.8 了解MVP模式吗

**MVP ，即 Model - Presenter - View。**

**Presenter 交互中间人**

Presenter主要作为沟通 View 和 Model 的桥梁，它从 Model 层检索数据后，返回给 View 层，使得 View 和 Model 没有耦合，也将业务逻辑从View角色上抽离出来。

**View 用户界面**

View通常是指 Activity、Fragment 或者某个 View 控件，它含有一个 Presenter 成员变量。通常 View 需要实现一个逻辑接口，将 View 上的操作会转交给 Presenter 进行实现，最后， Presenter 调用 View 的逻辑接口将结果返回给 View 元素。

**Model 数据的获取**

对于一个结构化的 App 来说， Model 角色主要是提供数据的存取功能。 Presenter 需要通过 Model 层存储，获取数据， Model 就像一个数据仓库。更直白地说， Model 是封装了数据库 DAO 或者网络获取数据的角色，或者两种数据获取方式的集合。

![MVP](http://img.blog.csdn.net/20171125094831024?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

[谷歌官方MVP Demo：todoapp](https://github.com/googlesamples/android-architecture/tree/todo-mvp/)

### 1.9 Touch事件传递流程

[参考1](http://hanhailong.com/2015/09/24/Android-%E4%B8%89%E5%BC%A0%E5%9B%BE%E6%90%9E%E5%AE%9ATouch%E4%BA%8B%E4%BB%B6%E4%BC%A0%E9%80%92%E6%9C%BA%E5%88%B6/)

[参考2](http://www.cnblogs.com/sunzn/archive/2013/05/10/3064129.html)



**基础知识**

(1) 所有Touch事件都被封装成了MotionEvent对象，包括Touch的位置、时间、历史记录以及第几个手指(多指触摸)等。

(2) 事件类型分为ACTION_DOWN, ACTION_UP, ACTION_MOVE, ACTION_POINTER_DOWN, ACTION_POINTER_UP, ACTION_CANCEL，每个事件都是以ACTION_DOWN开始ACTION_UP结束。

(3) 对事件的处理包括三类，分别为**传递**——dispatchTouchEvent()函数、**拦截**——onInterceptTouchEvent()函数、**消费**——onTouchEvent()函数和OnTouchListener

**传递流程**

(1) 事件从Activity.dispatchTouchEvent()开始传递，只要没有被停止或拦截，从最上层的View(ViewGroup)开始一直往下(子View)传递。子View可以通过onTouchEvent()对事件进行处理。

(2) 事件由父View(ViewGroup)传递给子View，ViewGroup可以通过onInterceptTouchEvent()对事件做拦截，停止其往下传递。

(3) 如果事件从上往下传递过程中一直没有被停止，且最底层子View没有消费事件，事件会反向往上传递，这时父View(ViewGroup)可以进行消费，如果还是没有被消费的话，最后会到Activity的onTouchEvent()函数。

(4) 如果View没有对ACTION_DOWN进行消费，之后的其他事件不会传递过来。

(5) OnTouchListener优先于onTouchEvent()对事件进行消费。 上面的消费即表示相应函数返回值为true。

### 1.10 ANR是什么？怎样避免和解决ANR

ANR:Application Not Responding，即应用无响应。

主要原因：**主线程做了耗时的操作**。

原因一般有两种：

(1)当前的事件没有机会得到处理（UI线程正在处理前一个事件没有及时完成或者looper被某种原因阻塞住）

(2)当前的事件正在处理，但没有及时完成

UI线程尽量只做跟UI相关的工作，耗时的工作（数据库操作，I/O，连接网络或者其他可能阻碍UI线程的操作）放入单独的线程处理，尽量用Handler来处理UI thread和thread之间的交互。

**查找ANR的方式：**

导出`/data/data/anr/traces.txt`，找出函数和调用过程，分析代码。

### 1.11 Android注册广播有几种方式? 它们的适用情况是什么?

Android中有两种广播的注册方式：
1. **静态注册**：AndroidManifest.xml配置文件中；
2. **动态注册**：Java代码； 静态注册适用于全局广播；动态注册适用于局部广播；

补充一点：有些广播只能通过动态方式注册，比如时间变化事件、屏幕亮灭事件、电量变更事件，因为这些事件触发频率通常很高，如果允许后台监听，会导致进程频繁创建和销毁，从而影响系统整体性能。

### 1.12 版本适配，各版本有什么新特性，开发要注意的问题？

#### **Android 6.0 ，动态请求权限。**
分为正常权限 和 危险权限。危险权限（如相机，定位，查看手机状态，读写磁盘）需要动态申请。

**所有危险的 Android 系统权限都属于权限组。**
如果应用请求其清单中列出的危险权限，而应用目前在权限组中没有任何权限，则系统会向用户显示一个对话框，描述应用要访问的权限组。对话框不描述该组内的具体权限。
如果应用请求其清单中列出的危险权限，而应用在同一权限组中已有另一项危险权限，则系统会立即授予该权限，而无需与用户进行任何交互。

[参考 权限](https://www.cnblogs.com/liuzhipenglove/p/7102692.html)

#### Android 7.0 FileProvider
[参考](https://blog.csdn.net/next_second/article/details/78585745)

对于面向Android 7.0的应用，Android框架执行的StrictMode API政策禁止在您的应用外部公开file://URI。如果一项包含文件URI的intent离开您的应用，则应用出现故障，并出现FileUriExposedException异常。

**解决方案:**

要在应用间共享文件，您应发送一项content://URI，并授予URI临时访问权限。进行此授权的最简单方式是使用FileProvider类。如需了解有关权限和共享文件的详细信息，请参阅共享文件。

FileProvider 使用场景，调用相机（指定存储位置），调用系统的安装器（指定apk文件目录）。

### 1.13 APK的更新机制，实现逻辑？

步骤：
请求后台服务器，获取最新的版本号，与本地的apk版本号比较（一般是比较VersionCode），如果服务器的版本新，则弹出对话框，提示用户下载更新（如果是强制更新，则确保该对话框不点击确定，则用户无法进入下一步。）下载完成之后，调用系统的安装器，安装apk。（注意Android 7.0之后，要使用FileProvider来做应用间共享文件）。

### 1.14 ContentProvider的作用？

1. 我们想在自己的应用中访问别的应用，或者说一些ContentProvider暴露给我们的一些数据，比如手机联系人，短信等！我们想对这些数据进行读取或者修改，这就需要用到ContentProvider了！
2. 我们自己的应用，想把自己的一些数据暴露出来，给其他的应用进行读取或操作，我们也可以用到ContentProvider，另外我们可以选择要暴露的数据，就避免了我们隐私数据的的泄露！

### 1.15 Android中有没有使用数据库，用到什么框架，怎么增加一个字段？

数据库映射框架:GreenDAO.

增加一个字段：
1. 数据库版本号增加1。
2. 在onUpgrade()方法中，判断版本号，调用或者直接使用sql语句。


## 2. Java基础

### 2.1 二分查找

二分查找也称折半查找（Binary Search），它是一种效率较高的查找方法。但是，折半查找要求线性表必须采用顺序存储结构，而且表中元素按关键字有序排列。

[题目链接](http://www.lintcode.com/zh-cn/problem/first-position-of-target/)

```
给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。

**样例**

在数组 [1, 2, 3, 3, 4, 5, 10] 中二分查找3，返回2。
```

**时间复杂度：**

时间复杂度可以表示`O(h)=O(log2n)`

Java实现：

```
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        int len = nums.length;
        int begin = 0;
        int end = len - 1;
        int middle = (begin + end) / 2;
        while (begin <= end) {
            if (target > nums[middle]) {
                begin = middle + 1;
            } else if (target < nums[middle]) {
                end = middle - 1;
            } else {
                while (middle >= 0 && nums[middle] == target) {
                    middle--;
                }
                return middle + 1;
            }
            middle = (begin + end) / 2;
        }
        return -1;
    }
```

### 2.2 冒泡排序

冒泡排序算法的运作如下：（从后往前）

    比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
    针对所有的元素重复以上的步骤，除了最后一个。
    持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
    
**时间复杂度**

冒泡排序总的平均时间复杂度为
。

**算法稳定性**
冒泡排序就是把小的元素往前调或者把大的元素往后调。比较是相邻的两个元素比较，交换也发生在这两个元素之间。所以，如果两个元素相等，我想你是不会再无聊地把他们俩交换一下的；如果两个相等的元素没有相邻，那么即使通过前面的两两交换把两个相邻起来，这时候也不会交换，所以相同元素的前后顺序并没有改变，所以冒泡排序是一种**稳定**排序算法。

[参考-百度百科](https://baike.baidu.com/item/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F/4602306?fr=aladdin)

Java代码：
```
public class BubbleSort
{
    public void sort(int[] a)
    {
        int temp = 0;
        for (int i = a.length - 1; i > 0; --i)
        {
            for (int j = 0; j < i; ++j)
            {
                if (a[j + 1] < a[j])
                {
                    temp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = temp;
                }
            }
        }
    }
}
```



# 参考

### [国内一线互联网公司内部面试题库](https://github.com/JackyAndroid/AndroidInterview-Q-A)

### [Android 学习资料收集](https://github.com/Freelander/Android_Data)

### [值得阅读的android技术文章 ](https://github.com/zmywly8866/Worth-Reading-the-Android-technical-articles)

### [InterviewQuestion](https://github.com/leerduo/InterviewQuestion)

### [LearningNotes](https://github.com/francistao/LearningNotes)