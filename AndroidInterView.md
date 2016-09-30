#Android面试题#

1. 请解释下在单线程模型中Message,Handler,Message Queue,Looper之间的关系。
拿主线程来说，主线程启动时会调用Looper.prepare()方法，会初始化一个Looper，放入ThreadLocal中，接着调用Looper.loop()不断遍历Message Queue。

Handler的创建依赖于当前线程中的Looper，如果当前线程没有Looper则必须调用Looper.prepare()。Handler调用sendMessage到MessageQueue。Looper不断从MessageQueue中取出消息，回调handleMessage()方法。