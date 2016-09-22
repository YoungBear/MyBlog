# 观察者模式 #
　　本文github地址：
　　https://github.com/YoungBear/MyBlog/blob/master/Observer.md

　　设计原则：为了交互对象之间的<font color=red>松耦合</font>而努力。

　　观察者模式定义了对象之间的一对多依赖，这样一来，当一个对象改变状态是，它的<font color=red>所有依赖者</font>都会收到通知并自动更新。

　　观察者模式是一个使用率非常高的模式，它最常使用的地方是GUI系统、订阅--发布系统。以为这个模式的一个重要作用就是<font color=red>解耦</font>，将被观察者和观察者解耦，使得它们之间的依赖性更小，甚至做到毫无依赖。

　　JDK内置类型：Observer 和 Observable，Observer是抽象的观察者角色，Observable是抽象的主题(被观察者)角色。

```java
public class Coder implements Observer {
    // 观察者
    private String name;

    public Coder(String name) {
        this.name = name;
    }

    @Override
    public void update(Observable arg0, Object arg1) {
        System.out.println("Hi, " + name + ", DevTechFrontier has updated, content: " + arg1);
    }

    @Override
    public String toString() {
        return "Coder : " + name;
    }
}

public class DevTechFrontier extends Observable {
    // 被观察者
    public void postNewPublication(String content) {
        // 标识状态或者内容发生改变
        setChanged();
        // 通知所有观察者
        notifyObservers(content);
    }
}

public class Test {

    public static void main(String[] args) {
        // 被观察者
        DevTechFrontier devTechFrontier = new DevTechFrontier();

        // 观察者
        Coder mrSimple = new Coder("mr.simple");
        Coder coder1 = new Coder("coder-1");
        Coder coder2 = new Coder("coder-2");
        Coder coder3 = new Coder("coder-3");

        // 注册
        devTechFrontier.addObserver(mrSimple);
        devTechFrontier.addObserver(coder1);
        devTechFrontier.addObserver(coder2);
        devTechFrontier.addObserver(coder3);

        // 发布消息
        devTechFrontier.postNewPublication("This is new Publication!");

    }
}

```

　　demo地址：　　　  
　　https://github.com/YoungBear/DesignPattern/tree/master/src/com/example/observer

　　Android的自大组件之一BroadcastReceiver，它作为应用内、进程间的一种重要通信手段，能够将某个消息通过广播的形式传递给它注册的对应广播接收器的对象，接收对象需要通过Context的registerReceiver函数注册到AMS(ActivityManagerService)中，当通过sendBroadcast发送广播时，所有注册了对应的IntentFilter的BroadcastReceiver对象就会收到这个消息，BroadcastReceiver的onReceive方法就会被调用，这就是一个典型的发布--订阅系统，也就是我们的观察者模式。

　　Android中的ListView，我们在ListView添加数据后，都会调用Adapter的notifyDataSetChanged()方法，这也是一个典型的观察者模式。