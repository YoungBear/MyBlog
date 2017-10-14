# GitHub API 学习笔记

HOST: `https://api.github.com`

## Search Api

[Search Api官方文档地址](https://developer.github.com/v3/search/)

### Rate limit
当使用`Basic Authentication`, `OAuth`, 或者 `client ID and secret`请求的时候，每分钟最多可以请求30次(30 requests per minute)，如果没有认证的请求，则每分钟最多10次请求(10 requests per minute)。

### 分页加载

`page`： 第几页，从1开始(如果小于1，则默认为第1页)

`per_page` : 每页多少个项

### 搜索仓库 Search repositories

`GET /search/repositories`

可选的参数有:

|    参数     |    类型     |    描述     |
|    :--:    |    :--:    |    :--:    |
|    q       |   string   | 搜索的关键词  |
|   sort     |   string   |排序的类型，是`stars`,`forks`,`updated`中的一个。默认是最佳匹配|
|order|string|排序方式，根据sort参数提供的值来排序，`asc`：升序,`desc`：降序。默认为`desc`。|

其中，关键词q可以包含其他的属性，如user，topic等属性，格式为`q=<keyword>+user:<username>+language:<language>`

eg.

```
curl -s 'https://api.github.com/search/repositories?q=java+user:youngbear+language:java'
```

### 搜索Commits Search commits

`GET /search/commits`

搜索的时候，只有**默认分支**会被涉及到，大部分情况下，该分支为master。（Only the default branch is considered. In most cases, this will be the master branch.）

参数：

|    参数     |    类型     |    描述     |
|    :--:    |    :--:    |    :--:    |
|    q       |   string   | 搜索的关键词  |
|   sort     |   string   |排序的类型，是`author-date`或者`committer-date`。默认是最佳匹配|
|order|string|排序方式，根据sort参数提供的值来排序，`asc`：升序,`desc`：降序。默认为`desc`。|

搜索的关键词可以包含author,repo等属性.格式与搜索repositories相同，`q=[keyword]+author:<author_name>+repo:<repo_name>`。

eg.

```
curl -i 'https://api.github.com/search/commits?q=java+author:bearyang+repo:YoungBear/MyBlog'
```


### 搜索代码 Search Code

`GET /search/code`

特点:

- 搜索的时候，只有**默认分支**会被涉及到，大部分情况下，该分支为master。
- 只有小于384KB的文件才会被搜索到。（Only files smaller than 384 KB are searchable.）
- 搜索源代码的时候，必须要包含一个关键词，如`language:go`是无效的，但是`amazing language:go`是有效的。

参数：

|    参数     |    类型     |    描述     |
|    :--:    |    :--:    |    :--:    |
|    q       |   string   | 搜索的关键词  |
|   sort     |   string   |排序的类型，只能是`indexed`。默认是最佳匹配|
|order|string|排序方式，根据sort参数提供的值来排序，`asc`：升序,`desc`：降序。默认为`desc`。|

类似的，可以添加filename，language，user等参数值。具体参数请参考
[官网api](https://developer.github.com/v3/search/#search-code)。

eg.

```
curl -i 'https://api.github.com/search/code?q=butterknife+user:YoungBear+filename:build.gradle'

```

### 搜索问题 Search issues

`GET /search/issues`

参数：

|    参数     |    类型     |    描述     |
|    :--:    |    :--:    |    :--:    |
|    q       |   string   | 搜索的关键词  |
|   sort     |   string   |排序的类型，可以为`comments`，`created`或者`updated`。默认是最佳匹配|
|order|string|排序方式，根据sort参数提供的值来排序，`asc`：升序,`desc`：降序。默认为`desc`。|

类似地，可以添加state，label，repo等参数。详情请参考官网API。

eg.

```
curl -i 'https://api.github.com/search/issues?q=cache+label:bug+state:open+repo:bumptech/glides'
```

### 搜索用户 Search users

`GET /search/users`

参数：

|    参数     |    类型     |    描述     |
|    :--:    |    :--:    |    :--:    |
|    q       |   string   | 搜索的关键词  |
|   sort     |   string   |排序的类型，可以为`followers`，`repositories `或者`joined `。默认是最佳匹配|
|order|string|排序方式，根据sort参数提供的值来排序，`asc`：升序,`desc`：降序。默认为`desc`。|

关键词中的可选参数:

|    参数     |    类型     |    描述     |
|    :--:    |    :--:    |    :--:    |
|    type    |    string  |类型，可以为`user`或者`org`，分别代表个人和组织|
|     in     |    string  | 在哪个属性来搜索，可以为`login`，`email`，`fullname`或者其组合，分别代表登录的用户名，电子邮箱地址，名字全称。|
|   repos    |    int     |仓库数目，根据仓库数目来过滤用户，例如repos传递500则表明只返回仓库数目大于500的用户|
|   location |    string  |位置，根据位置来过滤用户|
|   language |    string  |语言，根据编程语言来过滤用户|
|   created  |YYYY-MM-DD的时间格式|根据时间过滤用户，只有在这个时间之前假如github的用户才会被返回|
|   followers|    int     |followers数目，根据follower的数目来过滤用户，只有大于等于该数目的用户才会被返回|

eg.

```
curl -i 'https://api.github.com/search/users?q=young+location:西安'
```
