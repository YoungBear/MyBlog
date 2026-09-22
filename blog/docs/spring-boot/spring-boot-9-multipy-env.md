---
title: "SpringBoot 学习笔记 9 - 多环境配置"
date: 2019-06-12
tags: []
---

# SpringBoot 学习笔记 9 - 多环境配置

在 `src/main/resources` 下新建文件:

```shell
application.yml
application-dev.yml
application-test.yml
application-prod.yml
```

其中，`application.yml` 用来指定具体使用哪个配置文件，其内容为：

```yaml
spring:
  profiles:
    active: test
```

则表示是使用的为 `application-test.yml`。

dev,test,prod分别表示开发，测试，生产环境。在实际的工作中，部署时使用脚本动态替换application.yml的active的值则可以做到多环境的部署。

可以在不同的环境下，配置不同的端口，数据库，日志等。



## [Demo GitHub地址](https://github.com/YoungBear/SpringBootDemo)




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
