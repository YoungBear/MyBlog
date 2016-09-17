# Java 自动装箱与拆箱(Autoboxing and unboxing) #

## 什么是自动装箱拆箱 ##

基本数据类型的自动装箱、拆箱是自J2SE 5.0开始提供的功能。

一般我们要创建一个类的对象实例的时候，我们会这样：

`Class a = new Class(parameter);`

当我们创建了一个Integer对象时，却可以这样:

`Integer i = 100;`(注意：不是 int i = 100;)

实际上，执行上面那句代码的时候，系统为我们执行了

`Integer i = Integer.valueOf(100);`

　　此即基本数据类型的<font color=red>自动装箱</font>功能。

## 什么时候自动装箱 ##
　　例如： Integer i = 100;

　　相当于编译器自动为您作以下的语法编译:

　　Integer i = Integer.valueOf(100);

## 什么时候自动拆箱 ##
　　自动拆箱(unboxing)，也就是将对象中的基本数据从对象中自动取出。如下可实现自动拆箱：

```
Integer i = 10;//装箱
int t = i;//拆箱，实际上执行了 int t = i.intValue();
```
　　在进行运算时，也可以进行拆箱。

```
Integer i = 10;
System.out.println(i++);
```

## Integer的自动装箱 ##
//在-128~127以外的数

Integer i1 = 200;

Integer i2 = 200;

System.out.println("i1 == i2: " + (i1 == i2));

//在-128~127之内的数

```
Integer i3 = 100;
Integer i4 = 100;
System.out.println("i3 == i4: " + (i3 == i4));
```

输出结果为：

```
i1 == i2: false
i3 == i4: true

```
说明：

equals()比较的是两个对象的值(内容)是否相同。

　　"==" 比较的是两个对象的引用(内存地址)是否相同，也用来比较两个<font color=red>基本数据类型</font>的变量值是否相等。

　　前面说过，int的自动装箱，是系统执行了Integer.valueOf(int i),先看看Integer.java的源代码：

```
// 没有设置的话，IngegerCache.high 默认是127
// IntegerCache.low是-128
public static Integer valueOf(int i) {
    if (i >= IntegerCache.low && i <= IntegerCache.high)
        return IntegerCache.cache[i + (-IntegerCache.low)];
    return new Integer(i);
}
```

　　对于–128到127（默认是127）之间的值，Integer.valueOf(int i) 返回的是缓存的Integer对象（并不是新建对象）

　　所以范例中，i3 与 i4实际上是指向同一个对象。

　　而其他值，执行Integer.valueOf(int i) 返回的是一个新建的 Integer对象，所以范例中，i1与i2 指向的是不同的对象。

　　当然，当不使用自动装箱功能的时候，情况与普通类对象一样，请看下例：

```
Integer i3 =new Integer(100); 
Integer i4 =new Integer(100); 
System.out.println("i3 == i4: "+(i3 == i4));//显示false
```

### Integer自动装箱拆箱总结 ###
自动装箱调用：Integer.valueOf(int n);

自动拆箱调用：Integer.intValue();


## String 的拆箱装箱 ##

　　第一个例子：

```
String str1 = "abc";
String str2 = "abc";
System.out.println("str1 == str2: " + (str1 == str2)); // 输出为 true
System.out.println("str1.equals(str2): " + str1.equals(str2)); // 输出为 true

String str3 = new String("abc");
String str4 = new String("abc");
System.out.println("str3 == str4: " + (str3 == str4)); // 输出为 false
System.out.println("str3.equals(str4): " + str3.equals(str4)); // 输出为 true
```

　　第二个例子：

```
String d = "2";
String e = "23";
e = e.substring(0, 1);
System.out.println("e.equals(d): " + e.equals(d)); // 输出为 true
System.out.println("e == d: " + (e == d)); // 输出为 false
```

　　第二个例子中，e的初始值与d并不同，因此e与d是各自创建了个对象，（e == d）为false。

　　同理可知，第一个例子中的str3与str4也是各自new了个对象，而str1与str2却是<font color=red>引用了同一个对象</font>。

参考：

http://www.cnblogs.com/danne823/archive/2011/04/22/2025332.html















