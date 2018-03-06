# Kotlin 学习笔记

## 1. String

### 1.1 字符串转化为字符数组

**toCharArray()**，相当于java的toCharArray()

```
    /**
     * 字符串转化为字符数组 toCharArray()，相当于java的toCharArray()
     */
    val str:String = "Hello"
    val chars = str.toCharArray()
    for (i in 0 until chars.size){
        println("i: " + i + ", ch: " + chars[i])
    }
```

### 1.2 字符数组转化为字符串

**String(array)**，相当于Java的String.valueOf(array)

```
    /**
     * 字符数组转化为字符串 String(array)，相当于Java的String.valueOf(array)
     */
    val array1:CharArray = charArrayOf('a','b','c')
    println(String(array1))
```

## 2. 循环

### 2.1 for循环中，0..n表示从0到n

```
    val n:Int = 10
    /**
     * for循环中，0..n表示从0到n
     */
    for (i in 0..n){
        println(i)
    }
```

### 2.2 for循环中，0 until n表示从0到n-1

```
    val n:Int = 10
    /**
     * for循环中，0 until n表示从0到n-1
     */
    for (i in 0 until n){
        println(i)
    }
```

### 2.3 循环遍历数组元素

使用for-each

```
    val words:Array<String> = arrayOf("a", "bb", "acd", "ace")
    for (word:String in words) {
        println(word)
    }
```

## 3. 数组

## 3.1 新建一个数组，指定长度

```
val result: IntArray = IntArray(len)
```

## 3.2 使用intArrayOf()初始化数组元素，类似还有booleanArrayOf()等：

```
val arrA = intArrayOf(12, 28, 46, 32, 50)
```

## 3.3 字符串数组

```
val words:Array<String> = arrayOf("a", "bb", "acd", "ace")
```


