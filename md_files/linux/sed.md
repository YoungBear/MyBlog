# sed 命令

sed 编辑器被称为流编辑器（stream editor）。

sed 编辑器可以根据命令来处理数据流中的数据。这些命令要么从命令行中输入，要么存储在一个命令文本文件中。sed 编辑器会执行下列操作：

- 一次从输入中读取一行数据。（即每次处理一行数据）
- 根据所提供的编辑器命令匹配数据。
- 按照命令修改流中的数据。
- 将新的数据输出到 STDOUT。



## 1. sed 常用命令

```shell
# 1. 替换指定文件中所有的 pattern 字符串为 replacement
sed -i 's/pattern/replacement/g' <file_name>
# 2. 批量文件替换字符串
## 当前目录搜索所有txt文件并替换字符串
find . -name '*.txt' | xargs sed -i 's/pattern/replacement/g'
```



## 2. sed 命令格式



**sed options scripts file**

sed 默认不会修改文件，除非使用了 -i 的选项。



## 3. sed 常用编辑器命令

- s：替换 substitute
- d：删除 delete
- i：插入 insert
- a：附件 append
- c：修改 change



### 3.1 替换命令 s

#### 1. 替换标记

替换命令默认情况只替换每行中出现的第一处。要让替换命令能够替换一行中的不同地方出现的文本必须使用**替换标记**（substitution flag）。替换标记会在替换命令字符串之后设置。

**格式**： `s/pattern/replacement/flags`

flag 的取值有4种：

- 数字：表明新文本将替换第几处模式匹配的地方（从1开始）；
- g：表明新文本将会替换所有匹配的文本（**常用**）；
- p：表明原先行的内容要打印出来；
- w file：将替换的结果写入到文件中。

#### 2. 替换字符

sed 默认使用正斜线 `/` 作为替换时的分隔符，但如果待替换的字符串包含文件的路径名，则需要转义，或者更好的方式是指定分隔符。

如 `sed 's!/bin/bash!/bin/csh!' /etc/password` 使用叹号作为分隔符。



## 4. sed 寻址方式

默认情况下，在 sed 编辑器中使用的命令会作用于文本数据的所有行。如果只想将命令作用于特定行或某些行，则必须使用行寻址（line addressing）。

两种寻址方式：

- 以数字形式表示行区间；
- 用文本模式来过滤出行



**数字方式的行寻址：**

```shell
# 1. 指定行号：2 表示匹配第2行
sed '2s/dog/cat/' data.txt
# 2. 行地址区间：2,3 表示匹配第2到3行
sed '2,3s/dog/cat/' data.txt
# 3. 指定行到文件末尾：2,$ 表示匹配从第2行开始的所有行
sed '2,$s/dog/cat/' data.txt
```



使用文本模式过滤器：

格式：`/pattern/command` ：可以使用正则表达式。





