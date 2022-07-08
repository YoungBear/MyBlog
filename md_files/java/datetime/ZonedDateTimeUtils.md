# 带时区时间日期 ZonedDateTime

## 1. 简介

ZonedDateTime表示带时区的日期时间，如`2007-12-03T10:15:30+01:00 Europe/Paris`.

参考官方文档描述：

https://docs.oracle.com/javase/8/docs/api/java/time/ZonedDateTime.html

## 2. 字符串与时间戳的转换 

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





相关方法代码可参考：

```java
package com.ysx.utils.datetime;

import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2022/6/15 21:58
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description 带时区日期时间工具类
 */
public class ZonedDateTimeUtils {

    /**
     * 根据时间戳返回指定格式的时间日期格式字符串
     * 使用系统默认时区
     *
     * @param timestamp 时间戳 毫秒 如 1655301989483L
     * @param pattern   格式字符串 如 yyyy-MM-dd'T'HH:mm:ss.SSSxxx'['VV']'
     * @return 格式化后的字符串 如 2022-06-15T22:06:29.483+08:00[Asia/Shanghai]
     */
    public static String long2String(long timestamp, String pattern) {
        Instant instant = Instant.ofEpochMilli(timestamp);
        DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern(pattern);
        ZonedDateTime zonedDateTime = ZonedDateTime.ofInstant(instant, ZoneId.systemDefault());
        return zonedDateTime.format(dateTimeFormatter);
    }

    /**
     * 根据时间戳返回指定格式的时间日期格式字符串
     * 使用系统默认时区
     *
     * @param timestamp 时间戳 毫秒 如 1655301989483L
     * @param formatter formatter 如 DateTimeFormatter.ISO_ZONED_DATE_TIME
     * @return 格式化后的字符串 如 2022-06-15T22:06:29.483+08:00[Asia/Shanghai]
     */
    public static String long2String(long timestamp, DateTimeFormatter formatter) {
        Instant instant = Instant.ofEpochMilli(timestamp);
        ZonedDateTime zonedDateTime = ZonedDateTime.ofInstant(instant, ZoneId.systemDefault());
        return zonedDateTime.format(formatter);
    }

    /**
     * 根据时间戳返回指定格式的时间日期格式字符串
     * 指定时区
     *
     * @param timestamp 时间戳 毫秒 如 1655301989483L
     * @param formatter formatter 如 DateTimeFormatter.ISO_ZONED_DATE_TIME
     * @param zoneId    时区信息 如 ZoneId.of("Europe/Moscow")
     * @return 格式化后的字符串 如 2022-06-15T17:06:29.483+03:00[Europe/Moscow]
     */
    public static String long2String(long timestamp, DateTimeFormatter formatter, ZoneId zoneId) {
        Instant instant = Instant.ofEpochMilli(timestamp);
        ZonedDateTime zonedDateTime = ZonedDateTime.ofInstant(instant, zoneId);
        return zonedDateTime.format(formatter);
    }


    /**
     * 时间日期格式字符串返回时间戳
     *
     * @param dateString 格式化后的字符串 如 2022-06-15T17:06:29.483+03:00[Europe/Moscow]
     * @param pattern    格式字符串 如 yyyy-MM-dd'T'HH:mm:ss.SSSxxx'['VV']'
     * @return 时间戳 毫秒 如 1655301989483L
     */
    public static long string2long(String dateString, String pattern) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern(pattern);
        ZonedDateTime zonedDateTime = ZonedDateTime.parse(dateString, formatter);
        return Instant.from(zonedDateTime).toEpochMilli();
    }

    /**
     * 时间日期格式字符串返回时间戳
     *
     * @param dateString 格式化后的字符串 如 2022-06-15T17:06:29.483+03:00[Europe/Moscow]
     * @param formatter  formatter 如 DateTimeFormatter.ISO_ZONED_DATE_TIME
     * @return 时间戳 毫秒 如 1655301989483L
     */
    public static long string2long(String dateString, DateTimeFormatter formatter) {
        ZonedDateTime zonedDateTime = ZonedDateTime.parse(dateString, formatter);
        return Instant.from(zonedDateTime).toEpochMilli();
    }

    /**
     * 时间日期格式字符串返回时间戳
     * 指定时区
     *
     * @param dateString 格式化后的字符串 如 2022-06-15T17:06:29.483+03:00[Europe/Moscow]
     * @param formatter  formatter 如 DateTimeFormatter.ISO_ZONED_DATE_TIME
     * @param zoneId     时区信息 如 ZoneId.of("Europe/Moscow")
     * @return 时间戳 毫秒 如 1655301989483L
     */
    public static long string2long(String dateString, DateTimeFormatter formatter, ZoneId zoneId) {
        formatter.withZone(zoneId);
        LocalDateTime localDateTime = LocalDateTime.parse(dateString, formatter);
        ZonedDateTime zonedDateTime = ZonedDateTime.of(localDateTime, zoneId);
        return Instant.from(zonedDateTime).toEpochMilli();
    }
}
```



相关单元测试方法：

```java
package com.ysx.utils.datetime;

import org.junit.Assert;
import org.junit.Test;

import java.time.ZoneId;
import java.time.format.DateTimeFormatter;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2022/6/15 22:05
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description 参考：
 * DateTimeFormatter：https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html
 * ZonedDateTime https://docs.oracle.com/javase/8/docs/api/java/time/ZonedDateTime.html
 */
public class ZonedDateTimeUtilsTest {

    @Test
    public void long2StringTest() {
        long timestamp = 1655301989483L;

        String dateStr1 = "2022-06-15T22:06:29.483+08:00[Asia/Shanghai]";
        Assert.assertEquals(dateStr1, ZonedDateTimeUtils.long2String(timestamp, DateTimeFormatter.ISO_ZONED_DATE_TIME));
        String dateStr2 = "2022-06-15T22:06:29.483+08:00";
        Assert.assertEquals(dateStr2, ZonedDateTimeUtils.long2String(timestamp, DateTimeFormatter.ISO_OFFSET_DATE_TIME));
        String dateStr3 = "2022-06-15T22:06:29.483";
        Assert.assertEquals(dateStr3, ZonedDateTimeUtils.long2String(timestamp, DateTimeFormatter.ISO_LOCAL_DATE_TIME));

        // 分别对应 pattern 字符串如下
        String pattern1 = "yyyy-MM-dd'T'HH:mm:ss.SSSxxx'['VV']'";
        Assert.assertEquals(dateStr1, ZonedDateTimeUtils.long2String(timestamp, pattern1));
        String pattern2 = "yyyy-MM-dd'T'HH:mm:ss.SSSxxx";
        Assert.assertEquals(dateStr2, ZonedDateTimeUtils.long2String(timestamp, pattern2));
        String pattern3 = "yyyy-MM-dd'T'HH:mm:ss.SSS";
        Assert.assertEquals(dateStr3, ZonedDateTimeUtils.long2String(timestamp, pattern3));

    }

    @Test
    public void string2longTest() {
        String str1 = "2022-06-15T22:06:29.483+08:00[Asia/Shanghai]";
        long timestamp = 1655301989483L;
        long timestamp1 = ZonedDateTimeUtils.string2long(str1, DateTimeFormatter.ISO_ZONED_DATE_TIME);
        Assert.assertEquals(timestamp, timestamp1);
        long timestamp11 = ZonedDateTimeUtils.string2long(str1, "yyyy-MM-dd'T'HH:mm:ss.SSSxxx'['VV']'");
        Assert.assertEquals(timestamp, timestamp11);

        String str2 = "2022-06-15T22:06:29.483+08:00";
        long timestamp2 = ZonedDateTimeUtils.string2long(str2, DateTimeFormatter.ISO_OFFSET_DATE_TIME);
        Assert.assertEquals(timestamp, timestamp2);
        long timestamp22 = ZonedDateTimeUtils.string2long(str2, "yyyy-MM-dd'T'HH:mm:ss.SSSxxx");
        Assert.assertEquals(timestamp, timestamp22);

        // 失败，因为没有带时区信息
//        String str3 = "2022-06-15T22:06:29.483";
//        long timestamp3 = DateTimeUtils.string2long(str3, DateTimeFormatter.ISO_LOCAL_DATE_TIME);
//        Assert.assertEquals(timestamp, timestamp3);
    }

    @Test
    public void long2StringWithZoneIdTest() {
        long timestamp = 1655301989483L;
        // 默认时区 Asia/Shanghai 2022-06-15T22:06:29.483+08:00[Asia/Shanghai]
        String dateStringShanghai = "2022-06-15T22:06:29.483+08:00[Asia/Shanghai]";
        Assert.assertEquals(dateStringShanghai, ZonedDateTimeUtils.long2String(timestamp, DateTimeFormatter.ISO_ZONED_DATE_TIME));
        // 指定时区 Europe/Moscow 2022-06-15T17:06:29.483+03:00[Europe/Moscow]
        ZoneId zoneIdMoscow = ZoneId.of("Europe/Moscow");
        String dateStringMoscow = "2022-06-15T17:06:29.483+03:00[Europe/Moscow]";
        Assert.assertEquals(dateStringMoscow, ZonedDateTimeUtils.long2String(timestamp, DateTimeFormatter.ISO_ZONED_DATE_TIME, zoneIdMoscow));
        // 指定时区 Europe/Paris 2022-06-15T16:06:29.483+02:00[Europe/Paris]
        ZoneId zoneIdParis = ZoneId.of("Europe/Paris");
        String dateStringParis = "2022-06-15T16:06:29.483+02:00[Europe/Paris]";
        Assert.assertEquals(dateStringParis, ZonedDateTimeUtils.long2String(timestamp, DateTimeFormatter.ISO_ZONED_DATE_TIME, zoneIdParis));
        // 指定时区 America/Los_Angeles 2022-06-15T07:06:29.483-07:00[America/Los_Angeles]
        ZoneId zoneIdLos_Angeles = ZoneId.of("America/Los_Angeles");
        String dateStringLos_Angeles = "2022-06-15T07:06:29.483-07:00[America/Los_Angeles]";
        Assert.assertEquals(dateStringLos_Angeles, ZonedDateTimeUtils.long2String(timestamp, DateTimeFormatter.ISO_ZONED_DATE_TIME, zoneIdLos_Angeles));
    }

    @Test
    public void string2longWithZoneIdTest() {
        long timestamp = 1655301989483L;
        ZoneId zoneIdShanghai = ZoneId.of("Asia/Shanghai");
        String str3 = "2022-06-15T22:06:29.483";
        long timestamp3 = ZonedDateTimeUtils.string2long(str3, DateTimeFormatter.ISO_LOCAL_DATE_TIME, zoneIdShanghai);
        Assert.assertEquals(timestamp, timestamp3);
    }
}

```

## 3. 常见时区

详细夏令时规定可参考：http://www.timeofdate.com/



| 时区ID字符串        | 标准偏移值standardOffset | 是否有夏令时 | 使用夏令时的偏移值offset |
| ------------------- | ------------------------ | ------------ | ------------------------ |
| Asia/Shanghai       | +08:00                   | 否           | 无                       |
| Europe/London       | +00:00                   | 是           | +01:00                   |
| Europe/Paris        | +01:00                   | 是           | +02:00                   |
| Europe/Berlin       | +01:00                   | 是           | +02:00                   |
| Europe/Moscow       | +03:00                   | 否           | 无                       |
| Asia/Seoul          | +09:00                   | 否           | 无                       |
| Asia/Tokyo          | +09:00                   | 否           | 无                       |
| Australia/Sydney    | +10:00                   | 是           | +11:00                   |
| America/Los_Angeles | -08:00                   | 是           | -07:00                   |
| America/New_York    | -05:00                   | 是           | -04:00                   |



获取方法：

```java
package com.ysx.utils.datetime;

import java.time.Instant;
import java.time.ZoneId;
import java.time.ZoneOffset;
import java.time.zone.ZoneRules;
import java.util.Set;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2022/6/15 23:18
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description 获取全球时区信息
 */
public class ZoneIdUtils {
    public static void main(String[] args) {
        Instant instant = Instant.now();
        Set<String> zoneIds = ZoneId.getAvailableZoneIds();
        System.out.println(zoneIds.size());
        zoneIds.stream().sorted().forEach(zoneIdString -> {
            ZoneId zoneId = ZoneId.of(zoneIdString);
            ZoneRules rules = zoneId.getRules();
            // 当前offset
            ZoneOffset offset = rules.getOffset(instant);
            // 标准offset
            ZoneOffset standardOffset = rules.getStandardOffset(instant);
            // 是否为夏令时
            boolean daylightSavings = rules.isDaylightSavings(instant);

            System.out.println(zoneIdString + ", offset: "
                    + offset + ", standardOffset: " + standardOffset
                    + ", daylightSavings: " + daylightSavings);
        });
    }
}

```



# 相关文章

## [1. LocalDateTime ZonedDateTime Instant 的相互转换](https://github.com/YoungBear/JavaUtils/blob/master/mdfiles/datetime/ConvertUtils.md)

## [2. 日期时间格式化与解析](https://github.com/YoungBear/JavaUtils/blob/master/mdfiles/datetime/FormatterUtils.md)

## [3. 带时区时间日期 ZonedDateTime](https://github.com/YoungBear/JavaUtils/blob/master/mdfiles/datetime/ZonedDateTimeUtils.md)

## [4. 夏令时](https://github.com/YoungBear/JavaUtils/blob/master/mdfiles/datetime/dst.md)



# [源代码地址](https://github.com/YoungBear/JavaUtils)

