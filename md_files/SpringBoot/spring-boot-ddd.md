# spring-boot 代码使用DDD结构



## 代码结构

```
└───com.example.demo
             ├───api
             │   └───controller
             ├───application
             │   ├───configuration
             │   │   ├───event
             │   │   └───listener
             │   └───service
             │       └───impl
             ├───domain
             │   ├───entity
             │   ├───repository
             │   │   └───dao
             │   └───service
             └───infrastructure
                 ├───entity
                 ├───enums
                 ├───exception
                 └───utils
```



## 架构看护

使用archunit的单元测试看护代码结构：



引入依赖：

```xml
<dependency>
    <groupId>com.tngtech.archunit</groupId>
    <artifactId>archunit-junit5</artifactId>
    <version>${archunit.version}</version>
    <scope>test</scope>
</dependency>
```



单元测试代码：

```java
package com.example.demo;

import com.tngtech.archunit.core.importer.ImportOption;
import com.tngtech.archunit.junit.AnalyzeClasses;
import com.tngtech.archunit.junit.ArchTest;
import com.tngtech.archunit.lang.ArchRule;

import static com.tngtech.archunit.lang.syntax.ArchRuleDefinition.noClasses;
import static com.tngtech.archunit.library.Architectures.layeredArchitecture;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2025-04-14 23:21
 * @blog <a href="https://blog.csdn.net/next_second">...</a>
 * @github <a href="https://github.com/YoungBear">...</a>
 * @description ddd 代码架构看护类
 */
@AnalyzeClasses(packages = "com.example.demo", importOptions = {ImportOption.DoNotIncludeTests.class})
public class CodeGuardArchTest {
    /**
     * infrastructure 不能被其他包引用（常用于不同领域之间的依赖看护）
     */
    @ArchTest
    static final ArchRule infrastructure_should_not_depend_on_others = noClasses().that()
            .resideInAPackage("..infrastructure..")
            .should()
            .dependOnClassesThat()
            .resideInAnyPackage("..application..", "..domain..", "..api..");

    /**
     * 代码分层依赖看护
     */
    @ArchTest
    static final ArchRule codeLayeredArchTest = layeredArchitecture().consideringAllDependencies()
            // 定义 interface 层
            .layer("api").definedBy("com.example.demo..api..")
            // 定义 application 层
            .layer("application").definedBy("com.example.demo..application..")
            // 定义 domain 层
            .layer("domain").definedBy("com.example.demo..domain..")
            // 定义 infrastructure 层
            .layer("infrastructure").definedBy("com.example.demo..infrastructure..")
            // api 层不能被其他层依赖
            .whereLayer("api").mayNotBeAccessedByAnyLayer()
            // application 层只能被 api 层依赖
            .whereLayer("application").mayOnlyBeAccessedByLayers("api")
            // domain 层只能被 api application 层依赖
            .whereLayer("domain").mayOnlyBeAccessedByLayers("api", "application");
}
```



## 源代码地址

 - [github](https://github.com/YoungBear/SpringBootDemo)
 - [gitee](https://gitee.com/YoungBear2023/spring-boot-demo)
