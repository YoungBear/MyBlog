# Python 列表

list是一种<font color=red>**有序**</font>的集合，可以随时添加和删除其中的元素。

列表中的数据的类型可以是相同的，也可以是不同的。



## 创建列表

使用中括号`[]`，元素之间用逗号`,`隔开：

```
>>> list1 = [1,2,3,4,5]
>>> list1
[1, 2, 3, 4, 5]
```

空列表用`[]`表示：

```
>>> list2 = []
>>> list2
[]
```

## 访问列表

### 1. 使用索引获取列表中的数据

**list_name.[index]**

超出索引时，会报错：`index out of range`。

另外，-1表示倒数第1个，-2表示倒数第2个。即

`list_name[-x]` 与 `list_name[-x + n]` 的值相同。

其中0 <= x <= n-1，n为列表的长度。

```
>>> list1 = [1,2,3,4,5]
>>> list1[0]
1
>>> list1[2]
3
>>> list1[4]
5
>>> list1[5]
Traceback (most recent call last):
  File "<pyshell#336>", line 1, in <module>
    list1[5]
IndexError: list index out of range
>>> list1[-1]
5
>>> list1[-2]
4
>>> 
```

### 2. 获取列表长度

**len(list_name)**

```
>>> list1 = [1,2,3,4,5]
>>> len(list1)
5
```

### 3. 使用加号连接列表

**list1 + list2**

生成一个新的列表，数据为list1和list2的数据之和。

```
>>> list1 = [1,2,3,4,5]
>>> list2 = [4,5,6,7,8]
>>> list1 + list2
[1, 2, 3, 4, 5, 4, 5, 6, 7, 8]
>>> 
```

### 4. 列表复制

**list1 * n**

返回一个新的列表，数据为list1的n份。

```
>>> list1 = [1,2,3,4,5]
>>> list1 * 3
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> 
```

### 5. 列表的遍历

使用**for each**语法：

```
>>> list1 = [1,2,3,4,5]
>>> for i in list1:
	print(i)

	
1
2
3
4
5
>>> 
```

### 6. 判断元素是否在列表中

**element in list** 返回元素是否在列表中

**element not in list** 返回元素是否不在列表中

```
>>> list1 = [1,2,3,4,5]
>>> 1 in list1
True
>>> 1 not in list1
False
>>> 100 in list1
False
>>> 100 not in list1
True
```

### 7. 删除元素

**del list[index]** 删除index索引的元素

```
>>> list1 = [1,2,3,4,5]
>>> del list1[3]
>>> list1
[1, 2, 3, 5]
>>> 
```

### 8. 修改列表中的值

**list[index] = newValue** 将列表index索引的元素赋予新的值newValue

```
>>> list1 = ["python", "java"]
>>> list1
['python', 'java']
>>> list1[0] = "C"
>>> list1
['C', 'java']
```

## 列表的API

### 1. 列表末尾添加新的对象

**list.append( obj )**

在列表末尾添加新的对象，无返回值。

```
>>> list1 = [1,2,3,4,5]
>>> list1
[1, 2, 3, 4, 5]
>>> list1.append(100)
>>> list1
[1, 2, 3, 4, 5, 100]
>>> 
```

### 2. 统计某个元素在列表中出现的次数

**list.count(obj)** 返回某个元素在列表中出现的次数。如果没有，则返回0。

```
>>> list1 = [1,1,2,3,3,4,4,4,5]
>>> list1
[1, 1, 2, 3, 3, 4, 4, 4, 5]
>>> list1.count(1)
2
>>> list1.count(4)
3
>>> list1.count(6)
0
>>> 
```

### 3. 追加一个序列

**list.extend(exq)** 追加一组元素到列表中，参数可以为列表。

```
>>> list1 = [1,2,3]
>>> list1.extend([100, 200])
>>> list1
[1, 2, 3, 100, 200]
>>> 
```

### 4. 找出某个值第一个匹配项的索引位置

**list.index(obj)** 从列表中找出某个值第一个匹配项的索引位置， 如果不存在则报异常ValueError。相当于Java中String的indexOf(str)方法。

```
>>> list1 = [10,11,12,12,13]
>>> list1
[10, 11, 12, 12, 13]
>>> list1.index(12)
2
>>> list1.index(100)
Traceback (most recent call last):
  File "<pyshell#385>", line 1, in <module>
    list1.index(100)
ValueError: 100 is not in list
```

### 5. 将对象插入列表

**list.insert(index, obj)** 将元素obj插入到list的index索引处，原来位置及后边的元素都向后移动一位。

```
>>> list1 = ['python', 'java', 'C']
>>> list1
['python', 'java', 'C']
>>> list1.insert(1, 'C++')
>>> list1
['python', 'C++', 'java', 'C']
```

### 6. 删除指定元素并返回

**list.pop(index)** 删除index索引处的元素，并返回该元素。如果不传递index值，即`list.pop()`，默认删除最后一个元素。

```
>>> list1 = ['python', 'java', 'C']
>>> list1
['python', 'java', 'C']
>>> list1.pop(0)
'python'
>>> list1
['java', 'C']
>>> list1.pop()
'C'
>>> list1
['java']
```

### 7. 移除列表中某个值的第一个匹配项

**list.remove(obj)** 移除列表中某个值的第一个匹配项

```
>>> list1 = ['python', 'java', 'python', 'C']
>>> list1
['python', 'java', 'python', 'C']
>>> list1.remove('python')
>>> list1
['java', 'python', 'C']
```

### 8. 反转列表

**list.reverse()** 反转列表。

```
>>> list1 = [1,2,3,4,5]
>>> list1
[1, 2, 3, 4, 5]
>>> list1.reverse()
>>> list1
[5, 4, 3, 2, 1]
```

### 9. 排序

**list.sort()** 对列表进行排序，默认升序，如果传递参数reverse = True，则降序排序。也可以对字符串排序，默认字典序升序。

升序：

```
>>> list1 = [1, 5, 2, 10, 9]
>>> list1
[1, 5, 2, 10, 9]
>>> list1.sort()
>>> list1
[1, 2, 5, 9, 10]
```

降序：

```
>>> list1 = [1, 5, 2, 10, 9]
>>> list1
[1, 5, 2, 10, 9]
>>> list1.sort(reverse = True)
>>> list1
[10, 9, 5, 2, 1]
```

字符串排序：

```
# 默认，升序
>>> list1 = ['python', 'java', 'c']
>>> list1
['python', 'java', 'c']
>>> list1.sort()
>>> list1
['c', 'java', 'python']
>>> 

# 降序
>>> list1 = ['python', 'java', 'c']
>>> list1
['python', 'java', 'c']
>>> list1.sort(reverse = True)
>>> list1
['python', 'java', 'c']
```

## 列表切片

列表切片指的是将列表的一部分切出来。

格式：**`list[start : end : step]`**

返回一个新的列表，其中，从list的start索引开始，到end索引截止，**不包括end**。步长为step。不设置步长是，默认步长为1。

```
>>> list1 = [0,1,2,3,4,5,6,7,8,9]
>>> list1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 默认步长为1
>>> list1[1:8]
[1, 2, 3, 4, 5, 6, 7]
>>> list1[1:8:2]
[1, 3, 5, 7]
>>>
```

一些省略：

- 如果**stop省略**，表示到**列表最后**，即从start开始到全部结束，也包括最后一个元素。

```
>>> list1 = [0,1,2,3,4,5,6,7,8,9]
>>> list1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 省略stop，从第三个元素到最后
>>> list1[3:]
[3, 4, 5, 6, 7, 8, 9]
# 省略stop，从第三个元素到最后，步长为2
>>> list1[3::2]
[3, 5, 7, 9]
>>>
```

- **start省略**，则表示**从0开始**。

```
>>> list1 = [0,1,2,3,4,5,6,7,8,9]
>>> list1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 省略start，从0开始，不包括5
>>> list1[:5]
[0, 1, 2, 3, 4]
# 省略start，从0开始，步长为2
>>> list1[:5:2]
[0, 2, 4]
```

- **start和stop都省略**，表示**全部**。

```
>>> list1 = [0,1,2,3,4,5,6,7,8,9]
>>> list1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# start 和 stop都省略，表示全部
>>> list1[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# start 和 stop都省略，表示全部
>>> list1[::]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# start 和 stop都省略，表示全部，步长为2
>>> list1[::2]
[0, 2, 4, 6, 8]
>>>
```

- 如果**start或者stop为负数**，则表示<font color=red>**倒数**</font>第n个。

```
>>> list1 = [0,1,2,3,4,5,6,7,8,9]
>>> list1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# start为-5，stop为-2，表示从倒数第5个到倒数第2个，即从(-5+10)到(-2+10)
# 即从5到8，不包含8。10表示列表的长度。
>>> list1[-5:-2]
[5, 6, 7]
# 从-5到-2，并且步长为2。
>>> list1[-5:-2:2]
[5, 7]
>>>
```

- 如果**step为负数**，表示<font color=red>**逆序**</font>。

```
>>> list1 = [0,1,2,3,4,5,6,7,8,9]
>>> list1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 逆序，从第8个元素到第2个元素，不包括第2个元素。
>>> list1[8:2:-1]
[8, 7, 6, 5, 4, 3]
# 逆序，从第8个元素到第2个元素，不包括第2个元素。步长为2。
>>> list1[8:2:-2]
[8, 6, 4]
# 逆序，全部，步长为1。
>>> list1[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# 逆序，全部，步长为2。
>>> list1[::-2]
[9, 7, 5, 3, 1]
# 逆序，从最后一个元素，到第6个元素，不包括第6个元素。
>>> list1[:6:-1]
[9, 8, 7]
# 逆序，从最后一个元素，到第6个元素，不包括第6个元素。步长为2。
>>> list1[:6:-2]
[9, 7]
# 逆序，从第3个元素到前面所有的元素。
>>> list1[3::-1]
[3, 2, 1, 0]
# 逆序，从第3个元素到前面所有的元素。步长为2。
>>> list1[3::-2]
[3, 1]
```





## 参考

[Python从零开始系列连载](https://ask.hellobi.com/blog/wangdawei/9970)

[廖雪峰 Python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316724772904521142196b74a3f8abf93d8e97c6ee6000)

[Python 3.5 中文API 列表](http://python.usyiyi.cn/translate/python_352/library/stdtypes.html#sequence-types-list-tuple-range)

