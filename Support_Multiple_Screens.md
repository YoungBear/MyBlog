#Android屏幕适配

#Android屏幕适配顺序

https://developer.android.com/guide/practices/screens_support.html
#配置限定符名称(由高到低)
1. MCC and MNC
2. Language and Region 语言和区域 eg. en
3. Layout Direction 布局方向 eg. ldrtl ldltr
4. Smallest Width 最小宽度(不考虑是宽度还是高度) sw<N>dp eg. sw720dp
5. Available Width 可用宽度 w<N>dp eg. w720dp 应用为多个资源目录提供不同的此配置值时，系统会使用最接近（但未超出）设备当前屏幕宽度的值。
6. Avalable Height 可用高度 h<N>dp eg. h720dp
7. Screen Size 屏幕尺寸 eg.small normal large xlarge
8. Screen Aspect 屏幕纵横比 eg. long(宽屏) notlong(非宽屏)
9. Screen Orientation 屏幕方向 eg. port(垂直) land(水平)
10. UI mode  UI模式 eg. car(车载手机) desk(桌面手机) television(电视) appliance(不带显示器) watch(手表)
11. Night mode 夜间模式 eg. night notnight
12. Screen pixel density(dpi) 屏幕像素密度， eg. ldpi mdpi hdpi xhdpi xxhdpi xxxhdpi nodpi tvdpi
13. Touch screen type 触摸屏类型, eg. notouch(设备没有触摸屏) finger(设备有一个专供用户通过手指直接与其交互的触摸屏)
14. Keyboard availability 键盘可用性 eg. keysexposed keyshidden keyssoft
15. Primary text inputmethod 主要文本输入法 eg. nokeys qwerty 12key
16. Navigation key avilability 导航键可用性 eg. navexposed navhidden
17. Primary non-touch navigation method 主要非触摸导航方法 eg. nonav dpad trackball wheel
18. Platform Version(API level) 平台版本（API 级别）eg. v3 v4 v7

##sizes:
- small
- normal
- large
- xlarge

**Android 3.2(API level 13)之后，sizes被废弃，使用available screen width 来代替。**

- smallestWidth  格式:sw<N>dp,eg. sw600dp,sw720dp
- Avaiable screen width 格式：w<N>dp，eg. w720dp, w1024dp
- Available screen height 格式：h<N>dp，eg. h720dp, h1024dp

##densities:

![](http://img.blog.csdn.net/20160122204438246)
- ldpi(low) ~ 120dpi
- mdpi(medimu) ~ 160dpi
- hdpi(high) ~ 240dpi
- xhdpi(extra-high) ~ 320dpi
- xxhdpi(extra-extra-high) ~ 480dpi
- xxxhdpi(extra-extra-extra-high) ~ 640dpi
- nodpi 它可用于您不希望缩放以匹配设备密度的位图资源
- tvdpi 介于mdpi和hdpi之间，约为213dpi。主要用于电视

##Orientation
- land
- port

#限定符命名规则
- 可以为单组资源指定多个限定符，并使用短划线分隔。例如，drawable-en-rUS-land 适用于横排美国英语设备。
- 这些限定符必须遵循限定符的顺序。即按优先级从高到低。例如：

错误： drawable-hdpi-port/

正确： drawable-port-hdpi/

- 不能嵌套备用资源目录。例如，您不能拥有 res/drawable/drawable-en/。
- <font color=red>值不区分大小写</font>。在处理之前，资源编译器会将目录名称转换为小写，以避免不区分大小写的文件系统出现问题。 名称中使用的任何大写字母只是为了便于认读。
- 对于每种限定符类型，仅支持一个值。例如，若要对西班牙语和法语使用相同的 Drawable 文件，则您肯定不能拥有名为 drawable-rES-rFR/ 的目录，而是需要两个包含相应文件的资源目录，如 drawable-rES/ 和 drawable-rFR/。然而，实际上您无需将相同的文件都复制到这两个位置。相反，您可以创建指向资源的别名。

##Android资源匹配算法
![这里写图片描述](http://img.blog.csdn.net/20161026152640938)

系统使用以下逻辑决定要使用的资源：

1. 淘汰与设备配置冲突的资源文件(屏幕像素密度(dpi)是唯一一个不会因为冲突而淘汰的限定符。)
2. 选择优先级最高的限定符，先从MCC开始，然后下移
3. 是否有资源目录包括此限定符？若无，返回第2步，看下一个限定符；若有，继续执行第4步
4. 淘汰不含此限定符的资源目录
5. 返回并重复第2步、第3步和第4步，直到只剩下一个目录为止。

注：限定符的优先级，比设备完全匹配的限定符数量更加重要。

参考：

http://blog.csdn.net/a220315410/article/details/11896189