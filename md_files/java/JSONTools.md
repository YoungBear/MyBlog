# Java 常用 Json 解析框架

常见json解析框架：

- [fastjson](https://github.com/alibaba/fastjson)
- [gson](https://github.com/google/gson)
- [jackson](https://github.com/FasterXML/jackson-databind)

## 1. fastjson

maven 引用：

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>1.2.56</version>
</dependency>
```

用法：

```java
Student student = StudentUtils.genStudent();
String jsonString = JSON.toJSONString(student);// 序列化
String jsonString1 = StudentUtils.STUDENT_STRING;
Student student1 = JSON.parseObject(jsonString1, Student.class);// 反序列化
```

## 2. Gson

maven 引用：

```xml
<dependency>
    <groupId>com.google.code.gson</groupId>
    <artifactId>gson</artifactId>
    <version>2.8.5</version>
</dependency>
```

用法：

```java
Student student = StudentUtils.genStudent();
Gson gson = new Gson();
String jsonString = gson.toJson(student); // 序列化
System.out.println(jsonString);

String jsonString1 = StudentUtils.STUDENT_STRING;
Student student1 = gson.fromJson(jsonString1, Student.class); // 反序列化
System.out.println(student1);
```

## 3. Jackson

maven 引用：

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.9.8</version>
</dependency>
```

用法：

```java
Student student = StudentUtils.genStudent();
ObjectMapper objectMapper = new ObjectMapper();
String jsonString = objectMapper.writeValueAsString(student); // 序列化
System.out.println(jsonString);

String jsonString1 = StudentUtils.STUDENT_STRING;
Student student1 = objectMapper.readValue(jsonString1, Student.class); // 反序列化
System.out.println(student1);
```

### [Demo 地址](https://github.com/YoungBear/JsonDemo)



## [更多文章](https://github.com/YoungBear/MyBlog/blob/master/README.md)