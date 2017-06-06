# getDimension,getDimensionPixelSize,getDimensionPixelOffset

`public float getDimension(@DimenRes int id)`

`public int getDimensionPixelSize(@DimenRes int id)`

`public int getDimensionPixelOffset(@DimenRes int id)`

代码位置：

`android.content.res.Resources.java`

首先，`getDimension`的返回值是**float**类型，其他两个函数返回值是**int**型，其中，`getDimensionPixelSize是`**四舍五入**取整，而`getDimensionPixelOffset`是**向下**取整，相当于`Math.floor`。

其次，这三个函数，如果资源文件中的单位为dp或者sp，则返回结果会自动乘以屏幕密度**density**；但如果单位是px，则返回结果不会乘以density。

测试源码位置：https://github.com/YoungBear/Hello

在首页点击选择GetDimensionActivity
