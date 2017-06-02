# TabLayout
介绍：

源码路径：
`android.support.design.widget.TabLayout.java`

`TabLayout provides a horizontal layout to display tabs.`
简单翻译下：TabLayout提供一个水平的布局来显示tabs。


## 一. 引入依赖库：
`compile 'com.android.support:design:26.0.0-alpha1'`

## 二. 使用TabLayout

### 第一种方法：
使用`TabLayout.newTab()`来创建Tab
```
    <android.support.design.widget.TabLayout
        android:id="@+id/tab_layout1"
        android:layout_width="match_parent"
        android:layout_height="wrap_content">

    </android.support.design.widget.TabLayout>
```

```
        mTabLayout1.addTab(mTabLayout1.newTab().setText("item1"));
        mTabLayout1.addTab(mTabLayout1.newTab().setText("item2"));
        mTabLayout1.addTab(mTabLayout1.newTab().setText("item3"));
        mTabLayout1.addTab(mTabLayout1.newTab().setText("item4"));
```

### 第二种方法：
使用`TabItem`

```
    <android.support.design.widget.TabLayout
        android:id="@+id/tab_layout2"
        android:layout_width="match_parent"
        android:layout_height="wrap_content">

        <android.support.design.widget.TabItem
            android:id="@+id/tab_item1"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="tab_item1"/>

        <android.support.design.widget.TabItem
            android:id="@+id/tab_item2"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="tab_item2"/>

        <android.support.design.widget.TabItem
            android:id="@+id/tab_item3"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="tab_item3"/>

        <android.support.design.widget.TabItem
            android:id="@+id/tab_item4"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="tab_item4"/>

    </android.support.design.widget.TabLayout>
```

### 第三种方法：
绑定ViewPager，调用方法：`setupWithViewPager(ViewPager)`，重写`PagerAdapter`的`getPageTitle`方法后，就可以添加导航的item。

```
    <android.support.design.widget.TabLayout
        android:id="@+id/tab_layout"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        app:tabIndicatorColor="@color/red"
        app:tabSelectedTextColor="@color/red"
        app:tabTextColor="@color/black"
        app:tabIndicatorHeight="@dimen/tab_indicator_height"
        app:tabTextAppearance="@style/MyTabLayoutTextAppearance"
        />

    <android.support.v4.view.ViewPager
        android:id="@+id/view_pager"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        />
```

Activity代码：

```
    @BindView(R.id.tab_layout)
    TabLayout mTabLayout;
    @BindView(R.id.view_pager)
    ViewPager mViewPager;

    private List<String> mTitleList = Arrays.asList("1","2","3","4","5","6","7","8");
    private List<Fragment> mFragmentList = new ArrayList<>();
    private TabFragmentPagerAdapter mTabFragmentPagerAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_tab);
        ButterKnife.bind(this);
        initFragmentViewPager();
    }

    private void initFragmentViewPager(){
        mFragmentList.add(new Fragment1());
        mFragmentList.add(new Fragment2());
        mFragmentList.add(new Fragment3());
        mFragmentList.add(new Fragment4());
        mFragmentList.add(new Fragment1());
        mFragmentList.add(new Fragment2());
        mFragmentList.add(new Fragment3());
        mFragmentList.add(new Fragment4());
        mTabFragmentPagerAdapter = new TabFragmentPagerAdapter(
                getSupportFragmentManager(),
                mTitleList,
                mFragmentList);

        mViewPager.setAdapter(mTabFragmentPagerAdapter);
        mTabLayout.setTabMode(TabLayout.MODE_SCROLLABLE);
        mTabLayout.setupWithViewPager(mViewPager);

    }
```
Adapter:

```
    private List<String> mTitles;
    private List<Fragment> mFragments;

    public TabFragmentPagerAdapter(FragmentManager fm, List<String> titles, List<Fragment> fragments) {
        super(fm);
        mTitles = titles;
        mFragments = fragments;
    }

    @Override
    public Fragment getItem(int position) {
        return mFragments.get(position);
    }

    @Override
    public int getCount() {
        return mFragments.size();
    }

    @Override
    public CharSequence getPageTitle(int position) {
        return mTitles.get(position);
    }
```

## 三 设置TabLayout的自定义属性
**设置指示器indicator的颜色：**

`app:tabIndicatorColor="@color/red"`

**设置指示器indicator的高度：**

`app:tabIndicatorHeight="@dimen/tab_indicator_height"`

**设置tab的字体颜色：**

`app:tabTextColor="@color/black"`

**设置tab选中的字体颜色：**

`app:tabSelectedTextColor="@color/red"`

**设置tab的字体大小：**

`app:tabTextAppearance="@style/MyTabLayoutTextAppearance"`

其中，MyTabLayoutTextAppearance为自定义的style：

```
    <style name="MyTabLayoutTextAppearance" parent="TextAppearance.Design.Tab">
        <item name="android:textSize">@dimen/tab_text_size</item>
    </style>
```

**添加icon：**

`android:icon="@mipmap/ic_launcher"`

或者

`mTabLayout1.addTab(mTabLayout1.newTab().setText("item1").setIcon(R.mipmap.ic_launcher));`

**设置TabLayout为可以滑动：**

`app:tabMode="scrollable"`

或者

`mTabLayout.setTabMode(TabLayout.MODE_SCROLLABLE);`

默认是fixed：固定的，标签很多时候会被挤压，不能滑动。

**tab内部的padding：**

```
        app:tabPadding="2dp"
        app:tabPaddingTop="2dp"
        app:tabPaddingBottom="2dp"
        app:tabPaddingStart="2dp"
        app:tabPaddingEnd="2dp"
```

**内容的显示模式：**

`app:tabGravity="center"`

center表示居中，如果是fill，则是充满。

**tab的宽度：**

```
app:tabMinWidth="120dp"
app:tabMaxWidth="120dp"
```

**TabLayout开始位置的偏移量：**

`app:tabContentStart="20dp"`

demo地址：
https://github.com/YoungBear/Hello

参考:

http://www.jianshu.com/p/2b2bb6be83a8

http://www.jianshu.com/p/ce1d060573ba#

