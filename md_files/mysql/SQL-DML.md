# MySQL 常用 SQL 命令（2. DML语句）

DML 操作是指对数据库中表记录的操作，主要包括表记录的插入（insert）、更新（update）、删除（delete）和查询（select），是日常使用最频繁的操作。

## 1. 插入记录 insert

`INSERT INTO <table_name>(field1, field2,...,fieldn) VALUES (value1, value2,...,valuen);`

eg.

```
mysql> insert into emp(ename,hiredate,sal,deptno) values('ysx', '2018-05-14','17000',2);
Query OK, 1 row affected (0.11 sec)

mysql> select * from emp;
+-------+------------+----------+--------+
| ename | hiredate   | sal      | deptno |
+-------+------------+----------+--------+
| ysx   | 2018-05-14 | 17000.00 |      2 |
+-------+------------+----------+--------+
1 row in set (0.00 sec)
```

也可以**不指定字段名称**，但是 values 后面的顺序应该和字段的排列顺序一致：

```
mysql> insert into emp values('huahua', '2018-01-16', '9000', 3);
Query OK, 1 row affected (0.09 sec)

mysql> select * from emp;
+--------+------------+----------+--------+
| ename  | hiredate   | sal      | deptno |
+--------+------------+----------+--------+
| ysx    | 2018-05-14 | 17000.00 |      2 |
| huahua | 2018-01-16 |  9000.00 |      3 |
+--------+------------+----------+--------+
2 rows in set (0.00 sec)
```

如果没有写字段，则这些字段可以自动设置为 NULL、默认值、自增的下一个数字。

**MySQL 特性：**

在 MySQL 中，insert 语句可以一次性插入多条记录，每条记录之间都用逗号分隔。这个特性可以使得 MySQL 在插入大量记录时，节省很多的网络开销，大大提高插入效率。

```
INSERT INTO <table_name> (field1,field2,...,fieldn)
VALUES
(record1_value1,record1_value2,...,record1_valuen),
(record2_value1,record2_value2,...,record2_valuen),
...
(recordn_value1,recordn_value2,...,recordn_valuen)
;
```

eg.

```
mysql> insert into dept values (5, 'dept5'),(6, 'dept6');
Query OK, 2 rows affected (0.10 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from dept;
+--------+----------+
| deptno | deptname |
+--------+----------+
|      5 | dept5    |
|      6 | dept6    |
+--------+----------+
2 rows in set (0.00 sec)
```

## 2. 更新记录 update

```
UPDATE <table_name> SET field1=value1,field2=value2,...,fieldn=valuen [WHERE CONDITION];
```

eg.

```
mysql> select * from emp;
+--------+------------+----------+--------+
| ename  | hiredate   | sal      | deptno |
+--------+------------+----------+--------+
| ysx    | 2018-05-14 | 17000.00 |      2 |
| huahua | 2018-01-16 |  9000.00 |      3 |
+--------+------------+----------+--------+
2 rows in set (0.00 sec)

mysql> update emp set sal=9500 where ename='huahua';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from emp;
+--------+------------+----------+--------+
| ename  | hiredate   | sal      | deptno |
+--------+------------+----------+--------+
| ysx    | 2018-05-14 | 17000.00 |      2 |
| huahua | 2018-01-16 |  9500.00 |      3 |
+--------+------------+----------+--------+
2 rows in set (0.00 sec)
```

**MySQL 特性：**

在 MySQL 里，update 命令可以同时更新多个表中的数据，语法如下：

```
UPDATE t1,t2,...,tn SET t1.field1=expr1,...,tn.exprn [WHERE CONDITION];
```

eg.

```
mysql> select * from emp;
+--------+------------+----------+--------+
| ename  | hiredate   | sal      | deptno |
+--------+------------+----------+--------+
| ysx    | 2018-05-14 | 17000.00 |      2 |
| huahua | 2018-01-16 |  9500.00 |      3 |
+--------+------------+----------+--------+
2 rows in set (0.00 sec)

mysql> select * from dept;
+--------+----------+
| deptno | deptname |
+--------+----------+
|      5 | dept5    |
|      6 | dept6    |
+--------+----------+
2 rows in set (0.00 sec)

mysql> update emp,dept set emp.sal=9600, dept.deptname='dept5_1' where emp.ename='ysx' and dept.deptno=5;
Query OK, 2 rows affected (0.07 sec)
Rows matched: 2  Changed: 2  Warnings: 0

mysql> select * from emp;
+--------+------------+---------+--------+
| ename  | hiredate   | sal     | deptno |
+--------+------------+---------+--------+
| ysx    | 2018-05-14 | 9600.00 |      2 |
| huahua | 2018-01-16 | 9500.00 |      3 |
+--------+------------+---------+--------+
2 rows in set (0.00 sec)

mysql> select * from dept;                                                      +--------+----------+
| deptno | deptname |
+--------+----------+
|      5 | dept5_1  |
|      6 | dept6    |
+--------+----------+
2 rows in set (0.00 sec)
```

**注意：**

多表更新的语法等多地用在了根据一个表的字段来动态地更新另外一个表的字段。

## 3. 删除记录 delete

```
DELETE FROM <table_name> [WHERE CONDITION];
```

**MySQL 特性：**

在 MySQL 中可以一次删除多个表的数据：

```
DELETE t1,t2,...,tn FROM t1,t2,...,tn [WHERE CONDITION];
```

eg.

```
mysql> select * from emp;
+--------+------------+---------+--------+
| ename  | hiredate   | sal     | deptno |
+--------+------------+---------+--------+
| ysx    | 2018-05-14 | 9600.00 |      2 |
| huahua | 2018-01-16 | 9500.00 |      3 |
+--------+------------+---------+--------+
2 rows in set (0.00 sec)

mysql> select * from dept;                                                      +--------+----------+
| deptno | deptname |
+--------+----------+
|      5 | dept5_1  |
|      6 | dept6    |
+--------+----------+
2 rows in set (0.00 sec)

mysql> delete a,b from emp a,dept b where a.ename='ysx' and b.deptno=5;
Query OK, 2 rows affected (0.02 sec)

mysql> select * from emp;
+--------+------------+---------+--------+
| ename  | hiredate   | sal     | deptno |
+--------+------------+---------+--------+
| huahua | 2018-01-16 | 9500.00 |      3 |
+--------+------------+---------+--------+
1 row in set (0.00 sec)

mysql> select * from dept;
+--------+----------+
| deptno | deptname |
+--------+----------+
|      6 | dept6    |
+--------+----------+
1 row in set (0.00 sec)

mysql>
```

## 4. 查询记录 select

```
SELECT * FROM <table_name> [WHERE CONDITION];
```

### 4.1 查询不重复的记录
使用 关键字 distinct。

### 4.2 条件查询

使用 where 条件语句进行条件查询。

### 4.3 排序和限制 order by 与 limit

使用 ORDER BY：

```
SELECT * FROM <table_name> [WHERE CONDITION] [ORDER BY field1 [DESC|ASC], field2 [DESC|ASC],...,fieldn [DESC|ASC]]
```

其中，DESC 表示降序，ASC 表示升序，默认是升序 ASC。

ORDER BY 后面可以跟多个不同的排序字段，并且每个排序字段可以有不同的排序顺序。

如果排序字段的值一样，则值相同的字段会按照第二个字段进行排序，以此类推。

LIMIT 关键字用来选择一部分数据：

```
SELECT ... [LIMIT offset_start,row_count];
```

其中，offset_start 表示记录的起始偏移量， row_count 表示显示的行数。
默认情况下，起始偏移量为 0，只需要写出记录行数就可以，这时，实际显示的就是前 n 条数据。

eg.

```
mysql> select * from dept;
+--------+----------+
| deptno | deptname |
+--------+----------+
|      6 | dept6    |
|      1 | dept1    |
|      2 | dept2    |
|      3 | dept3    |
|      4 | dept4    |
+--------+----------+
5 rows in set (0.00 sec)

mysql> select * from dept order by deptno limit 3;
+--------+----------+
| deptno | deptname |
+--------+----------+
|      1 | dept1    |
|      2 | dept2    |
|      3 | dept3    |
+--------+----------+
3 rows in set (0.00 sec)

mysql> select * from dept order by deptno limit 1,3;
+--------+----------+
| deptno | deptname |
+--------+----------+
|      2 | dept2    |
|      3 | dept3    |
|      4 | dept4    |
+--------+----------+
3 rows in set (0.00 sec)
```

**注意：**

limit是MySQL特有的语法，在其他数据库上并不能使用。

## 4. 聚合
聚合操作的语法：

```
SELECT [field1, field2,...,fieldn] fun_name
FROM <table_name>
[WHERE CONDITION]
[GROUP BY field1,field2,...,fieldn [WITH ROLLUP]]
[HAVING where_condition];
```

参数说明：

- fun_name 表示聚合操作，即聚合函数，如 sum（求和），count（记录数），max（最大值），min（最小值）等。
- GROUP BY 表示要进行分类聚合的字段。
- WITH ROLLUP 表示对分类聚合后的结果再进行汇总。
- HAVING 表示对分类后的结果再进行条件的过滤。

**注意：**

having 与 where 的区别在于， having 是对聚合后的结果进行条件的过滤，而 where 是在聚合前就对记录进行过滤，如果条件允许，我们尽可能用 where 先过滤记录，这样因为结果集减小，将对聚合的效率大大提高，最后再根据逻辑看是否用 having 进行再过滤。

eg.

```
mysql> select * from emp;
+----------+------------+----------+--------+
| ename    | hiredate   | sal      | deptno |
+----------+------------+----------+--------+
| huahua   | 2018-01-16 |  9500.00 |      3 |
| bearyang | 2018-05-14 | 17000.00 |      2 |
| xiaochen | 2018-05-14 | 18000.00 |      2 |
| dudu     | 2018-07-08 | 15000.00 |      2 |
+----------+------------+----------+--------+
4 rows in set (0.00 sec)

-- 在 emp 中统计公司的总人数：
mysql> select count(1) from emp;
+----------+
| count(1) |
+----------+
|        4 |
+----------+
1 row in set (0.00 sec)

-- 统计各个部门的人数：
mysql> select deptno, count(1) from emp group by deptno;
+--------+----------+
| deptno | count(1) |
+--------+----------+
|      3 |        1 |
|      2 |        3 |
+--------+----------+
2 rows in set (0.00 sec)

-- 统计各个部门的人数，再统计总人数：
mysql> select deptno, count(1) from emp group by deptno with rollup;
+--------+----------+
| deptno | count(1) |
+--------+----------+
|      2 |        3 |
|      3 |        1 |
|   NULL |        4 |
+--------+----------+
3 rows in set (0.00 sec)

-- 统计人数大于1人的部门：
mysql> select deptno, count(1) from emp group by deptno having count(1) > 1;
+--------+----------+
| deptno | count(1) |
+--------+----------+
|      2 |        3 |
+--------+----------+
1 row in set (0.00 sec)

-- 统计公司所有员工的薪水总额，最高，最低和平均值：
mysql> select sum(sal), max(sal), min(sal), avg(sal) from emp;
+----------+----------+----------+--------------+
| sum(sal) | max(sal) | min(sal) | avg(sal)     |
+----------+----------+----------+--------------+
| 59500.00 | 18000.00 |  9500.00 | 14875.000000 |
+----------+----------+----------+--------------+
1 row in set (0.00 sec)

-- 按照部门计算薪水平均值，再对所用人进行求薪水的平均值：
mysql> select deptno, avg(sal) from emp group by deptno with rollup;
+--------+--------------+
| deptno | avg(sal)     |
+--------+--------------+
|      2 | 16666.666667 |
|      3 |  9500.000000 |
|   NULL | 14875.000000 |
+--------+--------------+
3 rows in set (0.00 sec)
```

## 5. 表连接

- 内连接：仅选出两张表中互相匹配的记录；
- 外连接：会选择其他不匹配的记录。

eg.

```
mysql> select * from emp;
+----------+------------+----------+--------+
| ename    | hiredate   | sal      | deptno |
+----------+------------+----------+--------+
| huahua   | 2018-01-16 |  9500.00 |      3 |
| bearyang | 2018-05-14 | 17000.00 |      2 |
| xiaochen | 2018-05-14 | 18000.00 |      2 |
| dudu     | 2018-07-08 | 15000.00 |      2 |
+----------+------------+----------+--------+
4 rows in set (0.00 sec)

mysql> select * from dept;
+--------+----------+
| deptno | deptname |
+--------+----------+
|      6 | dept6    |
|      1 | dept1    |
|      2 | dept2    |
|      3 | dept3    |
|      4 | dept4    |
+--------+----------+
5 rows in set (0.00 sec)

mysql> select ename, deptname from emp, dept where emp.deptno = dept.deptno;
+----------+----------+
| ename    | deptname |
+----------+----------+
| bearyang | dept2    |
| xiaochen | dept2    |
| dudu     | dept2    |
| huahua   | dept3    |
+----------+----------+
4 rows in set (0.00 sec)
```

外连接分为**左外连接**和**右外连接**：

- 左连接：包含所有的左边表中的记录甚至是右边表中没有和它匹配的记录。
- 右连接：包含所有的右边表中的记录甚至是左边表中没有和它匹配的记录。

eg.

```
mysql> select * from emp;
+----------+------------+----------+--------+
| ename    | hiredate   | sal      | deptno |
+----------+------------+----------+--------+
| huahua   | 2018-01-16 |  9500.00 |      3 |
| bearyang | 2018-05-14 | 17000.00 |      2 |
| xiaochen | 2018-05-14 | 18000.00 |      2 |
| dudu     | 2018-07-08 | 15000.00 |      2 |
| gaogao   | 2018-08-10 | 22000.00 |      9 |
+----------+------------+----------+--------+
5 rows in set (0.00 sec)

mysql> select * from dept;
+--------+----------+
| deptno | deptname |
+--------+----------+
|      6 | dept6    |
|      1 | dept1    |
|      2 | dept2    |
|      3 | dept3    |
|      4 | dept4    |
+--------+----------+
5 rows in set (0.00 sec)

-- 内连接：互相匹配的记录
mysql> select ename, deptname from emp join dept on emp.deptno=dept.deptno;
+----------+----------+
| ename    | deptname |
+----------+----------+
| bearyang | dept2    |
| xiaochen | dept2    |
| dudu     | dept2    |
| huahua   | dept3    |
+----------+----------+
4 rows in set (0.00 sec)

-- 左外连接：左表所有记录
mysql> select ename, deptname from emp left join dept on emp.deptno=dept.deptno;
+----------+----------+
| ename    | deptname |
+----------+----------+
| bearyang | dept2    |
| xiaochen | dept2    |
| dudu     | dept2    |
| huahua   | dept3    |
| gaogao   | NULL     |
+----------+----------+
5 rows in set (0.00 sec)

-- 右外连接： 右表所有记录
mysql> select ename, deptname from emp right join dept on emp.deptno=dept.deptno;
+----------+----------+
| ename    | deptname |
+----------+----------+
| huahua   | dept3    |
| bearyang | dept2    |
| xiaochen | dept2    |
| dudu     | dept2    |
| NULL     | dept6    |
| NULL     | dept1    |
| NULL     | dept4    |
+----------+----------+
7 rows in set (0.00 sec)
```

## 6. 子查询

一个查询使用另一个 select 语句的结果，这时候就会用到子查询。常用关键字有 in, not in, =, !=, exists, not exists 等。

eg.

```
mysql> select * from emp;
+----------+------------+----------+--------+
| ename    | hiredate   | sal      | deptno |
+----------+------------+----------+--------+
| huahua   | 2018-01-16 |  9500.00 |      3 |
| bearyang | 2018-05-14 | 17000.00 |      2 |
| xiaochen | 2018-05-14 | 18000.00 |      2 |
| dudu     | 2018-07-08 | 15000.00 |      2 |
| gaogao   | 2018-08-10 | 22000.00 |      9 |
+----------+------------+----------+--------+
5 rows in set (0.00 sec)

mysql> select * from dept;
+--------+----------+
| deptno | deptname |
+--------+----------+
|      6 | dept6    |
|      1 | dept1    |
|      2 | dept2    |
|      3 | dept3    |
|      4 | dept4    |
+--------+----------+
5 rows in set (0.00 sec)

mysql> select * from emp where deptno in (select deptno from dept);
+----------+------------+----------+--------+
| ename    | hiredate   | sal      | deptno |
+----------+------------+----------+--------+
| huahua   | 2018-01-16 |  9500.00 |      3 |
| bearyang | 2018-05-14 | 17000.00 |      2 |
| xiaochen | 2018-05-14 | 18000.00 |      2 |
| dudu     | 2018-07-08 | 15000.00 |      2 |
+----------+------------+----------+--------+
4 rows in set (0.00 sec)
```

## 7. 记录联合

将两个表的数据合并到一起：

```
SELECT * FROM t1
UNION| UNION ALL
SELECT * FROM t2
...
UNION| UNION ALL
SELECT * FROM tn
```

UNION 是将 UNION ALL 后的结果进行一次 DISTINCT（去重）。

eg.

```
mysql> select * from emp;
+----------+------------+----------+--------+
| ename    | hiredate   | sal      | deptno |
+----------+------------+----------+--------+
| huahua   | 2018-01-16 |  9500.00 |      3 |
| bearyang | 2018-05-14 | 17000.00 |      2 |
| xiaochen | 2018-05-14 | 18000.00 |      2 |
| dudu     | 2018-07-08 | 15000.00 |      2 |
| gaogao   | 2018-08-10 | 22000.00 |      9 |
+----------+------------+----------+--------+
5 rows in set (0.00 sec)

mysql> select * from dept;
+--------+----------+
| deptno | deptname |
+--------+----------+
|      6 | dept6    |
|      1 | dept1    |
|      2 | dept2    |
|      3 | dept3    |
|      4 | dept4    |
+--------+----------+
5 rows in set (0.00 sec)

mysql> select deptno from emp union all select deptno from dept;
+--------+
| deptno |
+--------+
|      3 |
|      2 |
|      2 |
|      2 |
|      9 |
|      6 |
|      1 |
|      2 |
|      3 |
|      4 |
+--------+
10 rows in set (0.00 sec)

mysql> select deptno from emp union select deptno from dept;
+--------+
| deptno |
+--------+
|      3 |
|      2 |
|      9 |
|      6 |
|      1 |
|      4 |
+--------+
6 rows in set (0.00 sec)
```

## MySQL 系列：

### [1. MySQL 常用 SQL 命令（1. DDL语句）](https://github.com/YoungBear/MyBlog/blob/master/md_files/mysql/SQL-DDL.md)

### [2. MySQL 常用 SQL 命令（2. DML语句）](https://github.com/YoungBear/MyBlog/blob/master/md_files/mysql/SQL-DML.md)

### [3. MySQL 常用函数](https://github.com/YoungBear/MyBlog/blob/master/md_files/mysql/MySQL-Function.md)

### [4. MySQL 浮点数精度](https://github.com/YoungBear/MyBlog/blob/master/md_files/mysql/MySQLFloatPrecision.md)



### [更多文章](https://github.com/YoungBear/MyBlog/blob/master/README.md)