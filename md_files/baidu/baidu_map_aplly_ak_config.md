## 1. 关于Android端AK值申请及签名配置

[官方地址](http://lbsyun.baidu.com/apiconsole/key/create)

申请ak：

![](https://github.com/YoungBear/MyBlog/blob/master/pngs/baidu/baidu_ak_apply_android.png)

其中，百度api-key是与签名文件和包名绑定的，所以我们需要先获取**签名文件**，签名文件与SHA1值对应。我们需要输入**开发板SHA1**和**发布版SHA1**。

默认在Debug模式下，我们的签名文件是`~/.android/debug.keystore`，即用户目录下的`.android/debug.keystore`文件，其密码默认都为`android`。可以使用如下命令来获取签名文件的SHA1值。

```
keytool -list -v -keystore <签名文件>
```

输入密码后，可以查看结果：

查看debug签名文件的SHA1值：

![](https://github.com/YoungBear/MyBlog/blob/master/pngs/baidu/get_sha1_debug.png)

查看release签名文件的SHA1值：

![](https://github.com/YoungBear/MyBlog/blob/master/pngs/baidu/get_sha1_release.png)




其中，release签名文件可以用Android Studio来申请获得，用户需要输入文件名，密码，别名，别名密码。

通过`Build->Genetate Signed APK...->Next->Create New...`进入。

生成新的签名文件：

![](https://github.com/YoungBear/MyBlog/blob/master/pngs/baidu/as_apply_sign_file.png)

### 配置签名文件

在app目录下的build.gradle文件:

```
android {
    compileSdkVersion 26
    defaultConfig {
        // 其他配置
    }

    // 签名配置
    signingConfigs {
        debug {
            storeFile file('./debug.keystore')
            storePassword 'android'
            keyAlias 'androiddebugkey'
            keyPassword 'android'
        }
        release {
            storeFile file('<签名文件>')
            storePassword '<签名密码>'
            keyAlias '<别名>'
            keyPassword '<别名密码>'
        }
    }

    buildTypes {
        debug {
            // 其他配置
            signingConfig signingConfigs.debug //使用debug签名
        }
        release {
            // 其他配置
            signingConfig signingConfigs.release // 使用release签名
        }
    }

    // jni库
    sourceSets {
        main {
            jniLibs.srcDir 'libs'
        }
    }

}
```
一般情况下，签名文件及密码这些敏感信息，是不建议直接放在gradle代码里的，而应该建立一个配置文件`config.properties`，然后将该配置文件加到`.gitignore`文件中，即不在git库保存，放在安全的地方。下面有一节专门讲这个配置。

### 使用配置文件存放敏感信息

可以在app目录下建立一个配置文件`config.properties`，在里边存放签名文件及密码等敏感信息。

![](https://github.com/YoungBear/MyBlog/blob/master/pngs/baidu/config_preoperties.png)

```
# 配置文件 app/config.properties

# debug
DEBUG_STORE_FILE = ./debug.keystore
DEBUG_STORE_PASSWORD = android
DEBUG_KEY_ALIAS = androiddebugkey
DEBUG_KEY_PASSWORD = android

# release
RELEASE_STORE_FILE = ****
RELEASE_STORE_PASSWORD = ****
RELEASE_KEY_ALIAS = ****
RELEASE_KEY_PASSWORD = ****

```

在app目录下的build.gradle使用配置文件：

```
// 加载配置文件
Properties props = new Properties()
FileInputStream fis = new FileInputStream(file("./config.properties"))
BufferedReader bf = new BufferedReader(new InputStreamReader(fis, "UTF-8"));
props.load(bf)

android {
    // 签名配置
    signingConfigs {
        debug {
            storeFile file(props['DEBUG_STORE_FILE'])
            storePassword props['DEBUG_STORE_PASSWORD']
            keyAlias props['DEBUG_KEY_ALIAS']
            keyPassword props['DEBUG_KEY_PASSWORD']
        }
        release {
            storeFile file(props['RELEASE_STORE_FILE'])
            storePassword props['RELEASE_STORE_PASSWORD']
            keyAlias props['RELEASE_KEY_ALIAS']
            keyPassword props['RELEASE_KEY_PASSWORD']
        }
    }

    // 其他配置

}
```

先加载配置文件，然后使用`props['键']`来获取值。

另外，也可以使用`manifestPlaceholders`来配置不同的**渠道号**等信息。后续专门写一节来具体描述。

## 2. 在AndroidManifest文件中配置AK值

在Application标签下，配置mata-data值：

```
        <meta-data
            android:name="com.baidu.lbsapi.API_KEY"
            android:value="<你申请的ak值>" />
```

## 权限申请

百度地图及定位所需要的权限列表。

```
    <uses-permission android:name="com.android.launcher.permission.READ_SETTINGS" />
    <!-- 这个权限用于进行网络定位 -->
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <!-- 这个权限用于访问GPS定位 -->
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <!-- 用于访问wifi网络信息，wifi信息会用于进行网络定位 -->
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <!-- 获取运营商信息，用于支持提供运营商信息相关的接口 -->
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <!-- 用于读取手机当前的状态 -->
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <!-- 写入扩展存储，向扩展卡写入数据，用于写入离线定位数据 -->
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <!-- 访问网络，网络定位需要上网 -->
    <uses-permission android:name="android.permission.INTERNET" />
```

其中，在Android 6.0之后，即如果`compileSdkVersion >= 23`，危险权限需要**动态申请**。

在百度地图开发中，需要在获取到权限之后，初始化地图SDK：

```
SDKInitializer.initialize(getApplicationContext());
SDKInitializer.setCoordType(CoordType.BD09LL);
```

**需要注意的是**，这个初始化必须在含有MapView的Activity的setContentView()**之前**，否则会因为没有初始化而导致崩溃。

## 3. 百度定位配置Service

如果使用百度定位，需要在AndroidManifest文件的Application标签下配置service标签：

```
        <service
            android:name="com.baidu.location.f"
            android:enabled="true"
            android:process=":remote" />
```

## 4. 添加混淆配置

百度地图相关混淆配置：

```
-keep class com.baidu.** {*;}
-keep class vi.com.** {*;}
-dontwarn com.baidu.**
```

## [Demo地址](https://github.com/YoungBear/BaiduDemo)

## Tips：

1. 该demo在master分支上忽略了配置文件app/config.properties，如果您想查看配置文件，可以切换到config_dev分支。




## 参考：

http://blog.csdn.net/yujihu989/article/details/54589684


