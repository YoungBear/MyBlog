# git 常用命令

**查看帮助文档：**

`git xxx --help` 如 `git branch --help` 

**关于远程库：**

git 默认远程库名称为 `origin` ，用户也可以重命名远程库，本文默认使用 `origin` 作为远程库名称。



## 1. git push 推送

```shell
# 将本地分支，推送到远程分支
git push origin <local_br_name>:<remote_br_name>
# 将本地分支，推送到远程分支，并设置分支关联
git push -u origin <local_br_name>:<remote_br_name>
# 如果不添加冒号和远程分支名，则推送到同名分支，如果远程不存在该分支，则会新建该分支
git push origin <local_br_name>
# 如果省略本地分支名，则表示删除指定的远程分支，这等同于推送一个空的本地分支到远程分支
git push origin :<remote_br_name>
# 等同于删除远程分支 -d --delete
git push origin -d <remote_br_name>
git push origin --delete <remote_br_name>
# 将所有本地分支都推送到远程库
git push --all origin
# 推送本地所有标签到远程 origin 库
git push origin --tags
# 推送指定标签到远程库
git push origin <tag_name>
# 删除远程标签(与删除分支类似) -d --delete
git push origin :<tag_name>
git push origin -d <tag_name>
git push origin --delete <tag_name>
```

## 2. git log 日志

```shell
# 查看提交记录
git log
# 单行显示查看记录
git log --oneline
# 查看完整SHA值得单行查看提交记录
git log --pretty=oneline
# 单行显示并显示合并记录
git log --oneline --graph
# 查看某个用户的提交记录
git log --author=<user_name>
# 查看某文件的提交历史：
git log -p <file_path>
# 查看最近n次的提交
git log -<n>
# 查看提交详情,相当于 git show 所有提交
git log -p
# 查看提交的文件变化记录
git log --stat
```


## 3. git branch 分支

```shell
# 查看本地分支
git branch
# 查看本地和远程所有分支
git branch -a
# 创建分支
git branch <br_name>
# 切换到分支
git checkout <br_name>
# 创建并切换到新分支
git checkout -b <br_name>
# 从远程分支创建一个本地同名分支并跟踪，并切换到该本地分支
git checkout --track origin/<remote_br_name>

# 关联本地分支与远程分支，这样可以直接使用 git push 和 git pull 等
# 本地分支与远程分支关联 1. 如果不指定本地分支名，则默认为当前分支名
git branch --set-upstream-to=origin/<remote_br_name> [<local_br_name>]
# 本地分支与远程分支关联 2. 如果不指定本地分支名，则默认为当前分支名
git branch -u origin/<remote_br_name> [<local_br_name>]
# 取消本地分支与远程分支的关联，如果不指定本地分支名，则默认为当前分支名
git branch --unset-upstream [<local_br_name>]
# 查看分支关联关系
git branch -vv

# 重命名指定分支
git branch -m <old_br_name> <new_br_name>
# 重命名当前分支
git branch -m <new_br_name>

# 删除本地分支
git branch -d <br_name>
# 强制删除分支
git branch -D <br_name>
# 删除远程分支 1. eg. git branch -d -r origin/dev1212
git branch -d -r origin/<br_name>
# 删除远程分支 2. eg. git push origin --delete dev1212
git push origin --delete <br_name>
# 删除远程分支 3. eg. git push origin :dev1212
git push origin :<br_name>
```

## 4. git tag 标签

```shell
# 查看标签
git tag
# 新建标签
git tag <tag_name>
# 在指定提交上新建标签
git tag <tag_name> <SHA>
# 使用 vim 模式新建标签并添加说明
git tag <tag_name> -a
# 新建标签并添加说明(与 git commit -m "description" 和 git commit 类似)
git tag <tag_name> -m "description"

# 查看标签说明及最近一次的提交历史
git show <tag_name>

# 切换到标签处的代码
git checkout <tag_name>

# 推动标签到远程库(与推送分支类似)
git push origin <local_tag_name>:<remote_tag_name>
# 推送本地标签到远程同名标签
git push origin <local_tag_name>
# 推送本地所有标签到远程同名标签
git push origin --tags

# 删除本地标签
git tag -d <tag_name>
# 删除远程标签 1.
git push origin --delete <remote_tag_name>
# 删除远程标签 2.
git push origin :<remote_tag_name>
```



## 5. git remote 远程库

```shell
# 查看远程库
git remote
# 查看远程库及对应地址
git remote -v
# 新建远程库
git remote add [<remote_name>] <remote_url>
# 删除远程库
git remote remove <remote_name>
# 重命名远程库名称
git remote rename <old_remote_name> <new_remote_name>
```



## 6. git config 配置

查看 git 配置：

```
git config -l
```

### 6.1 系统级配置

```
git config --system user.name "username"
git config --system user.email "username@xx.com"
```

对应的配置文件为**`<git_setup_dir>/etc/gitconfig`**

### 6.2 全局级配置

```
git config --global user.name "username"
git config --global user.email "username@xx.com"
```

对应的配置文件为**`~/.gitconfig`**

### 6.3 仓库级配置

```
git config --local user.name "username"
git config --local user.email "username@xx.com"
```

对应的配置文件为**`.git/config`**

### 6.4 设置gui的编码
默认情况下，使用gitk查看代码时，代码中的中文会乱码，设置gui编码为utf-8后问题解决。

```
git config --global gui.encoding utf-8
```
### 6.5 常用git配置

```
[user]
        email = xxx
        name = xxx

[alias]
        st = status
        br = branch
        co = checkout
[color]
        ui = auto
```
## 7. 生成ssh公钥文件

```
# 生成
ssh-keygen -t rsa -C "your_email"
# 查看
cat ~/.ssh/id_rsa.pub
```

## 8. `.gitignore` 配置

git 工程下，`.gitignore` 文件表示对忽略文件进行配置，即这些文件不会进入git管理。

比如，SpringBoot 工程的一个`.gitignore` 文件:

```shell
/target/
.mvn

### STS ###
.apt_generated
.classpath
.factorypath
.project
.settings
.springBeans
.sts4-cache

### IntelliJ IDEA ###
.idea
*.iws
*.iml
*.ipr

### NetBeans ###
/nbproject/private/
/build/
/nbbuild/
/dist/
/nbdist/
/.nb-gradle/
```



## 9. 其他常用git命令

```shell
# 克隆代码仓库，可指定目录
git clone <repo-url> [dir-name]

# 在当前目录，初始化本地仓库，新建一个git库
git init

# 查看状态
git status

# 查看文件详细修改内容
git diff [file-path]

# 跟踪文件，存在暂存区
git add <file-path>

# 提交 commit
# vim 编辑模式提交
git commit
# 直接使用命令并添加commit信息
git commit -m "commit message"
# 重新编辑上一次提交
git commit --amend

# 取消暂存的文件
git reset <file-path>
# 切换到指定提交位置，后边的所有提交的相关文件都会变成未跟踪状态
git reset <commit-hash>
# 切换到指定提交位置，放弃后边所有的提交
git reset --hard <commit-hash>

# 撤销文件的修改，修改的文件由暂存区变成未跟踪状态
git checkout <file-path>
# 切换到指定分支
git checkout <branch-name>
# 切换到指定提交位置，默认为无名分支
git reset <commit-hash>

# 合并指定分支的修改到当前分支
git merge <branch-name>

# 暂存为跟踪的文件到栈容器中
git stash
# 查看栈容器中所有的缓存
git stash list
# 栈容器缓存出栈
git stash pop

# 从远程库拉取代码
git fetch [repo-name]
# 从远程库拉取代码，并将远程库已删除的部分也在本地删除
git fetch -p [repo-name]

# 从远程拉取代码，并和本地分支合并(相当于 git fetch + git merge)
git pull [repo-name]

# 从指定分支变基到当前分支，当前分支的提交，都会在指定分支的其他提交之后，而不是按照时间先后顺序合并
git rebase <branch-name>

# 将指定的提交合并到当前分支，可以将其他的分支的某一个提交合并到当前分支
git cherry-pick <commit-hash>

```



# [更多文章](https://github.com/YoungBear/MyBlog/blob/master/README.md)

