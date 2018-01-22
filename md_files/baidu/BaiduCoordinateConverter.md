# 百度经纬度坐标转换官方方法

[百度坐标转换官方文档](http://lbsyun.baidu.com/index.php?title=androidsdk/guide/tool/coordinate)

**国内主流坐标系类型：**

主要有以下三种

1. WGS84：为一种大地坐标系，也是目前广泛使用的<font color=red>**GPS**</font>全球卫星定位系统使用的坐标系；

2. GCJ02：是由中国国家测绘局制订的地理信息系统的坐标系统，是由WGS84坐标系经加密后的坐标系；又称<font color=red>**火星坐标系**</font>。

3. BD09：百度坐标系，在GCJ02坐标系基础上再次加密。其中BD09ll表示<font color=red>**百度经纬度坐标**</font>，BD09mc表示百度墨卡托米制坐标。

<font color=red>**百度地图SDK在国内（包括港澳台）使用的是BD09坐标（定位SDK默认使用GCJ02坐标）；在海外地区，统一使用WGS84坐标。开发者在使用百度地图相关服务时，请注意选择。**</font>

## 通用坐标转换方法（坐标之间互转）

### 1. GPS坐标转换成百度经纬度坐标

```
    /**
     * 将GPS设备采集的原始GPS坐标转换成百度经纬度坐标
     * 即GPS坐标转换为BD09LL坐标
     * @param sourceLatLng
     * @return
     */
    public static LatLng GPStoBD09LL(LatLng sourceLatLng) {
        CoordinateConverter converter  = new CoordinateConverter();
        converter.from(CoordType.GPS);
        converter.coord(sourceLatLng);
        return converter.convert();
    }
```

### 2. 火星坐标系坐标转换成百度经纬度坐标

```
    /**
     * 将火星坐标系坐标转换成百度经纬度坐标
     * 即GCJ02坐标转换为BD09LL坐标
     * @param sourceLatLng
     * @return
     */
    public static LatLng GCJ02toBD09LL(LatLng sourceLatLng) {
        CoordinateConverter converter  = new CoordinateConverter();
        converter.from(CoordType.COMMON);
        converter.coord(sourceLatLng);
        return converter.convert();
    }
```

### 3. 百度墨卡托米制坐标系坐标转换成百度经纬度坐标

```
    /**
     * 将百度墨卡托米制坐标系坐标转换成百度经纬度坐标
     * 即BD09MC转换成BD09LL
     *
     * @param sourceLatLng
     * @return
     */
    public static LatLng BD09MCtoBD09LL(LatLng sourceLatLng) {
        CoordinateConverter converter = new CoordinateConverter();
        converter.from(CoordType.BD09MC);
        converter.coord(sourceLatLng);
        return converter.convert();
    }
```

**注意：**

在使用百度地图开发的时候，需要确保定位返回的坐标类型和地图使用的坐标类型保持一致。


[完整代码及demo路径](https://github.com/YoungBear/BaiduDemo/blob/master/app/src/main/java/com/ysx/baidu/demo/utils/ConverterUtils.java)




