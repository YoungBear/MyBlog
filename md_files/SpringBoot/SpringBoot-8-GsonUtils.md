# SpringBoot 学习笔记8 - GsonUtils 工具类



## 1. 解析通用格式的json

通用的json格式为：(以Book.java为例)

```json
{
  "code": 0,
  "msg": "request successful.",
  "result": {
    "total": 4,
    "data": [
      {
        "name": "数学之美",
        "publisher": "人民邮电出版社",
        "author": "吴军"
      },
      {
        "name": "重构 改善既有代码的设计",
        "publisher": "人民邮电出版社",
        "author": "Martin Fowler"
      },
      {
        "name": "机器学习实战",
        "publisher": "人民邮电出版社",
        "author": "Peter Harrington"
      },
      {
        "name": "Effective Java中文版",
        "publisher": "机械工业出版社",
        "author": "Joshua Bloch"
      }
    ]
  }
}
```



一般我们使用通用的json时，微服务之间的调用，会涉及到json的解析，这时候需要传入一个Class对象，既可以解析出来整个的对象：

```java
    /**
     * Gson 解析通用数据格式
     * @param json
     * @param clazz
     * @param <T>
     * @return
     */
    public static <T> Result<T> parseString(String json, Class<T> clazz) {
        //...
    }
```

**具体实现方案：**

### 1.1 使用Gson依赖：

```xml
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
    <version>2.8.5</version>
</dependency>
```

### 1.2 Java 代码

```java
package com.example.demo.utils;

import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2019-05-14 22:47
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description
 */
public class ParameterizedTypeImpl implements ParameterizedType {
    private final Class raw;
    private final Type[] args;

    public ParameterizedTypeImpl(Class raw, Type[] args) {
        this.raw = raw;
        this.args = args != null ? args : new Type[0];
    }

    @Override
    public Type[] getActualTypeArguments() {
        return args;
    }

    @Override
    public Type getRawType() {
        return raw;
    }

    @Override
    public Type getOwnerType() {
        return null;
    }
}
```



```java
package com.example.demo.utils;

import com.example.demo.entity.common.Result;
import com.google.gson.Gson;

import java.lang.reflect.Type;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2019-05-14 22:44
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description Gson 工具类
 */
public class GsonUtils {
    private static final Gson GSON = new Gson();

    /**
     * Gson 解析通用数据格式
     * @param json
     * @param clazz
     * @param <T>
     * @return
     */
    public static <T> Result<T> parseString(String json, Class<T> clazz) {
        Type type = new ParameterizedTypeImpl(Result.class, new Class[]{clazz});
        Result<T> result = GSON.fromJson(json, type);
        return result;
    }
}
```

### 1.3 单元测试

```java
package com.example.demo.utils;

import com.example.demo.entity.Book;
import com.example.demo.entity.common.Result;
import org.junit.Assert;
import org.junit.Test;

import java.util.List;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2019-05-14 22:54
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description Gson 工具类测试
 */
public class GsonUtilsTest {

    @Test
    public void parseStringTest() {
        String json = "{\n" +
                "  \"code\": 0,\n" +
                "  \"msg\": \"request successful.\",\n" +
                "  \"result\": {\n" +
                "    \"total\": 4,\n" +
                "    \"data\": [\n" +
                "      {\n" +
                "        \"name\": \"数学之美\",\n" +
                "        \"publisher\": \"人民邮电出版社\",\n" +
                "        \"author\": \"吴军\"\n" +
                "      },\n" +
                "      {\n" +
                "        \"name\": \"重构 改善既有代码的设计\",\n" +
                "        \"publisher\": \"人民邮电出版社\",\n" +
                "        \"author\": \"Martin Fowler\"\n" +
                "      },\n" +
                "      {\n" +
                "        \"name\": \"机器学习实战\",\n" +
                "        \"publisher\": \"人民邮电出版社\",\n" +
                "        \"author\": \"Peter Harrington\"\n" +
                "      },\n" +
                "      {\n" +
                "        \"name\": \"Effective Java中文版\",\n" +
                "        \"publisher\": \"机械工业出版社\",\n" +
                "        \"author\": \"Joshua Bloch\"\n" +
                "      }\n" +
                "    ]\n" +
                "  }\n" +
                "}";
        Result<Book> bookResult = GsonUtils.parseString(json, Book.class);
        Assert.assertEquals(0, bookResult.getCode().intValue());
        Assert.assertEquals(4, bookResult.getResult().getTotal().intValue());
        List<Book> data = bookResult.getResult().getData();

        // 排序
        data.sort((a, b) -> a.getName().compareTo(b.getName()));

        Assert.assertEquals("Effective Java中文版", data.get(0).getName());
        Assert.assertEquals("Joshua Bloch", data.get(0).getAuthor());
        Assert.assertEquals("机械工业出版社", data.get(0).getPublisher());
        Assert.assertEquals("吴军", data.get(1).getAuthor());
        Assert.assertEquals("人民邮电出版社", data.get(2).getPublisher());
        Assert.assertEquals("重构 改善既有代码的设计", data.get(3).getName());
    }
}
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