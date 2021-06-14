# openssl pkey

The **pkey** command processes public or private keys. They can be converted between various forms and their components printed out.



pkey 是用来处理公钥私钥的工具。可以用来转换格式，打印组件。

**命令格式：**

`openssl pkey[options]`

`openssl pkey [-help] [-inform PEM|DER] [-outform PEM|DER] [-in filename] [-passin arg] [-out filename] [-passout arg] [-traditional] [-cipher] [-text] [-text_pub] [-noout] [-pubin] [-pubout] [-engine id] [-check] [-pubcheck]`





[openssl pekey 官方文档](https://www.openssl.org/docs/man1.1.1/man1/openssl-pkey.html)





**常用命令：**

```shell
# 1. 生成一个3072bit的RSA私钥 -----BEGIN PRIVATE KEY-----
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out rsa_private_3072.pem
# 2. 生成一个口令保护的3072bit的RSA私钥-----BEGIN ENCRYPTED PRIVATE KEY-----
openssl genpkey -aes256 -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out encrypted_rsa_private_3072.pem -pass pass:'Hello@123'
# 3. 查看私钥信息
openssl pkey -in rsa_private_3072.pem -text
# 4. 导出公钥 -----BEGIN PUBLIC KEY-----
openssl pkey -in rsa_private_3072.pem -out rsa_public_3072.pem -pubout
# 5. 查看私钥信息，不显示私钥的编码值
openssl pkey -in rsa_private_3072.pem -text -noout
# 6. 移除私钥的口令保护，即输出一个没有口令保护的私钥文件
openssl pkey -in key.pem -out keyout.pem
# 7. 使用口令保护一个私钥
openssl pkey -in key.pem -aes256 -out keyout.pem
# 8. 查看公钥信息
openssl pkey -in rsa_private_3072.pem -text_pub -noout
# 9. 指定输入口令，不指定则交互式输入（常用）
openssl pkey -in enc_private.pem -passin pass:'Hello@123' -text
# 10. 指定输出口令，不指定则交互式输入（常用）
openssl pkey -in enc_private.pem -passin pass:'Hello@123' -aes256 -passout pass:'Hello@456' -out enc_key_hello.pem


```





**选项：**

```shell
# 1. -help 打印帮助信息
openssl pkey -help
# 2. -inform DER|PEM 指定输入的格式，DER或者PEM，默认为PEM
openssl pkey -inform PEM -in rsa_private_3072.pem -text -noout
# 3. -outform DER|PEM 指定输出的格式，DER或者PEM，默认为PEM
openssl pkey -in key.pem -outform PEM -out keyout.pem
# 4. -in filename 指定输入的密钥文件。如果不指定则从标准输入。如果有口令保护则需要输入口令
openssl pkey -in key.pem -out keyout.pem
# 5. -passin arg 指定输入私钥文件的口令
openssl pkey -in enc_private.pem -passin pass:'Hello@123' -text
# 6. -out filename 指定输出文件，如果不指定则从标准输出
openssl pkey -in key.pem -out keyout.pem
# 7. -passout password 指定输出私钥文件的口令
openssl pkey -in enc_private.pem -passin pass:'Hello@123' -aes256 -passout pass:'Hello@456' -out enc_key_hello.pem
# 8. -traditional

# 9. -cipher 指定加密算法
openssl pkey -in key.pem -aes256 -out keyout.pem
# 10. -text 文本方式打印密钥信息
openssl pkey -in rsa_private_3072.pem -text
# 11. -text_pub 只打印公钥信息
openssl pkey -in rsa_private_3072.pem -text_pub -noout
# 12. -noout 不打印密钥的编码值
openssl pkey -in rsa_private_3072.pem -text -noout
openssl pkey -in rsa_private_3072.pem -text_pub -noout
# 13. -pubin 表示输入的是公钥文件，默认为私钥
openssl pkey -pubin -in rsa_public_3072.pem -text_pub -noout
# 14. -pubout 表示输出的是公钥文件，默认为私钥
openssl pkey -in rsa_private_3072.pem -pubout
# 15. -engine id 指定引擎ID

# 16. -check 检查私钥和公钥的组件的一致性
openssl pkey -check -in rsa_private_3072.pem
# 17. -pubcheck 检查私钥或公钥的组件的正确性
openssl pkey -pubcheck -in rsa_private_3072.pem
openssl pkey -pubcheck -pubin -in rsa_public_3072.pem


```















