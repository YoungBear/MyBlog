# 装饰者模式 #

　　本文github地址：

　　https://github.com/YoungBear/MyBlog/blob/master/Decorator.md

　　Decorator Pattern，也称为包装模式(Wrapper Pattern)。

　　装饰者模式，动态地将责任附加到对象上。想要扩展功能，装饰者提供有别于继承的另一种选择。

　　特点：装饰者和被装饰者必须是一样的类型，即<font color=red>有共同的超类</font>。

　　类图：

![装饰者模式UML类图](http://img.blog.csdn.net/20160922135701138 "")

　　角色介绍：

　　Compontent:抽象组件。

　　可以是一个接口或者抽象类，其充当的就是被装饰的原始对象，所有装饰者和被装饰者都继承或实现它。

　　ConcreteComponent:组件具体实现类。

　　该类使Component的基本实现，也是我们装饰的具体对象，即被装饰者。

　　Decorator：抽象装饰者。

　　顾名思义，其承担的职责就是为了装饰我们的组件对象，其内部一定要有一个<font color=red>指向组件对象的引用</font>。在大多是情况下，该类为抽象类，需要根据不同的装饰逻辑实现不同的具体子类。当然，如果装饰逻辑单一，只有一个的情况下我们可以省略该类直接作为具体的装饰者。

　　ConcreteDecoratorA: 装饰者具体实现类。

　　只是对抽象装饰者做出具体的实现。

　　Java I/O 中广泛用到了装饰者模式。

 　　一个简单的demo：
 
```java
// 作为Compontent，即被装饰的原始对象
// 人总是要穿衣服的，我们将人定义为一个抽象类，将其穿衣的行为定义为一个抽象方法
public abstract class Person {

    public abstract void dressed();

}

// ConcreteComponent，装饰的具体对象
// Boy 类是我们所要装饰的具体对象，先在需要一个装饰者来修饰我们的这个Boy对象
// 这里定义一个PersonCloth类来表示人所穿着的衣服
public class Boy extends Person {

    @Override
    public void dressed() {
    }
}

// Decorator，抽象装饰者
public abstract class PersonCloth extends Person {
    // 保持一个Person类的引用
    // 可以方便地调用具体被装饰对象中的方法
    protected Person mPerson;

    public PersonCloth(Person mPerson) {
        this.mPerson = mPerson;
    }

    @Override
    public void dressed() {
        // 调用Person类中的dressed方法
        mPerson.dressed();
    }
}

//高档衣服
public class ExpensiveCloth extends PersonCloth {
    public ExpensiveCloth(Person mPerson) {
        super(mPerson);
    }

    private void dressShirt() {
        System.out.println("dress a T-shirt");
    }

    private void dressLeather() {
        System.out.println("dress a Leather");
    }

    private void dressJean() {
        System.out.println("dress Jean Pants");
    }

    @Override
    public void dressed() {
        super.dressed();
        dressShirt();
        dressLeather();
        dressJean();
    }
}

// 便宜衣服
public class CheapCloth extends PersonCloth {
    public CheapCloth(Person mPerson) {
        super(mPerson);
    }

    private void dressShorts() {
        System.out.println("dress short pants");
    }

    @Override
    public void dressed() {
        super.dressed();
        dressShorts();
    }

}

// 测试程序
public class Test {

    public static void main(String[] args) {
        // 首先我们要有一个Person男孩
        Person person = new Boy();

        // 穿上便宜衣服
        PersonCloth clothCheap = new CheapCloth(person);
        clothCheap.dressed();

        // 穿上高级衣服
        PersonCloth clothExpensive = new ExpensiveCloth(person);
        clothExpensive.dressed();
    }
}


```

　　demo地址：
　　https://github.com/YoungBear/DesignPattern/tree/master/src/com/example/decorator