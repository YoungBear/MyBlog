#AsyncTask#

本文Github地址：

https://github.com/YoungBear/MyBlog/blob/master/AsyncTask.md

*Being yourself is an honor, because nobody else can be you.*

*做自己是一种荣耀，因为没有任何人能成为你。*

参考：

http://blog.csdn.net/lmj623565791/article/details/38614699

http://blog.csdn.net/guolin_blog/article/details/11711405

《Android开发艺术探索》

　　AsyncTask是一种轻量级的异步任务类，它可以在线程池中执行后台任务，然后把执行的进度和最终结果传递给主线程并在主线程更新UI。从实现上来说，AsyncTask封装了Thread和Handler，通过AsyncTask可以更加方便地执行后台任务以及在主线程访问UI。但是AsyncTask并不适合进行特别耗时的后台任务，对于特别耗时的任务来说，建议使用线程池。

　　AsyncTask是一个抽象的泛型类，它提供了Params、Progress和Result这三个泛型参数，其中Params表示参数的类型，Progress表示后台任务的执行进度的类型，而Result则表示后台任务的返回结果的类型，如果AsyncTask确实不需要传递具体的参数，那么这三个泛型参数可以用Void来代替。AsyncTask这个类的声明：

`public abstract class AsyncTask<Params, Progress, Result>`

　　AsyncTask提供了4个核心方法，它们的含义如下所示。

1. onPreExecute()，在主线程中执行，在异步任务执行之前，此方法会被调用，一般可以做一些准备工作。
2. doInBackground(Params...params)，在线程池中执行，此方法用于执行异步任务，params参数表示异步任务的<font color=red>输入参数</font>。在此方法中可以通过publishProgress方法来更新任务的进度，publishProgress方法会调用onProgressUpdate方法。此外此方法需要返回计算结果给onPostExecute方法。
3. onProgressUpdate(Progress...values)，在主线程中执行，当后台任务的执行进度发生改变时此方法会被调用。
4. onPoseExecute(Result result)，在主线程中执行，在异步任务执行之后，此方法会被调用，其中result参数是后台任务的返回值，即doInBackground的返回值。

　　上面这几个方法，onPreExecute先执行，接着是doInBackground，最后才是onPostExecute。除了上述四个方法以外，AsyncTask还提供了onCancelled()方法，它同样在主线程中执行，当异步任务被取消时，onCancalled()方法会被调用，这个时候onPostExecute()则不会被调用。

　　AsyncTask在具体使用的过程冲也是有一些条件限制的，主要有如下几点：

1. AsyncTask 的类必须在主线程中加载
2. AsyncTask 的对象必须在主线程中创建
3. execute 方法必须在UI线程调用
4. 不要在程序中直接调用onPreExecute()、onPostExecute()、doInBackground()和onProgressUpdate()方法
5. 一个AsyncTask对象只能执行一次，即只能调用一次 execute 方法，否则会报运行时异常
6. 在Android 1.6 之前，AsyncTask是串行执行任务的，Android 1.6 的时候 AsyncTask 开始采用线程池里处理并发任务，但是从Android 3.0 开始，为了避免AsyncTask 所带来的并发错误，AsyncTask 又采用一个线程来串行执行任务。尽管如此，在 Android 3.0 以及后续的版本中，我们仍然可以通过 AsyncTask 的 executeOnExecutor 方法来并发地执行任务。

##AsyncTask的工作原理
　　从它的execute方法开始分析。

　　源代码基于 <font color=red>API-24</font>，不同版本可能会有不同，但是不影响整体分析。

```java
    @MainThread
    public final AsyncTask<Params, Progress, Result> execute(Params... params) {
        return executeOnExecutor(sDefaultExecutor, params);
    }
    
    @MainThread
    public final AsyncTask<Params, Progress, Result> executeOnExecutor(Executor exec,
            Params... params) {
        if (mStatus != Status.PENDING) {
            switch (mStatus) {
                case RUNNING:
                    throw new IllegalStateException("Cannot execute task:"
                            + " the task is already running.");
                case FINISHED:
                    throw new IllegalStateException("Cannot execute task:"
                            + " the task has already been executed "
                            + "(a task can be executed only once)");
            }
        }

        mStatus = Status.RUNNING;

        onPreExecute();

        mWorker.mParams = params;
        exec.execute(mFuture);

        return this;
    }
```
　　executeOnExecutor 的执行过程为：

1. 设置当前AsyncTask的状态为RUNNING，上面的switch也可以看出，每个异步任务在完成前只能执行一次
2. 执行了onPreExecute()，当前依然在UI线程
3. 将我们传入的参数赋值给了mWorker.mParams
4. exec.execute(mFuture)

　　mWorker的定义：

```java
    private final WorkerRunnable<Params, Result> mWorker;
    private static abstract class WorkerRunnable<Params, Result> implements Callable<Result> {
        Params[] mParams;
    }
```
　　可以看到 WorkerRunnable 是 Callable 的子类，并且包含一个mParams用于保存我们传入的参数，下面看一下初始化 mWorker 的代码：

```java
    public AsyncTask() {
        mWorker = new WorkerRunnable<Params, Result>() {
            public Result call() throws Exception {
                mTaskInvoked.set(true);

                Process.setThreadPriority(Process.THREAD_PRIORITY_BACKGROUND);
                //noinspection unchecked
                Result result = doInBackground(mParams);
                Binder.flushPendingCommands();
                return postResult(result);
            }
        };
        // 省略 mFuture 代码
    }
```

　　可以看出来，使用匿名内部类完成了对 mWorker 的初始化，实现了 call 方法。call 方法中设置 mTaskInvoked 为 true，且最终调用了 doInBackground(mParams) 方法，并且将返回值 result 作为参数给 postResult 方法。接下来看 postResult 方法的实现：

```java
    private Result postResult(Result result) {
        @SuppressWarnings("unchecked")
        Message message = getHandler().obtainMessage(MESSAGE_POST_RESULT,
                new AsyncTaskResult<Result>(this, result));
        message.sendToTarget();
        return result;
    }
```
　　可以看到，postResult 中使用了异步消息机制，传递了一个消息 message，它的 what 是 MESSAGE_POST_RESULT，message.object 是 new AsyncTaskResult<Result>(this, result)。
```java
    @SuppressWarnings({"RawUseOfParameterizedType"})
    private static class AsyncTaskResult<Data> {
        final AsyncTask mTask;
        final Data[] mData;

        AsyncTaskResult(AsyncTask task, Data... data) {
            mTask = task;
            mData = data;
        }
    }
```
　　AsyncTaskResult就是一个简单的携带参数的对象。

　　再看 Handler 的实现：
```java
    private static Handler getHandler() {
        synchronized (AsyncTask.class) {
            if (sHandler == null) {
                sHandler = new InternalHandler();
            }
            return sHandler;
        }
    }
    private static class InternalHandler extends Handler {
        public InternalHandler() {
            super(Looper.getMainLooper());
        }

        @SuppressWarnings({"unchecked", "RawUseOfParameterizedType"})
        @Override
        public void handleMessage(Message msg) {
            AsyncTaskResult<?> result = (AsyncTaskResult<?>) msg.obj;
            switch (msg.what) {
                case MESSAGE_POST_RESULT:
                    // There is only one result
                    result.mTask.finish(result.mData[0]);
                    break;
                case MESSAGE_POST_PROGRESS:
                    result.mTask.onProgressUpdate(result.mData);
                    break;
            }
        }
    }    
```
　　getHandler 获取一个单例对象 sHandler。该 Handler 实现了handleMessage()方法，用来处理异步消息。在接收到 MESSAGE_POST_RESULT 消息时，执行了 result.mTask.finish(result.mData[0]);其实就是 AsyncTask.this.finish(result)，看 finish 方法的实现：
　　

```java
    private void finish(Result result) {
        if (isCancelled()) {
            onCancelled(result);
        } else {
            onPostExecute(result);
        }
        mStatus = Status.FINISHED;
    }
```
　　可以看到，如果我们调用了 cancel() 则执行 onCancelled回调；正常情况下，会调用 onPostExecute(result)。最后再将状态置为FINISHED。

　　mWorker 看完了，接下来看 mFuture 了。在 AsyncTask 的构造方法中完成了对mFuture 的初始化，将 mWorker 作为参数，重写了其 done 方法。

```java
    public AsyncTask() {
        //省略 mWorker 代码
        mFuture = new FutureTask<Result>(mWorker) {
            @Override
            protected void done() {
                try {
                    postResultIfNotInvoked(get());
                } catch (InterruptedException e) {
                    android.util.Log.w(LOG_TAG, e);
                } catch (ExecutionException e) {
                    throw new RuntimeException("An error occurred while executing doInBackground()",
                            e.getCause());
                } catch (CancellationException e) {
                    postResultIfNotInvoked(null);
                }
            }
        };
    }
```
　　任务执行结束会调用:postResultIfNotInvoked(get()); get() 表示 获取 mWorker 的 call 的返回值，即Result。然后看 postResultIfNotInvoked 方法。

```java
    private void postResultIfNotInvoked(Result result) {
        final boolean wasTaskInvoked = mTaskInvoked.get();
        if (!wasTaskInvoked) {
            postResult(result);
        }
    }
```
　　如果 mTaskInvoked 不为 true，则执行 postResult；但是在 mWorker 初始化时就已经将 mTaskInvoked 置为 true了，所以一般这个 postResult 执行不到。

　　好了，到这里，已经分析完了 execute 方法中出现的 mWorker和mFurture，不过这里一直是初始化这两个对象的代码，并没有真正的执行。下面看真正调用执行的地方。即 executeOnExecutor 方法中的 <font color=red>exec.execute(mFuture)</font>。 executeOnExecutor(sDefaultExecutor, params);两个参数params为 mFuture，看一下 sDefaultExecutor:

```java
    private static volatile Executor sDefaultExecutor = SERIAL_EXECUTOR;
    public static final Executor SERIAL_EXECUTOR = new SerialExecutor();
    private static class SerialExecutor implements Executor {
        final ArrayDeque<Runnable> mTasks = new ArrayDeque<Runnable>();
        Runnable mActive;

        public synchronized void execute(final Runnable r) {
            mTasks.offer(new Runnable() {
                public void run() {
                    try {
                        r.run();
                    } finally {
                        scheduleNext();
                    }
                }
            });
            if (mActive == null) {
                scheduleNext();
            }
        }

        protected synchronized void scheduleNext() {
            if ((mActive = mTasks.poll()) != null) {
                THREAD_POOL_EXECUTOR.execute(mActive);
            }
        }
    }
```
　　可以看到 sDefaultExecutor 其实是一个 SerialExecutor 的一个实例，其内部维持一个任务队列；看其 execute(Runnable r) 方法，将 r
放到 mTasks 的队尾(offer方法)。

　　判断当前 mActive 是否为空，为空则调用 scheduleNext 方法。scheduleNext，直接取出任务队列中的队首任务，如果不为 null 则传入 THREAD_POOL_EXECUTOR 进行执行。下面看 THREAD_POOL_EXECUTOR ：

```java
    public static final Executor THREAD_POOL_EXECUTOR;

    static {
        ThreadPoolExecutor threadPoolExecutor = new ThreadPoolExecutor(
                CORE_POOL_SIZE, MAXIMUM_POOL_SIZE, KEEP_ALIVE_SECONDS, TimeUnit.SECONDS,
                sPoolWorkQueue, sThreadFactory);
        threadPoolExecutor.allowCoreThreadTimeOut(true);
        THREAD_POOL_EXECUTOR = threadPoolExecutor;
    }
```
　　根据上一篇文章[Android 线程和线程池](http://blog.csdn.net/next_second/article/details/52703674 "") 可以看出，THREAD_POOL_EXECUTOR 是自己设置的一个线程池，参数为：

<font color=red>API-24</font>：

```java
    private static final int CPU_COUNT = Runtime.getRuntime().availableProcessors();
    // We want at least 2 threads and at most 4 threads in the core pool,
    // preferring to have 1 less than the CPU count to avoid saturating
    // the CPU with background work
    private static final int CORE_POOL_SIZE = Math.max(2, Math.min(CPU_COUNT - 1, 4));
    private static final int MAXIMUM_POOL_SIZE = CPU_COUNT * 2 + 1;
    private static final int KEEP_ALIVE_SECONDS = 30;
    private static final ThreadFactory sThreadFactory = new ThreadFactory() {
        private final AtomicInteger mCount = new AtomicInteger(1);

        public Thread newThread(Runnable r) {
            return new Thread(r, "AsyncTask #" + mCount.getAndIncrement());
        }
    };

    private static final BlockingQueue<Runnable> sPoolWorkQueue =
            new LinkedBlockingQueue<Runnable>(128);
```

<font color=red>API-19~API-23</font>

```java
    private static final int CPU_COUNT = Runtime.getRuntime().availableProcessors();
    private static final int CORE_POOL_SIZE = CPU_COUNT + 1;
    private static final int MAXIMUM_POOL_SIZE = CPU_COUNT * 2 + 1;
    private static final int KEEP_ALIVE = 1;

    private static final ThreadFactory sThreadFactory = new ThreadFactory() {
        private final AtomicInteger mCount = new AtomicInteger(1);

        public Thread newThread(Runnable r) {
            return new Thread(r, "AsyncTask #" + mCount.getAndIncrement());
        }
    };

    private static final BlockingQueue<Runnable> sPoolWorkQueue =
            new LinkedBlockingQueue<Runnable>(128);
```
<font color=red>在API-24版本上，</font>

**核心线程数限制在2~4之间；**

**线程池最大线程数目为CPU 核心数的 2 倍 + 1；**

**核心线程无超时机制，非核心线程在闲置时的超时时间为 30 秒；**

**任务队列容量为128。**

<font color=red>在API-19~API-23版本上，</font>

**核心线程数等于 CPU 核心数 + 1；**

**线程池最大线程数目为CPU 核心数的 2 倍 + 1；**

**核心线程无超时机制，非核心线程在闲置时的超时时间为 30 秒；**

**任务队列容量为128。**

　　下面再仔细看一下 SerialExecutor 的代码：

```
    private static class SerialExecutor implements Executor {
        final ArrayDeque<Runnable> mTasks = new ArrayDeque<Runnable>();
        Runnable mActive;

        public synchronized void execute(final Runnable r) {
            mTasks.offer(new Runnable() {
                public void run() {
                    try {
                        r.run();
                    } finally {
                        scheduleNext();
                    }
                }
            });
            if (mActive == null) {
                scheduleNext();
            }
        }

        protected synchronized void scheduleNext() {
            if ((mActive = mTasks.poll()) != null) {
                THREAD_POOL_EXECUTOR.execute(mActive);
            }
        }
    }
```
　　可以看到，SerialExecutor 是使用 ArrayDeque 这个队列来管理 Runnable 对象的，如果我们一次性启动了很多新任务，首先在第一次运行execute()方法的时候，会调用ArrayDeque的offer()方法将传入的Runnable对象添加到队列的尾部，然后判断mActive对象是不是为null，第一次运行当然是等于null了，于是会调用scheduleNext()方法。这个方法会从队列的头部取一个任务，并赋值给mActive对象，然后调用THREAD_POOL_EXECUTOR取执行取出的Runnable对象。之后如果又有新的任务被执行，同样还会调用offer()方法将传入的Runnable添加到队列的尾部，但是这时候mActive不是null，于是不会再调用scheduleNext()方法。只有在第一个任务执行完成，会调用finally块中的方法，即还是scheduleNext()。也就是说，每次当一个任务执行完毕后，下一个任务才会得到执行。所以说，虽然内部有一个线程池，其实调用的过程还是线性的。一个接着一个的执行，相当于单线程。

<font color=red>在API-19~API-23版本上，</font>

　　在魅族MX5手机上，CPU_COUNT(CPU核心数)为8，则核心线程数为9，线程池总大小为17，任务队列为128。即同一时刻能够运行的线程数为9，当我们启动了10个任务时，只有9个任务能够立刻执行，剩下的一个任务需要等待，当有一个任务执行完毕后，这个人会才会启动。

##AsyncTask曾经的缺陷

　　记得以前有个面试题经常会问道：AsyncTask运行的原理是什么？有什么缺陷？

　　以前对于缺陷的答案可能是：AsyncTask在并发执行多个任务时发生异常。其实还是存在的，在3.0以前的系统中还是会以支持多线程并发的方式执行，支持并发数也是我们上面所计算的128，阻塞队列可以存放10个；也就是同时执行138个任务是没有问题的；而超过138会马上出现java.util.concurrent.RejectedExecutionException；
而在在3.0以上包括3.0的系统中会为单线程执行（即我们上面代码的分析）。

测试代码：

```
package com.example.handlerlearn.activity;

import android.app.Activity;
import android.app.ProgressDialog;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import com.example.handlerlearn.R;

public class AsyncTaskActivity extends Activity {

    private static final String TAG = AsyncTaskActivity.class.getSimpleName();

    private ProgressDialog mDialog;
    private TextView mTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_async_task);

        mTextView = (TextView) findViewById(R.id.txt_show);

        mDialog = new ProgressDialog(this);
        mDialog.setMax(100);
        mDialog.setProgressStyle(ProgressDialog.STYLE_HORIZONTAL);
        mDialog.setCancelable(false);

        for (int i = 0; i < 138; i++) {
            new MyAsyncTask2().execute();
        }

//        new MyAsyncTask().execute();
    }

    private class MyAsyncTask2 extends AsyncTask<Void, Void, Void> {
        @Override
        protected Void doInBackground(Void... params) {
            try {
                Thread.sleep(10 * 1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            Log.e(TAG, Thread.currentThread().getName() + " doInBackground ");
            return null;
        }
    }
}

```

　　我们可以看到for循环中执行了138个异步任务，每个异步任务的执行需要10s；

###使用2.3.3模拟器运行
　　输出结果为：

　　AsyncTask#1 - AsyncTask #128同时输出

　　然后10s后，另外10个任务输出。

　　可以分析结果，得到结论：AsyncTask在2.2的系统中同时支持128个任务并发，至少支持10个任务等待；

![](http://img.blog.csdn.net/20160930235201458)

　　下面将138个任务，改成139个任务：

```
    for (int i = 0; i < 138; i++) {
        new MyAsyncTask2().execute();
    }
```

　　运行结果：会发生异常：java.util.concurrent.RejectedExecutionException ； 于是可以确定仅支持10个任务等待，超过10个则立即发生异常。


![](http://img.blog.csdn.net/20160930235336598)


　　简单说一下出现异常的原因：现在是139个任务，几乎同时提交，线程池支持128个的并发，然后阻塞队列数量为10，此时当第11个任务提交的时候则会发生异常。

　　简单看一下源码：

```
   public static final Executor THREAD_POOL_EXECUTOR
            = new ThreadPoolExecutor(CORE_POOL_SIZE, MAXIMUM_POOL_SIZE, KEEP_ALIVE,
                    TimeUnit.SECONDS, sPoolWorkQueue, sThreadFactory);
```
　　看ThreadPoolExecutor的execute方法：

```
    public void execute(Runnable command) {
        //...
        if (isRunning(c) && workQueue.offer(command)) {
            int recheck = ctl.get();
            if (! isRunning(recheck) && remove(command))
                reject(command);
            else if (workerCountOf(recheck) == 0)
                addWorker(null, false);
        }
        else if (!addWorker(command, false))
            reject(command);
    }
```
　　当阻塞队列满的时候workQueue.offer(command)返回false;然后执行addWorker(command,false)方法，如果返回false则执行reject()方法。

```
    private boolean addWorker(Runnable firstTask, boolean core) {

        //...
        int wc = workerCountOf(c);
        if (wc >= CAPACITY ||
            wc >= (core ? corePoolSize : maximumPoolSize))
            return false;
       //...
    }
```

　　可以看到当任务数目大于容量则返回false，最终在reject()中抛出异常:

```
    final void reject(Runnable command) {
        handler.rejectedExecution(command, this);
    }
```
　　上面就是使用2.3.3模拟器测试的结果；

###使用5.1(魅族MX5)运行
　　输出结果为：

　　把线程数改为139甚至1000，你可以看到任务每隔10s，一个接一个的在那缓慢的执行，不会抛什么异常，不过线程倒是一个一个的在那执行。(串行)


![](http://img.blog.csdn.net/20160930235455552)

###自定义线程池，在3.0及以上版本并行执行任务
　　如果想让AsyncTask可以在Android 3.0及以上的版本上<font color=red>并行</font>，可以采用AsyncTask的executeOnExecutor()方法，即可以自定义线程池。

eg.

```
    Executor exec = new ThreadPoolExecutor(15, 200, 10,  
            TimeUnit.SECONDS, new LinkedBlockingQueue<Runnable>());  
    new DownloadTask().executeOnExecutor(exec);  
```

　　这样就可以使用我们自定义的一个Executor来执行任务，而不是使用SerialExecutor。上述代码的效果允许在同一时刻有15个任务正在执行，并且最多能够存储200个任务。


![](http://img.blog.csdn.net/20160930235559740)

　　好了，如果现在大家去面试，被问到AsyncTask的缺陷，可以分为两个部分说，<font color=red>**在3.0以前，最大支持128个线程的并发，10个任务的等待。在3.0以后，无论有多少任务，都会在其内部单线程执行**</font>。



测试代码下载：

https://github.com/YoungBear/AsyncTaskLearn























