# Nginx 日志格式



## 默认日志格式配置

```shell
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
```

该格式记录了客户端IP、用户、时间、请求、状态码、响应数据量、来源页、UA及代理信息‌。





## 常见变量及含义

### **1. 客户端信息**

- **`$remote_addr`**
  客户端 IP 地址（直接连接的客户端 IP，若存在代理则可能是代理服务器的 IP）。
- **`$http_x_forwarded_for`**
  客户端原始 IP（当请求经过代理时，如 CDN 或负载均衡器，此变量记录原始客户端 IP 和代理链）。
- **`$remote_user`**
  通过 HTTP 基础认证的用户名，未认证时为 `-`。
- **`$http_user_agent`**
  客户端浏览器或工具的 User-Agent 信息（如 `Mozilla/5.0 ...`）。



### **2. 请求信息**

- **`$request`**
  完整的请求行，包含请求方法、URI 和协议（如 `GET /index.html HTTP/1.1`）。
- **`$request_method`**
  请求方法（如 `GET`、`POST`）。
- **`$request_uri`**
  完整的原始请求 URI（包含查询参数）。
- **`$args`**
  请求中的查询参数（即 `?` 后的部分，如 `name=john&age=30`）。
- **`$query_string`**
  同 `$args`。
- **`$scheme`**
  请求协议（如 `http` 或 `https`）。
- **`$host`**
  请求的 Host 头（域名或 IP + 端口）。
- **`$server_protocol`**
  服务器协议版本（如 `HTTP/1.1`）。



### **3. 响应信息**

- **`$status`**
  HTTP 响应状态码（如 `200`、`404`、`500`）。
- **`$body_bytes_sent`**
  发送给客户端的响应体大小（字节数，不包含响应头）。
- **`$bytes_sent`**
  发送给客户端的全部数据大小（包括响应头和响应体）。
- **`$sent_http_<header>`**
  响应头字段值，如 `$sent_http_content_type` 表示 `Content-Type` 头的值。



### **4. 连接信息**

- **`$connection`**
  连接序列号（唯一标识一个 TCP 连接）。
- **`$connection_requests`**
  当前连接上处理的请求数量（对于 HTTP Keep-Alive 连接有效）。
- **`$request_time`**
  请求处理时间（从读取客户端第一个字节到发送完响应的时间，单位：秒，精度到毫秒）。
- **`$upstream_response_time`**
  反向代理时，后端服务器的响应时间（单位：秒，可能有多个值，用逗号分隔）。



### **5. 反向代理相关**

- **`$upstream_addr`**
  反向代理的后端服务器地址（IP:Port）。
- **`$upstream_status`**
  后端服务器的 HTTP 响应状态码。
- **`$upstream_http_<header>`**
  后端服务器返回的响应头字段，如 `$upstream_http_server` 获取后端 `Server` 头的值。



### **6. 其他常用变量**

- **`$time_local`**
  本地时间的访问时间戳（格式：`19/May/2024:15:30:01 +0800`）。
- **`$server_port`**
  接收请求的服务器端口。
- **`$http_referer`**
  请求来源页面的 Referer 头（即用户从哪个页面跳转而来）。
- **`$request_length`**
  请求的总长度（包括请求行、请求头和请求体）。
- **`$gzip_ratio`**
  响应体的压缩比（如 `2.5` 表示压缩后大小是原始大小的 40%）。

