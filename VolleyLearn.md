#Volley学习

[Volley](https://developer.android.com/training/volley/index.html "")是Android下个一个网络请求库，它可以让Android下的网络访问更加简单和快速。默认情况下，Volley都是异步访问网络的，所以我们不必担心异步处理问题。

##Volley的优点：

1. 请求队列和请求优先级
2. 请求Cache和内存管理
3. 扩展性性强
4. 可以取消请求

##导入Volley的方法

###**第一种**
在build.gradle中添加dependency:

```
dependencies {
    ...
    compile 'com.android.volley:volley:1.0.0'
}
```

###**第二种**
使用源代码，作为一个library project。

```
git clone https://android.googlesource.com/platform/frameworks/volley
```
另外，也可以在源代码中导出jar包,使用jar包作为库。

##使用Volley进行网络请求

首先，在AndroidManifest.xml中添加网络访问权限，

```
<uses-permission android:name="android.permission.INTERNET"/>
```

##使用一个单例来管理请求(一般可以继承Application)
```
//VolleyController.java
public class VolleyController {

    public static final String TAG = VolleyController.class.getSimpleName();

    private static volatile VolleyController mInstance;
    private RequestQueue mRequestQueue;
    private ImageLoader mImageLoader;
    private static Context mContext;

    private VolleyController(Context context) {
        mContext = context.getApplicationContext();
        mRequestQueue = Volley.newRequestQueue(mContext);
        mImageLoader = new ImageLoader(mRequestQueue, new LruBitmapCache());
    }

    public static VolleyController getInstance(Context context) {
        if (mInstance == null) {
            synchronized (VolleyController.class) {
                if (mInstance == null) {
                    mInstance = new VolleyController(context);
                }
            }
        }
        return mInstance;
    }

    public RequestQueue getRequestQueue() {
        return mRequestQueue;
    }

    public ImageLoader getImageLoader() {
        return mImageLoader;
    }

    public <T> void addToRequestQueue(Request<T> req, String tag) {
        req.setTag(TextUtils.isEmpty(tag) ? TAG : tag);
        mRequestQueue.add(req);
    }

    public <T> void addToRequestQueue(Request<T> req) {
        req.setTag(TAG);
        mRequestQueue.add(req);
    }

    public void cancelPendingRequests(Object tag) {
        if (mRequestQueue != null) {
            mRequestQueue.cancelAll(tag);
        }
    }

}
```

还需要一个Cache来存放请求的图片：

```
//LruBitmapCache.java
public class LruBitmapCache extends LruCache<String, Bitmap> implements ImageLoader.ImageCache{

    public static int getDefaultLruCacheSize() {
        final int maxMemory = (int) (Runtime.getRuntime().maxMemory() / 1024);
        final int cacheSize = maxMemory / 8;
        return cacheSize;
    }

    public LruBitmapCache() {
        this(getDefaultLruCacheSize());
    }

    public LruBitmapCache(int sizeInKiloBytes) {
        super(sizeInKiloBytes);
    }

    @Override
    protected int sizeOf(String key, Bitmap value) {
        return value.getRowBytes() * value.getHeight() / 1024;
    }

    @Override
    public Bitmap getBitmap(String url) {
        return get(url);
    }

    @Override
    public void putBitmap(String url, Bitmap bitmap) {
        put(url, bitmap);
    }
}
```

###String Request

**新建一个Request并且把他加入到请求队列中RequestQueue：**

```
    private void simpleRequest() {

        StringRequest stringRequest = new StringRequest(
                Request.Method.GET,
                TEST_URL,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        Log.d(TAG, "onResponse, response: " + response);
                        txtDisplay.setText("Response is: " + response);
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.d(TAG, "onErrorResponse, error: " + error.getMessage());
                        txtDisplay.setText("That didn't work!");
                    }
                });

        VolleyController.getInstance(this).addToRequestQueue(stringRequest, TAG);
    }
```

**Volley工作原理图**

![Life of a request](http://img.blog.csdn.net/20161017172704368 "")

**在Activity的onStop()方法中cancel所有标记为该TAG的请求：**

```
@Override
protected void onStop() {
    super.onStop();
    VolleyController.getInstance(this).cancelPendingRequests(TAG);
}
```

**创建POST请求**

上面说的都是GET请求，下面来说一下POST请求，与GET请求不同的是，只要在创建请求的时候将请求类型改为POST请求，并且override Request的<font color=red>getParams</font>方法即可。

**添加请求头部信息**

override Request的<font color=red>getHeaders</font>方法。

```
    private void simplePostRequest() {
        StringRequest stringRequest = new StringRequest(
                Request.Method.POST,
                TEST_URL,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        Log.d(TAG, "post, onResponse, response: " + response);
                        txtDisplay.setText("Response is: " + response);
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.d(TAG, "post, onErrorResponse, error: " + error.getMessage());
                        txtDisplay.setText("That didn't work!");
                    }
                }
        ) {
            @Override
            protected Map<String, String> getParams() throws AuthFailureError {
                Map<String, String> params = new HashMap<String, String>();
                params.put("name", "Androidhive");
                params.put("email", "abc@androidhive.info");
                params.put("password", "password123");

                return params;
            }

            @Override
            public Map<String, String> getHeaders() throws AuthFailureError {
                HashMap<String, String> headers = new HashMap<String, String>();
                headers.put("Content-Type", "application/json");
                headers.put("apiKey", "xxxxxxxxxxxxxxx");
                return headers;
            }
        };
        //关闭Cache
        stringRequest.setShouldCache(false);
        VolleyController.getInstance(this).addToRequestQueue(stringRequest, TAG);
    }
```

###创建Image请求
Volley库中自带了NetworkImageView类，这个ImageView可以自动使用volley下载图片。

####**使用ImageRequest**

```
    private void imageRequest() {

        ImageRequest imageRequest = new ImageRequest(
                TEST_URL_1,
                new Response.Listener<Bitmap>() {
                    @Override
                    public void onResponse(Bitmap response) {
                        mImageView.setImageBitmap(response);
                    }
                }, 0, 0, null,
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.d(TAG, "onErrorResponse, error: " + error.getMessage());
                    }
                }
        );
        VolleyController.getInstance(this).addToRequestQueue(imageRequest, TAG);
    }
```

ImageRequest构造函数源代码：

```
    @Deprecated
    public ImageRequest(String url, Response.Listener<Bitmap> listener, int maxWidth, int maxHeight,
            Config decodeConfig, Response.ErrorListener errorListener) {
        this(url, listener, maxWidth, maxHeight,
                ScaleType.CENTER_INSIDE, decodeConfig, errorListener);
    }
```

可以看到，ImageRequest的构造函数接收6个参数

1. 第一个参数是图片的URL地址
2. 第二个参数是图片请求成功的回调，这里我们把返回的Bitmap参数设置到ImageView中
3. 第三和第四个参数分别用于指定允许图片最大的宽度和高度，如果指定的网络图片的宽度或高度大于这里的最大值，则会对图片进行压缩，指定成0的话就表示不管图片有多大，都不进行压缩。
4. 第五个参数用于指定图片的颜色属性，Bitmap.Config下的几个常量都可以在这里使用，其中ARGB_8888可以展示最好的颜色属性，每个图片像素占据4个人字节的大小，而RGB_565则表示每个图片像素占据2个字节大小。
5. 第六个参数是图片请求失败的回调，我们可以在请求失败时显示一张失败的图片。

####**使用ImageLoader**
ImageLoader也可以用于加载网络上的图片，并且它的内部也是使用ImageRequest来实现的，不过ImageLoader明显要比ImageRequest更加高效，因为它不仅可以帮我们对图片进行缓存，还可以过滤掉重复的链接，避免重复发送请求。

由于ImageLoader已经不是继承自Request的了，所以它的用法也和我们之前学到的内容有所不同，总结起来大致可以分为以下四步：

1. 创建一个RequestQueue对象
2. 创建一个ImageLoader对象
3. 获取一个ImageListener对象
4. 调用ImageLoader的get()方法加载网络上的图片


```
    private void imageLoaderGet() {
        ImageLoader imageLoader = VolleyController.getInstance(this).getImageLoader();
        imageLoader.get(TEST_URL_3, new ImageLoader.ImageListener() {
            @Override
            public void onResponse(ImageLoader.ImageContainer response, boolean isImmediate) {
                mImageView3.setImageBitmap(response.getBitmap());
            }

            @Override
            public void onErrorResponse(VolleyError error) {
                Log.e(TAG, "Image Load Error: " + error.getMessage());
            }
        });
    }
```

####**使用NetworkImageView**
NetworkImageView是一个自定义控件，它是继承自ImageView的，具备ImageView控件的所有功能，并且在原生的基础之上加入了加载网络图片的功能。

使用方法：

1. 在布局文件中添加NetworkImageView
2. 获取ImageLoader
3. 调用NetworkImageView的setImageUrl()方法

```
//...
    <com.android.volley.toolbox.NetworkImageView
        android:id="@+id/network_img_display"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"/>
        
    mNetworkImageView = (NetworkImageView) findViewById(R.id.network_img_display);
    private void setNetworkImageView() {
        ImageLoader imageLoader = VolleyController.getInstance(this).getImageLoader();
        mNetworkImageView.setImageUrl(TEST_URL_2, imageLoader);
    }

```

###JSON Request

```
    private void jsonRequest() {
        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(
                Request.Method.GET,
                TEST_URL,
                null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        txtDisplay.setText(response.toString());
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.e(TAG, "onErrorResponse, error: " + error.getMessage());
                    }
                });
        VolleyController.getInstance(this).addToRequestQueue(jsonObjectRequest, TAG);
    }

    private void jsonArrayRequest() {
        JsonArrayRequest jsonArrayRequest = new JsonArrayRequest(
                Request.Method.GET,
                TEST_URL2,
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        txtDisplay.setText(response.length() + "\n" + response.toString());
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.e(TAG, "onErrorResponse, error: " + error.getMessage());
                    }
                }
        );
        VolleyController.getInstance(this).addToRequestQueue(jsonArrayRequest, TAG);
    }
```

测试代码位置:https://github.com/YoungBear/VolleyLearn


参考：

http://www.androidhive.info/2014/05/android-working-with-volley-library-1/

http://bxbxbai.github.io/2014/09/14/android-working-with-volley/

https://developer.android.com/training/volley/index.html

http://blog.csdn.net/guolin_blog/article/details/17482165
