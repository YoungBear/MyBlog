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

###Simple Request

**新建一个Request并且把他加入到请求队列中RequestQueue：**

```
    private static final String TAG = SimpleRequestActivity.class.getSimpleName();
    private RequestQueue mRequestQueue;
    private static final String TEST_URL = "http://api.androidhive.info/volley/person_object.json";
    private TextView txtDisplay;
    
    // Instantiate the RequestQueue.
    mRequestQueue = Volley.newRequestQueue(this);

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
        // Set the tag on the request.
        stringRequest.setTag(TAG);

        mRequestQueue.add(stringRequest);
    }
```


![Life of a request](http://img.blog.csdn.net/20161017172704368 "")

**在Activity的onStop()方法中cancel所有标记为该TAG的请求：**

```
@Override
protected void onStop() {
    super.onStop();
    if (mRequestQueue != null) {
        mRequestQueue.cancelAll(TAG);
    }
}
```

**创建POST请求**
上面说的都是GET请求，下面来说一下POST请求，与GET请求不同的是，只要在创建请求的时候将请求类型改为POST请求，并且override Request的getParams方法即可。





















参考：

http://www.androidhive.info/2014/05/android-working-with-volley-library-1/

http://bxbxbai.github.io/2014/09/14/android-working-with-volley/

https://developer.android.com/training/volley/index.html
