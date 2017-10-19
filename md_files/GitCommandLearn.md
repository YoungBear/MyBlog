[本文github地址](https://github.com/YoungBear/MyBlog/blob/master/md_files/GitCommandLearn.md "")
## 查看log

```
查看某个用户的提交记录：
git log --author=<user_name>

查看某文件的提交历史：
git log -p <file_path>
```


## 重命名本地分支

```
重命名指定分支:
git branch -m <oldname> <newname>
重命名当前分支:
git branch -m <newname>
```

## 删除远程分支

```
删除远程分支：
git  push origin --delete <br_name>
```

## 查看git配置

```
git config -l
```

删除远程分支example：
![这里写图片描述](http://img.blog.csdn.net/20160729161727383)

## git 配置

### 系统级配置

```
git config --system user.name "username"
git config --system user.email "username@xx.com"
```

对应的配置文件为**`<git_setup_dir>/etc/gitconfig`**

### 全局级配置

```
git config --global user.name "username"
git config --global user.email "username@xx.com"
```

对应的配置文件为**`~/.gitconfig`**

### 仓库级配置

```
git config --local user.name "username"
git config --local user.email "username@xx.com"
```

对应的配置文件为**`.git/config`**

### 设置gui的编码
默认情况下，使用gitk查看代码时，代码中的中文会乱码，设置gui编码为utf-8后问题解决。

```
git config --global gui.encoding utf-8
```

## 生成ssh公钥文件

```
# 生成
ssh-keygen -t rsa -C "your_email"
# 查看
cat ~/.ssh/id_rsa.pub
```

参考：

http://www.cnblogs.com/lovezbs/p/4455784.html

http://blog.csdn.net/u014132720/article/details/51471630