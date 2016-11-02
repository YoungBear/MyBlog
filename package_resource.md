#android指定打包资源文件

　　在进行android开发时如果不是使用的eclipse等IDE，使用源码下开发再 mm的时候可能会发现 没有完全打包 hdpi mdpi ldpi下的资源。

　　我们可以通过如下的方式指定打包的资源文件：

##第一种

　　在android源码目录 build/target/product/full_base.mk

```
PRODUCT_AAPT_CONFIG := normal hdpi
```

　　这是系统的默认配置(可能不同产品目录不一样，这个是mtk5508的目录)，默认打包hdpi。如果需要添加其他的的资源，可以在后边添加，如tvdpi。这种方式通常适用于产品开发，开发过程中该产品只需要特定资源包下的资源。

##第二种

　　如果<font color=red>单个apk需要适配多个屏幕</font>，一个应用下需要打包多个资源包来适配不同的屏幕，可以在应用的Android.mk文件中，添加

```
LOCAL_AAPT_FLAGS := -c ldpi -c mdpi -c hdpi -c xhdpi -c xxhdpi
```

　　上面指定了编译时打包这五个资源包。

###注：
- 如果ldpi，mdpi，hdpi，xhdpi，xxhdpi中没有资源文件，编译后的apk中不会有对应的文件夹。
- 如果你进行的是<font color=red>平台应用</font>开发，最好不要使用第二种方式来指定，因为你这样会导致系统编译了多余的资源文件导致rom变大，只需要通过第一种方式指定默认的即可。

参考：

http://www.2cto.com/kf/201204/128139.html

http://blog.csdn.net/suck666/article/details/41958967