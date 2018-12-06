# MySQL float 和 double 的精度

在 MySQL 中，float 表示单精度浮点数， double 表示双精度浮点数，decimal 表示定点数。定义 这些类型的数据时，同时需要指定其长度和精度 ，即用**名称（M，D**）来表示，M表示该值的总共长度，D表示小数点后面的长度，M和D又称为精度和标度。

如果 float 和 double 不指定精度，则按照实际的精度来显示， decimal 不指定时，默认为(10,2)。

这里，还有一个问题，对于 float 和 double，如果不指定精度，则不会存储小数点末尾的0，只有指定了具体的精度值，才会存储小数点末尾的0。

eg.

```
mysql> create table test2(f1 float, f2 float(5,2), f3 double, f4 double(10,2));
Query OK, 0 rows affected (0.10 sec)

mysql> insert into test2 values(12.30, 12.30, 12.30, 12.30);
Query OK, 1 row affected (0.10 sec)

mysql> select * from test2;
+------+-------+------+-------+
| f1   | f2    | f3   | f4    |
+------+-------+------+-------+
| 12.3 | 12.30 | 12.3 | 12.30 |
+------+-------+------+-------+
1 row in set (0.00 sec)

mysql> insert into test2 values(12.300, 12.300, 12.300, 12.300);
Query OK, 1 row affected (0.05 sec)

mysql> select * from test2;
+------+-------+------+-------+
| f1   | f2    | f3   | f4    |
+------+-------+------+-------+
| 12.3 | 12.30 | 12.3 | 12.30 |
| 12.3 | 12.30 | 12.3 | 12.30 |
+------+-------+------+-------+
2 rows in set (0.00 sec)

mysql> insert into test2 values(12.305, 12.305, 12.305, 12.305);
Query OK, 1 row affected (0.07 sec)

mysql> select * from test2;
+--------+-------+--------+-------+
| f1     | f2    | f3     | f4    |
+--------+-------+--------+-------+
|   12.3 | 12.30 |   12.3 | 12.30 |
|   12.3 | 12.30 |   12.3 | 12.30 |
| 12.305 | 12.30 | 12.305 | 12.30 |
+--------+-------+--------+-------+
3 rows in set (0.00 sec)
```

所以，要想保留小数点末尾的0，则必须对 float 或 double 指定精度值。


## MySQL 系列：

### [1. MySQL 常用 SQL 命令（1. DDL语句）](https://github.com/YoungBear/MyBlog/blob/master/md_files/mysql/SQL-DDL.md)

### [2. MySQL 常用 SQL 命令（2. DML语句）](https://github.com/YoungBear/MyBlog/blob/master/md_files/mysql/SQL-DML.md)

### [3. MySQL 常用函数](https://github.com/YoungBear/MyBlog/blob/master/md_files/mysql/MySQL-Function.md)



### [更多文章](https://github.com/YoungBear/MyBlog/blob/master/README.md)