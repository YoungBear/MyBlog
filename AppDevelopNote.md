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

###6.1.7 遍历集合同时删除其中元素

ConcurrentModificationException

```
        HashMap<Integer, String> map = new HashMap<>();
        for (int i = 0; i < 10; i++) {
            map.put(i, "value " + i);
        }
        for (Map.Entry<Integer, String> entry : map.entrySet()) {
            Integer key = entry.getKey();
            if (key % 2 == 0) {
                map.remove(key);
            }
        }
```

遍历一个集合时不能删除该集合中的元素。

解决方案，需要再定义一个列表集合delList，用来保存需要删除的对象。

还有另一种产生这种崩溃的情况，那就是在多个线程中删除同一个集合中的元素。

如下列代码所示，vector是一个集合，我们建立了两个线程，线程1对其进行遍历，线程2对其进行插入操作。由于这两个线程同时在执行，所以就会产生ConcurrentModificationException的异常了:





























