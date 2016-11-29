#Environment相关函数

```
public static File getDataDirectory () : /data
public static File getDownloadCacheDirectory () : /data/cache
public static File getExternalStorageDirectory () : /storage/emulated/0
public static File getRootDirectory () : /system
public static String getExternalStorageState () : 返回usb挂载状态
```

Context相关方法:

```
public abstract File getFilesDir () : /data/data/<package-name>/files
public abstract File getCacheDir () : /data/data/<package-name>/cache
public abstract File getExternalCacheDir () : /storage/emulated/0/Android/data/<package-name>/cache

```
参考：

http://www.cnblogs.com/mengdd/p/3742623.html