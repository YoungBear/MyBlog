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

### [1. HelloWorld](./SpringBoot-1-HelloWorld.md)

### [2. logback 日志配置](./SpringBoot-2-logback.md)

### [3. 返回 Json 串](./SpringBoot-3-Json.md)

### [4. Tomcat 部署](./SpringBoot-4-Tomcat.md)

### [6. 返回统一的Json格式](./SpringBoot-6-CommonJson.md)

### [7. 处理全局异常](./SpringBoot-7-GlobalExceptionHandler.md)

### [9. 多环境支持](./SpringBoot-9-MultipyEnv.md)

### [10. 集成数据库](./SpringBoot-10-Database.md)

### [11. RestTemplate工具类](./SpringBoot-11-RestTemplateUtils.md)
