# Java 线程池(ThreadPoolExecutor)原理分析与使用

[原文地址](http://www.codeceo.com/article/java-threadpool-executor.html)

## 使用线程池的好处
1. 降低资源消耗
可以重复利用已创建的线程减低线程创建和销毁造成的消耗。
2. 提高相应速度
当任务到达时，任务可以不需要等到线程创建就能立即执行。
3. 提高线程的可管理性
线程是稀缺资源，如果无限制地创建，不仅会消耗系统资源，还会降低系统的稳定性，使用线程池可以进行进一步分配、调优和监控。

## 线程池的工作原理
首先我们看一下当一个新的任务提交到线程池之后，线程池是如何处理的
1. 线程池判断核心线程池里的线程是否都在执行任务。如果不是，则创建一个新的工作线程来执行任务。如果核心线程池里的线程都在执行任务，则执行第二步。
2. 线程池判断工作队列是否已经满。如果工作队列没有满，则将新提交的任务存储在这个工作队列里进行等待。如果工作队列满了，则执行第三步。
3. 线程池判断线程池的线程是否都处于工作状态。如果没有，则创建一个新的工作线程来执行任务。如果已经满了，则交给饱和策略来处理这个任务。

## 线程池饱和策略

Java中的线程池饱和策略

**1. AbortPolicy**

为Java线程池默认的阻塞策略，不执行此任务，而且直接抛出一个运行时异常，切记ThreadPoolExecutor.execute()需要try catch,否则程序会直接退出。

**2. DiscardPolicy**

直接抛弃，任务不执行，空方法

**3. DiscardOldestPolicy**

从队列里面抛弃head的一个任务，并再次execute此task。

**4. CallerRunsPolicy**

在调用execute的线程里面执行此command，会阻塞入口。

**5. 用户自定义拒绝策略（最常用）**

实现`RejectedExecutionHandler`，并自己定义策略模式。


下我们以ThreadPoolExecutor为例展示下线程池的工作流程图

![线程池工作原理_1][1]

![线程池工作原理_2][2]

1、如果当前运行的线程少于corePoolSize，则创建新线程来执行任务（注意，执行这一步骤需要获取全局锁）。

2、如果运行的线程等于或多于corePoolSize，则将任务加入BlockingQueue。

3、如果无法将任务加入BlockingQueue（队列已满），则在非corePool中创建新的线程来处理任务（注意，执行这一步骤需要获取全局锁）。

4、如果创建新线程将使当前运行的线程超出maximumPoolSize，任务将被拒绝，并调用RejectedExecutionHandler.rejectedExecution()方法。

ThreadPoolExecutor采取上述步骤的总体设计思路，是为了在执行execute()方法时，尽可能地避免获取全局锁（那将会是一个严重的可伸缩瓶颈）。在ThreadPoolExecutor完成预热之后（当前运行的线程数大于等于corePoolSize），几乎所有的execute()方法调用都是执行步骤2，而步骤2不需要获取全局锁。

## 线程池的使用

### 线程池的创建

我们可以通过ThreadPoolExecutor来创建一个线程池

```
    /**
     * @param corePoolSize 线程池基本大小，核心线程池大小，活动线程小于corePoolSize则直接创建，大于等于则先加到workQueue中，
     * 队列满了才创建新的线程。当提交一个任务到线程池时，线程池会创建一个线程来执行任务，即使其他空闲的基本线程能够执行新任务也会创建线程，
     * 等到需要执行的任务数大于线程池基本大小时就不再创建。如果调用了线程池的prestartAllCoreThreads()方法，
     * 线程池会提前创建并启动所有基本线程。
     * @param maximumPoolSize 最大线程数，超过就reject；线程池允许创建的最大线程数。如果队列满了，
     * 并且已创建的线程数小于最大线程数，则线程池会再创建新的线程执行任务
     * @param keepAliveTime
     * 线程池的工作线程空闲后，保持存活的时间。所以，如果任务很多，并且每个任务执行的时间比较短，可以调大时间，提高线程的利用率
     * @param unit  线程活动保持时间的单位）：可选的单位有天（DAYS）、小时（HOURS）、分钟（MINUTES）、
     * 毫秒（MILLISECONDS）、微秒（MICROSECONDS，千分之一毫秒）和纳秒（NANOSECONDS，千分之一微秒）
     * @param workQueue 工作队列，线程池中的工作线程都是从这个工作队列源源不断的获取任务进行执行
     */
    public ThreadPoolExecutor(int corePoolSize,
               int maximumPoolSize,
               long keepAliveTime,
               TimeUnit unit,
               BlockingQueue<Runnable> workQueue) {
        // threadFactory用于设置创建线程的工厂，可以通过线程工厂给每个创建出来的线程设置更有意义的名字
        this(corePoolSize, maximumPoolSize, keepAliveTime, unit, workQueue,
                Executors.defaultThreadFactory(), defaultHandler);
    }
```

### 向线程池提交任务

可以使用两个方法向线程池提交任务，分别为**execute()**和**submit()**方法。execute()方法用于提交不需要返回值的任务，所以无法判断任务是否被线程池执行成功。通过以下代码可知execute()方法输入的任务是一个Runnable类的实例。

```
threadsPool.execute(new Runnable() {
        @Override
        public void run() {
        }
    });
```

submit()方法用于提交需要返回值的任务。线程池会返回一个future类型的对象，通过这个future对象可以判断任务是否执行成功，并且可以通过future的get()方法来获取返回值，get()方法会阻塞当前线程直到任务完成，而使用get（long timeout，TimeUnit unit）方法则会阻塞当前线程一段时间后立即返回，这时候有可能任务没有执行完。

```
Future<Object> future = executor.submit(harReturnValuetask);
  try
    {
        Object s = future.get();
    }catch(
    InterruptedException e)
    {
        // 处理中断异常
    }catch(
    ExecutionException e)
    {
        // 处理无法执行任务异常
    }finally
    {
        // 关闭线程池
        executor.shutdown();
    }
```

### 关闭线程池

可以通过调用线程池的shutdown或shutdownNow方法来关闭线程池。它们的原理是遍历线程池中的工作线程，然后逐个调用线程的interrupt方法来中断线程，所以无法响应中断的任务可能永远无法终止。但是它们存在一定的区别，shutdownNow首先将线程池的状态设置成STOP，然后尝试停止所有的正在执行或暂停任务的线程，并返回等待执行任务的列表，而shutdown只是将线程池的状态设置成SHUTDOWN状态，然后中断所有没有正在执行任务的线程。

只要调用了这两个关闭方法中的任意一个，isShutdown方法就会返回true。当所有的任务都已关闭后，才表示线程池关闭成功，这时调用isTerminaed方法会返回true。至于应该调用哪一种方法来关闭线程池，应该由提交到线程池的任务特性决定，通常调用shutdown方法来关闭线程池，如果任务不一定要执行完，则可以调用shutdownNow方法。

### 合理的配置线程池

要想合理地配置线程池，就必须首先分析任务特性，可以从以下几个角度来分析。

1、任务的性质：CPU密集型任务、IO密集型任务和混合型任务。

2、任务的优先级：高、中和低。

3、任务的执行时间：长、中和短。

4、任务的依赖性：是否依赖其他系统资源，如数据库连接。

性质不同的任务可以用不同规模的线程池分开处理。CPU密集型任务应配置尽可能小的线程，如配置Ncpu+1个线程的线程池。由于IO密集型任务线程并不是一直在执行任务，则应配置尽可能多的线程，如2*Ncpu。混合型的任务，如果可以拆分，将其拆分成一个CPU密集型任务和一个IO密集型任务，只要这两个任务执行的时间相差不是太大，那么分解后执行的吞吐量将高于串行执行的吞吐量。如果这两个任务执行时间相差太大，则没必要进行分解。可以通过Runtime.getRuntime().availableProcessors()方法获得当前设备的CPU个数。优先级不同的任务可以使用优先级队列PriorityBlockingQueue来处理。它可以让优先级高的任务先执行

如果一直有优先级高的任务提交到队列里，那么优先级低的任务可能永远不能执行。执行时间不同的任务可以交给不同规模的线程池来处理，或者可以使用优先级队列，让执行时间短的任务先执行。依赖数据库连接池的任务，因为线程提交SQL后需要等待数据库返回结果，等待的时间越长，则CPU空闲时间就越长，那么线程数应该设置得越大，这样才能更好地利用CPU。

建议使用有界队列。有界队列能增加系统的稳定性和预警能力，可以根据需要设大一点儿，比如几千。有时候我们系统里后台任务线程池的队列和线程池全满了，不断抛出抛弃任务的异常，通过排查发现是数据库出现了问题，导致执行SQL变得非常缓慢，因为后台任务线程池里的任务全是需要向数据库查询和插入数据的，所以导致线程池里的工作线程全部阻塞，任务积压在线程池里。如果当时我们设置成无界队列，那么线程池的队列就会越来越多，有可能会撑满内存，导致整个系统不可用，而不只是后台任务出现问题。当然，我们的系统所有的任务是用单独的服务器部署的，我们使用不同规模的线程池完成不同类型的任务，但是出现这样问题时也会影响到其他任务。

### 线程池的监控

如果在系统中大量使用线程池，则有必要对线程池进行监控，方便在出现问题时，可以根据线程池的使用状况快速定位问题。可以通过线程池提供的参数进行监控，在监控线程池的时候可以使用以下属性

- taskCount：线程池需要执行的任务数量。
- completedTaskCount：线程池在运行过程中已完成的任务数量，小于或等于taskCount。
- largestPoolSize：线程池里曾经创建过的最大线程数量。通过这个数据可以知道线程池是否曾经满过。如该数值等于线程池的最大大小，则表示线程池曾经满过。
- getPoolSize：线程池的线程数量。如果线程池不销毁的话，线程池里的线程不会自动销毁，所以这个大小只增不减。
- getActiveCount：获取活动的线程数。

通过扩展线程池进行监控。可以通过继承线程池来自定义线程池，重写线程池的beforeExecute、afterExecute和terminated方法，也可以在任务执行前、执行后和线程池关闭前执行一些代码来进行监控。例如，监控任务的平均执行时间、最大执行时间和最小执行时间等。

  [1]: http://static.codeceo.com/images/2017/05/865a51dff69223f0cf5ad630e5ada19026.jpg
  [2]: http://static.codeceo.com/images/2017/05/865a51dff69223f0cf5ad630e5ada19027.jpg