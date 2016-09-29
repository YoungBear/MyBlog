#Android 线程和线程池

参考《Android 开发艺术探索》

*Stop saying "I wish" and start saying "I will".*

*不要再说“我希望...”，开始说“我会...”。*

##线程池的优点##
1. 重用线程池中的线程，避免因为线程的创建和销毁所带来的性能开销
2. 能有效控制线程池的最大并发数，避免大量的线程之间因互相抢占系统资源而导致的阻塞现象
3. 能够对线程进行简单的管理，并提供定时执行以及指定间隔循环执行等功能。


　　Android 中的线程池的概念来源于 Java 中的 Executor， Executor 是一个接口，真正的线程池的实现为 ThreadPoolExecutor。ThreadPoolExecutor 提供了一系列参数来配置线程池，通过不同的参数可以创建不同的线程池，从线程池的功能特性上来说，Android 的线程池主要分为 4 类，这 4 类线程池可以通过 Executor 所提供的工厂方法来得到。由于 Android 中的线程池都是直接或者间接通过配置 ThreadPoolExecutor 来实现的，所以先了解下 ThreadPoolExecutor。

package java.util.concurrent;

ThreadPoolExecutor.java

```java
public ThreadPoolExecutor(int corePoolSize,
                              int maximumPoolSize,
                              long keepAliveTime,
                              TimeUnit unit,
                              BlockingQueue<Runnable> workQueue,
                              ThreadFactory threadFactory,
                              RejectedExecutionHandler handler)
```

**corePoolSize**

　　线程池的核心线程数，默认情况下，核心线程会在线程池中一直存活，即使它们处于闲置状态。如果将 ThreadPoolExecutor 的allowCoreThreadTimeOut 属性设置为true，那么闲置的核心线程在等待新任务到来时会有超时策略，这个时间间隔有keepAliveTime所指定，当等待时间超过 keepAliveTime 所指定的时长后，核心线程就会被终止。

**maximumPoolSize**

　　线程池所能容纳的最大线程数，当活动线程数达到这个数值后，后续的新任务将会被阻塞。

**keepAliveTime**

　　非核心线程闲置时的超时时长，超过这个时长，非核心线程就会被回收。当ThreadPoolExecutor的 allowCoreThreadTimeOut 属性设置为 true 时，keepAliveTime 同样会作用于核心线程。

**unit**

　　用于指定 keepAliveTime 参数的时间单位。

**workQueue**

　　线程池中的任务队列，通过线程池的 execute 方法提交的 Runnable 对象会存储在这个参数中。

**threadFactory**

　　线程工厂，为线程池创建新线程的功能。ThreadFactory 是一个接口，它只有一个方法：Thread newThread(Runnable r)。

**handler**

　　当线程池无法执行新任务时，这个能是由于任务队列已满或者是无法成功执行任务，这个时候 ThreadPoolExecutor 会调用 handler 的 rejectedExecution 方法来通知调用者，默认情况下 rejectedExecution 方法会直接抛出一个 RejectedExecutionException。

　　ThreadPoolExecutor 执行任务时大致遵循如下规则：

1. 如果线程池中的线程数量未达到核心线程的数量，那么会直接启动一个核心线程来执行任务。
2. 如果线程池中的线程数量已经达到或者超过核心线程的数量，那么任务会被插入到任务队列中排队等待执行。
3. 如果在步骤 2 中无法将任务插入到任务队列中，这往往是由于任务队列已满，这个时候如果线程数量未达到线程池规定的最大值，那么会立即启动一个非核心线程来执行任务。
4. 如果步骤 3 中线程数量已经达到线程池规定的最大值，那么就拒绝执行此任务，ThreadPoolExecutor 会调用 RejectedExecutionHandler 的 rejectedExecution 方法来通知调用者。


##AsyncTask 中　ThreadPoolExecutor 的配置##

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

    /**
     * An {@link Executor} that can be used to execute tasks in parallel.
     */
    public static final Executor THREAD_POOL_EXECUTOR
            = new ThreadPoolExecutor(CORE_POOL_SIZE, MAXIMUM_POOL_SIZE, KEEP_ALIVE,
                    TimeUnit.SECONDS, sPoolWorkQueue, sThreadFactory);
```

　　从上面的代码可以知道，AsyncTask 对 THREAD_POOL_EXECUTOR 这个线程池进行了配置，配置后的线程池规格如下：

　　**核心线程数等于 CPU 核心数 + 1；**

　　**线程池的最大线程数为 CPU 核心数的 2 倍 + 1；**

　　**核心线程无超时机制，非核心线程在闲置时的超时时间为 1 秒；**

　　**任务队列的容量为 128。**


##Android 中最常用的四类线程池##

　　**FixedThreadPool**

```java
    public static ExecutorService newFixedThreadPool(int nThreads) {
        return new ThreadPoolExecutor(nThreads, nThreads,
                                      0L, TimeUnit.MILLISECONDS,
                                      new LinkedBlockingQueue<Runnable>());
    }
```

　　FixedThreadPool 是一种<font color=red>线程数量固定</font>的线程池，并且<font color=red>只有核心线程</font>。当线程处于空闲状态时，他们并不会被回收。当所有的线程都处于活动状态时，新任务都会处于等待状态，直到有线程空闲出来。由于 FixedThreadPool 只有核心线程并且这些核心线程不会被回收，这意味着它能够更加快速地相应外界的请求。

　　特点：

1. 线程数量固定
2. 只有核心线程
3. 没有超时机制
4. 任务队列没有大小限制


**CachedThreadPool**

```java
   public static ExecutorService newCachedThreadPool() {
        return new ThreadPoolExecutor(0, Integer.MAX_VALUE,
                                      60L, TimeUnit.SECONDS,
                                      new SynchronousQueue<Runnable>());
    }
```

　　CachedThreadPool 是一种<font color=red>线程数量不定</font>的线程池，它<font color=red>只有非核心线程</font>，并且其最大线程数为 Integer.MAX_VALUE 。由于 Integer.MAX_VALUE 是一个很大的数，实际上就相当于最大线程数可以任意大。当线程池中的线程都处于活动状态时，线程池会创建新的线程来处理新任务，否则就会利用空闲的线程来处理新任务。线程池中的空闲线程都有超时机制，这个超时时长为 60 秒，超过 60 秒闲置线程就会被回收。和 FixedThreadPool 不同的是， CacheedThreadPool 的任务队列其实相当于一个空集合，这将导致任何任务都会立即被执行，因为在这种场景下 SynchronousQueue 是无法插入任务的。从 CacheThreadPool 的特性来看，这类线程池比较适合<font color=red>执行大量的耗时较少的任务</font>。当整个线程池都处于闲置状态时，线程池中的线程都会超时而被停止，这个时候 CachedThreadPool 之中实际上是没有任何线程的，它几乎是不占用任何系统资源的。

　　特点：

1. 线程数目不固定
2. 只有非核心线程
3. 最大线程数任意大
4. 有超时机制，闲置线程超过 60 秒就会被回收
5. 任务队列为空集合，任何任务都会立即被执行


　　**ScheduledThreadPool**

```java
    public static ScheduledExecutorService newScheduledThreadPool(int corePoolSize) {
        return new ScheduledThreadPoolExecutor(corePoolSize);
    }
    
    public ScheduledThreadPoolExecutor(int corePoolSize) {
        super(corePoolSize, Integer.MAX_VALUE, 0, NANOSECONDS,
              new DelayedWorkQueue());
    }
```

　　ScheduledThreadPool 的核心线程数量是固定的，而非核心线程数是没有限制的，并且当非核心线程闲置时会被立即回收。ScheduledThreadPool 这类线程池主要用于<font color=red>执行定时任务和具有固定周期的重复任务</font>。

　　特点：

1. 核心线程固定
2. 非核心线程任意大
3. 有超时机制，闲置线程会被立即(0秒)回收

　　**SingleThreadExecutor**

```java
    public static ExecutorService newSingleThreadExecutor() {
        return new FinalizableDelegatedExecutorService
            (new ThreadPoolExecutor(1, 1,
                                    0L, TimeUnit.MILLISECONDS,
                                    new LinkedBlockingQueue<Runnable>()));
    }
```

　　SingleThreadExecutor 线程池内部只有一个核心线程，它确保所有的任务都在同一个线程中按顺序执行。SingleThreadExecutor 的意义在于统一所有的外界任务到一个线程中，这使得在这些任务之间不需要处理线程同步的问题。

　　特点：

1. 只有一个线程

##测试小程序##

Github地址：

https://github.com/YoungBear/JavaLearn/blob/master/src/com/example/executor/Test.java

```java
/**
 * 
 */
package com.example.executor;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

/**
 * @author bearyang
 *
 */
public class Test {

    /**
     * @param args
     */
    public static void main(String[] args) {
        Runnable command = new Runnable() {

            @Override
            public void run() {
                SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
                String timeString = format.format(new Date());
                System.out.println("current: " + timeString);
            }
        };

        ExecutorService fixedThreadPool = Executors.newFixedThreadPool(4);
        fixedThreadPool.execute(command);

        ExecutorService cacheThreadPool = Executors.newCachedThreadPool();
        cacheThreadPool.execute(command);

        ScheduledExecutorService scheduledExecutorService = Executors.newScheduledThreadPool(4);
        // 2000ms后执行command
        scheduledExecutorService.schedule(command, 2000, TimeUnit.MILLISECONDS);
        // 延迟10s后，每隔1s执行一次command
        scheduledExecutorService.scheduleAtFixedRate(command, 10 * 1000, 1000, TimeUnit.MILLISECONDS);

        ExecutorService singleThreadExecutor = Executors.newSingleThreadExecutor();
        singleThreadExecutor.execute(command);
    }

}

```