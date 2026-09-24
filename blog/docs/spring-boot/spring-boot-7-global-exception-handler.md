---
title: "SpringBoot 学习笔记7 - 处理全局异常"
date: 2019-05-15
tags: []
---

# SpringBoot 学习笔记7 - 处理全局异常



使用注解 `@RestControllerAdvice`，处理全局异常，在请求发生异常时，会通过该类进行处理：

```java
package com.example.demo.configuration;

import com.example.demo.entity.common.Result;
import com.example.demo.enums.ErrorEnum;
import com.example.demo.exception.DemoException;
import com.example.demo.utils.ResultUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2019-05-04 21:53
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description 全局异常处理
 */

@RestControllerAdvice
public class GlobalExceptionHandler {

    private static final Logger LOGGER = LoggerFactory.getLogger(GlobalExceptionHandler.class);

    // 未知异常
    @ExceptionHandler(value = Exception.class)
    public Result<String> defaultErrorHandler(Exception e) {
        LOGGER.error(e.getMessage(),e);
        return ResultUtils.error(ErrorEnum.UNKNOWN_ERROR);
    }

    // 自定义的异常
    @ExceptionHandler(value = DemoException.class)
    public Result<String> errorHandler(DemoException e) {
        LOGGER.error(e.getMessage(),e);
        return ResultUtils.error(e.getErrorEnum());
    }
}

```



## [Demo GitHub地址](https://github.com/YoungBear/SpringBootDemo)



## SpringBoot 学习笔记

### [1. HelloWorld](/spring-boot/spring-boot-1-hello-world)

### [2. logback 日志配置](/spring-boot/spring-boot-2-logback)

### [3. 返回 Json 串](/spring-boot/spring-boot-3-json)

### [4. Tomcat 部署](/spring-boot/spring-boot-4-tomcat)

### [6. 返回统一的Json格式](/spring-boot/spring-boot-6-common-json)

### [7. 处理全局异常](/spring-boot/spring-boot-7-global-exception-handler)

### [9. 多环境支持](/spring-boot/spring-boot-9-multipy-env)

### [10. 集成数据库](/spring-boot/spring-boot-10-database)

### [11. RestTemplate工具类](/spring-boot/spring-boot-11-rest-template-utils)
