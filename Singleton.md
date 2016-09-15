　　单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例的特殊类。通过单例模式可以保证系统中一个类只有一个实例。
## 1. 单例模式的用途 ##
　　单例模式主要是为了避免因为创建了多个实例造成资源的浪费，且多个实例由于多次调用容易导致结果出现错误，而使用单例模式能够保证整个应用中有且只有一个实例。从其名字中我们就可以看出所谓单例，就是单个实例也就是说它可以解决的问题是：可以保证一个类在内存中的对象的唯一性，在一些常用的工具类、线程池、缓存，数据库，账户登录系统、配置文件等程序中可能只允许我们创建一个对象，一方面如果创建多个对象可能引起程序的错误，另一方面创建多个对象也造成资源的浪费。在这种基础之上单例设计模式就产生了因为使用单例能够保证整个应用中有且只有一个实例。
## 2. 单例模式的要点 ##

###单例模式的类只提供私有的构造函数###
 
###类定义中含有一个该类的静态私有对象###

###该类提供了一个静态的公有的函数用于创建或获取它本身的静态私有对象###
## 3. 单例模式的写法 ##
 

### 3.1 饿汉式[线程安全] ###

 
```
public class Singleton {
    private static  Singleton instance = new Singleton();
    private Singleton() {}
    public static  Singleton getInstance() {
        return instance;
    }
}
```

　　<font color=red>优点</font>：从它的实现中我们可以看到，这种方式的实现比较简单，在类加载的时候就完成了实例化，避免了线程的同步问题。

　　<font color=red>缺点</font>：由于在类加载的时候就实例化了，所以没有达到Lazy Loading(懒加载)的效果，也就是说可能我没有用到这个实例，但是它也会加载，会造成内存的浪费(但是这个浪费可以忽略，所以这种方式也是推荐使用的)。

### 3.2 懒汉式 ###

　　在调用getInstance方法的时候才创建对象的，所以它比较懒因此被称为懒汉式。

#### 3.2.1. 线程不安全，不可用 ####
 
```
public class Singleton {
    private static Singleton instance;
    private Singleton() {}
    private static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```
　　线程不安全，在运行过程中可能存在这么一种情况：有多个线程去调用getInstance方法来获取Singleton的实例，那么就有可能发生这样一种情况当第一个线程在执行if(instance==null)这个语句时，此时instance是为null的进入语句。在还没有执行instance=new Singleton()时(此时instance是为null的)第二个线程也进入if(instance==null)这个语句，因为之前进入这个语句的线程中还没有执行instance=new Singleton()，所以它会执行instance=new Singleton()来实例化Singleton对象，因为第二个线程也进入了if语句所以它也会实例化Singleton对象。这样就导致了实例化了两个Singleton对象。

#### 3.2.2. 懒汉式线程安全的[线程安全，效率低不推荐使用] ####

```
public class Singleton {
    private static Singleton instance;
    private Singleton() {}
    private static synchronized Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```
　　<font color=red>缺点</font>：效率太低了，每个线程在想获得类的实例时候，执行getInstance()方法都要进行同步。而其实这个方法只执行一次实例化代码就够了，后面的想获得该类实例，直接return就行了。方法进行同步效率太低要改进。

#### 3.2.3  懒汉式变种，属于懒汉式中最好的写法，保证了：延迟加载和线程安全 ####

```
public class Singleton {
    private volatile static Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```
　　<font color=red>优点</font>：线程安全；延迟加载；效率较高。

　　在getInstance中做了两次null检查，确保了只有第一次调用单例的时候才会做同步，这样也是线程安全的，同时避免了每次都同步的性能损耗

### 3.3 内部类[推荐用] ###

```
public class Singleton {
    private Singleton() {}
    private static class SingletonHolder {
        private static Singleton instance = new Singleton();
    }
    public static Singleton getInstance() {
        return SingletonHolder.instance;
    }
}
```
　　这种方式跟饿汉式方式采用的机制类似，但又有不同。两者都是采用了<font color=red>类装载的机制</font>来保证初始化实例时只有一个线程。不同的地方在饿汉式方式是只要Singleton类被装载就会实例化，没有<font color=red>Lazy-Loading</font>的作用，而静态内部类方式在Singleton类被装载时并不会立即实例化，而是在需要实例化时，调用getInstance方法，才会装载SingletonHolder类，从而完成Singleton的实例化。类的静态属性只会在第一次加载类的时候初始化，所以在这里，JVM帮助我们保证了线程的安全性，在类进行初始化时，别的线程是无法进入的。
　　<font color=red>优点</font>：避免了线程不安全，延迟加载，效率高。
利用了classloader的机制来保证初始化instance时只有一个线程，所以也是线程安全的，同时没有性能损耗，所以推荐使用。

### 3.4 枚举[极推荐使用] ###

```
public enum SingletonEnum {

    instance;
    private SingletonEnum() {}
    public void method() {
    }
}
```
　　使用方法：
　　`SingletonEnum.instance.method();` 

　　可以看到枚举的书写非常简单，访问也很简单在这里SingletonEnum.instance这里的instance即为SingletonEnum类型的引用所以得到它就可以调用枚举中的方法了。

　　借助JDK1.5中添加的枚举来实现单例模式。不仅能避免<font color=red>多线程同步</font>问题，而且还能防止<font color=red>反序列化</font>重新创建新的对象，还能防止<font color=red>反射</font>时重新生成新的对象。可能是因为枚举在JDK1.5中才添加，所以在实际项目开发中，很少见人这么写过，这种方式也是最好的一种方式，如果在开发中JDK满足要求的情况下建议使用这种方式。

## 4. 饿汉式和懒汉式区别 ##

　　从<font color=red>名字</font>上来说，饿汉和懒汉，

　　饿汉就是类一旦加载，就把单例初始化完成，保证getInstance的时候，单例是已经存在的了，

　　而懒汉比较懒，只有当调用getInstance的时候，才回去初始化这个单例。

　　<font color=red>线程安全</font>：

　　饿汉式天生就是线程安全的，可以直接用于多线程而不会出现问题，

　　懒汉式本身是非线程安全的，为了实现线程安全有几种写法，分别是上面的3.2.2、3.2.3。
　　
## 5. 序列化、反射、clone破坏单例的sample和相应的解决方案 ##
参考：http://blog.csdn.net/three_man/article/details/42006475

　　该sample使用静态内部类形式的单例。
### 5.1 用序列化打破单例 ###

```
public class Singleton4 implements Serializable {

    private Singleton4() {
    }

    private static class SingletonHolder {
        /**
         * 静态初始化器，由JVM来保证线程安全
         */
        private static Singleton4 instance = new Singleton4();
    }

    private static Singleton4 getInstance() {
        return SingletonHolder.instance;
    }

    /**
     * 我们用序列化来打破单例
     * */
    public static void main(String[] args) throws Exception {
        Singleton4 s1 = Singleton4.getInstance();
        File objectF = new File("object");
        if (!objectF.exists()) {
            objectF.createNewFile();
        }
        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(
                objectF));
        out.writeObject(s1);
        out.close();
        ObjectInputStream in = new ObjectInputStream(new FileInputStream(
                objectF));
        Singleton4 s2 = (Singleton4) in.readObject();
        in.close();
        System.out.println("s1 == s2 ?: " + (s1 == s2));
    }

}
```

上面程序输出结果为:

s1 == s2 ?: false

结果表明，序列化和反序列化破坏了单例。

解决方案：

增加readResolve方法，Java反序列化的时候会用这个方法的返回值直接代替序列化得到的对象。

```
public class Singleton4 implements Serializable {

    private Singleton4() {
    }

    private static class SingletonHolder {
        /**
         * 静态初始化器，由JVM来保证线程安全
         */
        private static Singleton4 instance = new Singleton4();
    }

    private static Singleton4 getInstance() {
        return SingletonHolder.instance;
    }

    // 需要增加readResolve方法，Java反序列化的时候会用这个方法的返回值直接代替序列化得到的对象
    private Object readResolve() {
        return SingletonHolder.instance;
    }

    /**
     * 我们用序列化来打破单例
     * */
    public static void main(String[] args) throws Exception {
        Singleton4 s1 = Singleton4.getInstance();
        File objectF = new File("object");
        if (!objectF.exists()) {
            objectF.createNewFile();
        }
        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(
                objectF));
        out.writeObject(s1);
        out.close();
        ObjectInputStream in = new ObjectInputStream(new FileInputStream(
                objectF));
        Singleton4 s2 = (Singleton4) in.readObject();
        in.close();
        System.out.println("s1 == s2 ?: " + (s1 == s2));
    }

}
```

输出结果为:

s1 == s2 ?: true

### 5.2 通过反射来打破其的单例性 ###

```
public class Singleton5 {

    private Singleton5() {
    }

    private static class SingletonHolder {
        /**
         * 静态初始化器，由JVM来保证线程安全
         */
        private static Singleton5 instance = new Singleton5();
    }

    private static Singleton5 getInstance() {
        return SingletonHolder.instance;
    }

    //通过反射来打破其的单例性,说明使用反射调用私有构造器也是可以破坏单例的
    public static void main(String[] args) throws Exception{
        Singleton5 s1 = Singleton5.getInstance();
        Constructor<Singleton5> c = Singleton5.class.getDeclaredConstructor();
        c.setAccessible(true);
        Singleton5 s2 = c.newInstance();
        System.out.println("s1 == s2 ?: " + (s1 == s2));  
    }
```

上面程序输出的结果是:

s1 == s2 ?: false

表明使用反射调用私有构造器也是可以破坏单例的。

解决方案：

用一个计数器来记录构造函数调用的次数，如果大于，则抛出异常。

```
public class Singleton5 {
    
    //解决方法，用一个计数器来记录构造函数调用的次数，如果大于，则抛出异常
    private static int COUNT = 0;
    private Singleton5() {
        if(++COUNT > 1){  
            throw new RuntimeException("can not be construt more than once");  
        }
    }
    
    private static class SingletonHolder {
        /**
         * 静态初始化器，由JVM来保证线程安全
         */
        private static Singleton5 instance = new Singleton5();
    }

    private static Singleton5 getInstance() {
        return SingletonHolder.instance;
    }

    //通过反射来打破其的单例性,说明使用反射调用私有构造器也是可以破坏单例的
    public static void main(String[] args) throws Exception{
        Singleton5 s1 = Singleton5.getInstance();
        Constructor<Singleton5> c = Singleton5.class.getDeclaredConstructor();
        c.setAccessible(true);
        Singleton5 s2 = c.newInstance();
        System.out.println("s1 == s2 ?: " + (s1 == s2));  
    }
}
```

输出结果：

抛出了异常：

java.lang.RuntimeException: can not be construt more than once
at com.example.singleton.Singleton5.<init>

### 5.3 通过clone来破坏单例性 ###

```
public class Singleton6 implements Cloneable {

    private Singleton6() {
    }

    private static class SingletonHolder {
        private static Singleton6 instance = new Singleton6();
    }

    public static Singleton6 getInstance() {
        return SingletonHolder.instance;
    }

    // 用clone来破坏单例性
    public static void main(String[] args) throws CloneNotSupportedException {
        Singleton6 s1 = Singleton6.getInstance();
        Singleton6 s2 = (Singleton6) s1.clone();
        System.out.println("s1 == s2 ?: " + (s1 == s2));
    }
}
```

上面程序输出的结果是:

s1 == s2 ?: false

解决方案:

重写clone方法，返回单例对象即可。

```
public class Singleton6 implements Cloneable {

    private Singleton6() {
    }

    private static class SingletonHolder {
        private static Singleton6 instance = new Singleton6();
    }

    public static Singleton6 getInstance() {
        return SingletonHolder.instance;
    }

    // 解决方案，重写clone方法
    @Override
    protected Object clone() throws CloneNotSupportedException {
        return SingletonHolder.instance;
    }

    // 用clone来破坏单例性
    public static void main(String[] args) throws CloneNotSupportedException {
        Singleton6 s1 = Singleton6.getInstance();
        Singleton6 s2 = (Singleton6) s1.clone();
        System.out.println("s1 == s2 ?: " + (s1 == s2));
    }
}
```

### 5.4 当枚举单例遇到序列化、反射、clone ###

####通过反序列化其也会返回INSTANCE对象。####

####使用反射，会抛出异常:####
java.lang.NoSuchMethodException:com.example.singleton.TestEnum.<init>()#

####没有clone方法。####

```TestEnum.java
public enum TestEnum implements Serializable, Cloneable{
    //定义一个枚举的元素，它就代表了Singleton的一个实例
    instance;
    public void method() {
        //do something
    }
    //调用方法 SingleEnum.instance.method();
}
```

```
public class TestEnumLearn {

    public static void main(String[] args) throws Exception {
        TestEnum s1 = TestEnum.instance;
        File objectF = new File("object");
        if (!objectF.exists()) {
            objectF.createNewFile();
        }
        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(
                objectF));
        out.writeObject(s1);
        out.close();
        ObjectInputStream in = new ObjectInputStream(new FileInputStream(
                objectF));
        // 通过反序列化其也会返回INSTANCE对象
        TestEnum s2 = (TestEnum) in.readObject();
        in.close();
        System.out.println("s1 == s2 ?: " + (s1 == s2));

        // 运行时异常java.lang.NoSuchMethodException:
        // com.example.singleton.TestEnum.<init>()
        Constructor<TestEnum> c = TestEnum.class.getDeclaredConstructor();
        c.setAccessible(true);
        TestEnum s3 = c.newInstance();
        System.out.println("s1 == s3 ?: " + (s1 == s3));

        // 其没有clone方法
    }
}
```

## 小插曲 ##
　　有一次去Ｎ公司面试Android开发，让写一个单例模式。我使用内部类完成了，面试官问这种内部类是饿汉还是懒汉方式，以及内部类写法和double check写法的区别，我的回答是内部类写法算是饿汉式，但又和普通饿汉不一样，因为普通饿汉式是在内加载完成的时候，就创建了对象，而内部类是在第一次调用getInstance()的时候，才会创建对象。和double check的区别，没回答好，回答只是写法不一样，可能没有get到面试官的意思吧。我提了一句枚举类型，面试官又问了区别，回答了写法简单，能防止反射和序列化，面试官疑惑：<font color=red>跟反射和序列化有关系吗？</font>当时不太肯定，也没有争辩，如果看过提前看过这个文章的话，肯定会跟他好好聊聊的。

　　那次表现太差了，很多Android基础的知识都没回答好，然后，就没有然后了。

参考：

http://blog.csdn.net/dmk877/article/details/50311791
http://blog.csdn.net/jason0539/article/details/23297037/
http://www.iteye.com/topic/652440



