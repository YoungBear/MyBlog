# 日期时间格式化与解析

## 1. 简述

主要介绍LocalDateTime，ZonedDateTime的格式化及解析。

常见带日期时间格式：

| 字段名        | 字段值                                       |
| ------------- | -------------------------------------------- |
| api格式       | DateTimeFormatter.ISO_ZONED_DATE_TIME        |
| 字符串pattern | yyyy-MM-dd'T'HH:mm:ss.SSSxxx'['VV']'         |
| 示例          | 2022-06-15T22:06:29.483+08:00[Asia/Shanghai] |
| api格式       | DateTimeFormatter.ISO_OFFSET_DATE_TIME       |
| 字符串pattern | yyyy-MM-dd'T'HH:mm:ss.SSSxxx                 |
| 示例          | 2022-06-15T22:06:29.483+08:00                |
| api格式       | DateTimeFormatter.ISO_LOCAL_DATE_TIME        |
| 字符串pattern | yyyy-MM-dd'T'HH:mm:ss.SSS'                   |
| 示例          | 2022-06-15T22:06:29.483                      |

## 2. 详细java代码：

```java
package com.ysx.utils.datetime;

import java.time.LocalDateTime;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2022/6/26 22:57
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description 格式化与解析
 */
public class FormatterUtils {

    /**
     * 使用默认格式格式化本地日期时间
     * 默认格式为ISO_LOCAL_DATE_TIME，即 yyyy-MM-dd'T'HH:mm:ss.SSS，如 2022-06-15T22:06:29.483
     *
     * @param localDateTime 本地日期时间
     * @return 格式化字符串
     */
    public static String local2String(LocalDateTime localDateTime) {
        return local2String(localDateTime, DateTimeFormatter.ISO_LOCAL_DATE_TIME);

    }

    /**
     * 指定格式格式化本地日期时间
     *
     * @param localDateTime 本地日期时间
     * @param pattern       格式：如 yyyy-MM-dd'T'HH:mm:ss.SSS
     * @return 格式化字符串
     */
    public static String local2String(LocalDateTime localDateTime, String pattern) {
        DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern(pattern);
        return local2String(localDateTime, dateTimeFormatter);
    }

    /**
     * 指定 DateTimeFormatter 格式化本地日期时间
     *
     * @param localDateTime     本地日期时间
     * @param dateTimeFormatter DateTimeFormatter 如 DateTimeFormatter.ISO_LOCAL_DATE_TIME
     * @return 格式化字符串
     */
    public static String local2String(LocalDateTime localDateTime, DateTimeFormatter dateTimeFormatter) {
        return localDateTime.format(dateTimeFormatter);
    }

    /**
     * 使用默认格式解析本地日期时间
     *
     * @param localDateTimeString 格式化字符串 如 2022-06-15T22:06:29.483
     * @return 本地日期时间
     */
    public static LocalDateTime string2Local(String localDateTimeString) {
        return string2Local(localDateTimeString, DateTimeFormatter.ISO_LOCAL_DATE_TIME);

    }

    /**
     * 指定格式解析本地日期时间
     *
     * @param localDateTimeString 格式化字符串 如 2022-06-15T22:06:29.483
     * @param pattern             格式：如 yyyy-MM-dd'T'HH:mm:ss.SSS
     * @return 本地日期时间
     */
    public static LocalDateTime string2Local(String localDateTimeString, String pattern) {
        DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern(pattern);
        return string2Local(localDateTimeString, dateTimeFormatter);
    }

    /**
     * 指定 DateTimeFormatter 解析本地日期时间
     *
     * @param localDateTimeString 格式化字符串 如 2022-06-15T22:06:29.483
     * @param dateTimeFormatter   DateTimeFormatter 如 DateTimeFormatter.ISO_LOCAL_DATE_TIME
     * @return 本地日期时间
     */
    public static LocalDateTime string2Local(String localDateTimeString, DateTimeFormatter dateTimeFormatter) {
        return LocalDateTime.parse(localDateTimeString, dateTimeFormatter);
    }

    /**
     * 使用默认格式格式化带时区的日期时间
     *
     * @param zonedDateTime 带时区的日期时间
     * @return 格式化带时区的日期时间 格式为：yyyy-MM-dd'T'HH:mm:ss.SSSxxx'['VV']' 如 2022-06-15T22:06:29.483+08:00[Asia/Shanghai]
     */
    public static String zoned2String(ZonedDateTime zonedDateTime) {
        return zonedDateTime.format(DateTimeFormatter.ISO_ZONED_DATE_TIME);

    }

    /**
     * 使用默认格式解析带时区的日期时间
     *
     * @param zonedDateTimeString 格式化带时区的日期时间 格式为：yyyy-MM-dd'T'HH:mm:ss.SSSxxx'['VV']' 如 2022-06-15T22:06:29.483+08:00[Asia/Shanghai]
     * @return 带时区的日期时间
     */
    public static ZonedDateTime string2Zoned(String zonedDateTimeString) {
        return ZonedDateTime.parse(zonedDateTimeString, DateTimeFormatter.ISO_ZONED_DATE_TIME);
    }


}

```

## 3. 对应单元测试：

```java
package com.ysx.utils.datetime;

import org.junit.Assert;
import org.junit.Test;

import java.time.LocalDateTime;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2022/6/26 23:15
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description
 */
public class FormatterUtilsTest {

    @Test
    public void localFormatTest() {
        String localDateTimeString = "2022-06-15T22:06:29.483";
        LocalDateTime localDateTime = LocalDateTime.parse(localDateTimeString, DateTimeFormatter.ISO_LOCAL_DATE_TIME);

        String localDateTimeString1 = FormatterUtils.local2String(localDateTime);
        String localDateTimeString2 = FormatterUtils.local2String(localDateTime, "yyyy-MM-dd'T'HH:mm:ss.SSS");
        String localDateTimeString3 = FormatterUtils.local2String(localDateTime, DateTimeFormatter.ISO_LOCAL_DATE_TIME);
        Assert.assertEquals(localDateTimeString, localDateTimeString1);
        Assert.assertEquals(localDateTimeString, localDateTimeString2);
        Assert.assertEquals(localDateTimeString, localDateTimeString3);

    }

    @Test
    public void localParseTest() {
        String localDateTimeString = "2022-06-15T22:06:29.483";
        LocalDateTime localDateTime = LocalDateTime.parse(localDateTimeString, DateTimeFormatter.ISO_LOCAL_DATE_TIME);

        LocalDateTime localDateTime1 = FormatterUtils.string2Local(localDateTimeString);
        LocalDateTime localDateTime2 = FormatterUtils.string2Local(localDateTimeString, "yyyy-MM-dd'T'HH:mm:ss.SSS");
        LocalDateTime localDateTime3 = FormatterUtils.string2Local(localDateTimeString, DateTimeFormatter.ISO_LOCAL_DATE_TIME);

        Assert.assertEquals(localDateTime, localDateTime1);
        Assert.assertEquals(localDateTime, localDateTime2);
        Assert.assertEquals(localDateTime, localDateTime3);
    }

    @Test
    public void zonedFormatTest() {
        String zonedDateTimeString = "2022-06-15T22:06:29.483+08:00[Asia/Shanghai]";
        DateTimeFormatter formatter = DateTimeFormatter.ISO_ZONED_DATE_TIME;
        ZonedDateTime zonedDateTime = ZonedDateTime.parse(zonedDateTimeString, formatter);
        String zonedDateTimeString1 = FormatterUtils.zoned2String(zonedDateTime);
        Assert.assertEquals(zonedDateTimeString, zonedDateTimeString1);
    }

    @Test
    public void zonedParseTest() {
        String zonedDateTimeString = "2022-06-15T22:06:29.483+08:00[Asia/Shanghai]";
        DateTimeFormatter formatter = DateTimeFormatter.ISO_ZONED_DATE_TIME;
        ZonedDateTime zonedDateTime = ZonedDateTime.parse(zonedDateTimeString, formatter);
        ZonedDateTime zonedDateTime1 = FormatterUtils.string2Zoned(zonedDateTimeString);
        Assert.assertEquals(zonedDateTime, zonedDateTime1);
    }
}

```









# 相关文章

## [1. LocalDateTime ZonedDateTime Instant 的相互转换](https://github.com/YoungBear/JavaUtils/blob/master/mdfiles/datetime/ConvertUtils.md)

## [2. 日期时间格式化与解析](https://github.com/YoungBear/JavaUtils/blob/master/mdfiles/datetime/FormatterUtils.md)

## [3. 带时区时间日期 ZonedDateTime](https://github.com/YoungBear/JavaUtils/blob/master/mdfiles/datetime/ZonedDateTimeUtils.md)

## [4. 夏令时](https://github.com/YoungBear/JavaUtils/blob/master/mdfiles/datetime/dst.md)



# [源代码地址](https://github.com/YoungBear/JavaUtils)
