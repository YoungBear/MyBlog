#RxJava

参考：http://gank.io/post/560e15be2dca930e00da1083

##异步

###扩展的观察者模式
RxJava作为一个工具库，使用的是通用形式的观察者模式。如下图：

![](http://ww3.sinaimg.cn/mw1024/52eb2279jw1f2rx4446ldj20ga03p74h.jpg)

##RxJava的观察者模式

RxJava的四个基本概念：

- Observable 可观察者，即被观察者
- Observer 观察者
- subscribe 订阅，事件
- Observable和Observer通过subscribe()方法实现订阅关系，从而Observable可以在需要的时候发出事件来通知Observer

与传统观察者模式不同，RxJava的事件回调方法除了普通事件onNext()(相当于onClick()/onEvent())之外，还定义了两个特殊的事件：onCompleted()和onError()。

- onCompleted():事件队列完结。RxJava不仅把每个事件单独处理，还会把它们看做一个队列。RxJava规定，当不会再有新的onNext()发出时，需要触发onCompleted()方法作为标志。
- onError():事件队列异常。在事件处理过程中出异常时，onError()会被触发，同时队列自动终止，不允许再有事件发出。
- 在一个正确运行的事件序列中，onCompleted()和onError()有且只有一个，并且是时间序列中的最后一个。需要注意的是，onCompleted()和onError()二者也是互斥的，即在队列中调用了其中一个，就不应该再调用另一个。

RxJava的观察者模式大致如下图：

![](http://ww3.sinaimg.cn/mw1024/52eb2279jw1f2rx46dspqj20gn04qaad.jpg)


###基本实现