# find 命令

[TOC]

find 命令用来查找文件，其原理为：沿着文件层次结构向下遍历，匹配符合条件的文件，执行相应的操作。默认的操作是打印出文件和目录，也可以使用 -print 选项来指定。

## 常见命令

```shell
# 查找当前目录下的java文件
find . -type f -name "*.java"
# 查找当前目录下以example开头,.txt结尾的文件(忽略大小写)
find . -iname "example*.txt"
# 查找当前目录下大于2M的文件，并打印其文件信息
find . -type f -size +2M -print0 | xargs -0 ls -lh
# 查找当前面目录下修改时间超过7天的文件并删除
find . -type f -mtime +7 -print0 | xargs -0 rm -f
# 查找当前目录下的java文件并统计及行数
find . -type f -name "*.java" -print0 | xargs -0 wc -l
```



## 选项

### -print

-print 默认使用功能\n 分隔输出的每个文件或者目录名。

而 -print0 使用空白字符 '\0' 来分隔。通常用于将包含换行符或者空白字符的文件名传给 xargs 命令。

### -name

-name 表示根据文件名称匹配，可以是通配符也可以是正则表达式。

-iname 表示忽略大小写。



### 逻辑操作 -a -o

-a，-and 表示逻辑与。

-o, -or 表示逻辑或。

```shell
# 当前目录查找 .zip 或者 .tar.gz 结尾的文件
find . \( -name '*.zip' -o -name '*.tar.gz' \) -print
# 当前目录查找 arthas 开头，.zip 结尾的文件
find . \( -name 'arthas*' -and -name '*.zip' \) -print

## 其中 \( 和 \) 表示将 -o 或者 -and 两边视为一个整体
```





### ! 否定参数

使用 ! 表示排除匹配到的模式。

```shell
# 匹配所有不以 .txt 结尾的文件
find . ! -name "*.txt" -print
```



### 目录深度

find 命令在查找时默认会遍历完所有的子目录。默认情况下，find 命令不会跟随符号链接，除非使用 -L 参数。但如果碰上了指向自身的链接，find 命令就会陷入死循环。

-maxdepth 表示限制find命令的最大深度

-mindepth 表示限制find命令的最小深度，1表示当前目录。

```shell
# 当前目录查找.java结尾的文件，最小深度为6，最大深度为7
find . -mindepth 6 -maxdepth 7 -name ".java" -print
```



### 文件类型 -type

通过 -type 指定类型。

```shell
# 查找当前目录下的所有的Example开头的文件
find . -type f -name "Example*" -print
```

文件类型列表

| 文件类型 | 类型参数 |
| -------- | -------- |
| 普通文件 | f        |
| 符号链接 | l        |
| 目录     | d        |
| 字符设备 | c        |
| 块设备   | b        |
| 套接字   | s        |
| FIFO     | p        |



### 文件大小 -size

```shell
# 当前目录查找大于 2M 的文件
find . -type f -size +2M -print
# 当前目录查找小于 2M 的文件
find . -type f -size -2M -print
# 当前目录查找等于 2M 的文件
find . -type f -size 2M -print
```

文件大小单位：

| 单位 | 描述                |
| ---- | ------------------- |
| c    | 字节                |
| w    | 字，2字节           |
| b    | 块，512字节         |
| k    | 千字节（1024字节）  |
| M    | 兆字节（1024K字节） |
| G    | 吉字节（1024M字节） |
| T    | 太字节（1024G字节） |

ls命令可以使用 -lh 选项查看文件的大小。



### 文件时间戳

-atime 最后一次访问时间

-mtime 最近一次被修改的时间

-ctime 元数据（如权限或者属主）最后一次改变的时间

可以用 stat 命令查看文件时间戳

使用整数值来指定天数。其中+表示大于，-表示小于，不加表示刚好。

另外，-amin，-mmin，-cmin 表示按照分钟计算时间。

```shell
# 查看当前目录下最近一次修改时间超过七天的文件
find . -type f -mtime +7 -print
```

-newer 表示指定一个用于比较修改时间的参考文件，即找出比参考文件更新的（更近的修改时间）的文件。

```shell
# 查看当前目录下比 LICENSE.txt 文件更新的文件
find . -type f -newer LICENSE.txt -print
```



### 权限 -perm

```shell
# 当前目录下查找 644 权限的文件
find . -type -f -perm 644 -print
```



### 属主 -user

```shell
# 当前目录下查找 属主为 paas 的文件
find . -type f -user paas -print
```



### 指定命令 -exec

使用 -exec 选项可以结合其他命令使用



```shell
# 把当前目录下的 修改时间超过7天的 .log.zip 文件，移动到 /tmp/baklog/ 目录下
find . -type f -mtime +7 -name "*.log.zip" -exec mv {} /tmp/baklog/ \;
```



### 跳过目录 -prune

-prune 用于排除某些匹配。

```shell
# 当前目录下查看文件，排除 .git 目录
find . -name '.git' -prune -o -type f -print
```

