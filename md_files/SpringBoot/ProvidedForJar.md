# spring-boot 不打包provided的依赖



## 背景

在java工程中，有的依赖仅需要在编译态，而运行态不需要，如lombok，所以一般情况下，需要在pom的依赖配置中设置其scope为provided。

eg.

```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.34</version>
    <scope>provided</scope>
</dependency>
```

对于不同的打包方式，打包结果会有不同：

- war 包，BOOT-INF\lib\ 不会包含该依赖。
- jar 包，BOOT-INF\lib\ 中会包含该依赖的jar包。



## 方法

在spring-boot-maven-plugin打包插件的配置，使用标签 exclude，可以排除指定的jar包。或者使用 excludeGroupIds 标签。



使用 exclude 标签：

```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>org.projectlombok</groupId>
                            <artifactId>lombok</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
        <finalName>SpringBoot2Demo</finalName>
    </build>
```



使用 excludeGroupIds 标签：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <configuration>
                <excludeGroupIds>
                    org.projectlombok
                </excludeGroupIds>
            </configuration>
        </plugin>
    </plugins>
    <finalName>SpringBoot2Demo</finalName>
</build>
```