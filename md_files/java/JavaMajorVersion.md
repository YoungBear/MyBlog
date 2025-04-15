# Java版本对应关系表

以下Java主要版本（Major Version）与公开大版本号的对应关系

| **公开大版本名称** | **Major 版本号** | **内部版本号格式** | **示例（`java -version`输出）** |
| :----------------- | :--------------- | :----------------- | :------------------------------ |
| Java 8 (1.8)       | 52 (0x34)        | `1.8.0_XXX`        | `1.8.0_301`                     |
| Java 9             | 53 (0x35)        | `9.0.X`            | `9.0.4`                         |
| Java 10            | 54 (0x36)        | `10.0.X`           | `10.0.2`                        |
| Java 11 (LTS)      | 55 (0x37)        | `11.0.X`           | `11.0.12`                       |
| Java 12            | 56 (0x38)        | `12.0.X`           | `12.0.2`                        |
| Java 13            | 57 (0x39)        | `13.0.X`           | `13.0.2`                        |
| Java 14            | 58 (0x3A)        | `14.0.X`           | `14.0.2`                        |
| Java 15            | 59 (0x3B)        | `15.0.X`           | `15.0.2`                        |
| Java 16            | 60 (0x3C)        | `16.0.X`           | `16.0.2`                        |
| Java 17 (LTS)      | 61 (0x3D)        | `17.0.X`           | `17.0.3`                        |
| Java 18            | 62 (0x3E)        | `18.0.X`           | `18.0.2`                        |
| Java 19            | 63 (0x3F)        | `19.0.X`           | `19.0.1`                        |
| Java 20            | 64 (0x40)        | `20.0.X`           | `20.0.1`                        |
| Java 21 (LTS)      | 65 (0x41)        | `21.0.X`           | `21.0.0`                        |



### **关键说明**

1. **Major版本号的作用**

   - 用于.class文件的兼容性标识。例如，Java 8生成的类文件Major版本号为52，Java 11为55。
   - JVM会根据Major版本号判断是否支持运行该.class文件（低版本JVM无法运行高版本类文件）。

2. **版本命名规则的演变**

   - **Java 8及之前**：使用`1.x`格式（如Java 8对应`1.8.0`）。
   - **Java 9及之后**：直接使用单个数字（如Java 9、11、17），并采用半年发布周期（非LTS版本仅提供6个月支持，LTS版本支持数年）。

3. **如何查看当前Java版本**

   ```shell
   java -version
   # 示例输出：
   openjdk version "21" 2023-09-19
   OpenJDK Runtime Environment (build 21+35-2513)
   OpenJDK 64-Bit Server VM (build 21+35-2513, mixed mode, sharing)
   ```

   

### **版本信息获取途径**

1. **官方文档**

   - **Oracle Java版本列表**：[Oracle Java SE Releases](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)
   - **OpenJDK官方维基**：[JDK Release Project](https://openjdk.org/projects/jdk/)

2. **版本发布说明（Release Notes）**

   - 每个版本的详细变更和版本号可在对应版本的Release Notes中查找：
     - OpenJDK: [JDK Release Notes](https://jdk.java.net/#release-notes)
     - Oracle: [Java SE Documentation](https://docs.oracle.com/en/java/javase/index.html)

3. **Class文件版本号查询**

   - 使用`javap`命令查看.class文件的Major版本号：

     ```shell
     javap -v DemoApplication.class | grep "major version"
       major version: 65
     # major version: 65 对应Java 21
     ```

4. **第三方资源**

   - **维基百科**：[Java版本历史](https://en.wikipedia.org/wiki/Java_version_history)
   - **Java版本支持时间表**：[Java版本支持时间表（如Azul）](https://www.azul.com/products/zulu-support/)



### **注意事项**

- **LTS（长期支持）版本**：Java 8、11、17、21为LTS版本，企业环境中广泛使用，提供长期更新支持。
- **兼容性问题**：高版本Java编译的类文件无法在低版本JVM中运行（需通过`-source`和`-target`参数指定兼容性）。
- **版本号跳跃**：Java 9的Major版本号为53，而非51（因历史原因跳过了Java 1.9的命名）。

