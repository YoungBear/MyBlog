##Android学习笔记##
    android:excludeFromRecents="true"
表示在最近列表里边不会出现该应用。

造成内存泄漏：

Java 中，非静态内部类和匿名内部类会持有外部类的隐式引用，而静态内部类不会。

解决方案：

1. 可以将Handler作为一个内部类，使用<font color=red>弱引用</font>的方式指向所在的activity，这样就不会导致内存泄漏。

弱引用：弱引用的对象拥有短暂的生命周期。在垃圾回收器线程扫描它所管辖的内存区域的过程中，一旦发现了只具有弱引用的对象，不管当前内存空间足够与否，都会回收它的内存。不过，由于垃圾回收器是一个优先级很低的线程，因此不一定会很快发现那些只具有弱引用的对象。

2. 可以在Activity的onDestroy()中，调用`mHandler.removeCallbacksAndMessages(null);`方法，，即清除掉所有的回调消息。

参考：
http://blog.csdn.net/card361401376/article/details/51493352

http://jiajixin.cn/2015/01/06/memory_leak/

##撞库

##Android 线程和线程池


##todo 20160928

AsyncTask

HandlerThread

IntentService

ArrayDeque



