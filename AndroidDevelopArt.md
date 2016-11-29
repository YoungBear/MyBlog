#Android 开发艺术探索 读书笔记

##第4章 View的工作原理

###4.3 View的工作流程

View的三大流程：

- measure 确定View的测量宽/高
- layout 确定View的最终宽/高和四个顶点的位置
- draw 将View绘制到屏幕上

####4.3.1 measure过程

measure过程分情况来看，如果只是一个原始的View，那么通过measure方法就完成了测量过程，如果是一个ViewGroup，除了完成自己的测量过程外，还会遍历去调用所有子元素的measure方法，各个子元素再递归去执行这个流程。

**1. View的measure过程**

View的measure方法是final的，所以不能覆盖它，measure中会调用onMeasure方法：

```
    protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
        setMeasuredDimension(getDefaultSize(getSuggestedMinimumWidth(), widthMeasureSpec),
                getDefaultSize(getSuggestedMinimumHeight(), heightMeasureSpec));
    }
```

setMeasuredDimension方法会设置View的宽/高的测量值，因此我们只需要看getDefaultSize方法即可：

```
    public static int getDefaultSize(int size, int measureSpec) {
        int result = size;
        int specMode = MeasureSpec.getMode(measureSpec);
        int specSize = MeasureSpec.getSize(measureSpec);

        switch (specMode) {
        case MeasureSpec.UNSPECIFIED:
            result = size;
            break;
        case MeasureSpec.AT_MOST:
        case MeasureSpec.EXACTLY:
            result = specSize;
            break;
        }
        return result;
    }
```

从getDefaultSize方法的实现来看，View的宽/高由specSize决定，所以我们可以得出如下结论：直接继承View的自定义控件需要重写onMeasure方法并设置wrap_content时的自身大小，否则在布局中使用wrap_content就相当于使用match_parent。为什么呢？这个原因需要结合上述代码和表4-1才能更好地理解。从上述代码中我们知道，如果View在布局中使用wrap_content，那么它的specMode是AT_MOST模式，在这种模式下，它的宽/高等于specSize；查表4-1可知，这种情况下View的specSize是parentSize，而parentSize是父容器中目前可以使用的大小，也就是父容器当前剩余的空间大小。很显然，View的宽/高就等于父容器当前剩余的空间大小，这种效果和在布局中使用match_parent完全一致。解决方案：

```
    @Override
    protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
        super.onMeasure(widthMeasureSpec, heightMeasureSpec);
        int widthSpecMode = MeasureSpec.getMode(widthMeasureSpec);
        int widthSpecSize = MeasureSpec.getSize(widthMeasureSpec);
        int heightSpecMode = MeasureSpec.getMode(heightMeasureSpec);
        int heightSpecSize = MeasureSpec.getSize(heightMeasureSpec);
        if (widthSpecMode == MeasureSpec.AT_MOST && heightSpecMode == MeasureSpec.AT_MOST) {
            setMeasuredDimension(mWidth, mHeight);
        } else if (widthSpecMode == MeasureSpec.AT_MOST) {
            setMeasuredDimension(mWidth, heightSpecSize);
        } else if (heightSpecMode == MeasureSpec.AT_MOST) {
            setMeasuredDimension(widthSpecSize, mHeight);
        }
    }
```

在上面的代码中，我们只需要给View指定一个默认的内部宽/高(mWidth和mHeight)，并在wrap_content是设置此宽/高即可。对于非wrap_content情形，我们沿用系统的测量值即可，至于这个默认的内部宽/高的大小如何指定，这个没有固定的依据，根据需要灵活指定即可。如果查看TextView、ImageView等的源码就可以知道，针对wrap_content情形，它们的onMeasure方法均做了特殊处理。

**2. ViewGroup 的measure 过程**

对于 ViewGroup 来说，除了完成自己的 measure 过程之外，还会遍历去调用所有子元素的 measure 方法，各个子元素再递归去执行这个过程。和 View 不同的是， ViewGroup 是一个抽象类，因此它没有重写 View 的 onMeasure 方法，但是它提供了一个叫 measureChildren 的方法，如下所示。

```
    protected void measureChildren(int widthMeasureSpec, int heightMeasureSpec) {
        final int size = mChildrenCount;
        final View[] children = mChildren;
        for (int i = 0; i < size; ++i) {
            final View child = children[i];
            if ((child.mViewFlags & VISIBILITY_MASK) != GONE) {
                measureChild(child, widthMeasureSpec, heightMeasureSpec);
            }
        }
    }
```

从上述代码来看，ViewGroup 在 measure 时，会对每一个子元素进行 measure， measureChild 这个方法的实现也很好理解，如下所示。

```
    protected void measureChild(View child, int parentWidthMeasureSpec,
            int parentHeightMeasureSpec) {
        final LayoutParams lp = child.getLayoutParams();

        final int childWidthMeasureSpec = getChildMeasureSpec(parentWidthMeasureSpec,
                mPaddingLeft + mPaddingRight, lp.width);
        final int childHeightMeasureSpec = getChildMeasureSpec(parentHeightMeasureSpec,
                mPaddingTop + mPaddingBottom, lp.height);

        child.measure(childWidthMeasureSpec, childHeightMeasureSpec);
    }
```

很显然， measureChild 的思想就是取出子元素的 LayoutParams，然后再通过 getChildMeasureSpec 来创建子元素的 MeasureSpec，接着将 MeasureSpec 直接传递给 View 的 measure 方法来进行测量。 getChildMeasureSpec 的工作过程已经在上面进行了详细分析，通过表 4-1 可以更清楚地了解它的逻辑。

我们知道， ViewGroup 并没有定义其测量的具体过程，这是因为 ViewGroup 是一个抽象类，其测量过程的 onMeasure 方法需要各个子类去具体实现，比如 LinearLayout、RelativeLayout 等，为什么 ViewGroup 不像 View 一样对其 onMeasure 方法做统一的实现呢？那是因为不同的 ViewGroup 子类有不同的布局特性，这导致它们的测量细节各不相同，比如 LinearLayout 和 RelativeLayout 这两者的布局特性显然不同，因此 ViewGroup 无法做统一实现。下面就通过 LinearLayout 的 onMeasure 方法来分析 ViewGroup 的 measure 过程，其他 Layout 类型读者可以自行分析。

//todo LinearLayout 的 onMeasure 分析

```
    @Override
    protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
        if (mOrientation == VERTICAL) {
            measureVertical(widthMeasureSpec, heightMeasureSpec);
        } else {
            measureHorizontal(widthMeasureSpec, heightMeasureSpec);
        }
    }
```

##第8章 理解Window和WindowManager

