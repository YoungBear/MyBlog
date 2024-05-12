# Postman 禁止更新配置

postman禁止更新



## 1. 背景

在postman v10.14版本，必须登录才可以使用分组功能。所以可以使用旧版本，并配置不更新，旧版本基本可以满足日常开发测试需求。

## 2. 方案

配置hosts，不更新postman。

```shell
# host路径 C:\Windows\System32\drivers\etc\hosts
## postman禁止更新
0.0.0.0 dl.pstmn.io
0.0.0.0 sync-v3.getpostman.com
0.0.0.0 getpostman.com
0.0.0.0 go.pstmn.io

```



## 3. 旧版本postman软件分享

百度网盘

链接：https://pan.baidu.com/s/1qsY1xyw-ZC0TT4MvYFJZ8w 
提取码：s3lw
