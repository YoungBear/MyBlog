# SpringBoot 学习笔记5 - Swagger-ui

## 1. 配置 pom 依赖

```xml
        <dependency>
            <groupId>io.springfox</groupId>
            <artifactId>springfox-swagger2</artifactId>
            <version>${springfox.version}</version>
        </dependency>

        <dependency>
            <groupId>io.springfox</groupId>
            <artifactId>springfox-swagger-ui</artifactId>
            <version>${springfox.version}</version>
        </dependency>
```

## 2. 添加 Swagger-ui 配置类

```java
package com.example.demo.configuration;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2019/3/24 10:10
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description Swagger ui 配置类
 */
@Configuration
@EnableSwagger2
public class SwaggerConfiguration {


    /**
     * 创建API应用
     * apiInfo() 增加API相关信息
     * 通过select()函数返回一个ApiSelectorBuilder实例,用来控制哪些接口暴露给Swagger来展现，
     * 本例采用指定扫描的包路径来定义指定要建立API的目录。
     *
     * @return
     */
    @Bean
    public Docket createRestApi() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(apiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.example.demo.controller"))
                .paths(PathSelectors.any())
                .build();
    }

    /**
     * 创建该API的基本信息（这些基本信息会展现在文档页面中）
     * 访问地址：http://项目实际地址/swagger-ui.html
     * @return
     */
    private ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .title("Spring Boot 学习之路- Swagger UI")
                .description("https://github.com/YoungBear/SpringBootDemo")
                .version("1.0")
                .contact(new Contact("ysx",
                        "https://blog.csdn.net/next_second",
                        "youngbear@aliyun.com"))
                .build();
    }

}

```

## 3. 使用注解添加接口描述

- `@Api` 注解在接口类上，描述类的功能。
- `@ApiOperation` 注解在方法上，描述方法的功能。
- `@ApiModel` 注解在类上，一般是请求或者返回实体类。
- `ApiModelProperty` 注解在属性上，用于描述实体的属性。



eg.

```java
package com.example.demo.controller;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2018/11/28 21:55
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description
 */
@RestController
@Api("Hello 测试接口")
public class HelloController {
    private static final Logger LOGGER = LoggerFactory.getLogger(HelloController.class);

    @RequestMapping(value = hi, method = RequestMethod.GET)
    @ResponseBody
    @ApiOperation(hi)
    public String hello() {
        LOGGER.trace("trace Hello");
        LOGGER.debug("debug Hello");
        LOGGER.info("info Hello");
        LOGGER.warn("warn Hello");
        LOGGER.error("error Hello");
        return "Hello World!";
    }
}

```



## 4. 接口地址：

如果使用 SpringBoot jar包方式启动，则文档地址为：

http://localhost:8080/swagger-ui.html

(默认端口为8080)

如果使用 tomcat 部署启动，则文档地址为：

http://localhost:9090/Demo/swagger-ui.html


## 5. 生产环境不显示Swagger-UI

在Swagger-UI的配置类`SwaggerConfiguration`中，对类添加注解：

```java
@Profile({"dev", "test"})
```

表示只在dev和test环境显示Swagger-UI，在其他环境不显示。



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

