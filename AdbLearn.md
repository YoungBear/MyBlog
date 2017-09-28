# Android adb 常用命令

Android开发环境安装好之后，需要将adb路径添加到环境变量(PATH)中，这样，就可以在命令行下直接使用adb命令了。

需要注意的是，有的命令需要先进入手机的linux系统，然后才可以使用，即adb shell, ...，这里称这种命令为**shell命令**。另外有的命令可以直接用adb 使用，这里称之为**非shell命令**。通常两者可以通用的，下面会分别列出这两种命令。

## 常用非Shell命令

### 连接相关
```
adb version 查看adb版本
adb devices 查看连接设备
adb connect <android_ip>    连接android设备（需要在同一网段下）
adb kill-server 杀死adb 服务
adb start-server 启动adb服务
adb reboot 重启手机
```

### 多个Android设备

```
adb devices 查看连接设备
adb -s <device_name> shell 进入指定的设备shell
```

![adb_more_devices](http://img.blog.csdn.net/20170808140035506?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

```
串口下输入命令，保证可以adb connect成功
stop adbd
setprop service.adb.tcp.port 5555
start adbd
```

### 应用相关
```
adb shell pm list packages    显示所有应用信息
adb shell pm list packages -s    显示系统应用信息
adb shell pm list packages -3   显示第三方应用信息
adb shell pm list permissions -d -g    显示权限信息
adb shell pm clear <package_name>    清除数据
adb shell pm install <package_name>    安装应用
adb shell pm install -r -r <package_name>    保留数据和缓存文件，重新安装apk
adb shell pm uninstall <package_name>    卸载应用(与adb uninstall相同)

adb install <package_name>    安装应用
adb install -r <package_name>    保留数据和缓存文件，重新安装apk
adb uninstall <package_name>    卸载应用
```

### 获取手机系统信息

```
adb shell cat /proc/cpuinfo     显示cpu信息
adb get-serialno    获取序列号
adb shell  cat /sys/class/net/wlan0/address    获取mac地址
adb shell getprop ro.product.model    获取设备型号
adb shell wm size    查看屏幕分辨率
adb shell wm density    查看屏幕密度
```

### log相关

```
adb logcat -v time    带时间戳的log
adb logcat -c    清除log
adb logcat -b <buffer>    查看不同类型的log，如main,system,radio,events,crash,all.默认为main log
adb logcat | grep -i "str"    忽略大小写筛选指定字符串log
adb logcat | grep -iE "str1|str2|str3"    筛选多个字符串
adb logcat > log.txt    打印log输入到文件

```

### fastboot模式

```
adb reboot-bootloader
fastboot flash boot boot.img
fastboot flash recovery recovery.img
fastboot flash android system.img
```

### 输入文本

```
adb shell input text "str" 在EditText中输入文本。通常在TV或者盒子上，代替用遥控器输入
对应shell命令为：
input text "str"

注：也可以模拟其他事件，如点击，触摸等等。
```

### 文件相关

```
adb remount    
adb push <file_path> <dest_path>    从PC向手机端push文件
adb pull <target_path> <dest_path>    从手机端向PC端拉取文件
eg.
adb remount
adb push Hello.apk /system/app/Hello/
```

### 截屏与录屏
```
截屏：
adb shell screencap -p <output_file>    截取屏幕，并设置图片存储路径
adb pull <output_file> .    拉取该截图到PC
adb shell rm <output_file>    删除截图文件
eg.
adb shell screencap -p /sdcard/screen.png

录屏：
adb shell screenrecord <output_file> 录屏
```

### dumpsys 查看信息相关

```
adb shell dumpsys    显示当前android系统信息(四大组件，内容太多，一般使用重定向)
adb shell dumpsys > info.txt 显示当前android系统信息(文件重定向)

activity：
adb shell dumpsys activity    显示当前所有activity信息
adb shell dumpsys activity top    查看当前应用的 activity 信息

package：
adb shell dumpsys package [package_name] 查看应用信息

内存：
adb shell dumpsys meminfo [package_name/pid] 查看指定进程名或者是进程 id 的内存信息

数据库：
adb shell dumpsys dbinfo [package_name] 查看指定包名应用的数据库存储信息(包括存储的sql语句)

```

### am 相关

```
启动Activity:
adb shell am start -n <package_name>/<package_name>.<activity_name>
eg.
adb shell am start -n com.example.hello/com.example.hello.MainActivity

启动Service:
adb shell am startservice -n <package_name>/<package_name>.<service_name>    启动service
eg.
adb shell am startservice -n com.example.test/com.example.test.TestService

发送广播:
adb shell am broadcast -a <action>    发送广播

```

### 查看网络信息

```
adb shell netcfg    查看设备的 ip 地址
adb shell netstat    查看设备的端口号信息
```

### 属性信息

```
adb shell getprop [prop_name]    查看属性信息
adb shell setprop <prop_name> <value>    设置属性值
```

### Monkey测试

```
adb shell monkey [options] <event-count>
adb shell monkey -p <package_name> -v <event_number>
对指定应用，做evnet_number个随机伪事件
```

### 查看进程信息

```
adb shell ps    查看进程信息
```

## 常用shell命令
在命令行下先执行adb shell，进入linux系统，然后再执行这些命令。
通常，大部分非shell命令都对应shell命令。这个使用者灵活掌握即可。

eg.

`adb shell logcat` 对应 `logcat`

`adb shell getprop` 对应 `getprop`

`adb shell am start -n` 对应 `am start -n`




## 其他
显示cpu信息:
![这里写图片描述](http://img.blog.csdn.net/20160712191745739)

### 启动一个Activity ###
前提，在*真机*上，该Activity在AndroidManifest.xml中的exported属性必须为true才可以用adb shell 启动，在*模拟器*上不需要。即`android:exported="true"`。exported的default值是false的。
启动一个Activity:
`adb shell am start -n <package name>/<activity name>`
eg.

```
adb shell am start -n com.example.hello/com.example.hello.MainActivity
```
或者

```
adb shell am start -n com.example.hello/.MainActivity
```

在真机上exported为false的时候，执行命令会出现异常:

```
adb shell am start -n com.example.hello/.activity.HelloActivity
Starting: Intent { cmp=com.example.hello/.activity.HelloActivity }
java.lang.SecurityException: Permission Denial: starting Intent { flg=0x10000000 cmp=com.example.hello/.activity.HelloActivity } from null (pid=9098, uid=2000) not exported from uid 10221
	at android.os.Parcel.readException(Parcel.java:1546)
	at android.os.Parcel.readException(Parcel.java:1499)
	at android.app.ActivityManagerProxy.startActivityAsUser(ActivityManagerNative.java:2642)
	at com.android.commands.am.Am.runStart(Am.java:766)
	at com.android.commands.am.Am.onRun(Am.java:305)
	at com.android.internal.os.BaseCommand.run(BaseCommand.java:47)
	at com.android.commands.am.Am.main(Am.java:97)
	at com.android.internal.os.RuntimeInit.nativeFinishInit(Native Method)
	at com.android.internal.os.RuntimeInit.main(RuntimeInit.java:284)
```

### adb 截图命令



#### 截图保存到SD卡里再导出

```bash
$ adb shell screencap -p /sdcard/screen.png
$ adb pull /sdcard/screen.png
$ adb shell rm /sdcard/screen.png
```
这种方法比较麻烦，需要3步：

1. 截图保存到sdcard 
2. 将图片导出
3. 删除sdcard中的图片

#### 截图直接保存到电脑(Windows only)

```bash
$ adb shell screencap -p | sed 's/\r$//' > screen.png
```
执行adb shell 将\n转换\r\n, 因此需要用sed删除多余的\r

#### 使用alias
修改~/.bashrc，添加一句：
```bash
alias adb-screencap="adb shell screencap -p | sed 's/\r$//'"
```
执行`source ~/.bashrc`后，可以直接使用
`adb-screencap > screen.png` 截图并保存到电脑上

参考：

http://blog.csdn.net/jiangwei0910410003/article/details/73385819

http://blog.csdn.net/wirelessqa/article/details/29187339