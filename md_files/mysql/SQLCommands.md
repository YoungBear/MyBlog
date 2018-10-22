# MySQL 常用 SQL 命令

SQL : Structure Query Language 结构化查询语言。
SQL 语句分类：

- DDL (Data Definition Language): 数据定义语言。如 create, drop, alter等。
- DML (Data Manipulation Language): 数据操纵语言。如 insert, delete, update, select等。
- DCL (Data Control Language): 数据控制语言。如 grant, revoke等。

**连接数据库：**

```
mysql -u <user_name> -p
```
eg.

```
192:~ youngbear$ mysql -u bearyang -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.11 MySQL Community Server - GPL

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

本文章使用的 MySQL 版本是 **8.0.11**。

## 1. DDL 语句
### 1.1 创建数据库:

`CREATE DATABASE <dbname>;`

**显示数据库：**

`show databases;`

**使用数据库：**

`USE <dbname>;`

**显示数据库中的表：**

`show tables;`

**使用表：**

`USE <table_name>;`

### 1.2 删除数据库

`DROP DATABASE <dbname>;`

eg.

```
mysql> drop database db201810;
Query OK, 0 rows affected (0.10 sec)
```

注意： 在 MySQL 里面，drop 语句操作的结果都是显示 **"0 rows affected"** 。

### 1.3 创建表
**创建表的基本语句：**

```
CREATE TABLE <table_name> (
    column_name_1 column_type_1 constraints,
    column_name_2 column_type_2 constraints,
    column_name_n column_type_n constraints
);
```

eg.

```
mysql> create table emp(
    ->     ename varchar(10),
    ->     hiredate date,
    ->     sal decimal(10,2),
    ->     deptno int(2)
    -> );
Query OK, 0 rows affected (0.12 sec)
```

**查看表的定义：**

`DESC <table_name>;`

eg.

```
mysql> desc emp;
+----------+---------------+------+-----+---------+-------+
| Field    | Type          | Null | Key | Default | Extra |
+----------+---------------+------+-----+---------+-------+
| ename    | varchar(10)   | YES  |     | NULL    |       |
| hiredate | date          | YES  |     | NULL    |       |
| sal      | decimal(10,2) | YES  |     | NULL    |       |
| deptno   | int(2)        | YES  |     | NULL    |       |
+----------+---------------+------+-----+---------+-------+
4 rows in set (0.01 sec)
```

查看创建表的 SQL 语句：

`show create table <table_name> \G;`

eg.

```
mysql> show create table emp \G;
*************************** 1. row ***************************
       Table: emp
Create Table: CREATE TABLE `emp` (
  `ename` varchar(10) DEFAULT NULL,
  `hiredate` date DEFAULT NULL,
  `sal` decimal(10,2) DEFAULT NULL,
  `deptno` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
1 row in set (0.00 sec)

ERROR:
No query specifieds
```

其中，engine 表示**存储引擎**， charset 表示**字符集**， collate 表示 **校对集**。

"\G" 选项的含义是使得记录能够按照字段竖向排列，以便更好地显示内容较长的记录。

### 1.4 删除表

`DROP TABLE <table_name>;`

eg.

```
mysql> drop table emp;
Query OK, 0 rows affected (0.04 sec)
```

### 1.5 修改表

#### 1.5.1 修改表类型

```
ALTER TABLE <table_name> MODIFY [COLUMN] <column_definition> [FIRST|AFTER <col_name>];
```

eg. 修改表emp的ename字段定义，将 varchar(10)改为varchar(20):

```
mysql> desc emp;
+----------+---------------+------+-----+---------+-------+
| Field    | Type          | Null | Key | Default | Extra |
+----------+---------------+------+-----+---------+-------+
| ename    | varchar(10)   | YES  |     | NULL    |       |
| hiredate | date          | YES  |     | NULL    |       |
| sal      | decimal(10,2) | YES  |     | NULL    |       |
| deptno   | int(2)        | YES  |     | NULL    |       |
+----------+---------------+------+-----+---------+-------+
4 rows in set (0.01 sec)

mysql> alter table emp modify ename varchar(20);
Query OK, 0 rows affected (0.08 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc emp;
+----------+---------------+------+-----+---------+-------+
| Field    | Type          | Null | Key | Default | Extra |
+----------+---------------+------+-----+---------+-------+
| ename    | varchar(20)   | YES  |     | NULL    |       |
| hiredate | date          | YES  |     | NULL    |       |
| sal      | decimal(10,2) | YES  |     | NULL    |       |
| deptno   | int(2)        | YES  |     | NULL    |       |
+----------+---------------+------+-----+---------+-------+
4 rows in set (0.00 sec)
```

#### 1.5.2 增加表字段

```
ALTER TABLE <table_name> ADD [COLUMN] <column_definition> [FIRST|AFTER <col_name>];
```

eg. 在表 emp 中新增加字段 age，类型为 int(3):

```
mysql> desc emp;
+----------+---------------+------+-----+---------+-------+
| Field    | Type          | Null | Key | Default | Extra |
+----------+---------------+------+-----+---------+-------+
| ename    | varchar(20)   | YES  |     | NULL    |       |
| hiredate | date          | YES  |     | NULL    |       |
| sal      | decimal(10,2) | YES  |     | NULL    |       |
| deptno   | int(2)        | YES  |     | NULL    |       |
+----------+---------------+------+-----+---------+-------+
4 rows in set (0.00 sec)

mysql> alter table emp add column age int(3);
Query OK, 0 rows affected (0.12 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc emp;
+----------+---------------+------+-----+---------+-------+
| Field    | Type          | Null | Key | Default | Extra |
+----------+---------------+------+-----+---------+-------+
| ename    | varchar(20)   | YES  |     | NULL    |       |
| hiredate | date          | YES  |     | NULL    |       |
| sal      | decimal(10,2) | YES  |     | NULL    |       |
| deptno   | int(2)        | YES  |     | NULL    |       |
| age      | int(3)        | YES  |     | NULL    |       |
+----------+---------------+------+-----+---------+-------+
5 rows in set (0.01 sec)
```

其中，column可以省略。

#### 1.5.3 删除表字段

```
ALTER TABLE <table_name> DROP [COLUMN] <col_name>;
```

eg. 删除 emp 的 age 字段：

```
mysql> desc emp;
+----------+---------------+------+-----+---------+-------+
| Field    | Type          | Null | Key | Default | Extra |
+----------+---------------+------+-----+---------+-------+
| ename    | varchar(20)   | YES  |     | NULL    |       |
| hiredate | date          | YES  |     | NULL    |       |
| sal      | decimal(10,2) | YES  |     | NULL    |       |
| deptno   | int(2)        | YES  |     | NULL    |       |
| age      | int(3)        | YES  |     | NULL    |       |
+----------+---------------+------+-----+---------+-------+
5 rows in set (0.01 sec)

mysql> alter table emp drop age;
Query OK, 0 rows affected (0.08 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc emp;
+----------+---------------+------+-----+---------+-------+
| Field    | Type          | Null | Key | Default | Extra |
+----------+---------------+------+-----+---------+-------+
| ename    | varchar(20)   | YES  |     | NULL    |       |
| hiredate | date          | YES  |     | NULL    |       |
| sal      | decimal(10,2) | YES  |     | NULL    |       |
| deptno   | int(2)        | YES  |     | NULL    |       |
+----------+---------------+------+-----+---------+-------+
4 rows in set (0.01 sec)
```

#### 1.5.4 字段改名

```
ALTER TABLE <table_name> CHANGE [COLUMN] <old_col_name> <column_definition> [FIRST|AFTER <col_name>];
```

eg. 将 emp 的 age 改名为 age1, 同时修改字段类型为 int(4);

```
mysql> desc emp;
+----------+---------------+------+-----+---------+-------+
| Field    | Type          | Null | Key | Default | Extra |
+----------+---------------+------+-----+---------+-------+
| ename    | varchar(20)   | YES  |     | NULL    |       |
| hiredate | date          | YES  |     | NULL    |       |
| sal      | decimal(10,2) | YES  |     | NULL    |       |
| deptno   | int(2)        | YES  |     | NULL    |       |
| age      | int(3)        | YES  |     | NULL    |       |
+----------+---------------+------+-----+---------+-------+
5 rows in set (0.00 sec)

mysql> alter table emp change age age1 int(4);
Query OK, 0 rows affected (0.10 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc emp;
+----------+---------------+------+-----+---------+-------+
| Field    | Type          | Null | Key | Default | Extra |
+----------+---------------+------+-----+---------+-------+
| ename    | varchar(20)   | YES  |     | NULL    |       |
| hiredate | date          | YES  |     | NULL    |       |
| sal      | decimal(10,2) | YES  |     | NULL    |       |
| deptno   | int(2)        | YES  |     | NULL    |       |
| age1     | int(4)        | YES  |     | NULL    |       |
+----------+---------------+------+-----+---------+-------+
5 rows in set (0.00 sec)
```

**注意：**
change 和 modify 都可以修改表的定义，不同的是 change 后面需要写两次列名，不方便。但是 change 的优点是修改列名称， modify 则不能。

#### 1.5.5 修改字段排列顺序

前面的**字段增加**和**修改语法**（ADD/CHANGE/MODIFY）中，都有一个可选项[FIRST|AFTER <col_name>]，表示修改字段在表中的位置。ADD 增加新字段默认在表的最后位置，而 CHANGE/MODIFY 默认都不会改变字段的位置。

eg1. 将新增字段 birth 加在 ename 之后：

```
mysql> desc emp;
+----------+---------------+------+-----+---------+-------+
| Field    | Type          | Null | Key | Default | Extra |
+----------+---------------+------+-----+---------+-------+
| ename    | varchar(20)   | YES  |     | NULL    |       |
| hiredate | date          | YES  |     | NULL    |       |
| sal      | decimal(10,2) | YES  |     | NULL    |       |
| deptno   | int(2)        | YES  |     | NULL    |       |
| age1     | int(4)        | YES  |     | NULL    |       |
+----------+---------------+------+-----+---------+-------+
5 rows in set (0.01 sec)

mysql> alter table emp add birth date after ename;
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc emp;
+----------+---------------+------+-----+---------+-------+
| Field    | Type          | Null | Key | Default | Extra |
+----------+---------------+------+-----+---------+-------+
| ename    | varchar(20)   | YES  |     | NULL    |       |
| birth    | date          | YES  |     | NULL    |       |
| hiredate | date          | YES  |     | NULL    |       |
| sal      | decimal(10,2) | YES  |     | NULL    |       |
| deptno   | int(2)        | YES  |     | NULL    |       |
| age1     | int(4)        | YES  |     | NULL    |       |
+----------+---------------+------+-----+---------+-------+
6 rows in set (0.00 sec)
```

eg. 2. 修改字段 age1 为 age,类型改为 int(3)， 并将它放在最前面：

```
mysql> desc emp;
+----------+---------------+------+-----+---------+-------+
| Field    | Type          | Null | Key | Default | Extra |
+----------+---------------+------+-----+---------+-------+
| ename    | varchar(20)   | YES  |     | NULL    |       |
| birth    | date          | YES  |     | NULL    |       |
| hiredate | date          | YES  |     | NULL    |       |
| sal      | decimal(10,2) | YES  |     | NULL    |       |
| deptno   | int(2)        | YES  |     | NULL    |       |
| age1     | int(4)        | YES  |     | NULL    |       |
+----------+---------------+------+-----+---------+-------+
6 rows in set (0.00 sec)

mysql> alter table emp change age1 age int(3) first;
Query OK, 0 rows affected (0.07 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc emp;
+----------+---------------+------+-----+---------+-------+
| Field    | Type          | Null | Key | Default | Extra |
+----------+---------------+------+-----+---------+-------+
| age      | int(3)        | YES  |     | NULL    |       |
| ename    | varchar(20)   | YES  |     | NULL    |       |
| birth    | date          | YES  |     | NULL    |       |
| hiredate | date          | YES  |     | NULL    |       |
| sal      | decimal(10,2) | YES  |     | NULL    |       |
| deptno   | int(2)        | YES  |     | NULL    |       |
+----------+---------------+------+-----+---------+-------+
6 rows in set (0.00 sec)
``` 

#### 1.5.6 更改表名

`ALTER TABLE <table_name> RENAME [TO] <new_table_name>;`

eg. 将 emp 改为 emp1;

```
mysql> alter table emp rename emp1;
Query OK, 0 rows affected (0.05 sec)

mysql> show tables;
+--------------------+
| Tables_in_db201810 |
+--------------------+
| emp1               |
+--------------------+
1 row in set (0.00 sec)
```

todo:
DML 和DCL。

# 参考

[1. 深入浅出 MySQL 数据库开发、优化与管理维护](https://baike.baidu.com/item/%E6%B7%B1%E5%85%A5%E6%B5%85%E5%87%BAMySQL%E6%95%B0%E6%8D%AE%E5%BA%93%E5%BC%80%E5%8F%91%E3%80%81%E4%BC%98%E5%8C%96%E4%B8%8E%E7%AE%A1%E7%90%86%E7%BB%B4%E6%8A%A4/6692124)

