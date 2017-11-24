# python 字典

python中的字典，即dict，全称是dictionary，在其它语言中称为map。使用键-值（key-value）存储，具有极快的查找速度。

## python字典的特点

注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

1. 查找和插入的速度极快，不会随着key的增加而变慢；
2. 需要占用大量的内存，内存浪费多。

而list相反：

1. 查找和插入的时间随着元素的增加而增加；
2. 占用空间小，浪费内存很少。

所以，dict是用**空间来换取时间**的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是<font color=red>**不可变对**象</font>。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key。

由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值覆盖掉。

## 初始化字典

### 1. 使用花括号{}

```
>>> dict1 = {'one' : 1, 'two' : 2}
>>> dict1
{'one': 1, 'two': 2}
```

### 2. 使用dict()函数

参数为**列表套元组**或者**元组套列表**，**列表套列表** 、**元组套元组**。

```
# 参数是一个列表，列表的元素是元组
>>> dict1 = dict([('one', 1), ('two', 2)])
>>> dict1
{'one': 1, 'two': 2}

# 参数是一个列表，列表的元素是列表
>>> dict1 = dict([['one', 1], ['two', 2]])
>>> dict1
{'one': 1, 'two': 2}

# 参数是一个元组，列表的元素是列表
>>> dict1 = dict((['one', 1], ['two', 2]))
>>> dict1
{'one': 1, 'two': 2}

# 参数是一个元组，列表的元素是元组
>>> dict1 = dict((('one', 1), ('two', 2)))
>>> dict1
{'one': 1, 'two': 2}
```

除了使用初始化，还可以向字典中**插入数据**：

`dict_name[key] = value`

```
>>> dict1 = {'one' : 1, 'two' : 2}
>>> dict1
{'one': 1, 'two': 2}
>>> dict1['three'] = 3
>>> dict1
{'one': 1, 'two': 2, 'three': 3}
>>> 
```

## dict操作

### 通过key值访问

**使用中括号**

`dict_name[key]` 如果key不存在，就会报错。

**通过get() 函数**

```
dict_name.get(key) # key不存在时，返回None
dict_name.get(key, defalut_value) # 指定默认值，key不存在时，返回默认值
```

**注意：返回None的时候Python的交互环境不显示结果。**

```
>>> dict1 = {'one' : 1, "two" : 2}
>>> dict1['one']
1
>>> dict1['three']
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    dict1['three']
KeyError: 'three'
>>> dict1.get('one')
1
>>> dict1.get('three')
>>> dict1.get('three', 0)
0
>>>
```

### 判断是否存在key

使用`key in dict`来判断key是否在字典中，返回布尔值。

```
>>> dict1
{'one': 1, 'two': 2}
>>> 'one' in dict1
True
>>> 'three' in dict1
False
```

### 使用pop获取值并删除键值对

```
>>> dict1 = {'one' : 1, 'two' : 2}
>>> dict1
{'one': 1, 'two': 2}
>>> dict1.pop('one')
1
>>> dict1
{'two': 2}
```

### 使用for each遍历字典

```
>>> dict1
{'Three': 3, 'one': 1, 'two': 2, 'Four': 4}
>>> for key in dict1.keys():
	print(key, dict1[key])

	
Three 3
one 1
two 2
Four 4
```

### 使用deepcopy进行字典的深拷贝

```
>>> import copy
>>> dict1
{'Three': 3, 'one': 1, 'two': 2, 'Four': 4}
>>> dict2 = copy.deepcopy(dict1)
>>> dict2
{'Three': 3, 'one': 1, 'two': 2, 'Four': 4}
>>> dict2.clear()
>>> dict2
{}
>>> dict1
{'Three': 3, 'one': 1, 'two': 2, 'Four': 4}
```

## 字典常用api

1. **dict.keys()** 返回包含字典所有key的列表。
2. **dict.values()** 返回包含字典所有value的列表。
3. **dict.items()** 返回包含所有（键，值）项的列表。
4. **dict.clear()** 删除字典中的所有项或元素，无返回值(注意，不是删除字典，而是清空字典内容）
5. **dict.get(key , default=None)** 返回字典中key对应的值，若key不存在，则返回default的值（default默认为None）
6. **dict.pop(key [,default])** 如果字典中存在key，则<font color=red>删除</font>并返回key对应的value；如果key不存在，且没有给出default值，则引发KeyError异常。
7. **dict.setdefault(key , default = None)** 如果字典不存在key，则由dict[key] = default为其赋值。
8. **dicta.update(dictb)** 将字典dictb中键值对添加到dicta中。

# python 集合set

## 参考

[廖雪峰 Python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)