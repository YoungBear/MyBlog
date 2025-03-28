# 使用DateTimeFormatterBuilder构建灵活的日期时间格式



## 1. 前缀0可选



```java
    @Test
    @DisplayName("前缀0可选")
    public void test_for_optional_prefix_zero() {
        DateTimeFormatter formatter = new DateTimeFormatterBuilder()
                // 日期部分（年、月、日）
                .appendValue(ChronoField.YEAR, 4) // 年份固定4位
                .appendLiteral('/') // 日期分隔符（可替换为 '-' 等）
                .appendValue(ChronoField.MONTH_OF_YEAR, 1, 2, SignStyle.NORMAL) // 1-2位月份
                .appendLiteral('/')
                .appendValue(ChronoField.DAY_OF_MONTH, 1, 2, SignStyle.NORMAL) // 1-2位日期
                // 解析策略（可选：STRICT, SMART, LENIENT）
                .toFormatter()
                .withResolverStyle(ResolverStyle.STRICT);

        assertEquals("2025-01-05", LocalDate.parse("2025/1/5", formatter).toString());
        assertEquals("2025-01-05", LocalDate.parse("2025/01/05", formatter).toString());
        assertEquals("2025-12-05", LocalDate.parse("2025/12/5", formatter).toString());
        assertEquals("2025-12-05", LocalDate.parse("2025/12/05", formatter).toString());
        assertEquals("2025-12-25", LocalDate.parse("2025/12/25", formatter).toString());
    }
```



## 2. ResolverStyle的几种模式



```java
    /**
     * STRICT: 严格按照字段的有效范围和日历规则解析，不允许任何无效值或越界行为
     */
    @Test
    @DisplayName("STRICT模式 严格模式")
    public void test_for_strict() {
        DateTimeFormatter formatter = new DateTimeFormatterBuilder()
                // 日期部分（年、月、日）
                .appendValue(ChronoField.YEAR, 4) // 年份固定4位
                .appendLiteral('/') // 日期分隔符（可替换为 '-' 等）
                .appendValue(ChronoField.MONTH_OF_YEAR, 1, 2, SignStyle.NORMAL) // 1-2位月份
                .appendLiteral('/')
                .appendValue(ChronoField.DAY_OF_MONTH, 1, 2, SignStyle.NORMAL) // 1-2位日期
                // 解析策略（可选：STRICT, SMART, LENIENT）
                .toFormatter()
                .withResolverStyle(ResolverStyle.STRICT);

        assertThrows(DateTimeException.class, () -> {
            LocalDate.parse("2025/02/29", formatter);
            LocalDate.parse("2025/13/01", formatter);
            LocalDate.parse("2025/01/32", formatter);
        });

    }

    /**
     * 自动修正明显不合理的日期，但不会跨月/年调整。修正规则基于“合理推断”
     * 默认值
     */
    @Test
    @DisplayName("SMART模式 智能模式，默认值")
    public void test_for_smart() {
        DateTimeFormatter formatter = new DateTimeFormatterBuilder()
                // 日期部分（年、月、日）
                .appendValue(ChronoField.YEAR, 4) // 年份固定4位
                .appendLiteral('/') // 日期分隔符（可替换为 '-' 等）
                .appendValue(ChronoField.MONTH_OF_YEAR, 1, 2, SignStyle.NORMAL) // 1-2位月份
                .appendLiteral('/')
                .appendValue(ChronoField.DAY_OF_MONTH, 1, 2, SignStyle.NORMAL) // 1-2位日期
                // 解析策略（可选：STRICT, SMART, LENIENT）
                .toFormatter()
                .withResolverStyle(ResolverStyle.SMART);
        // 对于非闰年的 02/29 会自动调整为 02/28
        assertEquals("2025-02-28", LocalDate.parse("2025/02/29", formatter).toString());
        // 对于 04/31的错误 会自动调整为 04/30
        assertEquals("2025-04-30", LocalDate.parse("2025/04/31", formatter).toString());

        // 对于明显的错误，也会报异常如 1月32日，13月01日
        assertThrows(DateTimeException.class, () -> {
            LocalDate.parse("2025/01/32", formatter);
            LocalDate.parse("2025/13/01", formatter);
        });
    }

    /**
     * 允许日期时间值超出合理范围，按“溢出进位”的数学逻辑自动调整
     */
    @Test
    @DisplayName("LENIENT模式 宽松模式")
    public void test_for_lenient() {
        DateTimeFormatter formatter = new DateTimeFormatterBuilder()
                // 日期部分（年、月、日）
                .appendValue(ChronoField.YEAR, 4) // 年份固定4位
                .appendLiteral('/') // 日期分隔符（可替换为 '-' 等）
                .appendValue(ChronoField.MONTH_OF_YEAR, 1, 2, SignStyle.NORMAL) // 1-2位月份
                .appendLiteral('/')
                .appendValue(ChronoField.DAY_OF_MONTH, 1, 2, SignStyle.NORMAL) // 1-2位日期
                // 解析策略（可选：STRICT, SMART, LENIENT）
                .toFormatter()
                .withResolverStyle(ResolverStyle.LENIENT);
        // 自动调整为后一天
        assertEquals("2025-03-01", LocalDate.parse("2025/02/29", formatter).toString());
        assertEquals("2026-01-01", LocalDate.parse("2025/13/01", formatter).toString());
        assertEquals("2025-02-01", LocalDate.parse("2025/01/32", formatter).toString());

    }
```





## 3. 时间字段可选



```java
    @Test
    @DisplayName("时间字段可选")
    public void test_for_optional_time() {
        DateTimeFormatter formatter = new DateTimeFormatterBuilder()
                // 日期部分（年、月、日）
                .appendValue(ChronoField.YEAR, 4) // 年份固定4位
                .appendLiteral('/') // 日期分隔符（可替换为 '-' 等）
                .appendValue(ChronoField.MONTH_OF_YEAR, 1, 2, SignStyle.NORMAL) // 1-2位月份
                .appendLiteral('/')
                .appendValue(ChronoField.DAY_OF_MONTH, 1, 2, SignStyle.NORMAL) // 1-2位日期
                // 时间部分（时、分、秒，可选）
                .optionalStart() // 时间部分为可选
                .appendLiteral(' ') // 日期和时间之间的分隔符（如 'T' 或空格）
                .appendValue(ChronoField.HOUR_OF_DAY, 1, 2, SignStyle.NORMAL) // 1-2位小时（24小时制）
                .appendLiteral(':')
                .appendValue(ChronoField.MINUTE_OF_HOUR, 1, 2, SignStyle.NORMAL) // 1-2位分钟
                .appendLiteral(':')
                .appendValue(ChronoField.SECOND_OF_MINUTE, 1, 2, SignStyle.NORMAL) // 1-2位秒
                .optionalEnd() // 时间部分结束
                // 默认值处理（例如时间部分缺失时，默认为 00:00:00）
                .parseDefaulting(ChronoField.HOUR_OF_DAY, 0)
                .parseDefaulting(ChronoField.MINUTE_OF_HOUR, 0)
                .parseDefaulting(ChronoField.SECOND_OF_MINUTE, 0)
                // 解析策略（可选：STRICT, SMART, LENIENT）
                .toFormatter()
                .withResolverStyle(ResolverStyle.STRICT);


        assertEquals("2025-01-05T01:05:08", LocalDateTime.parse("2025/1/5 1:5:8", formatter).toString());
        assertEquals("2025-12-05T23:05:59", LocalDateTime.parse("2025/12/5 23:5:59", formatter).toString());
        assertEquals("2025-09-30T00:00", LocalDateTime.parse("2025/9/30", formatter).toString());

        // 只能时分秒一起省略，不能单独省略秒字段
        assertThrows(DateTimeException.class, () -> {
            LocalDateTime.parse("2025/03/28 8:00", formatter);
        });
    }
```





## [源代码地址](https://github.com/YoungBear/JavaUtils/blob/master/src/test/java/com/ysx/utils/datetime/DateTimeFormatterBuilderTest.java)
