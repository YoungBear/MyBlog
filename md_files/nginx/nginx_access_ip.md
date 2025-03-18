# nginx 配置ip黑白名单



## 配置ip白名单

nginx.conf内容，以server模块的配置为例。其中，allow和deny可以在http，server，location中配置。

```shell
    server {
        listen       80;
        server_name  localhost;

        # 白名单配置
        allow 192.168.3.7;  # 允许单个IP
        allow 192.168.3.9/32;    # 允许一个网段
        deny all;             # 拒绝其他所有IP

        location / {
            root   html;
            index  index.html index.htm;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
```



如果客户端主机的ip为192.168.3.8，访问该nginx的地址：http://192.168.3.9/，页面会提示403，参考日志：

```shell
# error.log
2025/03/19 00:03:39 [error] 12608#11280: *18 access forbidden by rule, client: 192.168.3.8, server: localhost, request: "GET / HTTP/1.1", host: "192.168.3.9"
# access.log
192.168.3.8 - - [19/Mar/2025:00:03:39 +0800] "GET / HTTP/1.1" 403 555 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Safari/537.36"
```





## 配置ip黑名单

```shell
    server {
        listen       80;
        server_name  localhost;

        # 黑名单配置
        deny 192.168.3.8;   # 拒绝单个IP
        deny 192.168.3.0/24;   # 拒绝一个网段
        allow all;             # 允许其他所有IP

        location / {
            root   html;
            index  index.html index.htm;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
```



如果客户端主机的ip为192.168.3.8，访问该nginx的地址：http://192.168.3.9/，页面会提示403，参考日志：

```shell
# error.log
2025/03/19 00:06:20 [error] 7876#4384: *19 access forbidden by rule, client: 192.168.3.8, server: localhost, request: "GET / HTTP/1.1", host: "192.168.3.9"
# access.log
192.168.3.8 - - [19/Mar/2025:00:06:20 +0800] "GET / HTTP/1.1" 403 555 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Safari/537.36"
```



## 关于作用域

`allow` 和 `deny` 指令可在不同配置层级生效，包括：

  - **全局层级**（`http` 块）：影响所有虚拟主机。
  - **虚拟主机层级**（`server` 块）：仅针对特定域名或端口。
  - **请求路径层级**（`location` 块）：针对特定 URL 路径或资源。
  - **嵌套 `location` 块**：更细粒度的控制。





## 注意事项

- **规则顺序**：Nginx 按 `allow`/`deny` 指令的顺序执行，一旦匹配则停止检查。使用时建议先处理例外再使用通用规则。
- **性能优化**：避免在 `http` 块中定义大量规则，尽量缩小作用域（如 `location`）。处理大量IP时，`geo` 模块比 `allow`/`deny` 更高效。
- **日志调试**：若规则未生效，检查Nginx错误日志 `/var/log/nginx/error.log`。
- **动态更新**：对于频繁变化的IP列表，可将IP存储在外部文件并通过 `include` 引入。



## 参考

[Module ngx_http_access_module](https://nginx.org/en/docs/http/ngx_http_access_module.html)
