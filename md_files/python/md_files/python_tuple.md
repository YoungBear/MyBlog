# Python 系列笔记

 Python 元组

[Python 列表](https://github.com/YoungBear/MyBlog/blob/master/md_files/python/md_files/python_list.md)

[Python 字典](https://github.com/YoungBear/MyBlog/blob/master/md_files/python/md_files/python_dict.md)

[Python 集合](https://github.com/YoungBear/MyBlog/blob/master/md_files/python/md_files/python_set.md)


[geopy 在python中的使用](https://github.com/YoungBear/MyBlog/blob/master/md_files/python/geopy.md)



## 元组定义

元组和列表相似，可以存储不同类型的数据。但是，元组是<font color=red>不可改变</font>的，**创建后就不能做任何修改操作了**。

## 创建元组

- 使用一对小括号表示空元组:`()`
- 对只有一个元素的元组使用尾随逗号：`a,`或`(a,)`
- 以逗号分隔元素:`a, b, c` 或者 `(a, b, c)`
- 使用tuple()内建：`tuple()` 或 `tuple(iterable)`

```
# 创建一个空元组
>>> tuple1 = ()
>>> tuple1
()

# 使用一个逗号创建只有一个元素的元组，防止跟一个元素歧义。
>>> tuple1 = 'hello',
>>> tuple1
('hello',)
>>> tuple2 = ('hello',)
>>> tuple2
('hello',)

# 使用逗号分隔元素来创建元组
>>> tuple1 = 1,2,3
>>> tuple1
(1, 2, 3)
>>> tuple2 = ('a','b','c')
>>> tuple2
('a', 'b', 'c')

# 使用tuple()函数创建
>>> tuple1 = tuple()
>>> tuple1
()
>>> tuple2 = tuple('hello')
>>> tuple2
('h', 'e', 'l', 'l', 'o')
>>> tuple3 = tuple([1,2,3,4,5])
>>> tuple3
(1, 2, 3, 4, 5)
```

## 元组常用API

在Python中，元组，列表，range都属于序列类型(Sequence Types)。而序列类型有一些通用的API，我们可以列出来：

此表按照<font color=red>**优先级升序**</font>列出了序列类型的操作。在表中，<font color=red>**s和t是相同类型的序列**</font>，<font color=red>**n，i，j 和k是整数**</font>，x是满足s强加的任何类型和值限制的任意对象。

in和not in操作具有与比较操作相同的优先级。+（连接）和*（重复）操作具有与相应数值操作相同的优先级。

|操作         |结果        |备注|
|:----------:|:----------:|:----------:|
|x in s|如果s包含x，返回True，否则返回False|(1)|
|x not in s|如果s包含x，返回False，否则返回True|(1)|
|s + t|s和t的连接操作|（6）（7）|
|s * n or n * s|相当于将s添加到自身n次|(2）（7）|
|s[i]|s的第i项，从第0项开始|（3）|
|s[i:j]|s的从第i项到第j-1项|（3）（4）|
|s[i:j:k]|s的从第i项到第j-1项,间隔为k|（3）（5）|
|len(s)|s的长度||
|min(s)|s的最小项||
|max(s)|s的最大项||
|s.index（x [， i [， j]]）|在s中（在索引i之后或索引j之前）的x|（8）|
|s.count(x)|s中x的总出现次数||

说明：

(1) 除了包含外，对于一些特殊的序列类型，如**str, bytes, bytearray**，in 和 not in 也可以用来判断子串：

```
>>> 'hel' in 'hello'
True
>>> 'hel' not in 'hello'
False
>>> 'ho' in 'hello'
False
>>> 'ho' not in 'hello'
True
```

(2) 如果n小于0，则按0来计算，即返回一个s同类型的空结果。

```
>>> (1,2,3) * -1
()
>>> (1,2,3) * 0
()
>>> (1,2,3) * 2
(1, 2, 3, 1, 2, 3)
```

需要注意的是，s中的元素不会被复制，而是被引用了多次，即如果s中的元素是可变的，则改变使用该方法后，其会指向同一个地址，如果将该地址指向的元素改变，则所有使用该地址的对象的都会改变：

```
>>> list1 = [[]] * 3
>>> list1
[[], [], []]
>>> list1[0].append('a')
>>> list1
[['a'], ['a'], ['a']]
```

可以使用下面的方法来创建一个包含不同列表的列表：

```
>>> list1 = [[] for i in range(3)]
>>> list1
[[], [], []]
>>> list1[0].append(3)
>>> list1[1].append(5)
>>> list1[2].append(7)
>>> list1
[[3], [5], [7]]
```

(3) 如果i或j是**负值**，该索引是相对于字符串结尾的值：用len(s) + i或len(s) + j取代。但请注意0仍然是-0。

(4) s从i到j的切片定义为索引为k项组成的序列，其中i < = k < j。如果i或j大于len(s)，则使用len(s)。如果i省略或为None，则使用0。如果j省略或为None，则使用len(s)。如果i大于或等于j，则切片为空。

(5) s从i到i步长为k的切片定义为索引`x = i + n*k`的项组成的序列，其中`0 <= n < (j-i)/k`。换句话说，索引是`i+k`、`i+3*k`、`i`、`i+2*k`等等，在到达j（但不包括j）时停止。如果i或j大于len(s)，则使用len(s)。如果i或j省略或为None，那么它们是"终点"值（哪一端取决于标志k）。请注意，k不能为零。如果k是None，它被视为1。

(6) 连接不可变序列总是导致一个新的对象。这意味着通过重复级联构建序列将在总序列长度中具有二次运行时成本。要获得线性运行时成本，必须切换到以下选项之一：

- 如果连接str对象，则可以构建一个列表，并在结尾使用str.join()，否则写入io.StringIO并在完成时检索其值
- 如果连接bytes对象，您可以类似地使用bytes.join()或io.BytesIO，或者您可以进行in-place concatenation bytearray对象。bytearray对象是可变的，并具有有效的过分配机制
- 如果连接tuple对象，请扩展list
- 对于其他类型，调查相关类文件

(7) 一些序列类型（例如range）仅支持遵循特定模式的项序列，因此不支持序列连接或重复。

(8) 在s中找不到x时，index引发ValueError。当支持时，索引方法的附加参数允许有效搜索序列的子部分。传递额外的参数大致相当于使用s[i:j].index(x)，只是不复制任何数据，返回的索引相对于序列的开始，而不是开始的切片。

## 元组的优点

1. 元组的运算速度比列表快，如果你经常要遍历一个序列，且不需要修改内容，用元组比列表好。

2. 元组相当于给数据加了保护（不可修改），有些场合需要这种不可修改的内容。



## 参考

[Python 官方 API ](https://docs.python.org/3.5/library/stdtypes.html#sequence-types-list-tuple-range)