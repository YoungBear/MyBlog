# Linux 压缩命令

## 1. tar 命令

```shell
# 1. 生成 .tar 包
tar -cvf <dest.tar> <source_file>
# 2. 将tar包解压,-C表示指定解压目录，默认当前目录
tar -xvf <file.tar> [-C <dest_dir>]
# 3. 生成 .tar.gz 包
tar -czvf <dest.tar.gz> <source_file>
# 4. 将.tar.gz包解压，-C表示指定解压目录，默认当前目录
tar -xzvf <file.tar.gz> [-C <dest_dir>]
```

eg.

```shell
# 1. 打包生成.tar
192:tar youngbear$ ls
HelloDir
192:tar youngbear$ tar -cvf HelloDir.tar HelloDir
a HelloDir
a HelloDir/Hello.txt
192:tar youngbear$ ls
HelloDir     HelloDir.tar
# 2. 解压.tar
192:tar youngbear$ rm -rf HelloDir
192:tar youngbear$ ls
HelloDir.tar
192:tar youngbear$ tar -xvf HelloDir.tar
x HelloDir/
x HelloDir/Hello.txt
192:tar youngbear$ ls
HelloDir     HelloDir.tar
# 解压.tar到指定目录
192:tar youngbear$ mkdir testdir
192:tar youngbear$ tar -xvf HelloDir.tar -C testdir/
x HelloDir/
x HelloDir/Hello.txt
192:tar youngbear$ ls testdir/
HelloDir
# 3. 打包生成.tar.gz
192:tar youngbear$ tar -czvf HelloDir.tar.gz HelloDir
a HelloDir
a HelloDir/Hello.txt
192:tar youngbear$ ls
HelloDir        HelloDir.tar.gz testdir
# 4. 解压.tar.gz
192:tar youngbear$ rm -rf HelloDir
192:tar youngbear$ tar -xzvf HelloDir.tar.gz
x HelloDir/
x HelloDir/Hello.txt
192:tar youngbear$ ls
HelloDir        HelloDir.tar.gz testdir
# 解压 .tar.gz 到指定目录
192:tar youngbear$ tar -xzvf HelloDir.tar.gz -C testdir/
x HelloDir/
x HelloDir/Hello.txt
192:tar youngbear$ ls testdir/
HelloDir
```



### [更多文章](https://github.com/YoungBear/MyBlog/blob/master/README.md)

