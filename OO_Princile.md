#面向对象的六大原则

- 单一职责原则 Single Responsibility Principle, SRP
- 开闭原则 Open Close Principle, OCP
- 里氏替换原则 Liskov Substitution Principle, LSP
- 依赖倒置原则 Dependence Inversion Principle, DIP
- 接口隔离原则 Interface Segregation Principle, ISP 
- 迪米特原则 Law of Demeter, LOD


##单一职责原则：

就一个类而言，应该仅有一个引起它变化的原因。简单地说，一个类中应该是一组相关性很高的函数、数据的封装。

##开闭原则

软件中的对象（类、模块、函数等）应该对于扩展是开放的，但是，对于修改是封闭的。

##里氏替换原则

所有引用基类的地方必须能透明地使用其子类的对象。

##依赖倒置原则

依赖倒置原则指代了一种特定的解耦形式，使得高层次的模块不依赖于低层次的模块的实现细节的目的，依赖模块被颠倒了。

依赖倒置原则有以下几个关键点：

1. 高层模块不应该依赖低层模块，两者都应该依赖其抽象；
2. 抽象不应该依赖细节；
3. 细节应该依赖抽象。

##接口隔离原则

客户端不应该依赖它不需要的接口。

另一种定义：类间的依赖关系应该建立在最小的接口上。

##迪米特原则

迪米特原则，也称为最少知识原则（Least Knowledge Principle）。

一个对象应该对其他对象有最少的了解。



