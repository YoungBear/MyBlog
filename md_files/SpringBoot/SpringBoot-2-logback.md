# SpringBoot 学习笔记2 - logback日志配置


## 日志 logback.xml 配置

参考：[logback的使用和logback.xml详解](https://www.cnblogs.com/warking/p/5710303.html)

日志输出级别：
根据Level的级别，优先级大的优先输出，优先级从大到小为：
`ERROR>WARN>INFO>DEBUG>TRACE`



```
%d{yyyy-MM-dd'T'HH:mm:ss.SSS zXXX} 表示显示带时区的时间格式，如：
022-02-25T22:18:54.373 CST+08:00 [main] INFO  com.example.demo.DemoApplication:61 - xxx
```





logback-spring.xml的例子：

```
<?xml version="1.0" encoding="UTF-8"?>
<configuration>

    <!-- springboot 提供的显示颜色的工具 -->
    <conversionRule conversionWord="clr" converterClass="org.springframework.boot.logging.logback.ColorConverter" />

    <property name="LOG_HOME" value="/Users/youngbear/logs" />
    <property name="PROJECT_NAME" value="springbootdemo" />
    <!-- 控制台输出 -->
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
            <!--格式化输出：%d表示日期，%thread表示线程名，%-5level：级别从左显示5个字符宽度%msg：日志消息，%L表示打印日志所在文件的行数，%n是换行符-->
            <pattern>%d{yyyy-MM-dd'T'HH:mm:ss.SSS zXXX} [%thread] %-5level %logger{50}:%L - %msg%n</pattern>
        </encoder>
    </appender>
    <!-- 输出到文件 -->
    <appender name="FILE"  class="ch.qos.logback.core.rolling.RollingFileAppender">
        <!-- file 标签用来表示当前日志的文件，如果没有改标签的话，则使用FileNamePattern中的配置 -->
        <file>${LOG_HOME}/${PROJECT_NAME}/springbootdemo.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <!--日志文件输出的文件名-->
            <FileNamePattern>${LOG_HOME}/${PROJECT_NAME}/springbootdemo.%d{yyyy-MM-dd}.log</FileNamePattern>
            <!--日志文件保留天数-->
            <MaxHistory>15</MaxHistory>
        </rollingPolicy>
        <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
            <!--格式化输出：%d表示日期，%thread表示线程名，%-5level：级别从左显示5个字符宽度%msg：日志消息，%L表示打印日志所在文件的行数，%n是换行符-->
            <pattern>%d{yyyy-MM-dd'T'HH:mm:ss.SSS zXXX} [%thread] %-5level %logger{50}:%L - %msg%n</pattern>
        </encoder>
        <!--日志文件最大的大小-->
        <triggeringPolicy class="ch.qos.logback.core.rolling.SizeBasedTriggeringPolicy">
            <MaxFileSize>50MB</MaxFileSize>
        </triggeringPolicy>
    </appender>

    <!-- 日志输出级别 -->
    <root level="INFO">
        <appender-ref ref="STDOUT" />
        <appender-ref ref="FILE" />
    </root>
</configuration>
```

访问时，日志输出为：

```
2022-02-25T22:32:49.434 CST+08:00 [http-nio-8888-exec-1] INFO  com.example.demo.service.impl.HelloServiceImpl:27 - info Hello null
2022-02-25T22:32:49.434 CST+08:00 [http-nio-8888-exec-1] WARN  com.example.demo.service.impl.HelloServiceImpl:28 - warn Hello null
2022-02-25T22:32:49.435 CST+08:00 [http-nio-8888-exec-1] ERROR com.example.demo.service.impl.HelloServiceImpl:29 - error Hello null
```




## [Demo GitHub地址](https://github.com/YoungBear/SpringBootDemo)



## SpringBoot 学习笔记

### [1. HelloWorld](./SpringBoot-1-HelloWorld.md)

### [2. logback 日志配置](./SpringBoot-2-logback.md)

### [3. 返回 Json 串](./SpringBoot-3-Json.md)

### [4. Tomcat 部署](./SpringBoot-4-Tomcat.md)

### [5. Swagger-ui](./SpringBoot-5-Swagger-ui.md)

### [6. 返回统一的Json格式](./SpringBoot-6-CommonJson.md)

### [7. 处理全局异常](./SpringBoot-7-GlobalExceptionHandler.md)

### [8. GsonUtils 工具类](./SpringBoot-8-GsonUtils.md)

### [9. 多环境支持](./SpringBoot-9-MultipyEnv.md)

### [10. 集成数据库](./SpringBoot-10-Database.md)

