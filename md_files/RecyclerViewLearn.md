# RecyclerView的用法

## 1.添加依赖库
```
compile 'com.android.support:recyclerview-v7:25.3.1'
```

## 2. 代码实现

布局文件：

```
    <android.support.v7.widget.RecyclerView
        android:id="@+id/recycler_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />
```

创建Adapter：

```
public class ActivityAdapter extends RecyclerView.Adapter<ActivityAdapter.ViewHolder> {


    private List<ActivityBean> mData;
    private OnItemClickListener mOnItemClickListener;

    public ActivityAdapter(List<ActivityBean> mData) {
        this.mData = mData;
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.layout_activity_item, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(final ViewHolder holder, int position) {
        holder.tvTitle.setText(mData.get(position).getTitle());
        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(mOnItemClickListener != null) {
                    mOnItemClickListener.onItemClick(v, holder.getLayoutPosition());
                }
            }
        });

    }

    @Override
    public int getItemCount() {
        return mData == null ? 0 : mData.size();
    }

    static final class ViewHolder extends RecyclerView.ViewHolder {
        @BindView(R.id.tv_title)
        TextView tvTitle;

        public ViewHolder(View itemView) {
            super(itemView);
            ButterKnife.bind(this, itemView);
        }
    }

    public void setOnItemClickListener(OnItemClickListener onItemClickListener) {
        mOnItemClickListener = onItemClickListener;
    }

    public interface OnItemClickListener {
        void onItemClick(View v, int position);
    }


}
```

在Activity中初始化RecyclerView：

```
    private void initRecyclerView() {
        //添加数据
        addData();
        mAdapter = new ActivityAdapter(mData);
        //设值layout manager
        LinearLayoutManager layoutManager = new LinearLayoutManager(this);
        layoutManager.setOrientation(LinearLayoutManager.VERTICAL);
        mRecyclerView.setLayoutManager(layoutManager);
        //设置item的宽和高为常量，避免了RecyclerView重新计算item的宽高
        mRecyclerView.setHasFixedSize(true);
        //设置分割线
        DividerItemDecoration dividerItemDecoration =
                new DividerItemDecoration(this, DividerItemDecoration.VERTICAL);
        dividerItemDecoration.setDrawable(ContextCompat.getDrawable(this, R.drawable.recycler_view_divider));
        mRecyclerView.addItemDecoration(dividerItemDecoration);
        mRecyclerView.setAdapter(mAdapter);
        //设置点击事件
        mAdapter.setOnItemClickListener(new ActivityAdapter.OnItemClickListener() {
            @Override
            public void onItemClick(View v, int position) {
                startActivity(mData.get(position).getaClass());

            }
        });

    }
```

## 3. 设置item的点击效果(api 21以上才有效)

第一种:

```
android:background="?android:attr/selectableItemBackground"
```

第二种:

```
//item的设置
android:background="@drawable/activity_recycler_view_item_bg"

//res/drawable/activity_recycler_view_item_bg.xml
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="@color/recycler_view_item_bg_pressed_color" android:state_pressed="true" />
    <item android:drawable="@color/recycler_view_item_bg_normal_color" />
</selector>

//res/drawable-v21/activity_recycler_view_item_bg.xml
<?xml version="1.0" encoding="utf-8"?>
<ripple xmlns:android="http://schemas.android.com/apk/res/android"
    android:color="@color/recycler_view_item_bg_pressed_color">
    <item android:drawable="@color/recycler_view_item_bg_normal_color" />
</ripple>
```


[demo源代码的github地址](https://github.com/YoungBear/Hello)
