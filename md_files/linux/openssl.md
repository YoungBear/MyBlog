# openssl 常用命令

[openssl 1.1.1 官方文档](https://www.openssl.org/docs/man1.1.1/man1/)



# 常用命令

```shell
# 查看版本号
openssl version
openssl version -a
```







## 1.  dgst 摘要

**命令格式：**

`openssl dgst [options] [file...]`

[openssl dgst 官方文档](https://www.openssl.org/docs/man1.1.1/man1/dgst.html)



```shell
# 1. 查看帮助
-help
# 2. 打印支持的算法列表（常用）
-list
# 3. 打印结果用冒号分割（only hex）
-c
# 4. 打印BIO debug信息
-d
# 5. 结果使用十六进制格式输出（默认）
-hex
# 6. 结果使用二进制格式输出
-binary
# 7. 结果使用coreutils格式，即如同sha1sum，md5sum 等命令格式的输出
-r
# 8. 指定输出到文件，默认为标准输出（常用）
-out <filename>
# 9. 使用私钥生成数字签名（常用）
-sign <filename>
# 10. 使用公钥校验一个文件的数字签名（常用）
-verify <filename>
# 11. 使用私钥校验一个文件的数字签名（常用）
-prverify <filename>
# 12. 指定待校验的签名文件（常用）
-signature <filename>
# 13. 指定私钥的格式
-keyform arg
# 14. 指定私钥的密码（指定或者交互式输入）
-passin arg
# 15. 计算hmac
-hmac key
```



eg.



```shell
# 1. 计算文件的摘要值，默认使用SHA256算法
$ openssl dgst data.txt
SHA256(data.txt)= 2df88bbb4d80c92068907c6b249dc465e6563fd57c3497d39b7f56ac702f33ee

# 2. 计算文件的摘要值，指定使用MD5算法
$ openssl dgst -md5 data.txt
MD5(data.txt)= d52a0055b4650959add65064fd21f87d
# -c
$ openssl dgst -c -md5 data.txt
MD5(data.txt)= d5:2a:00:55:b4:65:09:59:ad:d6:50:64:fd:21:f8:7d
# -r
$ openssl dgst -r -md5 data.txt
d52a0055b4650959add65064fd21f87d *data.txt

# 3. 计算文件的MD5摘要，并输出到指定文件
$ openssl dgst -md5 -out data.md5 data.txt

# 4. 使用私钥生成数字签名（如果私钥是口令保护的则需要输入口令）
$ openssl dgst -sha256 -sign private-key.pem -out signature.sign data.txt
Enter pass phrase for private-key.pem:

# 5. 使用公钥校验签名
$ openssl dgst -sha256 -verify public-key.pem -signature signature.sign data.txt
Verified OK
# 6. 使用私钥校验签名
$ openssl dgst -sha256 -prverify private-key.pem -signature signature.sign data.txt
Enter pass phrase for private-key.pem:
Verified OK
# 7. 指定私钥的密码校验签名
$ openssl dgst -sha256 -prverify private-key.pem -passin pass:Tiantian@123 -signature signature.sign data.txt
Verified OK

# 8. 计算hmac值
$ openssl dgst -sha256 -hmac testkey2021 data.txt
HMAC-SHA256(data.txt)= 0ab58fc5b256824cad9c3b78a95f01520c0c1575258bd75a6a7558d039a4dca9
```









参考：https://wiki.openssl.org/index.php/Command_Line_Utilities

```shell
# 生成私钥
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out private-key.pem
# 生成口令保护的私钥
openssl genpkey -aes256 -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out private-key.pem
# 生成口令保护的私钥
openssl genpkey -aes256 -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out private-key.pem -pass pass:Tiantian@123
# 查看私钥
openssl pkey -in private-key.pem -passin pass:Tiantian@123 -text
# 导出公钥
openssl pkey -in private-key.pem -passin pass:Tiantian@123 -out public-key.pem -pubout
# 查看公钥
openssl pkey -in public-key.pem -pubin -text
# 将PKCS1格式的私钥转换为PKCS8格式的私钥
openssl pkcs8 -topk8 -inform PEM -in private-key.pem -passin pass:Tiantian@123 -outform pem -out private-key-pkcs8.pem -passout pass:Tiantian@123
```

