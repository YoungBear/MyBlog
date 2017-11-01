[GreenDAO Github地址][1]
[GreenDAO 官方网站][2]

## 介绍
GreenDAO是一个开源的Android端ORM(Object Relational Mapping 对象关系映射)框架，可以让用户使用Java方法来做增删改查等动作。

![GreenDAO结构][3]

## 使用

### 1. 添加gradle依赖

在**project**的build.gradle文件中添加：

注意，以下的greendao请输入**最新版本**。[在这里可以查看最新版本][4]
```
// In your root build.gradle file:
buildscript {
    repositories {
        jcenter()
        mavenCentral() // add repository
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:3.0.0'
        classpath 'org.greenrobot:greendao-gradle-plugin:3.2.2' // add plugin
    }
}
```

在具体的**module**的build.gradle文件中添加：

```
// In your app projects build.gradle file:
apply plugin: 'com.android.application'
apply plugin: 'org.greenrobot.greendao' // apply plugin
 
dependencies {
    compile 'org.greenrobot:greendao:3.2.2' // add library
}
```

### 2. 设置数据库版本等信息
在module的build.gradle文件添加：

```
greendao {
    schemaVersion 1
}
```
schemaVersion的值表示数据库版本号。

另外，用户还可以设置daoPackage属性。

- daoPackage表示通过gradle插件生成的数据库相关文件的包名，默认为你的entity所在的包名。

### 3. 编写实体类

```
@Entity
public class Player {
    @Id
    private Long id;
    @Unique
    private String name;
    private Integer age;
}
```

点击build后，AndroidStudio会自动生成这个类的其他部分：

```
@Entity
public class Player {
    @Id
    private Long id;
    @Unique
    private String name;
    private Integer age;
    @Generated(hash = 1461101279)
    public Player(Long id, String name, Integer age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }
    @Generated(hash = 30709322)
    public Player() {
    }
    public Long getId() {
        return this.id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return this.name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Integer getAge() {
        return this.age;
    }
    public void setAge(Integer age) {
        this.age = age;
    }
}
```

同时，AS会默认在`GreenDAOLearn\app\build\generated\source\greendao\com\ysx\greendaolearn\entity`目录下生成三个文件：

- DaoMaster.java
- DaoSession.java
- PlayerDao.java

![greendao_gen][5]

由于我们在.gitignore中添加了build，则该目录下的文件不会放在git库中，这些代码每次build的时候都会重新生成。

#### 实体类中常用的注解：

```
@Entity 　表明这个实体类会在数据库中生成一个与之相对应的表。 
@Id 　对应数据表中的 Id 字段，有了解数据库的话，是一条数据的唯一标识。 
@Property(nameInDb = “STUDENTNUM”) 　表名这个属性对应数据表中的 STUDENTNUM 字段。 
@Property 　可以自定义字段名，注意外键不能使用该属性 
@NotNull 　该属性值不能为空 
@Transient 　该属性不会被存入数据库中 
@Unique 　表名该属性在数据库中只能有唯一值
```

### 4. 操作数据库

#### 初始化数据库：

```
    /**
     * 数据库名称
     */
    private static final String DATABASE_NAME = "players.db";
    private DaoSession mDaoSession;
    /**
     * 初始化DaoSession
     * 即获取一个全局的DaoSession实例
     * // TODO: 2017/10/31 可以使用一个单例类单独管理这个对象
     */
    private void initDaoSession() {
        DaoMaster.OpenHelper openHelper = new DaoMaster.DevOpenHelper(
                mContext.getApplicationContext(), DATABASE_NAME, null);
        DaoMaster daoMaster = new DaoMaster(openHelper.getWritableDatabase());
        mDaoSession = daoMaster.newSession();
    }
```

全局保存一个DaoSession对象，用来对数据库进行操作。

#### 增

```
    /**
     * 插入一条数据
     *
     * @param player
     */
    private void insertData(Player player) {
        PlayerDao playerDao = mDaoSession.getPlayerDao();
        playerDao.insert(player);
    }
```

#### 删

```
    /**
     * 根据id删除一条数据
     *
     * @param id
     */
    private void deleteData(long id) {
        PlayerDao playerDao = mDaoSession.getPlayerDao();
        playerDao.deleteByKey(id);
    }
```

#### 改

```
    /**
     * 更新一条数据
     * 更新年龄
     *
     * @param id
     * @param age
     */
    private void updateData(long id, int age) {
        Log.d(TAG, "updateData: id: " + id + ", age: " + age);
        PlayerDao playerDao = mDaoSession.getPlayerDao();
        Player player = playerDao.queryBuilder()
                .where(PlayerDao.Properties.Id.eq(id))
                .build()
                .unique();
        player.setAge(age);
        playerDao.update(player);
    }
```

#### 查

```
    /**
     * 获取全部数据，按照Id升序排列
     *
     * @return 数据列表
     */
    private List<Player> getAllData() {
        PlayerDao playerDao = mDaoSession.getPlayerDao();
        return playerDao.queryBuilder()
                .orderAsc(PlayerDao.Properties.Id)
                .build()
                .list();
    }
```

## 混淆配置

```
-keep class org.greenrobot.greendao.**{*;}
-keepclassmembers class * extends org.greenrobot.greendao.AbstractDao {
public static java.lang.String TABLENAME;
}
-keep class **$Properties
```

# [Demo源代码地址][6]

# 参考

http://blog.csdn.net/zone_/article/details/69054997

http://blog.csdn.net/njweiyukun/article/details/51893092


  [1]: https://github.com/greenrobot/greenDAO
  [2]: http://greenrobot.org/greendao/
  [3]: http://greenrobot.org/wordpress/wp-content/uploads/greenDAO-orm-320.png
  [4]: http://search.maven.org/#search%7Cga%7C1%7Cg:%22org.greenrobot%22%20AND%20a:%22greendao%22
  [5]: http://img.blog.csdn.net/20171031192043622?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast
  [6]: https://github.com/YoungBear/GreenDAOLean