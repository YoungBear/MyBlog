# grep 查找指定类型的文件

在文件 `~/.bashrc` 中添加下面的配置。完成之后，执行 `source ~/.bashrc` 使命令生效。就可以使用了。

```
alias grep='grep --color=auto'

# 自定义函数 在指定文件中查找字符串

# jgrep匹配当前目录下的所有java文件
# eg. jgrep History -in
function jgrep()
{
    find . -iname  "*\.java" -print0 | xargs -0 grep --color -n "$@"
}

# 在 xml 文件中查找
function xmlgrep()
{
    find . -iname  "*\.xml" -print0 | xargs -0 grep --color -n "$@"
}
```

### [更多文章](https://github.com/YoungBear/MyBlog/blob/master/README.md)