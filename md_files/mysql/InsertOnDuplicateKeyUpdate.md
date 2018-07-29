# `insert` 语句的`on duplicate key update`

在mysql中，insert语句有这样的用法`insert into <table_name> values (v1, v2, v3) on duplicate key update ...`

这样的含义是：如果主键重复，或者`unique key`重复，则执行`update`语句；否则执行`insert`语句。

eg.

比如，有一个表`people`:

```
create table people(
    id int not null auto_increment,
    name varchar(100) not null,
    age int,
    primary key(id)
);
```

已经有数据：

```
mysql> select * from people;
+----+--------+------+
| id | name   | age  |
+----+--------+------+
|  3 | John   |   30 |
|  4 | \James |   33 |
+----+--------+------+
2 rows in set (0.00 sec)
```

然后，再执行`insert into people (id, name, age) values (3, 'Jack', 21) on duplicate key update name = 'Jack', age = 21;`语句的时候，因为已经存在主键3了，所以不执行`insert`语句，而执行`update`语句：

```
mysql> insert into people (id, name, age) values (3, 'Jack', 21) on duplicate key update name = 'Jack', age = 21;
Query OK, 2 rows affected (0.02 sec)

mysql> select * from people;
+----+--------+------+
| id | name   | age  |
+----+--------+------+
|  3 | Jack   |   21 |
|  4 | \James |   33 |
+----+--------+------+
2 rows in set (0.00 sec)
```

### [更多文章](https://github.com/YoungBear/MyBlog/blob/master/README.md)