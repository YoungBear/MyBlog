# 夏令时



## 1. 概念

夏令时，（Daylight Saving Time：DST），也叫夏时制，又称“[日光节约时制](https://baike.baidu.com/item/日光节约时制/10349737)”和“夏令时间”，是一种为节约能源而人为规定地方时间的制度，在这一制度实行期间所采用的统一时间称为“夏令时间”。一般在天亮早的夏季人为将时间调快一小时，可以使人早起早睡，减少照明量，以充分利用光照资源，从而节约照明用电。各个采纳夏时制的国家具体规定不同。全世界有近110个国家每年要实行夏令时。

1986年4月，中国中央有关部门发出“在全国范围内实行夏时制的通知”，具体做法是：每年从四月中旬第一个星期日的凌晨2时整（北京时间），将时钟拨快一小时，即将表针由2时拨至3时，夏令时开始；到九月中旬第一个星期日的凌晨2时整（[北京夏令时](https://baike.baidu.com/item/北京夏令时/1882131)），再将时钟拨回一小时，即将表针由2时拨至1时，夏令时结束。从1986年到1991年的六个年度，除1986年因是实行夏时制的第一年，从5月4日开始到9月14日结束外，其它年份均按规定的时段施行。在夏令时开始和结束前几天，新闻媒体均刊登有关部门的通告。1992年起，夏令时暂停实行。

参考百度百科：https://baike.baidu.com/item/%E5%A4%8F%E4%BB%A4%E6%97%B6/1809579?fr=aladdin

## 2. Java中的常见方法



判断是否为夏令时，根据指定日期时间和指定时区：

```java
    /**
     * 是否是夏令时
     *
     * @param zoneIdString 时区id
     * @param instant      时间信息
     * @return 是否是夏令时
     */
    public static boolean isDST(String zoneIdString, Instant instant) {
        ZoneId zoneId = ZoneId.of(zoneIdString);
        ZoneRules rules = zoneId.getRules();
        return rules.isDaylightSavings(instant);
    }
```



详细请参考：

```
package com.ysx.utils.datetime;

import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.time.zone.ZoneRules;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2022/6/26 12:38
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description 夏令时
 * 参考：http://www.timeofdate.com/
 * 美国的夏令时，从每年3月第2个星期天凌晨开始，到每年11月第1个星期天凌晨结束。以2017年为例，美国2017年夏令时从3月12日开始，到11月5日结束。
 * America/New_York PT1H -04:00
 * 参考：http://www.timeofdate.com/country/United%20States
 * 澳大利亚的夏令时：从每年10月的第1个周日凌晨开始，到每年4月第1个周日凌晨结束。以2017年为例，澳大利亚在4月2日结束夏令时，在10月1日重新开始夏令时
 * Australia/Sydney PT1H +11:00
 * http://www.timeofdate.com/country/Australia
 */
public class DSTUtils {

    /**
     * 是否是夏令时
     *
     * @param zoneIdString 时区id
     * @param instant      时间信息
     * @return 是否是夏令时
     */
    public static boolean isDST(String zoneIdString, Instant instant) {
        ZoneId zoneId = ZoneId.of(zoneIdString);
        ZoneRules rules = zoneId.getRules();
        return rules.isDaylightSavings(instant);
    }

    /**
     * 是否是夏令时
     *
     * @param zoneIdString 时区id，如Asia/Shanghai
     * @param localDateTime localDateTime
     * @return 是否是夏令时
     */
    public static boolean isDST(String zoneIdString, LocalDateTime localDateTime) {
        ZoneId zoneId = ZoneId.of(zoneIdString);
        Instant instant = localDateTime.atZone(zoneId).toInstant();
        return isDST(zoneIdString, instant);
    }

    /**
     * 是否是夏令时
     *
     * @param zoneIdString 时区id，如Asia/Shanghai
     * @param timestamp 时间戳 如1655301989483L
     * @return 是否是夏令时
     */
    public static boolean isDST(String zoneIdString, long timestamp) {
        return isDST(zoneIdString, Instant.ofEpochMilli(timestamp));
    }

    /**
     * 是否是夏令时
     *
     * @param zoneIdString     时区id，如Asia/Shanghai
     * @param isoLocalDateTime iso日期时间格式，如：2022-06-15T22:06:29.483
     * @return 是否是夏令时
     */
    public static boolean isDST(String zoneIdString, String isoLocalDateTime) {
        DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ISO_LOCAL_DATE_TIME;
        ZoneId zoneId = ZoneId.of(zoneIdString);
        dateTimeFormatter.withZone(zoneId);
        LocalDateTime localDateTime = LocalDateTime.parse(isoLocalDateTime, dateTimeFormatter);
        return isDST(zoneIdString, localDateTime);
    }
}

```







## 3. 常见国家地区夏令时

详细夏令时规定可参考：http://www.timeofdate.com/



| 时区ID字符串        | 标准偏移值standardOffset | 是否有夏令时 | 使用夏令时的偏移值offset |
| ------------------- | ------------------------ | ------------ | ------------------------ |
| Asia/Shanghai       | +08:00                   | 否           | 无                       |
| Europe/London       | +00:00                   | 是           | +01:00     |
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

