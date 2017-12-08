## Assets工具类

### 1. Assets简介

Android 中资源分为两种：

1. 一种是**res**下可编译的资源文件, 这种资源文件系统会在R.java里面自动生成该资源文件的ID，访问也很简单,只需要调用R.XXX.id即可
2. 第二种就是放在**assets**文件夹下面的原生资源文件,放在这个文件夹下面的文件**不会被R文件编译**,所以不能像第一种那样直接使用.Android提供了一个工具类,方便我们操作获取assets文件下的文件:AssetManager。

### AssetManager

AssetManager提供了如下方法用于处理assets：

```
//列出该目录下的下级文件和文件夹名称
String[] list(String path);

//以顺序读取模式打开文件，默认模式为ACCESS_STREAMING
InputStream open(String fileName);

//以指定模式打开文件。读取模式有以下几种：
//ACCESS_UNKNOWN : 未指定具体的读取模式
//ACCESS_RANDOM : 随机读取
//ACCESS_STREAMING : 顺序读取
//ACCESS_BUFFER : 缓存读取
InputStream open(String fileName, int accessMode);

//关闭AssetManager实例
// 注意： getAssets()得到的AssetManager 不要close，应为这个AssetManager还会被系统使用。
void close()
```

<font color=red>**注意：**</font> getAssets()得到的AssetManager 不要close，应为这个AssetManager还会被系统使用。

### 2. Assets工具类结合Gson获取实体类对象

Android开发中，有时候在后台服务没有做好的情况下，我们需要在前端调UI，所以就需要创建假数据，即实体类对象，用来模拟在网络获取的实体类对象。所以，我们可以在本地assets文件夹下放一个文本文件，用来存放一个假的数，然后结合Assets相关API，读取改文件并解析为实体类。

本案例中使用json来传递数据，并使用Google的开源库**Gson**来解析Json。

具体代码为：

```
public final class AssetsUtils {

    private AssetsUtils() {
        throw new UnsupportedOperationException("u can't instantiate me...");
    }

    /**
     * 从文件中获取字符串
     *
     * @param fileName
     * @param context
     * @return
     */
    public static String getString(String fileName, Context context) {
        StringBuilder stringBuilder = new StringBuilder();
        try {
            AssetManager assetManager = context.getAssets();
            BufferedReader bf = new BufferedReader(new InputStreamReader(
                    assetManager.open(fileName)));
            String line;
            while ((line = bf.readLine()) != null) {
                stringBuilder.append(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return stringBuilder.toString();
    }

    /**
     * 根据字符串返回实体类
     *
     * @param fileName
     * @param context
     * @param tClass
     * @param <T> 实体类
     * @return
     */
    public static <T>  T getJsonObject(String fileName, Context context, Class<T> tClass) {
        String jsonStr = getString(fileName, context);
        Gson gson = new Gson();
        return gson.fromJson(jsonStr, tClass);
    }
}
```

首先，通过getString方法，获取文件的字符串，然后，通过泛型方法getJsonObject，来将解析字符串，转换为实体类对象。

DemoActivity为[AssetsActivity](https://github.com/YoungBear/Hello/blob/master/app/src/main/java/com/example/hello/activity/AssetsActivity.java)。对应实体类代码为：[RepositoriesBean](https://github.com/YoungBear/Hello/blob/master/app/src/main/java/com/example/hello/model/bean/RepositoriesBean.java)。可以使用AS的插件GsonFormat来自动生成。Activity代码为：

```
public class AssetsActivity extends BaseActivity {
    private static final String TAG = "AssetsActivity";

    private static final String REPOSITORIES_FILE_NAME = "github_repositories.json";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_assets);
        testJsonObject();
    }

    /**
     *
     */
    private void testJsonObject() {
        RepositoriesBean repositoriesBean = AssetsUtils.getJsonObject(REPOSITORIES_FILE_NAME,
                AssetsActivity.this, RepositoriesBean.class);

        boolean incomplete_results = repositoriesBean.isIncomplete_results();
        int total_count = repositoriesBean.getTotal_count();
        List<RepositoriesBean.ItemsBean> items = repositoriesBean.getItems();

        LogUtils.d(TAG, "testJsonObject, incomplete_results: " + incomplete_results
                + "\ntotal_count: " + total_count
                + "\nitems.size(): " + items.size());

    }


}
```

该Demo使用Github的[搜索仓库API](https://api.github.com/search/repositories?q=java+user:youngbear+language:java)的返回结果作为实体类。更过Github API的内容请参考[GitHub API 学习笔记 Search API](http://blog.csdn.net/next_second/article/details/78238328)和[Github 开发官方地址](https://developer.github.com/v3/)。




参考：

[Android中读取assets目录下的文件详细介绍](http://blog.csdn.net/greathfs/article/details/52123984)