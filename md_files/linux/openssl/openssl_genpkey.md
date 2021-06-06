# openssl genpkey

genpkey用于生成一个私钥。

**命令格式：**

`openssl genpkey [options]`

`openssl genpkey [-help] [-out filename] [-outform PEM|DER] [-pass arg] [-cipher] [-engine id] [-paramfile file] [-algorithm alg] [-pkeyopt opt:value] [-genparam] [-text]`





[openssl genpkey 官方文档](https://www.openssl.org/docs/man1.1.1/man1/openssl-genpkey.html)





**常用命令：**

```shell
# 1. 生成一个私钥
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out private-key.pem
# 2. 

```





**选项：**

```shell
# 1. -help 打印帮助信息
openssl genpkey -help
# 2. -out filename 输出到指定文件。如果不指定则输出到标准输出
openssl genpkey -algorithm RSA -out key.pem
# 3. -outform DER|PEM 指定输出的格式，DER或者PEM，默认为PEM
openssl genpkey -algorithm RSA -outform PEM
# 4. -pass arg 指定密码，使用 -pass pass:<xxx> 输出文件的密码，如果不指定则使用标准输入指定
openssl genpkey -algorithm RSA -out key.pem -aes-256-cbc -pass pass:'hello'
# 5. -cipher 指定私钥的加密算法

# 6. -engine id 指定engine id

# 7. -algorithm alg 指定公钥算法，如RSA，DSA，DH。该选项必须要使用-pkeyopt选项（常用）
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out key.pem
# 8. -pkeyopt opt:value 指定公钥算法的选项值，具体值与使用的算法相关。
# 通常有 KEY GENERATION OPTIONS和PARAMETER GENERATION OPTIONS两个选项
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -pkeyopt rsa_keygen_primes:3 -pkeyopt rsa_keygen_pubexp:12345 -out key.pem
# 9. -genparam 指定私钥的生成参数

# 10. -paramfile filename

# 11. -text 文本方式输出私钥相关信息



```



## 1. 密钥生成选项 KEY GENERATION OPTIONS：

密钥生成选项，每个算法都有不同的选项值。

### 1.1 RSA

1. `rsa_keygen_bits:numbits` 指定 rsa 密钥的比特长度，一般为1024的倍数。
2. `rsa_keygen_primes:numprimes` 指定生成 rsa 密钥的素数值，默认为2。
3. `rsa_keygen_pubexp:value` 指定 rsa 公共指数值，可以是一个很大的数。默认为65537。



### 1.2 RSA-PSS

Note: by default an **RSA-PSS** key has no parameter restrictions.

`rsa_keygen_bits:numbits, rsa_keygen_primes:numprimes, rsa_keygen_pubexp:value` 与RSA相同。

1. `rsa_keygen_bits:numbits` 指定 rsa 密钥的比特长度，一般为1024的倍数。
2. `rsa_keygen_primes:numprimes` 指定生成 rsa 密钥的素数值，默认为2。
3. `rsa_keygen_pubexp:value` 指定 rsa 公共指数值，可以是一个很大的数。默认为65537。
4. `rsa_pss_keygen_md:digest` 指定digest算法，如果指定则只能使用摘要算法签名。
5. `rsa_pss_keygen_mgf1_md:digest` 指定digest算法，如果指定则只能使用该摘要算法作为MGF1的参数。
6. `rsa_pss_keygen_saltlen:len` 设置盐值长度，如果指定则使用时盐值不能小于该长度。



### 1.3 EC

1. `ec_paramgen_curve:curve` The EC curve to use. OpenSSL supports NIST curve names such as "P-256".
2. `ec_param_enc:encoding` The encoding to use for parameters. The "encoding" parameter must be either "named_curve" or "explicit". The default value is "named_curve".



## 2. PARAMETER GENERATION OPTIONS

### 2.1 DSA



### 2.2 DH 



### 2.3 EC







```
PARAMETER GENERATION OPTIONS
The options supported by each algorithm and indeed each implementation of an algorithm can vary. The options for the OpenSSL implementations are detailed below.

DSA Parameter Generation Options
dsa_paramgen_bits:numbits
The number of bits in the generated prime. If not specified 2048 is used.

dsa_paramgen_q_bits:numbits
The number of bits in the q parameter. Must be one of 160, 224 or 256. If not specified 224 is used.

dsa_paramgen_md:digest
The digest to use during parameter generation. Must be one of sha1, sha224 or sha256. If set, then the number of bits in q will match the output size of the specified digest and the dsa_paramgen_q_bits parameter will be ignored. If not set, then a digest will be used that gives an output matching the number of bits in q, i.e. sha1 if q length is 160, sha224 if it 224 or sha256 if it is 256.

DH Parameter Generation Options
dh_paramgen_prime_len:numbits
The number of bits in the prime parameter p. The default is 2048.

dh_paramgen_subprime_len:numbits
The number of bits in the sub prime parameter q. The default is 256 if the prime is at least 2048 bits long or 160 otherwise. Only relevant if used in conjunction with the dh_paramgen_type option to generate X9.42 DH parameters.

dh_paramgen_generator:value
The value to use for the generator g. The default is 2.

dh_paramgen_type:value
The type of DH parameters to generate. Use 0 for PKCS#3 DH and 1 for X9.42 DH. The default is 0.

dh_rfc5114:num
If this option is set, then the appropriate RFC5114 parameters are used instead of generating new parameters. The value num can take the values 1, 2 or 3 corresponding to RFC5114 DH parameters consisting of 1024 bit group with 160 bit subgroup, 2048 bit group with 224 bit subgroup and 2048 bit group with 256 bit subgroup as mentioned in RFC5114 sections 2.1, 2.2 and 2.3 respectively. If present this overrides all other DH parameter options.

EC Parameter Generation Options
The EC parameter generation options are the same as for key generation. See "EC Key Generation Options" above.
```





















