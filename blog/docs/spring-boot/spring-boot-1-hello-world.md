---
title: "SpringBoot 学习笔记1 - HelloWorld"
date: 2019-05-15
tags: []
---

# SpringBoot 学习笔记1 - HelloWorld


从 [Spring Initializr](https://start.spring.io/) 官网生成项目包，选择 web模块。

然后，新建 `HelloController`

```
@RestController
public class HelloController {

    @RequestMapping("/hello")
    @ResponseBody
    public String hello() {
        return "Hello World!";
    }
}
```

在 `DemoApplication` 类中，运行程序：`Run DemoApplication.main()`，在浏览器地址栏输入：`http://localhost:8080/hello` ，就可以看到结果：`Hello World!`。



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
