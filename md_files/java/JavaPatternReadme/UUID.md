# Java UUID 正则表达式

UUID，即通用唯一识别码（Universally Unique Identifier）。

UUID的介绍(来自[百度百科](<https://baike.baidu.com/item/UUID/5921266?fr=aladdin>))

UUID是指在一台机器上生成的数字，它保证对在同一时空中的所有机器都是唯一的。

UUID由以下几部分的组合：

（1）当前日期和时间，UUID的第一个部分与时间有关，如果你在生成一个UUID之后，过几秒又生成一个UUID，则第一个部分不同，其余相同。

（2）时钟序列。

（3）全局唯一的IEEE机器识别号，如果有网卡，从网卡MAC地址获得，没有网卡以其他方式获得。

**标准的UUID的格式：**

`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` (8-4-4-4-12)

其中每个x表示一个16进制的数字(小写)。即共32的16进制的数字，使用分隔符，分割成8-4-4-4-12五部分。

用正则表达式表示为：

```java
[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}
```

对应可以编写Java 工具类：

```java
package com.ysx.pattern;

import java.util.UUID;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2019-04-23 22:50
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description
 */
public class UUIDPattern {

    /**
     * 标准的UUID
     * 32位16进制的数字，用分隔符分成8-4-4-4-12的格式
     */
    private static final Pattern UUID_PATTERN = Pattern.compile("[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}");

    /**
     * 判断一个字符串是否是有效的UUID
     *
     * @param uuid
     * @return
     */
    public static boolean isValidUUID(String uuid) {
        Matcher matcher = UUID_PATTERN.matcher(uuid);
        return matcher.matches();
    }

    /**
     * 随机生成UUID
     *
     * @return
     */
    public static String uuid() {
        return UUID.randomUUID().toString();
    }
}
```



#[更多文章](https://github.com/YoungBear/MyBlog/blob/master/README.md)