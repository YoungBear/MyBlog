# Python 系列笔记

[Python 元组](https://github.com/YoungBear/MyBlog/blob/master/md_files/python/md_files/python_tuple.md)

[Python 列表](https://github.com/YoungBear/MyBlog/blob/master/md_files/python/md_files/python_list.md)

[Python 字典](https://github.com/YoungBear/MyBlog/blob/master/md_files/python/md_files/python_dict.md)

[<font color=red>**Python 集合**</font>](https://github.com/YoungBear/MyBlog/blob/master/md_files/python/md_files/python_set.md)

[geopy 在python中的使用](https://github.com/YoungBear/MyBlog/blob/master/md_files/python/geopy.md)

## 集合简介

python中的集合是一种**不重复**的**无序集**，与java中的Set类似。使用花括号{}来定义。

可以说，set是一组存放key的集合。

## 创建集合

可以使用`{}`和`set()`函数两种方式来创建一个集合。

### 1. 使用花括号创建

集合元素是不可变类型，所以可以使用数值，字符串，元组，而不能使用列表，字典当做元素值。

```
>>> set1 = {1,2,'three', 'four', (10, 11)}
>>> set1
{'four', 2, (10, 11), 'three', 1}
```

如果你创建时在集合中写了重复的值，不会报错，但根据互异性，只会保存一个：

```
>>> set2 = {1,2,3,3,4}
>>> set2
{1, 2, 3, 4}
```

创建**空集合**要使用<font color=red>**set()**</font>，而不能使用**{}**，因为后者指的是创建空字典。

```
>>> set3 = set()
>>> set3
set()
```

### 2. 使用set()函数创建

参数可以使用**列表**，或者**元组**。该集合的元素就是列表或元组的元素。

还可以使用**字符串**来创建集合，得到的集合的元素是字符串的每个字符。

**注意：集合会自动过滤相同的重复元素，只保留一个元素。**

```
# 使用列表创建集合
>>> set4 = set([1,2,3,4,5])
>>> set4
{1, 2, 3, 4, 5}

# 使用元组创建集合
>>> set5 = set(('one', 'two', 'three', 'four'))
>>> set5
{'one', 'two', 'four', 'three'}

# 使用字符串创建集合
>>> set6 = set('Hello')
>>> set6
{'e', 'o', 'H', 'l'}
```

## 集合常用api

1. **set.add(key)** 集合添加一个元素。
2. **seta.update(setb)** 将集合setb中的元素添加到集合seta中。与字典的update函数类似。
3. **set.pop()** 删除并且返回集合中的**任意元素**。
4. **set.remove(key)** 删除集合中的元素key，如果key不存在就**报错**。无返回值。
5. **set.discard(key)** 删除集合中的元素key，如果key不存在则**什么也不做**。无返回值。
6. **set.clear()** 清空集合。

## 集合的遍历

使用for each来遍历集合

```
>>> set5
{'one', 'e', 'H', 'l', 'three'}
>>> for key in set5:
	print(key)

	
one
e
H
l
three
>>> 
```

## 集合数学运算

[参考](http://blog.csdn.net/isoleo/article/details/13000975)

### 符号对应关系

![符号对应关系](http://img.blog.csdn.net/20171124143405421?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### 1. 交集

**&** 和  **intersection()**

```
>>> set1 = {1,2,3,4,5}
>>> set2 = {4,5,6,7,8}
>>> set1 & set2
{4, 5}
>>> set1.intersection(set2)
{4, 5}
```

### 2. 并集

**|**  和  **union()**

```
>>> set1 = {1,2,3,4,5}
>>> set2 = {4,5,6,7,8}
>>> set1 | set2
{1, 2, 3, 4, 5, 6, 7, 8}
>>> set1.union(set2)
{1, 2, 3, 4, 5, 6, 7, 8}
```

### 3. 差集

**-**  和  **different**

```
>>> set1 = {1,2,3,4,5}
>>> set2 = {4,5,6,7,8}
>>> set1 - set2
{1, 2, 3}
>>> set1.difference(set2)
{1, 2, 3}
```

### 4. 异或

**^** 和 **symmetric_difference**

```
>>> set1 = {1,2,3,4,5}
>>> set2 = {4,5,6,7,8}
>>> set1 ^ set2
{1, 2, 3, 6, 7, 8}
>>> set1.symmetric_difference(set2)
{1, 2, 3, 6, 7, 8}
```

### 5. 子集

**<=**  和  **issubset**

```
>>> set1 = {1, 2, 3, 4, 5}
>>> set2 = {4, 5, 6, 7, 8}
>>> set3 = {1, 2, 3, 4}
>>> set3 <= set1
True
>>> set3 <= set2
False
>>> set3.issubset(set1)
True
>>> set3.issubset(set2)
False
```

### 6. 父集

>=  和  issuperset

```
>>> set1 = {1, 2, 3, 4, 5}
>>> set2 = {4, 5, 6, 7, 8}
>>> set3 = {1, 2, 3, 4}
>>> set1 >= set3
True
>>> set2 >= set3
False
>>> set1.issuperset(set3)
True
>>> set2.issuperset(set3)
False
```

### 7. 包含

**in** 判断元素是否在集合中

```
>>> set1 = {1, 2, 3, 4, 5}
>>> 1 in set1
True
>>> 6 in set1
False
```

### 8. 不包含

**not in** 判断元素是否不在集合中

```
>>> set1 = {1, 2, 3, 4, 5}
>>> 1 not in set1
False
>>> 6 not in set1
True
```

### 相关的update函数
不带update的函数，表示将结果生成新的一个集合并返回；

带update的函数，表示将结果赋予调用的集合，没有返回值。

比如说，求并集的预算函数set1.intersection_update(set2)相当于
set1 &= set2，即set1 = set1.interection(set2)。其他的函数类似。

```
# 使用 &=
>>> set1 = {1, 2, 3, 4, 5}
>>> set2 = {4, 5, 6, 7, 8}
>>> set1 &= set2
>>> set1
{4, 5}

# 使用 intersection_update
>>> set1 = {1, 2, 3, 4, 5}
>>> set2 = {4, 5, 6, 7, 8}
>>> set1.intersection_update(set2)
>>> set1
{4, 5}
>>> 
```

**相关运算符及对应函数：**

|运算符号    |对应函数    |
|:----------:|:----------:|
|&=          |intersection_update|
|-=          |difference_update|
|^=          |symmetric_difference_update|






