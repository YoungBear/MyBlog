# LocalDateTime ZonedDateTime Instant 的相互转换

## 1. 概念



| 类名          | 描述             | 示例                                         |
| ------------- | ---------------- | -------------------------------------------- |
| LocalDateTime | 本地日期时间     | 2022-06-15T22:06:29.483                      |
| ZonedDateTime | 带时区的日期时间 | 2022-06-15T22:06:29.483+08:00[Asia/Shanghai] |
| Instant       | 时间戳           | 1655301989483                                |



## 2. 常用java代码

```java
package com.ysx.utils.datetime;

import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2022/6/26 22:22
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description LocalDateTime ZonedDateTime Instant 的相互转换
 */
public class ConvertUtils {

    /**
     * 将 ZonedDateTime 转换为 LocalDateTime
     *
     * @param zonedDateTime 带时区的日期时间
     * @return 本地日期时间
     */
    public static LocalDateTime zoned2Local(ZonedDateTime zonedDateTime) {
        return zonedDateTime.toLocalDateTime();
    }

    /**
     * 将 LocalDateTime 转换为 ZonedDateTime
     *
     * @param localDateTime 本地日期时间
     * @param zoneId        时区
     * @return 带时区的日期时间
     */
    public static ZonedDateTime local2Zoned(LocalDateTime localDateTime, ZoneId zoneId) {
        return ZonedDateTime.of(localDateTime, zoneId);
    }

    /**
     * 将 Instant 转换为 LocalDateTime
     *
     * @param instant 时间戳
     * @param zoneId  时区
     * @return 本地日期时间
     */
    public static LocalDateTime instant2local(Instant instant, ZoneId zoneId) {
        return instant.atZone(zoneId).toLocalDateTime();
    }

    /**
     * 将 LocalDateTime 转换为 Instant
     *
     * @param localDateTime 本地日期时间
     * @param zoneId        时区
     * @return 时间戳
     */
    public static Instant local2Instant(LocalDateTime localDateTime, ZoneId zoneId) {
        return localDateTime.atZone(zoneId).toInstant();
    }


    /**
     * 将 Instant 转换为 ZonedDateTime
     *
     * @param instant 时间戳
     * @param zoneId  时区
     * @return 带时区的日期时间
     */
    public static ZonedDateTime instant2Zoned(Instant instant, ZoneId zoneId) {
        return instant.atZone(zoneId);
    }

    /**
     * 将 ZonedDateTime 转换为 Instant
     *
     * @param zonedDateTime 带时区的日期时间
     * @return 时间戳
     */
    public static Instant zoned2Instant(ZonedDateTime zonedDateTime) {
        return zonedDateTime.toInstant();
    }
}

```



单元测试：

```java
package com.ysx.utils.datetime;

import org.junit.Assert;
import org.junit.Test;

import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2022/6/26 22:40
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description
 */
public class ConvertUtilsTest {

    @Test
    public void testZonedDateTime() {
        String zonedDateTimeString = "2022-06-15T22:06:29.483+08:00[Asia/Shanghai]";
        DateTimeFormatter formatter = DateTimeFormatter.ISO_ZONED_DATE_TIME;
        ZonedDateTime zonedDateTime = ZonedDateTime.parse(zonedDateTimeString, formatter);

        // zoned2Local
        LocalDateTime localDateTime = ConvertUtils.zoned2Local(zonedDateTime);
        String localDateTimeString = "2022-06-15T22:06:29.483";
        Assert.assertEquals(localDateTimeString, localDateTime.format(DateTimeFormatter.ISO_LOCAL_DATE_TIME));
        // zoned2Instant
        Instant instant = ConvertUtils.zoned2Instant(zonedDateTime);
        long timestamp = 1655301989483L;
        Assert.assertEquals(timestamp, instant.toEpochMilli());
    }

    @Test
    public void testLocalDateTime() {
        String localDateTimeString = "2022-06-15T22:06:29.483";
        LocalDateTime localDateTime = LocalDateTime.parse(localDateTimeString, DateTimeFormatter.ISO_LOCAL_DATE_TIME);
        ZoneId zoneId = ZoneId.of("Asia/Shanghai");

        // local2Zoned
        ZonedDateTime zonedDateTime = ConvertUtils.local2Zoned(localDateTime, zoneId);
        String zonedDateTimeString = "2022-06-15T22:06:29.483+08:00[Asia/Shanghai]";
        Assert.assertEquals(zonedDateTimeString, zonedDateTime.format(DateTimeFormatter.ISO_ZONED_DATE_TIME));
        // local2Instant
        Instant instant = ConvertUtils.local2Instant(localDateTime, zoneId);
        long timestamp = 1655301989483L;
        Assert.assertEquals(timestamp, instant.toEpochMilli());
    }

    @Test
    public void testInstant() {
        long timestamp = 1655301989483L;
        Instant instant = Instant.ofEpochMilli(timestamp);
        ZoneId zoneId = ZoneId.of("Asia/Shanghai");

        // instant2local
        LocalDateTime localDateTime = ConvertUtils.instant2local(instant, zoneId);
        String localDateTimeString = "2022-06-15T22:06:29.483";
        Assert.assertEquals(localDateTimeString, localDateTime.format(DateTimeFormatter.ISO_LOCAL_DATE_TIME));

        // instant2Zoned
        ZonedDateTime zonedDateTime = ConvertUtils.instant2Zoned(instant, zoneId);
        String zonedDateTimeString = "2022-06-15T22:06:29.483+08:00[Asia/Shanghai]";
        Assert.assertEquals(zonedDateTimeString, zonedDateTime.format(DateTimeFormatter.ISO_ZONED_DATE_TIME));
    }

}

```



# 相关文章

## [1. LocalDateTime ZonedDateTime Instant 的相互转换](https://github.com/YoungBear/JavaUtils/blob/master/mdfiles/datetime/ConvertUtils.md)

## [2. 日期时间格式化与解析](https://github.com/YoungBear/JavaUtils/blob/master/mdfiles/datetime/FormatterUtils.md)

## [3. 带时区时间日期 ZonedDateTime](https://github.com/YoungBear/JavaUtils/blob/master/mdfiles/datetime/ZonedDateTimeUtils.md)

## [4. 夏令时](https://github.com/YoungBear/JavaUtils/blob/master/mdfiles/datetime/dst.md)



# [源代码地址](https://github.com/YoungBear/JavaUtils)



