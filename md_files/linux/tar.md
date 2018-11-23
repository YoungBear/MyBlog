# Linux 常用压缩解压命令

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



## 2. zip 与 unzip

```shell
# 1. 压缩为 .zip 包, -r 表示可递归执行，用于压缩文件夹
zip -r <dest.zip> <source_file>
# 2. 解压缩，默认解压到当前目录，-d 可指定解压的目标目录
unzip <file.zip> [-d <dest_dir>]
# 3. 压缩 -P 表示加密码压缩
zip -r -P <password> <dest.zip> <source_file>
# 4. 使用密码解压缩 -P，如果不加 -P 去解压加密的文件时，会使用交互模式提醒用户输入密码
unzip -P <password> <file.zip> [-d <dest_dir>]
```

eg.

```shell
# 1. 压缩为 .zip 包
192:tar youngbear$ ls
HelloDir testdir
192:tar youngbear$ zip -r HelloDir.zip HelloDir
  adding: HelloDir/ (stored 0%)
  adding: HelloDir/Hello.txt (stored 0%)
192:tar youngbear$ ls
HelloDir     HelloDir.zip testdir
# 2. 解压
# 解压到当前目录(default)
192:tar youngbear$ ls
HelloDir.zip testdir
192:tar youngbear$ unzip HelloDir.zip
Archive:  HelloDir.zip
   creating: HelloDir/
 extracting: HelloDir/Hello.txt
192:tar youngbear$ ls
HelloDir     HelloDir.zip testdir
# 解压到指定目录 -d
192:tar youngbear$ ls testdir/
192:tar youngbear$ unzip HelloDir.zip -d testdir/
Archive:  HelloDir.zip
   creating: testdir/HelloDir/
 extracting: testdir/HelloDir/Hello.txt
192:tar youngbear$ ls testdir/
HelloDir
# 3. 加密压缩 -P <passsword>
192:tar youngbear$ ls
HelloDir testdir
192:tar youngbear$ zip -r -P 13579 HelloDir.zip HelloDir
  adding: HelloDir/ (stored 0%)
  adding: HelloDir/Hello.txt (stored 0%)
192:tar youngbear$ ls
HelloDir     HelloDir.zip testdir
# 4. unzip交互输入密码解压加密压缩文件
192:tar youngbear$ ls
HelloDir.zip testdir
192:tar youngbear$ unzip HelloDir.zip
Archive:  HelloDir.zip
   creating: HelloDir/
[HelloDir.zip] HelloDir/Hello.txt password:
 extracting: HelloDir/Hello.txt
192:tar youngbear$ ls
HelloDir     HelloDir.zip testdir
# unzip 使用 -P 解压加密压缩文件
192:tar youngbear$ ls
HelloDir.zip testdir
192:tar youngbear$ unzip -P 13579 HelloDir.zip
Archive:  HelloDir.zip
   creating: HelloDir/
 extracting: HelloDir/Hello.txt
192:tar youngbear$ ls
HelloDir     HelloDir.zip testdir
```







### [更多文章](https://github.com/YoungBear/MyBlog/blob/master/README.md)

