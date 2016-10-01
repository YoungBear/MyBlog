#Handler内存泄漏

本文GitHub地址：

https://github.com/YoungBear/MyBlog/blob/master/handler_memory_leak.md

*I figure life is a gift and I don't intend on wasting it.*

*我觉得生命是一份礼物，我不想浪费它。*

参考：

http://www.2cto.com/kf/201502/378500.html

http://www.cnblogs.com/jevan/p/3168828.html


　　在Android常用编程中，Handler在进行异步操作并处理返回结果时经常被使用。通常我们的代码会这样实现：

```
public class HandlerMemoryLeakActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_handler_memory_leak);
    }

    private final Handler mHandler = new Handler() {
        @Override
        public void handleMessage(Message msg) {
            //...
        }
    };
}
```

　　但是，其实上面的代码可能导致内存泄露，当你使用Android lint工具的话，会得到这样的警告：

```
This Handler class should be static or leaks might occur (com.example.multifragment.SampleActivity.1)
 
Issue: Ensures that Handler classes do not hold on to a reference to an outer class
Id: HandlerLeak
 
Since this Handler is declared as an inner class, it may prevent the outer class from being garbage collected.
If the Handler is using a Looper or MessageQueue for a thread other than the main thread, then there is no issue. 
If the Handler is using the Looper or MessageQueue of the main thread, you need to fix your Handler declaration, 
as follows: Declare the Handler as a static class; In the outer class, instantiate a WeakReference to the outer 
class and pass this object to your Handler when you instantiate the Handler; Make all references to members 
of the outer class using the WeakReference object.
```

　　大体翻译如下:

　　Handler 类应该应该为static类型，否则有可能造成泄露。在程序消息队列中排队的消息保持了对目标Handler类的应用。如果Handler是个内部类，那么它也会保持它所在的外部类的引用。为了避免泄露这个外部类，应该将Handler声明为static嵌套类，并且使用对外部类的弱应用。


　　看到这里，可能还是有一些搞不清楚，代码中哪里可能导致内存泄露，又是如何导致内存泄露的呢？那我们就慢慢分析一下。

1. 当一个Android应用启动的时候，会自动创建一个供应用主线程使用的Looper实例。Looper的主要工作就是一个一个处理消息队列中的消息对象。在Android中，所有Android框架的事件（比如Activity的生命周期方法调用和按钮点击等）都是放入到消息中，然后加入到Looper要处理的消息队列中，由Looper负责一条一条地进行处理。主线程中的Looper生命周期和当前应用一样长。

 

2. 当一个Handler在主线程进行了初始化之后，我们发送一个target为这个Handler的消息到Looper处理的消息队列时，实际上已经发送的消息已经包含了一个Handler实例的引用，只有这样Looper在处理到这条消息时才可以调用Handler.handleMessage(Message)完成消息的正确处理。

 

3. 在Java中，非静态的内部类和匿名内部类都会隐式地持有其外部类的引用。静态的内部类不会持有外部类的引用。


　　确实上面的代码示例有点难以察觉内存泄露，那么下面的例子就非常明显了：

```
public class HandlerMemoryLeakActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_handler_memory_leak);

        mHandler.postDelayed(new Runnable() {
            @Override
            public void run() {
                //do something
            }
        }, 10 * 60 * 1000);
        finish();
    }

    private final Handler mHandler = new Handler() {
        @Override
        public void handleMessage(Message msg) {
            //...
        }
    };
}
```

　　分析一下上面的代码，当我们执行了Activity的finish方法，被延迟的消息会在被处理之前存在于主线程消息队列中10分钟，而这个消息中又包含了Handler的引用，而Handler是一个匿名内部类的实例，其<font color=red>持有外面的HandlerMemoryLeakActivity的引用</font>，所以这导致了HandlerMemoryLeakActivity无法回收，进行导致HandlerMemoryLeakActivity持有的很多资源都无法回收，这就是我们常说的内存泄露。

　　注意上面的new Runnable这里也是匿名内部类实现的，同样也会持有HandlerMemoryLeakActivity的引用，也会阻止HandlerMemoryLeakActivity被回收。

　　要解决这种问题，思路就是不使用非静态内部类，继承Handler时，要么是<font color=red>**放在单独的类文件**</font>中，要么<font color=red>**就是使用静态内部类**</font>。因为静态的内部类不会持有外部类的引用，所以不会导致外部类实例的内存泄露。当你需要在静态内部类中调用外部的Activity时，我们可以使用<font color=red>**弱引用**</font>来处理。另外关于同样也需要将Runnable设置为静态的成员属性。注意：一个静态的匿名内部类实例不会持有外部类的引用。 修改后不会导致内存泄露的代码如下

```
public class HandlerMemoryLeakActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_handler_memory_leak);

        mHandler.postDelayed(sRunnable, 10 * 60 * 1000);
        finish();
    }

    private final MyHandler mHandler = new MyHandler(this);
    private static final Runnable sRunnable = new Runnable() {
        @Override
        public void run() {
            //do something
        }
    };

    private static class MyHandler extends Handler {
        WeakReference<HandlerMemoryLeakActivity> mActivity;

        public MyHandler(HandlerMemoryLeakActivity activity) {
            this.mActivity = new WeakReference<HandlerMemoryLeakActivity>(activity);
        }

        @Override
        public void handleMessage(Message msg) {
            HandlerMemoryLeakActivity activity = mActivity.get();
            if (activity != null) {
                //do something with activity
            }

            super.handleMessage(msg);
        }
    }
}
```

　　**其实在Android中很多的内存泄露都是由于在Activity中使用了非静态内部类导致的，就像本文提到的一样，所以当我们使用时要非静态内部类时要格外注意，如果其实例的持有对象的生命周期大于其外部类对象，那么就有可能导致内存泄露**。
　　
测试代码地址：

https://github.com/YoungBear/AsyncTaskLearn/blob/master/app/src/main/java/com/example/handlerlearn/activity/HandlerMemoryLeakActivity.java
