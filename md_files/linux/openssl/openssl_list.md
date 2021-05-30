# openssl list

openssl list 命令可以查看支持的算法，特性。

**命令格式：**

`openssl list [options]`

[openssl list 官方文档](https://www.openssl.org/docs/man1.1.1/man1/list.html)



常用命令：

```shell
# 1. 查看帮助
openssl list -help
# 以一列的形式显示，-1必须是在第一个位置
openssl list -1
# 2. List of standard commands 查看所有标准命令
openssl list -commands
# 3. List of message digest commands 查看散列命令
openssl list -digest-commands
# 4. List of message digest algorithms 查看散列算法
openssl list -digest-algorithms
# 5. List of cipher commands 查看对称加密命令
openssl list -cipher-commands
# 6. List of cipher algorithms 查看对称加密算法
openssl list -cipher-algorithms
# 7. List of public key algorithms 查看公钥算法
openssl list -public-key-algorithms
# 8. List of public key methods 查看公钥方法
openssl list -public-key-methods
# 9. List of disabled features 查看缺失的特性
openssl list -disabled
# 10. List missing detailed help strings 查看缺失的帮助信息
openssl list -missing-help
# 11. List options for specified command 查看指定命令的选项
openssl list -options val
```

eg. openssl list -help

```shell
$ openssl list -help
Usage: list [options]
Valid options are:
 -help                   Display this summary
 -1                      List in one column
 -commands               List of standard commands
 -digest-commands        List of message digest commands
 -digest-algorithms      List of message digest algorithms
 -cipher-commands        List of cipher commands
 -cipher-algorithms      List of cipher algorithms
 -public-key-algorithms  List of public key algorithms
 -public-key-methods     List of public key methods
 -disabled               List of disabled features
 -missing-help           List missing detailed help strings
 -options val            List options for specified command
```



eg. openssl list -commands

```shell
$ openssl list -commands
asn1parse         ca                ciphers           cms
crl               crl2pkcs7         dgst              dhparam
dsa               dsaparam          ec                ecparam
enc               engine            errstr            gendsa
genpkey           genrsa            help              list
nseq              ocsp              passwd            pkcs12
pkcs7             pkcs8             pkey              pkeyparam
pkeyutl           prime             rand              rehash
req               rsa               rsautl            s_client
s_server          s_time            sess_id           smime
speed             spkac             srp               storeutl
ts                verify            version           x509
```



eg. openssl list -cipher-commands

```shell
$ openssl list -cipher-commands
aes-128-cbc       aes-128-ecb       aes-192-cbc       aes-192-ecb
aes-256-cbc       aes-256-ecb       aria-128-cbc      aria-128-cfb
aria-128-cfb1     aria-128-cfb8     aria-128-ctr      aria-128-ecb
aria-128-ofb      aria-192-cbc      aria-192-cfb      aria-192-cfb1
aria-192-cfb8     aria-192-ctr      aria-192-ecb      aria-192-ofb
aria-256-cbc      aria-256-cfb      aria-256-cfb1     aria-256-cfb8
aria-256-ctr      aria-256-ecb      aria-256-ofb      base64
bf                bf-cbc            bf-cfb            bf-ecb
bf-ofb            camellia-128-cbc  camellia-128-ecb  camellia-192-cbc
camellia-192-ecb  camellia-256-cbc  camellia-256-ecb  cast
cast-cbc          cast5-cbc         cast5-cfb         cast5-ecb
cast5-ofb         des               des-cbc           des-cfb
des-ecb           des-ede           des-ede-cbc       des-ede-cfb
des-ede-ofb       des-ede3          des-ede3-cbc      des-ede3-cfb
des-ede3-ofb      des-ofb           des3              desx
idea              idea-cbc          idea-cfb          idea-ecb
idea-ofb          rc2               rc2-40-cbc        rc2-64-cbc
rc2-cbc           rc2-cfb           rc2-ecb           rc2-ofb
rc4               rc4-40            rc5               rc5-cbc
rc5-cfb           rc5-ecb           rc5-ofb           seed
seed-cbc          seed-cfb          seed-ecb          seed-ofb
sm4-cbc           sm4-cfb           sm4-ctr           sm4-ecb
```

