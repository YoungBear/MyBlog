# Android MVP 架构

MVP ，即 Model - Presenter - View。

**Presenter 交互中间人**

Presenter主要作为沟通 View 和 Model 的桥梁，它从 Model 层检索数据后，返回给 View 层，使得 View 和 Model 没有耦合，也将业务逻辑从View角色上抽离出来。

**View 用户界面**

View通常是指 Activity、Fragment 或者某个 View 控件，<font color=red>**它含有一个 Presenter 成员变量**</font>。通常 View 需要实现一个<font color=red>**逻辑接口**</font>，将 View 上的操作会转交给 Presenter 进行实现，最后， Presenter 调用 View 的逻辑接口将结果返回给 View 元素。

**Model 数据的获取**

对于一个结构化的 App 来说， Model 角色主要是提供数据的存取功能。 Presenter 需要通过 Model 层存储，获取数据， Model 就像一个数据仓库。更直白地说， Model 是封装了数据库 DAO 或者网络获取数据的角色，或者两种数据获取方式的集合。

![MVP模式](http://img.blog.csdn.net/20171125094831024?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

在MVP里，如图，Presenter 完全将 Model 和 View 进行了分离，主要的程序逻辑在 Presenter 里实现。而且， Presenter 与具体的 View 是没有直接关联的，而是通过定义好的**接口**进行交互，从而使得在变更 View 时可以保持 Presenter 的不变，这点符合面向接口编程的特点。 View 只应该有简单的 get/set 方法，以及用户输入和 UI 更新的内容，除此之外就不应该有更多的内容。决不允许 View 直接访问 Model，这就是其与 MVC 的很大的不同之处。

# 代码练习

## [1. UserActivity](https://github.com/YoungBear/AndroidMVP/blob/master/md_files/android_mvp_user_activity.md)






## 参考

[谷歌官方MVP Demo：todoapp](https://github.com/googlesamples/android-architecture/tree/todo-mvp/)

[Android MVP 详解](http://www.jianshu.com/p/9a6845b26856)









