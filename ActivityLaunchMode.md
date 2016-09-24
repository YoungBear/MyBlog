# Android Activity 启动模式 #

本文github地址：

https://github.com/YoungBear/MyBlog/blob/master/ActivityLaunchMode.md

说明，本文sample中使用的简写，launchMode分别为：

standard    在sample中用Activity A 来表示

singleTop    在sample中用Activity B 来表示

singleTask    在sample中用Activity C 来表示

singleInstance    在sample中用Activity D 来表示

查看当前任务栈情况命令：

`adb shell dumpsys activity`


## standard ##
　　默认启动模式

　　不管当前栈顶有没有实例，都会新建一个A实例，将Activity放在栈顶。

## singleTop ##
　　栈顶复用模式

　　如果当前栈顶元素是我们需要启动的Activity的一个实例，则这个Activity不会再次被创建，而是先调用<font color=red>onPause()</font>方法，然后再调用<font color=red>onNewIntent</font>方法，<font color=red>onResume()</font>,即onPause()->onNewIntent()->onResume()。

　　如果当前栈顶没有该Activity的实例，则新建一个实例放在栈顶。

eg.

1. A    栈内元素为 A(从栈顶到栈底)
2. A->B    栈内元素为 B A
3. A->B->B    栈内元素为 B A （B栈顶复用）

第3步，B启动B的时候，发现当前栈顶有B实例，则调用onPause()->onNewIntent()->onResume()<font color=red>(onPause()是上一个B调用的</font>)。

## singleTask ##
　　栈内复用模式

　　以singleTask模式启动的Activity首先就会寻找自己需要的任务栈，如果没有，就会创建一个，然后把自己给放进栈里面。要是有发现自己需要的任务栈，就会看里面有没有这个Activity的实例，没有的话就在栈顶加入新创的实例，要是有的话就会弹出该实例上面的所有元素，即<font color=red>它上面所有元素都出栈</font>，从而把所需求的实例给推到栈顶。

　　一个应用的默认的任务栈是包名，也可以在manifest.xml文件中，用taskAffinity指定任务栈，如android:taskAffinity="com.test.task",(字符串中必须包含分割符".")

　　具体分析下，默认是同一个任务栈，假如A是standard，C是singleTask，如果

1. A    栈内元素为 A1(从栈顶到栈底)
2. A->C    栈内元素为 C A1
3. A->C-A    栈内元素为 A2 C A1
4. A-C-A-C    栈内元素为 C A1 (之前栈顶的A2出栈)

　　在第4步，A启动C的时候，由于当前任务栈中已经有实例C了，所以A出栈，C调用onNewIntent()->onRestart()->onStart()->onResume()。

　　如果当前栈顶就是该实例的话，就与singleTop相同了，即调用onPause()->onNewIntent()->onResume()。

　　如果在<font color=red>另一个应用</font>中打开C，则会新开一个task(任务栈)。例如，在程序Another的MainActivity中，去启动C，则当前任务栈情况为：

![](http://img.blog.csdn.net/20160924235822634)


　　从图中可以看出来，another的MainActivity的任务栈ID是#25220,而C(即SingleTaskActivity)的任务栈编号是#25222。这时候，如果按Home键，再次启动C的主程序，则会显示刚才another打开的页面，而不是C的主程序页面。如果再次启动another的时候，也是在another的主页面，而不是调到的C的页面。

　　常见的一个例子就是，在图库中点击分享，选择微信好友，进入微信好友列表，然后再按Home键。这时候，如果点击进入微信，则会发现不是微信主页面，而是让用户选择分享好友的界面，用户可以继续分享图片。(测试平台是：魅族MX5 Flyme 5.1.9.0A，图库5.3.01，微信6.3.23)

　　对比一下another启动A(Standard)的情况：

![](http://img.blog.csdn.net/20160924235832458)

　　从图中可以看出来，another的MainActivity和C在同一个任务栈中，编号为#25220。这时候，如果按Home键，再次启动C的主程序，则会显示C的主程序页面，如果启动another,则跳转到打开的C的页面，这与singleTask现象不同。

　　同样举一个魅族图库上的例子，进入一个图片，分享，选择微信朋友圈，进入微信朋友圈编辑页面，按Home键退出。这时候，如果点击进入微信，则会进入微信主界面，如果进入图库，则会跳转到微信朋友圈的编辑界面。

　　个人觉得，分享给微信好友，相当于和好友聊天，这就相当于微信的MainActivity，所以需要使用singleTask；而分享到朋友圈，则只是微信的一个附加功能，不会影响用户的聊天。

## singleInstance ##
　　单实例模式

　　它具备上一个singleTask的所有属性，其次，它只能<font color=red>独自的</font>存在于一个单独的任务栈。即这个task只有这个实例，<font color=red>不允许有别的Activity存在</font>。

例如：

1. A1
2. A1->D
3. A1->D->A2    (A1和A2是同一个任务栈，在前台，D是独立的一个任务栈，在后台)
4. A1->D->A2->D    (实际结果是D的任务栈成为前台任务栈，A1和A2成为后台任务栈)

第3步的时候，任务栈情况截图：
![](http://img.blog.csdn.net/20160924235803222)

　　有图片中的任务栈情况可以看出，A1和A2是同一个任务栈#25235,而D是单独的一个任务栈#25236。这时候，如果按back键，则退出情况为A2->A1->D(先前台任务栈，再后台任务栈)。

　　第4步，可以看出来，singleInstance与singleTask的不同是，singleInstance不会让当前栈顶的实例出栈，而是将其独立的任务栈移到前台，将当前的任务栈移到后台。这时候也会调用onNewIntent()->onRestart()->onStart()->onResume()。

测试代码地址：

https://github.com/YoungBear/LaunchModeLearn

参考：

http://www.jianshu.com/p/185fd7e36bd3

http://blog.csdn.net/shinay/article/details/7898492/
