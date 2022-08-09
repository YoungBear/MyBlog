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
