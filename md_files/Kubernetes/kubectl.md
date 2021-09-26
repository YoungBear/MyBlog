# kubectl 常用命令

[官方文档](https://kubernetes.io/docs/reference/kubectl/overview/)

[中文文档](https://kubernetes.io/zh/docs/reference/kubectl/overview/)



## 1. 语法

```shell
kubectl [command] [TYPE] [NAME] [flags]
```

其中 `command`、`TYPE`、`NAME` 和 `flags` 分别是：

- `command`：指定要对一个或多个资源执行的操作，例如 `create`、`get`、`describe`、`delete`。
- `TYPE`：指定资源类型。资源类型不区分大小写，可以指定单数、复数或缩写格式。
- `NAME`：指定资源名称。资源名称区分大小写。如果不指定资源名称，则显示所有资源的信息。
- `flag`：指定可选的参数。例如，可以使用 `-s` 或 `-server` 参数指定 Kubernetes API 服务器的地址和端口。



## 2. 常用命令

```shell
# 查看帮助信息
kubectl help
# 查看所有namespace
kubectl get ns
# 查看pod
kubectl get pod -n <ns> -owide
# 查看service
kubectl get svc -n <ns>
# 查看secrets
kubectl get secrets -n <ns>
kubectl get secrets -n <ns> <secret-name> -o yaml
# 查看configmap
kubectl get cm -n <ns>
# 查看nodes
kubectl get nodes -n <ns>
# 编辑
kubectl edit cm -n <ns> <cm-id>
kubectl edit secret -n <ns> <secret-id>
# 进入容器
kubectl exec -it <pod-id> -n <ns> /bin/bash
# 日志
kubectl logs <pods-id> -n <ns>
## 显示实时日志，类似于tail -f
kubectl logs -f <pod-id> -n <ns>
```



示例：

```shell
kubectl get ns
kubectl get pod -owide -n kube-system
kubectl get svc -n kube-system

```

