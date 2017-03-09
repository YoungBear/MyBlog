#App研发录 读书笔记

##Activity的onCreate()方法中做以下三件事情：

1. initVariables 初始化变量
2. initViews 初始化组件
3. loadDatas 加载数据


##6.1 Java语法相关异常
###6.1.1 空指针 NullPointException

###6.1.2 角标越界
关键字：

1. indexOutOfBoundsException
2. StringIndexOutOfBoundsException
3. ArrayIndexOutOfBoundsException

###6.1.3 试图调用一个空对象的方法
关键字：

Attempt to invoke virtual method on a null object reference

###6.1.4 类型转换异常
关键字：

ClassCastException: classA cannot be cast to classB

这类Crash都是由于强制类型转换导致的，如下所示：

```
Object x = new Integer(0);
String str = (String) x;
```

折就会抛出ClassCastException的异常了。

解决方案是，使用安全类型转换函数，参见本书第1章中1.6节介绍的类型安全安全转换函数。在把字符串转换为整数、小数或布尔类型时，我们要为其制定<font color=red>转换失败时的默认值。</font>否则，就会得到一个空值，放到哪里使用都会崩溃。

###6.1.5 数字转换错误

NumberFormatException

在数据类型转换过程中，如果转换不成功，一般抛出ClassCastException的异常。只有一个例外情况，当字符型转换为数字失败时，Android系统会抛出NumberFormatException异常，如下所示：

```
String abc = "123xxx45";
int result = Integer.parseInt(abc);
```

这种情况多发生在服务器返回数据，没有按照约定返回整数而是字符串，客户端必须事先考虑到这种情况，如果转换失败，必须有默认值而不是直接就崩溃了。

###6.1.6 声明数组时长度为-1

NegativeArraySizeException

eg.

```
String[] arg1 = new String[args.length - 1];
```
当args数组中没有元素时，就会出现int[-1]的场景。
