# 百度 Place Suggestion API

由于最新版的百度SDK(2017-10-27)，在Android SDK 已经不再支持**地点输入提示服务**，所以如果我们需要模糊搜索的时候，需要单独申请服务端应用。

原有申请的Android SDK，可以继续使用**Place API v2**。



[官方文档](http://lbsyun.baidu.com/index.php?title=webapi/place-suggestion-api)

访问URL：

eg.

```
http://api.map.baidu.com/place/v2/suggestion?query=天安门&region=北京&city_limit=true&output=json&ak=你的ak //GET请求
```

具体要求请查看[官方文档](http://lbsyun.baidu.com/index.php?title=webapi/place-suggestion-api)。


服务器端有两种校验方式：

- IP白名单校验
- sn校验


## IP白名单校验
只有IP白名单内的服务器才能成功发起调用。

格式:

```
202.198.16.3,202.198.0.0/16 
```

填写**IP地址**或**IP前缀网段**，**英文半角逗号**分隔。如果不想对IP做任何限制，请设置为**0.0.0.0/0** （谨慎使用，AK如果泄露配额会被其用户消费，上线前可以用作Debug，线上正式ak请设置合理的IP白名单）

## sn校验

// todo 查看申请的ak所对应的sn值截图

[官方sn说明文档](http://lbsyun.baidu.com/index.php?title=lbscloud/api/appendix)

官方是以前缀`/geocoder/v2/?`为例的，由于我们需要使用的是地点输入提示服务，所以我们需要将前缀改为`/place/v2/suggestion?`。

```
http://api.map.baidu.com/place/v2/suggestion?q=丽江&region=全国&output=json&ak=your_ak&timestamp=1509167078641&sn=7de5a22212ffaa9e326444c75a58f9a0
／／后面的sn就是要计算的，sk不需要在url里出现，但是在计算sn的时候需要sk（假设sk=yoursk）
```

所以，我们简单说一下sn的生成方法：


这个是工具类SnUtils，用来生成sn。

```
public class SnUtils {
    private static final String TAG = "SnUtils";

    /**
     * @param host      前缀 /place/v2/suggestion?
     * @param sk        sk值
     * @param paramsMap 存储参数及值的map
     * @return 获取sn签名
     */
    public static String getSnValue(String host, String sk, Map<String, String> paramsMap) {
        try {
            String paramsStr = toQueryString(paramsMap);
            String wholeStr = new String(host + paramsStr + sk);
            String tempStr = URLEncoder.encode(wholeStr, "UTF-8");
            return MD5(tempStr);
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        return "";

    }

    /**
     * 对Map内所有value作utf8编码，拼接返回结果
     *
     * @param data
     * @return
     * @throws UnsupportedEncodingException
     */
    public static String toQueryString(Map<?, ?> data)
            throws UnsupportedEncodingException {
        StringBuffer queryString = new StringBuffer();
        for (Map.Entry<?, ?> pair : data.entrySet()) {
            queryString.append(pair.getKey() + "=");
            queryString.append(URLEncoder.encode((String) pair.getValue(),
                    "UTF-8") + "&");
        }
        if (queryString.length() > 0) {
            queryString.deleteCharAt(queryString.length() - 1);
        }
        return queryString.toString();
    }

    /**
     * 来自stackoverflow的MD5计算方法
     * 调用了MessageDigest库函数，并把byte数组结果转换成16进制
     *
     * @param md5
     * @return
     */
    public static String MD5(String md5) {
        try {
            java.security.MessageDigest md = java.security.MessageDigest
                    .getInstance("MD5");
            byte[] array = md.digest(md5.getBytes());
            StringBuffer sb = new StringBuffer();
            for (int i = 0; i < array.length; ++i) {
                sb.append(Integer.toHexString((array[i] & 0xFF) | 0x100)
                        .substring(1, 3));
            }
            return sb.toString();
        } catch (java.security.NoSuchAlgorithmException e) {
        }
        return null;
    }
}
```

实际调用demo：

需要注意的是，sn字段需要放在最后。

官方说明：

计算sn跟参数对出现顺序有关，get请求请使用LinkedHashMap保存<key,value>，该方法根据key的插入顺序排序；post请使用TreeMap保存<key,value>，该方法会自动将key按照字母a-z顺序排序。所以get请求可自定义参数顺序（**sn参数必须在最后**）发送请求，但是post请求必须按照字母a-z顺序填充body（sn参数必须在最后）。以get请求为例：

`http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak`

paramsMap中先放入address，再放output，然后放ak，放入顺序必须跟get请求中对应参数的出现顺序保持一致。

```
public class BaiduTest {
    public static void main(String[] args) {
        Map<String, String> paramsMap = new LinkedHashMap<>();
        paramsMap.put("q", "丽江");
        paramsMap.put("region", "全国");

        paramsMap.put("output", "json");
        paramsMap.put("ak", "your_ak");
        paramsMap.put("timestamp", String.valueOf(System.currentTimeMillis()));

        String sn = SnUtils.getSnValue("/place/v2/suggestion?", "your_sk", paramsMap);
        /**
         * sn值要放在最后
         */
        paramsMap.put("sn", sn);

        String url = null;
        try {
            url = "http://api.map.baidu.com/place/v2/suggestion" + "?" + SnUtils.toQueryString(paramsMap);
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        System.out.println("url: " + url);
    }
}
```

## Android代码实现

说明：

首页是地图页面，会调用百度定位，成功后，地图会将当前位置移动到屏幕中心。

搜索：

点击搜索后，可以进行模糊搜索，即调用Place Sug API，返回一个结果列表，其中包含经纬度信息，点击item的时候，将finish掉这个SearchActivity，并将item的经纬度信息回传给地图Activity。

核心代码为：

设置item监听:

```
    mPlaceSugAdapter.setOnItemClickListener(new PlaceSugAdapter.OnItemClickListener() {
            @Override
            public void onItemClick(View view, int position) {
                Log.d(TAG, "Result onItemClick, position: " + position);
                backToMapActivity(mData.get(position));
            }
        });
```

退出并返回地图Activity：

```
    /**
     * @param resultBean 百度位置信息
     *                   返回到MapActivity
     */
    private void backToMapActivity(BaiduPlaceSugBean.ResultBean resultBean) {
        Intent data = new Intent();
        data.putExtra(SearchPlaceConstant.EXTRA_LATITUDE, resultBean.getLocation().getLat());
        data.putExtra(SearchPlaceConstant.EXTRA_LONGITUDE, resultBean.getLocation().getLng());
        setResult(Activity.RESULT_OK, data);
        Log.d(TAG, "backToGisActivity:"
                + "\nlatitude: " + resultBean.getLocation().getLat()
                + "\nlongitude: " + resultBean.getLocation().getLng());

        finish();
    }
```

startActivityForResult的回调方法：

获取传递来的经纬度，然后地图定位到该位置。并用Marker标出。

```
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == REQUEST_CODE_SEARCH) {
            if (resultCode == Activity.RESULT_OK) {
                double latitude = data.getDoubleExtra(SearchPlaceConstant.EXTRA_LATITUDE, 0D);
                double longitude = data.getDoubleExtra(SearchPlaceConstant.EXTRA_LONGITUDE, 0D);
                LatLng latLng = new LatLng(latitude, longitude);

                Log.d(TAG, "onActivityResult: mLatLng: " + latLng);
                MapStatus.Builder builder = new MapStatus.Builder();
                builder.target(latLng);
                MapStatusUpdate mapStatusUpdate = MapStatusUpdateFactory.newMapStatus(builder.build());
                mBaiduMap.setMapStatus(mapStatusUpdate);
                if (mSearchBd == null) {
                    mSearchBd = BitmapDescriptorFactory.fromResource(R.drawable.ic_location);
                }
                MarkerOptions option = new MarkerOptions().icon(mSearchBd).position(latLng);
                mBaiduMap.addOverlay(option);

            }
        }
        super.onActivityResult(requestCode, resultCode, data);
    }
```

![地址输入提示服务demo](https://github.com/YoungBear/MyBlog/blob/master/pngs/baidu/baidu_place_sug_demo_360_640.gif)

## [Demo地址](https://github.com/YoungBear/BaiduDemo)

