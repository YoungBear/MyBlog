# openssl pkcs12

[openssl pkcs12 官方文档](https://www.openssl.org/docs/man1.1.1/man1/openssl-pkcs12.html)

## 1. 描述
The pkcs12 command allows PKCS#12 files (sometimes referred to as PFX files) to be created and parsed. PKCS#12 files are used by several programs including Netscape, MSIE and MS Outlook.

pkcs12 命令是用来创建或者解析 PKCS12 格式（有时候也称PFX格式）的文件。

pkcs12 格式文件用于 Netscape, MSIE, MS Outlook等服务器。

pkcs12 格式的文件，可以理解为证书+私钥，即 cert+key。

## 2. 常用命令



### 解析命令

```shell
# 查看证书信息 -info
openssl pkcs12 -in server.p12 -info
# 不打印私钥和证书内容 -noout
openssl pkcs12 -in server.p12 -noout
# 只输出客户端证书(不包含CA证书) -clerts
openssl pkcs12 -in server.p12 -clcerts
# 只输出CA证书(不包含客户端证书) -cacerts
openssl pkcs12 -in server.p12 -cacerts
# 不输出证书 -nocerts
openssl pkcs12 -in server.p12 -nocerts
# 不输出私钥 -nokeys
openssl pkcs12 -in server.p12 -nokeys
# 不加密私钥 -nodes
openssl pkcs12 -in server.p12 -nodes
```

### 创建命令

```shell
# 创建 -export
# 前提 已获得 私钥文件 server.key和证书文件 server.crt(可以用下边命令生成)
# 使用 genpkey 生成 server.key
openssl genpkey -aes256 -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out server.key
# 使用 req 命令生成 server.crt 文件
openssl req -x509 -new -sha256 -days 3650 -key server.key -out server.crt -subj "/C=CN/test123"

# 创建 server.p12 -export(需要交互式输入server.key的口令，以及输出的server.p12的口令)
openssl pkcs12 -inkey server.key -in server.crt -export -out server.p12

# 提取PEM文件(含私钥)
openssl pkcs12 -in server.p12 -out server.pem
# 仅提取私钥并设置私钥口令，默认为 des3 加密算法
openssl pkcs12 -nocerts -in server.p12 -out server.key
# 仅提取私钥并设置私钥口令，指定 -aes256 加密算法
openssl pkcs12 -nocerts -in server.p12 -aes256 -out server.key
# 仅提取私钥并不设置私钥口令
openssl pkcs12 -nocerts -nodes -in server.p12 -out server.key
# 检查私钥
openssl rsa -in server.key -check
# 仅提取证书(所有证书)
openssl pkcs12 -nokeys -in server.p12 -out server.crt
# 仅提取CA证书
openssl pkcs12 -nokeys -cacerts -in server.p12 -out cacert.crt
# 仅提取server证书
openssl pkcs12 -nokeys -clcerts -in server.p12 -out server.crt

```





## 3. 命令选项

参考官方文档：

[openssl pkcs12 官方文档](https://www.openssl.org/docs/man1.1.1/man1/openssl-pkcs12.html)
