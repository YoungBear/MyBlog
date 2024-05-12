[TOC]

# Redis 基础



## 1. Redis 简介

Redis 全称： REmote DIctionary Server，即远程字典服务。

是一个开源的使用ANSI C语言编写、支持网络、可基于内存亦可以持久化的日志型、Key-Value型数据库。



## 2. Redis安装

### 2.1 windows下安装

参考：https://www.runoob.com/redis/redis-install.html

下载地址：https://github.com/tporadowski/redis/releases

将 `Redis-x64-5.0.14.1.zip` 解压后，把该路径添加到环境变量，打开命令行，就可以运行。

```shell
# 指定配置文件启动
redis-server redis.windows.conf

# 连接
redis-cli -h 127.0.0.1 -p 6379

# 设置并查看
127.0.0.1:6379> set nametest valuetest123
OK
127.0.0.1:6379> get nametest
"valuetest123"


```



windows下查看并删除redis进程：

```shell
# 根据端口查看
netstat -ano | findstr 6379
# 根据进程名查看
tasklist | findstr redis
# 杀掉进程
taskkill -pid <进程号> -f -t
```



### 2.2 可视化工具

AnotherRedisDesktop:

https://github.com/qishibo/AnotherRedisDesktopManager/releases



## 3. 集成springboot

### 3.1 添加pom依赖

```xml
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
```



### 3.2 添加配置：

```yaml
spring:
  redis:
    # Redis数据库索引（默认为0）
    database: 1
    # Redis本地服务器地址，默认为127.0.0.1
    host: 127.0.0.1
    # Redis服务器端口,默认为6379.若有改动按改动后的来
    port: 6379
    #Redis服务器连接密码，默认为空，若有设置按设置的来
    password:
    jedis:
      pool:
        # 连接池最大连接数，若为负数则表示没有任何限制
        max-active: 8
        # 连接池最大阻塞等待时间，若为负数则表示没有任何限制
        max-wait: -1
        # 连接池中的最大空闲连接
        max-idle: 8
```





### 3.3 添加测试代码

```java
package com.example.demo.controller;

import com.example.demo.entity.common.Result;
import com.example.demo.exception.DemoException;
import com.example.demo.utils.ResultUtils;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.concurrent.TimeUnit;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2022/5/9 23:28
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description redis基础
 */
@RestController
@Api("redis 测试接口")
@RequestMapping(value = "redis", produces = MediaType.APPLICATION_JSON_VALUE)
public class RedisController {
    private static final Logger LOGGER = LoggerFactory.getLogger(HelloController.class);

    @Autowired
    private StringRedisTemplate redisTemplate;

    @RequestMapping(value = "/setString", method = RequestMethod.POST)
    @ApiOperation("setString")
    public Result<String> setString(@ApiParam(name = "key", value = "key") @RequestParam(required = true) String key,
                                    @ApiParam(name = "value", value = "value") @RequestParam(required = true) String value) {

        redisTemplate.opsForValue().set(key, value);
        // 设置过期时间为1小时
        redisTemplate.expire(key, 3600L, TimeUnit.SECONDS);
        return ResultUtils.success("set successful.");
    }


    @RequestMapping(value = "/getString", method = RequestMethod.GET)
    @ApiOperation("getString")
    public Result<String> getString(@ApiParam(name = "key", value = "key") @RequestParam(required = true) String key) {
        String value = redisTemplate.opsForValue().get(key);
        Long expire = redisTemplate.getExpire(key);
        LOGGER.info("value: {}, expire: {}", value, expire);
        return ResultUtils.success("value: " + value + ", expire: " + expire);
    }
}

```



访问查看效果：

```shell
# 设置
curl -X POST "http://localhost:8888/redis/setString?key=name1&value=value1" -H "accept: application/json"

{
  "code": 0,
  "msg": "request successful.",
  "result": {
    "total": 1,
    "data": [
      "set successful."
    ]
  }
}
# 查看

curl -X GET "http://localhost:8888/redis/getString?key=name1" -H "accept: application/json"

{
  "code": 0,
  "msg": "request successful.",
  "result": {
    "total": 1,
    "data": [
      "value: value1, expire: 3580"
    ]
  }
}
```





## todo

### 1. redis基础

### 2. redis常用命令

### 3. springboot集成redis常用api

