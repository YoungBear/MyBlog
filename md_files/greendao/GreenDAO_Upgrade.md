## 数据库升级

我们可以自定义一个MyOpenHelper类，来继承DaoMaster.OpenHelper，当初始化数据库的时候，我们就可以调用这个类来新建对象:

```
    MyOpenHelper openHelper = new MyOpenHelper(
                    context.getApplicationContext(), DATABASE_NAME, null);
```

```
    /**
     * 定义一个MySQLiteOpenHelper类，用来处理数据库升级
     */
    static class MyOpenHelper extends DaoMaster.OpenHelper {

        public MyOpenHelper(Context context, String name, SQLiteDatabase.CursorFactory factory) {
            super(context, name, factory);
        }

        @Override
        public void onUpgrade(Database db, int oldVersion, int newVersion) {
            super.onUpgrade(db, oldVersion, newVersion);
        }
    }
```

在app的build.gradle文件中，将greendao 里边的schemaVersion字段增加，则做到了数据库升级的效果。再次运行程序，就会调用我们的MyOpenHelper的onUpgradle方法。

在这里，我们采用github上很有用的数据库升级数据迁移开元库[GreenDaoUpgradeHelper](https://github.com/yuweiguocn/GreenDaoUpgradeHelper)。在数据库升级的时候，做数据迁移。具体使用方法为：

假如为Player添加一个Integer的champion字段，用来表示获得的总冠军次数。

1. 将schemaVersion的值由1改为2.
2. 数据迁移：覆盖MyOpenHelper的onUpgrade方法。即调用MigrationHelper的migrate方法，实现接口ReCreateAllTableListener的两个方法（这是固定的），再将PlayerDao.class作为另个一个参数传入。
3. 修改显示champion的Adapter的方法：

```
    if (player.getChampion() == null) {
            holder.mTvChampion.setVisibility(View.GONE);
        } else {
            holder.mTvChampion.setVisibility(View.VISIBLE);
            holder.mTvChampion.setText(mContext.getString(R.string.player_champion, player.getChampion()));
        }
```

```
    /**
     * 定义一个MySQLiteOpenHelper类，用来处理数据库升级
     */
    static class MyOpenHelper extends DaoMaster.OpenHelper {

        public MyOpenHelper(Context context, String name, SQLiteDatabase.CursorFactory factory) {
            super(context, name, factory);
        }

        @Override
        public void onUpgrade(Database db, int oldVersion, int newVersion) {
            super.onUpgrade(db, oldVersion, newVersion);
            Log.d(TAG, "onUpgrade: old: " + oldVersion + ", new: " + newVersion);
            if (oldVersion <= 1) {
                MigrationHelper.migrate(db, new MigrationHelper.ReCreateAllTableListener() {
                    @Override
                    public void onCreateAllTables(Database db, boolean ifNotExists) {
                        DaoMaster.createAllTables(db, ifNotExists);
                    }

                    @Override
                    public void onDropAllTables(Database db, boolean ifExists) {
                        DaoMaster.dropAllTables(db, ifExists);
                    }
                }, PlayerDao.class);

            }

        }
    }
```

### **注意**

新添加的字段的数据类型必须是对象类型，如果是基本数据类型，则需要改为其对应的包装类，否则，在数据库升级做数据迁移的时候，就会出现异常`android.database.sqlite.SQLiteConstraintException`，导致数据迁移失败，对于用户的使用体验是很差的。

![数据迁移失败][7]

# [Demo源代码地址][6]

[GreenDaoUpgradeHelper地址][8]


[6]: https://github.com/YoungBear/GreenDAOLean
[7]: http://img.blog.csdn.net/20171103000530238?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast
[8]: https://github.com/yuweiguocn/GreenDaoUpgradeHelper