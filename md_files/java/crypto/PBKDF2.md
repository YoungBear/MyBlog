# 使用 PBKDF2 导出密钥

java默认提供的方法为：

```java
    /**
     * 使用算法 PBKDF2 基于 SHA-256 导出密钥
     * 使用 JCE 默认方法，使用默认的 Provider
     *
     * @param password       口令
     * @param salt           盐值
     * @param iterationCount 迭代次数
     * @return 导出结果
     */
    public static byte[] derivedKeyUsingJCE(char[] password, byte[] salt, int iterationCount) throws GeneralSecurityException {
        SecretKeyFactory fact = SecretKeyFactory.getInstance("PBKDF2WITHHMACSHA256");
        return fact.generateSecret(new PBEKeySpec(password, salt, iterationCount, KEY_LENGTH)).getEncoded();
    }
```



参考代码：

```java
import org.bouncycastle.crypto.PBEParametersGenerator;
import org.bouncycastle.crypto.digests.SHA256Digest;
import org.bouncycastle.crypto.generators.PKCS5S2ParametersGenerator;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.bouncycastle.util.encoders.Hex;

import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import java.security.GeneralSecurityException;
import java.security.Security;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2020/6/30 22:40
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description 使用 PBKDF2 算法导出口令
 */
public class PBKDF2Practise {

    // key 长度 256 bit，32字节
    private static final int KEY_LENGTH = 256;
    // 测试盐值(随机生成)
    private static final byte[] TEST_SALT = {127, 28, 114, -2, -84, -125, -6, 27, 44, 109, 82, 127, 43, 124, 5, 99};
    // 测试口令
    private static final String TEST_PASSWORD = "@T2b45&l";
    // 测试迭代次数
    private static final int ITERATION_COUNT = 1000;

    public static void main(String[] args) throws GeneralSecurityException {
        char[] passwordChars = TEST_PASSWORD.toCharArray();
        byte[] bytesBC = derivedKeyUsingBC(passwordChars, TEST_SALT, ITERATION_COUNT);
        System.out.println(Hex.toHexString(bytesBC));
        byte[] bytesJCE = derivedKeyUsingJCE(passwordChars, TEST_SALT, ITERATION_COUNT);
        System.out.println(Hex.toHexString(bytesJCE));
        byte[] bytesJCEBC = derivedKeyUsingJCEBC(passwordChars, TEST_SALT, ITERATION_COUNT);
        System.out.println(Hex.toHexString(bytesJCEBC));

    }

    /**
     * 使用算法 PBKDF2 基于 SHA-256 导出密钥
     * 使用 BouncyCastle 提供的 low-level API
     *
     * @param password       口令
     * @param salt           盐值
     * @param iterationCount 迭代次数
     * @return 导出结果
     */
    public static byte[] derivedKeyUsingBC(char[] password, byte[] salt, int iterationCount) {
        PBEParametersGenerator generator = new PKCS5S2ParametersGenerator(new SHA256Digest());
        generator.init(PBEParametersGenerator.PKCS5PasswordToUTF8Bytes(password), salt, iterationCount);
        return ((KeyParameter) generator.generateDerivedParameters(KEY_LENGTH)).getKey();
    }

    /**
     * 使用算法 PBKDF2 基于 SHA-256 导出密钥
     * 使用 JCE 默认方法，使用默认的 Provider
     *
     * @param password       口令
     * @param salt           盐值
     * @param iterationCount 迭代次数
     * @return 导出结果
     */
    public static byte[] derivedKeyUsingJCE(char[] password, byte[] salt, int iterationCount) throws GeneralSecurityException {
        SecretKeyFactory fact = SecretKeyFactory.getInstance("PBKDF2WITHHMACSHA256");
        return fact.generateSecret(new PBEKeySpec(password, salt, iterationCount, KEY_LENGTH)).getEncoded();
    }

    /**
     * 使用算法 PBKDF2 基于 SHA-256 导出密钥
     * 使用 JCE 默认方法，使用 BouncyCastle 的 Provider
     *
     * @param password       口令
     * @param salt           盐值
     * @param iterationCount 迭代次数
     * @return 导出结果
     */
    public static byte[] derivedKeyUsingJCEBC(char[] password, byte[] salt, int iterationCount) throws GeneralSecurityException {
        Security.addProvider(new BouncyCastleProvider());
        SecretKeyFactory fact = SecretKeyFactory.getInstance(
                "PBKDF2WITHHMACSHA256", "BC");
        return fact.generateSecret(new PBEKeySpec(password, salt, iterationCount, KEY_LENGTH)).getEncoded();
    }
}
```

其中，使用BouncyCastle的话，需要引入pom依赖：

```xml
<dependency>
    <groupId>org.bouncycastle</groupId>
    <artifactId>bcprov-jdk15on</artifactId>
    <version>1.65</version>
</dependency>
```

