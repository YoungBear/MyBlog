# openssl

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

