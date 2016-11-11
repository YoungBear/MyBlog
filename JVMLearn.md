#深入理解Java虚拟机 读书笔记

##两种异常

- StackOverflowError: 线程请求的<font color=red>栈深度</font>大于虚拟机所允许的最大空间
- OutOfMemoryError: 虚拟机在扩展栈时无法申请到足够的内存空间

但是，这两种异常存在着一些互相重叠的地方：当栈空间无法继续分配是，到底是内存太小，还是已使用的栈空间太大，其本质上只是对同一件事情的两种描述而已。

##String是final类型的，所以String不能被继承

##String.intern()：
　　**<font color=red>如果字符串常量池中已经包含一个等于此String对象的字符串，则返回代表池中这个字符串的String对象；否则，将此String对象包含的字符串添加到常量池中，并且返回此String对象的引用。</font>**

*注：“==” 比较的是两个对象的引用(内存地址)是否相同*

###采用new 创建的字符串对象，不会进入字符串常量池
```
        String a = "abc";
        String b = new String("abc");
        String c = "abc";
        System.out.println("a == b: " + (a == b));//输出为false
        System.out.println("b.intern() == a: " + (b.intern() == a));//输出为true
        System.out.println("a == c : " + (a == c));//输出为true
```
- 字符串"abc"已经在字符串常量池中，并有一个引用a。
- 而变量b是new出来的String，则b是一个新的引用，故有a == b 为false。
- 由于字符串常量池中已经有"abc"了，所以a.intern()返回的是字符串常量池中的该字符串的引用，所以会有b.intern() == a 为true。
- 引用c也指向字符串常量池中的"abc"，所以a == c 为true。

###字符串相加的时候，都是静态字符串的结果会添加到字符串常量池，如果其中包含变量，则不会进入字符串常量池
```
        String a = "abcd";
        String b = "ab" + "cd";
        String c = "ab";
        String d = c + "cd";
        String e = c + "cd";
        System.out.println("a == b : " + (a == b));//输出为true
        System.out.println("a == d : " + (a == d));//输出为false
        System.out.println("d == e : " + (d == e));//输出为false

        System.out.println(d.intern() == e);
```
- 字符串"abcd"已经在字符串常量池中，并有一个引用a。
- 引用b引用静态字符串"ab" + "cd"，则b所引用的对象也在字符串常量池中，故a == b 为true。
- 引用d是变量c+常量"cd"，包含了变量，则不会进入字符串常量池，而会有一个新的引用，故a == d 为false。
- 同理，e也已是一个新的引用，故有 d == e 为false。

　　这是今天在看《深入理解Java虚拟机》这本java经典读物，看到有关方法区和运行时常量池这块，才发现String还有这么多的坑，所以就自己实际写测试代码看了下，小小的总结下。String经常会在面试中问到，所以深入理解了还是很重要的。