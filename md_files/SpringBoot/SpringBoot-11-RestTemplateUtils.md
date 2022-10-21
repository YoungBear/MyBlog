# RestTemplate工具类

RestTemplateUtils工具类代码：

```java
package com.example.demo.utils;

import com.example.demo.enums.ErrorEnum;
import com.example.demo.exception.DemoException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;

import javax.annotation.Resource;

/**
 * Http请求工具类
 *
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2022/8/7 23:32
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description
 */
@Component
public class RestTemplateUtils {
    private static final Logger LOGGER = LoggerFactory.getLogger(RestTemplateUtils.class);

    @Resource
    private RestTemplate restTemplate;

    /**
     * http get 请求
     *
     * @param url url
     * @param responseType response类型
     * @param <T> 类型参数
     * @return response body
     */
    public <T> T get(String url, ParameterizedTypeReference<T> responseType) {
        return http(url, HttpMethod.GET, null, responseType);
    }

    /**
     * http post 请求
     *
     * @param url url
     * @param request 请求体
     * @param responseType response类型
     * @param <T> 类型参数
     * @return response body
     */
    public <T> T post(String url, Object request, ParameterizedTypeReference<T> responseType) {
        return http(url, HttpMethod.POST, request, responseType);
    }

    /**
     * http 请求
     *
     * @param url url
     * @param httpMethod method
     * @param request request
     * @param responseType response类型
     * @param <T> 类型参数
     * @return response body
     */
    public <T> T http(String url, HttpMethod httpMethod, Object request, ParameterizedTypeReference<T> responseType) {
        HttpHeaders httpHeaders = new HttpHeaders();
        httpHeaders.setContentType(MediaType.APPLICATION_JSON);
        HttpEntity<Object> requestData = new HttpEntity<>(request, httpHeaders);
        ResponseEntity<T> responseEntity;
        try {
            responseEntity = restTemplate.exchange(url, httpMethod, requestData, responseType);
        } catch (RestClientException e) {
            LOGGER.error("RestClientException when exchange", e);
            throw new DemoException(e, ErrorEnum.HTTP_REQUEST_ERROR);
        }
        if (responseEntity.getStatusCode() != HttpStatus.OK) {
            LOGGER.error("http request has response but status is not ok");
            throw new DemoException(ErrorEnum.HTTP_REQUEST_ERROR);
        }
        T body = responseEntity.getBody();
        if (body == null) {
            LOGGER.error("http request has response but response body is null");
            throw new DemoException(ErrorEnum.HTTP_REQUEST_ERROR);
        }
        return body;
    }

}

```



验证：

```java
package com.example.demo.controller;

import com.example.demo.entity.Book;
import com.example.demo.entity.EmployeeVo;
import com.example.demo.entity.common.ResultVo;
import com.example.demo.exception.DemoException;
import com.example.demo.utils.RestTemplateUtils;
import com.example.demo.utils.ResultVoUtils;
import com.google.gson.Gson;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2018/11/28 21:55
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description
 */
@RestController
@RequestMapping(value = "hello", produces = MediaType.APPLICATION_JSON_VALUE)
public class HelloController {
    private static final Logger LOGGER = LoggerFactory.getLogger(HelloController.class);

    @Resource
    private RestTemplateUtils restTemplateUtils;

    @GetMapping(value = "/request-get")
    public ResultVo<Void> requestGet() {
        String url = "http://localhost:8888/employee/query/2";
        ResultVo<EmployeeVo> resultVo = restTemplateUtils.get(url,
                new EmployeeVoParameterizedTypeReference());
        LOGGER.info("code: {}", resultVo.getCode());
        EmployeeVo employeeVo = resultVo.getResult().getData().get(0);
        LOGGER.info("employeeVo: {}", new Gson().toJson(employeeVo));
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
                book, new BookParameterizedTypeReference());
        LOGGER.info("code: {}", resultVo.getCode());
        Book responseBook = resultVo.getResult().getData().get(0);
        LOGGER.info("employeeVo: {}", new Gson().toJson(responseBook));
        return ResultVoUtils.success(null);
    }

    private static class EmployeeVoParameterizedTypeReference extends ParameterizedTypeReference<ResultVo<EmployeeVo>> {
    }

    ;

    private static class BookParameterizedTypeReference extends ParameterizedTypeReference<ResultVo<Book>> {
    }

    ;


}

```



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
