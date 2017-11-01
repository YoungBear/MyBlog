# 使用一个单例来管理DaoSession

编写一个单例类，可以全局保留唯一一个DaoSession对象。各Activity都可以调用这个对象，避免了创建多个对象的开销。在Application的onCreate()方法中进行初始化。

```
public class GreenDaoManager {
    private static final String TAG = "GreenDaoManager";

    private static final String DATABASE_NAME = "players.db";
    /**
     * 全局保持一个DaoSession
     */
    private DaoSession daoSession;

    private boolean isInited;

    private static final class GreenDaoManagerHolder {
        private static final GreenDaoManager sInstance = new GreenDaoManager();
    }

    public static GreenDaoManager getInstance() {
        return GreenDaoManagerHolder.sInstance;
    }

    private GreenDaoManager() {

    }

    /**
     * 初始化DaoSession
     *
     * @param context
     */
    public void init(Context context) {
        if (!isInited) {
            DaoMaster.OpenHelper openHelper = new DaoMaster.DevOpenHelper(
                    context.getApplicationContext(), DATABASE_NAME, null);
            DaoMaster daoMaster = new DaoMaster(openHelper.getWritableDatabase());
            daoSession = daoMaster.newSession();
            isInited = true;
        }
    }

    public DaoSession getDaoSession() {
        return daoSession;
    }
}
```

**初始化：**

```
public class MyApplication extends Application {
    @Override
    public void onCreate() {
        super.onCreate();
        init();
    }

    /**
     * 初始化
     */
    private void init() {
        GreenDaoManager.getInstance().init(getApplicationContext());
    }
}
```

在AndroidManifest.xml中该Application的名字：

```
    <application
        android:name=".MyApplication"
        // 其他代码...
    </application>
```

在Activity中使用单例类：

```
    /**
     * 获取一个全局的DaoSession实例
     */
    private void initDaoSession() {
        mDaoSession = GreenDaoManager.getInstance().getDaoSession();
    }
```

获取到DaoSession对象之后，可以对其进行增删改查等操作。

# [Demo源代码地址][6]


  [6]: https://github.com/YoungBear/GreenDAOLean
