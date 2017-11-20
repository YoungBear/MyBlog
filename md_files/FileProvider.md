# Android FileProvider的使用

[FileProvider官方API](https://developer.android.google.cn/reference/android/support/v4/content/FileProvider.html)

[Android 7.0 Changes](https://developer.android.google.cn/about/versions/nougat/android-7.0-changes.html)

## Android 7.0 在应用间共享文件
对于面向Android 7.0的应用，Android框架执行的StrictMode API政策禁止在您的应用外部公开`file://URI`。如果一项包含文件URI的intent离开您的应用，则应用出现故障，并出现`FileUriExposedException`异常。

**解决方案:**

要在应用间共享文件，您应发送一项`content://URI`，并授予URI临时访问权限。进行此授权的最简单方式是使用[FileProvider]()类。如需了解有关权限和共享文件的详细信息，请参阅[共享文件](https://developer.android.google.cn/training/secure-file-sharing/index.html)。

## FileProvider简介

FileProvider是ContentProvider的一个特殊的子类，它让应用间共享文件变得更加容易，其通过创建一个Content URI来代替File URI。

一个Content URI 允许开发者可赋予一个临时的读或写权限。当创建一个包含Content URI的Intent的时候，为了能够让另一个应用也可以使用这个URI，你需要调用`Intent.setFlags()`来添加权限。只要接收Activity的栈是活跃的，则客户端应用就可以获取到这些权限。如果该Intent是用来启动一个Service，则只要该Service是正在运行的，则也可以获取到这些权限。

相比之下，如果想要通过File URI来控制权限，开发者必须修改底层文件系统的权限。这些权限会对任意的app开放，直到你修改了它。这种级别的访问基本上是不安全的。

通过Content URI来提高文件访问的安全性，使得FileProvider成为Android安全基础设置的一个关键部分。

## FileProvider的使用

1. 定义一个FileProvider
2. 指定有效的文件
3. 从一个File得到一个对应的Content URI
4. 对URI赋予临时权限
5. 分享这个URI给另一个App

### 1. 定义一个FileProvider

由于FileProvider中已经包含了为file生成Content URI的基本代码了，所以开发者不必再去定义一个FileProvider的子类。你可以在XML文件中指定一个FileProvider：在manifest中使用`<provider>`标签来指定。

```
<manifest>
    ...
    <application>
        ...
        <provider
            android:name="android.support.v4.content.FileProvider"
            android:authorities="com.mydomain.fileprovider"
            android:exported="false"
            android:grantUriPermissions="true">
            ...
        </provider>
        ...
    </application>
</manifest>
```

说明：

- `name`的值一般都固定为`android.support.v4.content.FileProvider`。如果开发者继承了FileProvider，则可以写上其绝对路径。
- `authorities`字段的值用来表明使用的使用者，在FileProvider的函数`getUriForFile`需要传入该参数。
- `exported` 的值为false，表示该FileProvider只能本应用使用，不是public的。
- `grantUriPermissions` 的值为true，表示允许赋予临时权限。

### 2. 指定有效的文件

只有事先指定了目录，一个FileProvider才可以为文件生成一个对应的Content URI。要指定一个路径，需要在XML文件中指定其存储的路径。使用`<paths>`标签。例如:

```
<paths xmlns:android="http://schemas.android.com/apk/res/android">
    <files-path name="my_images" path="images/"/>
</paths>
```

上边的`paths` 元素指定`/data/data/<package-name>/files/images/`为共享的目录。(file-path所对应的目录与Context.getFilesDir()所对应，即`/data/data/<package-name>/files`)。其中：name属性表示在**URI中的描述**，path属性表示**文件实际存储**的位置。


`<paths>`里边的元素必须是一下的一个或者多个：

1. `<files-path name="name" path="path" />` 对应Context.getFilesDir() + "/path/"，即`/data/data/<package-name>/files/path/`。
2. `<cache-path name="name" path="path" />` 对应Context.getCacheDir() + "/path/"，即`/data/data/<package-name>/cache/path/`。
3. `<external-files-path name="name" path="path" />` 对应Context.getExternalFilesDir(null) + "/path/"，即`/storage/emulated/0/Android/data/<package_name>/files/path/`。
4. `<external-cache-path name="name" path="path" />` 对应Context.getExternalCacheDir() + "/path/"，即`/storage/emulated/0/Android/data/<package-name>/cache/path/`。
5. `<external-path name="name" path="path" />` 对应Environment.getExternalStorageDirectory() + "/path/"，即`/storage/emulated/0/path/`。

这些paths里边有相同的子元素，即name和path。

#### **name**

这是URI的path。为了加强安全性，这个值隐藏了分享文件的子目录，具体的文件真实路径在path字段中保存。

A URI path segment. To enforce security, this value hides the name of the subdirectory you're sharing. The subdirectory name for this value is contained in the path attribute.

#### **path**

分享文件的真实路径。需要注意的是，这个值表示的是一个子目录，不是一个具体的文件或者多个文件。开发者不能通过文件名来分享一个文件，也不能通过一个通配符来分享文件。

The subdirectory you're sharing. While the name attribute is a URI path segment, the path value is an actual subdirectory name. Notice that the value refers to a subdirectory, not an individual file or files. You can't share a single file by its file name, nor can you specify a subset of files using wildcards.

将paths里边的内容放在一个xml文件中，将该文件放在res/xml/目录下，然后在manifest的provider标签中指定它：

res/xml/file_paths.xml

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <paths>
        <files-path name="my_files" path="text/"/>
        <cache-path name="my_cache" path="text/" />
        <external-files-path name="external-files-path" path="text/" />
        <external-path name="my_external_path" path="text/" />
    </paths>
</resources>
```

AndroidManifest.xml

```
        <provider
            android:name="android.support.v4.content.FileProvider"
            android:authorities="com.ysx.fileproviderserver.fileprovider"
            android:exported="false"
            android:grantUriPermissions="true">
            <meta-data
                android:name="android.support.FILE_PROVIDER_PATHS"
                android:resource="@xml/file_paths" />
        </provider>
```

### 3. 从一个File得到一个对应的Content URI

```
        File file = new File(mContext.getFilesDir() + "/text", "hello.txt");
        Uri data;
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            data = FileProvider.getUriForFile(mContext, "com.ysx.fileproviderserver.fileprovider", file);
        } else {
            data = Uri.fromFile(file);
        }
```

需要注意的是，

1. 文件的绝对路径与第二步指定的文件目录保持一致：(假设包名为com.ysx.fileproviderserver)。如上边的代码的文件的绝对路径为`/data/data/com.ysx.fileproviderserver/files/text/hello.txt`，对应paths中的内容为:`<files-path name="my_files" path="text/"/>`。
2. getUriForFile()的第二个参数是authority，与manifest文件中声明的authorities保持一致。

这时候，我们得到的URI的串为：`content://com.ysx.fileproviderserver.fileprovider/my_files/hello.txt`。

### 4. 赋予临时权限

两种方法：（通常使用第2种）

1. Context.grantUriPermission(package, Uri, mode_flags) 
2. Intent.setFlags() 

`intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION | FLAG_GRANT_WRITE_URI_PERMISSION);`

**FLAG_GRANT_READ_URI_PERMISSION**：表示读取权限；
**FLAG_GRANT_WRITE_URI_PERMISSION**：表示写入权限。

你可以同时或单独使用这两个权限，视你的需求而定。

### 5. 分享这个URI给另一个App

通常是通过Intent来传递的。eg.

```
    private void shareFile() {
        Log.d(TAG, "shareFile: ");
        Intent intent = new Intent();
        ComponentName componentName = new ComponentName("com.ysx.fileproviderclient",
                "com.ysx.fileproviderclient.MainActivity");
        intent.setComponent(componentName);
        File file = new File(mContext.getFilesDir() + "/text", "hello.txt");
        Uri data;
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            data = FileProvider.getUriForFile(mContext, FILE_PROVIDER_AUTHORITIES, file);
            // 给目标应用一个临时授权
            intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
        } else {
            data = Uri.fromFile(file);
        }
        intent.setData(data);
        startActivity(intent);
    }
```

## 常见的使用场景：

1. 调用照相机，指定照片存储路径。
2. 调用系统安装器，传递apk文件。

调用照相机：

```
    /**
     * @param activity 当前activity
     * @param authority FileProvider对应的authority
     * @param file 拍照后照片存储的文件
     * @param requestCode 调用系统相机请求码
     */
    public static void takePicture(Activity activity, String authority, File file, int requestCode) {
        Intent intent = new Intent();
        Uri imageUri;
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            imageUri = FileProvider.getUriForFile(activity, authority, file);
            intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
        } else {
            imageUri = Uri.fromFile(file);
        }
        intent.setAction(MediaStore.ACTION_IMAGE_CAPTURE);
        intent.putExtra(MediaStore.EXTRA_OUTPUT, imageUri);
        activity.startActivityForResult(intent, requestCode);
    }
```

调用安装器：

```
    /**
     * 调用系统安装器安装apk
     *
     * @param context 上下文
     * @param authority FileProvider对应的authority
     * @param file apk文件
     */
    public static void installApk(Context context, String authority, File file) {
        Intent intent = new Intent(Intent.ACTION_VIEW);
        Uri data;
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            data = FileProvider.getUriForFile(context, authority, file);
            intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
        } else {
            data = Uri.fromFile(file);
        }
        intent.setDataAndType(data, INSTALL_TYPE);
        context.startActivity(intent);
    }
```

## [实例代码](https://github.com/YoungBear/FileProviderLearn)

[FileProvider官方API](https://developer.android.google.cn/reference/android/support/v4/content/FileProvider.html)

[Android 7.0 Changes](https://developer.android.google.cn/about/versions/nougat/android-7.0-changes.html)

## 参考：

[Android 7.0适配-应用之间共享文件(FileProvider)](http://www.jianshu.com/p/55eae30d133c)



