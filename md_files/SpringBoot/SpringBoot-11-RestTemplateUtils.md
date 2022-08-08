# RestTemplate工具类

RestTemplateUtils工具类代码：

```java
package com.example.demo.utils;

import com.example.demo.entity.common.ResultVo;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

import javax.annotation.Resource;


@Component
public class RestTemplateUtils {

    @Resource
    private RestTemplate restTemplate;

    public <T> ResultVo<T> get(String url, ObjectParameterizedTypeReference<T> responseType) {
        return http(url, HttpMethod.GET, null, responseType);
    }

    public <T> ResultVo<T> post(String url, Object request, ObjectParameterizedTypeReference<T> responseType) {
        return http(url, HttpMethod.POST, request, responseType);
    }

    public <T> ResultVo<T> http(String url, HttpMethod httpMethod, Object request, ObjectParameterizedTypeReference<T> responseType) {
        HttpHeaders httpHeaders = new HttpHeaders();
        httpHeaders.setContentType(MediaType.APPLICATION_JSON);
        HttpEntity<Object> requestData = new HttpEntity<>(request, httpHeaders);
        return restTemplate.exchange(url, httpMethod, requestData, responseType).getBody();
    }

    public static class ObjectParameterizedTypeReference <T> extends ParameterizedTypeReference<ResultVo<T>> {}
}

```



验证：

```java
package com.example.demo.controller;

import com.example.demo.entity.Book;
import com.example.demo.entity.EmployeeVo;
import com.example.demo.entity.common.ResultVo;
import com.example.demo.exception.DemoException;
import com.example.demo.service.IHelloService;
import com.example.demo.utils.RestTemplateUtils;
import com.example.demo.utils.ResultVoUtils;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;

@RestController
@Api("Hello 测试接口")
@RequestMapping(value = "hello", produces = MediaType.APPLICATION_JSON_VALUE)
public class HelloController {
    private static final Logger LOGGER = LoggerFactory.getLogger(HelloController.class);

    @Resource
    private RestTemplateUtils restTemplateUtils;


    @GetMapping(value = "/request-get")
    public ResultVo<Void> requestGet() {
        String url = "http://localhost:8888/employee/query/2";
        ResultVo<EmployeeVo> resultVo = restTemplateUtils.get(url,
                new RestTemplateUtils.ObjectParameterizedTypeReference<>());
        LOGGER.info("code: {}", resultVo.getCode());
        return ResultVoUtils.success(null);
    }

    @GetMapping(value = "/request-post")
    public ResultVo<Void> requestPost() {
        Book book = new Book();
        book.setAuthor("吴军");
        book.setPublisher("人民邮电出版社");
        book.setName("数学之美");
        String url = "http://localhost:8888/v1/book/one-book";
        ResultVo<Book> resultVo = restTemplateUtils.post(url,
                book,
                new RestTemplateUtils.ObjectParameterizedTypeReference<>());
        LOGGER.info("code: {}", resultVo.getCode());
        return ResultVoUtils.success(null);
    }
}

```



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

### [11. RestTemplate工具类](./SpringBoot-11-RestTemplateUtils.md)