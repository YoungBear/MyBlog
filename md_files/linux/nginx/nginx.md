# nginx 基础



默认情况下，Nginx被安装在目录 `usr/local/nginx/` 中。其中二进制文件的路径为`usr/local/nginx/sbin/nginx`，配置文件路径为 `usr/local/nginx/conf/nginx.conf`。



Nginx使用一个master进程来管理多个work进程。一般情况下，worker进程的数量与服务器上的CPU核心数相等：

- 每一个worker进程用用来提供互联网服务。
- master进程用来管理worker进程。

## 1. 常用命令：

```shell
# 测试配置信息是否有错误
nginx -t
# 使运行的nginx重读配置项并生效
nginx -s reload
# 显示版本信息
nginx -v
# 显示编译阶段的参数
nginx -V
# 快速停止服务,-s表示向正在运行的Nginx服务发送信号量
nginx -s stop
```

