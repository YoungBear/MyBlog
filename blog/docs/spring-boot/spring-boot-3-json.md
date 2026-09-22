---
title: "SpringBoot 学习笔记3 - 返回 Json串"
date: 2019-05-15
tags: []
---

# SpringBoot 学习笔记3 - 返回 Json串


使用 `@RestController`:

```
@RestController
@RequestMapping("/v1/book")
public class BookController {

    @RequestMapping(value = "/books", method = RequestMethod.POST,
            produces = "application/json;charset=UTF-8")
    public List<Book> test() {
        List<Book> books = new ArrayList<>();
        Book b1 = new Book();
        b1.setName("数学之美");
        b1.setPublisher("人民邮电出版社");
        b1.setAuther("吴军");
        Book b2 = new Book();
        b2.setName("重构 改善既有代码的设计");
        b2.setPublisher("人民邮电出版社");
        b2.setAuther("Martin Fowler");
        Book b3 = new Book();
        b3.setName("机器学习实战");
        b3.setPublisher("人民邮电出版社");
        b3.setAuther("Peter Harrington");
        Book b4 = new Book();
        b4.setName("Effective Java中文版");
        b4.setPublisher("机械工业出版社");
        b4.setAuther("Joshua Bloch");
        books.add(b1);
        books.add(b2);
        books.add(b3);
        books.add(b4);
        return books;
    }

}
```

使用 curl 访问：

```
192:SpringBootDemo youngbear$ curl http://localhost:8080/v1/book/books -X POST
[{"name":"数学之美","publisher":"人民邮电出版社","author":"吴军"},{"name":"重构 改善既有代码的设计","publisher":"人民邮电出版社","author":"Martin Fowler"},{"name":"机器学习实战","publisher":"人民邮电出版社","author":"Peter Harrington"},{"name":"Effective Java中文版","publisher":"机械工业出版社","author":"Joshua Bloch"}]
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
