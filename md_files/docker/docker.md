# docker 常用命令

[官方文档](https://docs.docker.com/engine/reference/commandline/docker/)



## 1. 常用命令

```shell
# docker exec 表示执行命令
# 进入容器 CONTAINER表示容器id或name
docker exec -it CONTAINER bash
# 查看环境变量
docker exec CONTAINER env

# 查看镜像信息 NAME|ID表示镜像name或id
docker inspect NAME|ID
# 查看镜像详情 IMAGE 表示镜像name或id
docker image inspect IMAGE

# 由容器内向宿主机拷贝
docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH
# 由宿主机向容器内拷贝
docker cp [OPTIONS] SRC_PATH CONTAINER:DEST_PATH

```



示例：

```shell
# 由容器内向宿主机拷贝
docker cp f683eab:/opt/hello.txt /home/pass/
# 由宿主机向容器内拷贝
docker cp /home/pass/hello.txt f683eab:/opt/
```

