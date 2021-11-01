# grep 学习笔记

grep命令用来查找指定字符串。

**命令格式：**

```shell
grep [OPTION]... PATTERN [FILE]...
```

**常用命令：**

```shell
# 在指定文件./hello.txt查找字符串 Service，忽略大小写，显示行号
grep -in "Service" ./hello.txt
# 在当前目录递归查找字符串 Service，忽略大小写，显示行号
grep -Rin "Service" ./
# 在当前目录递归查找单词 Service，忽略大小写，显示行号
grep -Rinw "Service" ./
# 根据正则查询:查找WordA或者WordB
grep -Rinw "WordA|WordB" ./
```



**grep 常用选项**

```shell
-n, --line-number 显示匹配的行号
-i, --ignore-case 忽略大小写
-R, --dereference-recursive 递归查找目录中的文件，包含链接文件（-r不包含链接文件）
-w, --word-regexp 只匹配单词
-x, --line-regexp 只匹配整行
-c, --count 只打印每个文件匹配的次数

```



## grep 查找指定类型的文件

在文件 `~/.bashrc` 中添加下面的配置。完成之后，执行 `source ~/.bashrc` 使命令生效。就可以使用了。

```shell
alias grep='grep --color=auto'

# 自定义函数 在指定文件中查找字符串

# jgrep匹配当前目录下的所有java文件
# eg. jgrep -in History
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



## 附 grep --help

```shell
Usage: grep [OPTION]... PATTERN [FILE]...
Search for PATTERN in each FILE.
Example: grep -i 'hello world' menu.h main.c

Pattern selection and interpretation:
  -E, --extended-regexp     PATTERN is an extended regular expression
  -F, --fixed-strings       PATTERN is a set of newline-separated strings
  -G, --basic-regexp        PATTERN is a basic regular expression (default)
  -P, --perl-regexp         PATTERN is a Perl regular expression
  -e, --regexp=PATTERN      use PATTERN for matching
  -f, --file=FILE           obtain PATTERN from FILE
  -i, --ignore-case         ignore case distinctions
  -w, --word-regexp         force PATTERN to match only whole words
  -x, --line-regexp         force PATTERN to match only whole lines
  -z, --null-data           a data line ends in 0 byte, not newline

Miscellaneous:
  -s, --no-messages         suppress error messages
  -v, --invert-match        select non-matching lines
  -V, --version             display version information and exit
      --help                display this help text and exit

Output control:
  -m, --max-count=NUM       stop after NUM selected lines
  -b, --byte-offset         print the byte offset with output lines
  -n, --line-number         print line number with output lines
      --line-buffered       flush output on every line
  -H, --with-filename       print file name with output lines
  -h, --no-filename         suppress the file name prefix on output
      --label=LABEL         use LABEL as the standard input file name prefix
  -o, --only-matching       show only the part of a line matching PATTERN
  -q, --quiet, --silent     suppress all normal output
      --binary-files=TYPE   assume that binary files are TYPE;
                            TYPE is 'binary', 'text', or 'without-match'
  -a, --text                equivalent to --binary-files=text
  -I                        equivalent to --binary-files=without-match
  -d, --directories=ACTION  how to handle directories;
                            ACTION is 'read', 'recurse', or 'skip'
  -D, --devices=ACTION      how to handle devices, FIFOs and sockets;
                            ACTION is 'read' or 'skip'
  -r, --recursive           like --directories=recurse
  -R, --dereference-recursive  likewise, but follow all symlinks
      --include=FILE_PATTERN  search only files that match FILE_PATTERN
      --exclude=FILE_PATTERN  skip files and directories matching FILE_PATTERN
      --exclude-from=FILE   skip files matching any file pattern from FILE
      --exclude-dir=PATTERN  directories that match PATTERN will be skipped.
  -L, --files-without-match  print only names of FILEs with no selected lines
  -l, --files-with-matches  print only names of FILEs with selected lines
  -c, --count               print only a count of selected lines per FILE
  -T, --initial-tab         make tabs line up (if needed)
  -Z, --null                print 0 byte after FILE name

Context control:
  -B, --before-context=NUM  print NUM lines of leading context
  -A, --after-context=NUM   print NUM lines of trailing context
  -C, --context=NUM         print NUM lines of output context
  -NUM                      same as --context=NUM
      --color[=WHEN],
      --colour[=WHEN]       use markers to highlight the matching strings;
                            WHEN is 'always', 'never', or 'auto'
  -U, --binary              do not strip CR characters at EOL (MSDOS/Windows)

When FILE is '-', read standard input.  With no FILE, read '.' if
recursive, '-' otherwise.  With fewer than two FILEs, assume -h.
Exit status is 0 if any line is selected, 1 otherwise;
if any error occurs and -q is not given, the exit status is 2.

Report bugs to: bug-grep@gnu.org
GNU grep home page: <http://www.gnu.org/software/grep/>
General help using GNU software: <http://www.gnu.org/gethelp/>
```

