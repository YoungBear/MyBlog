adb 常用命令：

```
shell下：

adb version 查看adb版本
adb devices 查看连接设备




logcat过滤多个字符串(需要grep，没有的话，就要在adb shell下进行)
adb logcat | grep -E "str1|str2|str3"

adb shell pm list packages    显示所有应用信息
adb shell pm list packages -s    显示系统应用信息
adb shell pm list packages -3   显示第三方应用信息

adb install <package name>    安装应用
adb install -r <package name>    保留数据和缓存文件，重新安装apk
adb uninstall <package name>    卸载应用

adb connect <android_ip>    连接android设备（需要在同一网段下）

adb shell pm clear <package name>    清除数据

adb kill-server 杀死adb 服务
adb start-server 启动adb服务

adb reboot 重启

在EditText中输入文本
input text xxx
eg. adb shell下，input text hello
通常在TV或者盒子上，代替用遥控器输入

串口下输入命令，保证可以adb connect成功
stop adbd
setprop service.adb.tcp.port 5555
start adbd


adb shell dumpsys    显示当前android系统信息
adb shell dumpsys activity    显示当前所有activity信息

adb remount    
adb push <file_path> <dest_path>
adb pull <target_path> <dest_path>
eg.
adb remount
adb push Hello.apk /system/app/Hello/

发送广播：
adb shell am broadcast -a "com.test.action"

截图命令：
adb shell /system/bin/screencap -p /storage/sdcard0/screenshot.png

monkey
adb shell monkey [options] <event-count>
adb shell monkey -p <package_name> -v <event_number>
对指定应用，做evnet_number个随机伪事件


adb reboot-bootloader

fastboot模式
adb reboot-bootloader
fastboot flash boot boot.img
fastboot flash recovery recovery.img
fastboot flash android system.img


系统信息：

adb shell cat /proc/cpuinfo     显示cpu信息
adb get-serialno    获取序列号
adb shell  cat /sys/class/net/wlan0/address    获取mac地址
adb shell getprop ro.product.model    获取设备型号
adb shell wm size    查看屏幕分辨率
adb shell wm density    查看屏幕密度

```
![这里写图片描述](http://img.blog.csdn.net/20160712191745739)

## 启动一个Activity ##
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

##adb 截图命令

参考：

http://blog.csdn.net/wirelessqa/article/details/29187339

###截图保存到SD卡里再导出

```bash
$ adb shell screencap -p /sdcard/screen.png
$ adb pull /sdcard/screen.png
$ adb shell rm /sdcard/screen.png
```
这种方法比较麻烦，需要3步：

1. 截图保存到sdcard 
2. 将图片导出
3. 删除sdcard中的图片

###截图直接保存到电脑

```bash
$ adb shell screencap -p | sed 's/\r$//' > screen.png
```
执行adb shell 将\n转换\r\n, 因此需要用sed删除多余的\r

###使用alias
修改~/.bashrc，添加一句：
```bash
alias adb-screencap="adb shell screencap -p | sed 's/\r$//'"
```
执行`source ~/.bashrc`后，可以直接使用
`adb-screencap > screen.png` 截图并保存到电脑上