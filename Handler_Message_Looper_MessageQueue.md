#Android异步消息处理机制

*Everything is going on, but don't give up trying.*

*万事随缘，但不要放弃努力。*

参考：

http://blog.csdn.net/lmj623565791/article/details/38377229

　　Android UI是线程不安全的，即只能在主线程(UI线程)对UI进行操作。一般的做法是，创建一个Message对象，使用Handler发送出去，然后在Handler的handleMessage()方法中获取刚才发送的Message对象，在这里进行UI操作。这就是Android的异步消息处理机制。

　　异步消息处理线程启动后，会进入一个无限的循环体中，每循环一次，从其内部的消息队列中取出一个消息，然后回调相应的消息处理函数，执行完一个消息后则继续训话。若消息队列为空，线程则会阻塞等待。

　　Android 中Handler、Message、Looper和MessageQueue的关系：

　　Looper负责创建一个MessageQueue,然后进入一个无限循环体中不断从该MessageQueue中读取消息，而消息的创建者就是一个或者多个Handler。

##源码分析
###1. Looper

　　对于Looper主要是prepare()和loop()两个方法。

　　首先看prepare()方法

```
    public static void prepare() {
        prepare(true);
    }

    private static void prepare(boolean quitAllowed) {
        if (sThreadLocal.get() != null) {
            throw new RuntimeException("Only one Looper may be created per thread");
        }
        sThreadLocal.set(new Looper(quitAllowed));
    }
```

　　sThreadLocal是一个ThreadLocal对象，可以执子一个线程中存储变量。可以看到，prepare方法将一个Looper的实例放入了ThreadLocal，并且先判断sThreadLocal是否为null，否则抛出异常。这也就说明了Looper.prepare()方法不能被调用两次，同时也保证了一个线程中只有一个Looper实例。

　　下面看Looper的构造方法;

```
    private Looper(boolean quitAllowed) {
        mQueue = new MessageQueue(quitAllowed);
        mThread = Thread.currentThread();
    }
```
　　在构造方法中，创建了一个MessageQueue(消息队列)。

　　然后我们看loop()方法：

```
    public static void loop() {
        final Looper me = myLooper();
        if (me == null) {
            throw new RuntimeException("No Looper; Looper.prepare() wasn't called on this thread.");
        }
        final MessageQueue queue = me.mQueue;

        // Make sure the identity of this thread is that of the local process,
        // and keep track of what that identity token actually is.
        Binder.clearCallingIdentity();
        final long ident = Binder.clearCallingIdentity();

        for (;;) {
            Message msg = queue.next(); // might block
            if (msg == null) {
                // No message indicates that the message queue is quitting.
                return;
            }

            // This must be in a local variable, in case a UI event sets the logger
            final Printer logging = me.mLogging;
            if (logging != null) {
                logging.println(">>>>> Dispatching to " + msg.target + " " +
                        msg.callback + ": " + msg.what);
            }

            final long traceTag = me.mTraceTag;
            if (traceTag != 0) {
                Trace.traceBegin(traceTag, msg.target.getTraceName(msg));
            }
            try {
                msg.target.dispatchMessage(msg);
            } finally {
                if (traceTag != 0) {
                    Trace.traceEnd(traceTag);
                }
            }

            if (logging != null) {
                logging.println("<<<<< Finished to " + msg.target + " " + msg.callback);
            }

            // Make sure that during the course of dispatching the
            // identity of the thread wasn't corrupted.
            final long newIdent = Binder.clearCallingIdentity();
            if (ident != newIdent) {
                Log.wtf(TAG, "Thread identity changed from 0x"
                        + Long.toHexString(ident) + " to 0x"
                        + Long.toHexString(newIdent) + " while dispatching to "
                        + msg.target.getClass().getName() + " "
                        + msg.callback + " what=" + msg.what);
            }

            msg.recycleUnchecked();
        }
    }
    public static @Nullable Looper myLooper() {
        return sThreadLocal.get();
    }    
```

　　可以看到loop方法先调用myLooper()方法获取sThreadLocal存储的Looper实例，如果me为null则抛出异常，也就是说loop方法必须在prepare方法之后执行。

　　然后，拿到该Looper实例中的mQueue(消息队列)保存到queue中。

　　然后，是一个无限循环，每一次循环，取出queue中的一条消息msg，如果msg不为bull，则调用<font color=red>msg.target.dispatchMessage(msg)</font>;msg.target其实就是一个handler，即调用handler来处理消息。

　　最后调用msg.recycleUnchecked();释放资源。

####Looper的主要作用

1. 与当前线程绑定，保证一个线程只会有一个Looper实例，同时一个Looper实例也只有一个MessageQueue。
2. loop()方法，不断从MEssageQueue中去取消息，交给消息的target属性的dispatchMessage去处理。

　　接下来看Handler的具体实现

###2.Handler

　　使用Handler之前，我们都是初始化一个实例，比如用于更新UI线程，我们会在声明的时候直接初始化，或者在onCreate中初始化Handler实例。所以我们首先看Handler的构造方法，看其如何与MessageQueue联系上的，它在子线程中发送的消息（一般发送消息都在非UI线程）怎么发送到MessageQueue中的。

```
    public Handler() {
        this(null, false);
    }
    public Handler(Callback callback, boolean async) {
        if (FIND_POTENTIAL_LEAKS) {
            final Class<? extends Handler> klass = getClass();
            if ((klass.isAnonymousClass() || klass.isMemberClass() || klass.isLocalClass()) &&
                    (klass.getModifiers() & Modifier.STATIC) == 0) {
                Log.w(TAG, "The following Handler class should be static or leaks might occur: " +
                    klass.getCanonicalName());
            }
        }

        mLooper = Looper.myLooper();
        if (mLooper == null) {
            throw new RuntimeException(
                "Can't create handler inside thread that has not called Looper.prepare()");
        }
        mQueue = mLooper.mQueue;
        mCallback = callback;
        mAsynchronous = async;
    }    
```
　　调用mLooper = Looper.myLooper()即获取了当前线程的Looper实例对象，然后又获取该Looper对象的mQueue属性存储到mQueue中。这样就保证了handler的实例与我们Looper实例中MessageQueue关联上了。

　　然后看我们最常用的sendMessage方法：

```
    public final boolean sendMessage(Message msg)
    {
        return sendMessageDelayed(msg, 0);
    }
    public final boolean sendEmptyMessage(int what)
    {
        return sendEmptyMessageDelayed(what, 0);
    }
    public final boolean sendEmptyMessageDelayed(int what, long delayMillis) {
        Message msg = Message.obtain();
        msg.what = what;
        return sendMessageDelayed(msg, delayMillis);
    }
    public final boolean sendEmptyMessageAtTime(int what, long uptimeMillis) {
        Message msg = Message.obtain();
        msg.what = what;
        return sendMessageAtTime(msg, uptimeMillis);
    }
    public final boolean sendMessageDelayed(Message msg, long delayMillis)
    {
        if (delayMillis < 0) {
            delayMillis = 0;
        }
        return sendMessageAtTime(msg, SystemClock.uptimeMillis() + delayMillis);
    }
    public boolean sendMessageAtTime(Message msg, long uptimeMillis) {
        MessageQueue queue = mQueue;
        if (queue == null) {
            RuntimeException e = new RuntimeException(
                    this + " sendMessageAtTime() called with no mQueue");
            Log.w("Looper", e.getMessage(), e);
            return false;
        }
        return enqueueMessage(queue, msg, uptimeMillis);
    }    
```
　　可以看到，最终都调用了sendMessageAtTime(Message msg, long uptimeMillis)方法，此方法中直接过去消息队列mQueue，然后调用enqueueMessage(queue, msg, uptimeMillis):

```
    private boolean enqueueMessage(MessageQueue queue, Message msg, long uptimeMillis) {
        msg.target = this;
        if (mAsynchronous) {
            msg.setAsynchronous(true);
        }
        return queue.enqueueMessage(msg, uptimeMillis);
    }
```
　　enqueueMessage中首先为msg.target赋值为this，也就是把<font color=red>当前的handler</font>作为msg的target属性。最终会调用queue的enqueueMessage的方法，也就是说，handler发出的消息，最终会保存到消息队列中去。

　　现在已经很清楚了Looper会调用prepare()和loop()方法，在当前执行的线程中保存一个Looper实例，这个实例会保存一个MessageQueue对象，然后当前线程进入一个无限循环中去，不断从MessageQueue中读取Handler发来的消息。然后再回调创建这个消息的handler中的dispathMessage方法，下面我们赶快去看一看这个方法：

```
    public void dispatchMessage(Message msg) {
        if (msg.callback != null) {
            handleCallback(msg);
        } else {
            if (mCallback != null) {
                if (mCallback.handleMessage(msg)) {
                    return;
                }
            }
            handleMessage(msg);
        }
    }
    /**
     * Subclasses must implement this to receive messages.
     */
    public void handleMessage(Message msg) {
    }
```
　　dispatchMessage最终会调用handleMessage(msg)方法，而handleMessge方法默认什么也不执行，一般会在子类中实现。

　　到此，这个流程已经解释完毕，让我们首先总结一下

1、首先Looper.prepare()在本线程中保存一个Looper实例，然后该实例中保存一个MessageQueue对象；因为Looper.prepare()在一个线程中只能调用一次，所以MessageQueue在一个线程中只会存在一个。

2、Looper.loop()会让当前线程进入一个无限循环，不端从MessageQueue的实例中读取消息，然后回调msg.target.dispatchMessage(msg)方法。

3、Handler的构造方法，会首先得到当前线程中保存的Looper实例，进而与Looper实例中的MessageQueue想关联。

4、Handler的sendMessage方法，会给msg的target赋值为handler自身，然后加入MessageQueue中。

5、在构造Handler实例时，我们会重写handleMessage方法，也就是msg.target.dispatchMessage(msg)最终调用的方法。

　　好了，总结完成，大家可能还会问，那么在Activity中，我们并没有显示的调用Looper.prepare()和Looper.loop()方法，为啥Handler可以成功创建呢，这是因为在Activity的启动代码中，已经在当前UI线程调用了Looper.prepare()和Looper.loop()方法。**如果在子线程中实现Handler，则必须手动调用Looper.prepare()和Looper.loop()方法，才能实现异步消息处理**。

###3.Handler的post方法
　　我们也可以使用Handler的post方法，做UI的更新：

```
        new Thread(new Runnable() {
            @Override
            public void run() {
                mHandler.post(new Runnable() {
                    @Override
                    public void run() {
                        mTextView.setText("hello");
                    }
                });
            }
        }).start();
```
　　即在post的run方法中做UI更新。看一下post的源代码：

```
    public final boolean post(Runnable r)
    {
       return  sendMessageDelayed(getPostMessage(r), 0);
    }
    private static Message getPostMessage(Runnable r) {
        Message m = Message.obtain();
        m.callback = r;
        return m;
    }
```
　　可以看到，在getPostMessage中，得到了一个Message对象，然后将我们创建的Runnable对象作为callback属性，赋值给了此message.

　　注：产生一个Message对象，可以new  ，也可以使用Message.obtain()方法；两者都可以，但是<font color=red>更建议使用obtain方法</font>，因为Message内部维护了一个Message池用于Message的复用，避免使用new 重新分配内存。

　　上面已经分析，sendMessageDelayed最终和handler.sendMessage一样，都会调用到enqueueMessage方法，给msg.target赋值为handler，最终加入MessagQueue。

　　可以看到，这里msg的callback和target都有值，那么会执行哪个呢？

　　其实上面已经贴过代码，就是dispatchMessage方法：

```
    public void dispatchMessage(Message msg) {
        if (msg.callback != null) {
            handleCallback(msg);
        } else {
            if (mCallback != null) {
                if (mCallback.handleMessage(msg)) {
                    return;
                }
            }
            handleMessage(msg);
        }
    }
    private static void handleCallback(Message message) {
        message.callback.run();
    }
```
　　如果msg.callback不为null，则执行callback回调，也就是我们的Runnable对象(<font color=red>对应Handler中的post的参数Runnable</font>)，即在主线程中调用run方法。

###4.在子线程中使用Handler

　　其实Handler不仅可以更新UI，你完全可以在一个子线程中去创建一个Handler，然后使用这个handler实例在任何其他线程中发送消息，最终处理消息的代码都会在你创建Handler实例的线程中运行。

```
        //在子线程里边实现消息机制
        Thread testThread = new Thread() {
            private Handler handler;

            @Override
            public void run() {
                Looper.prepare();
                handler = new Handler() {
                    @Override
                    public void handleMessage(Message msg) {
                        Log.d(TAG, "handleMessage in sub thread..., msg.what: " + msg.what);
                        super.handleMessage(msg);
                    }
                };

                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        Message msg = Message.obtain();
                        msg.what = 1;
                        handler.sendMessage(msg);
                    }
                }).start();
                Looper.loop();
            }
        };
        testThread.start();
```
　　Android不仅给我们提供了异步消息处理机制让我们更好的完成UI的更新，其实也为我们提供了异步消息处理机制代码的参考~~不仅能够知道原理，最好还可以将此设计用到其他的非Android项目中去。

测试代码位置：

https://github.com/YoungBear/AsyncTaskLearn/blob/master/app/src/main/java/com/example/handlerlearn/activity/HandlerLearnActivity.java
















