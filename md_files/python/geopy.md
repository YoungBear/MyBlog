# geopy 在python中的使用

[geopy](https://github.com/geopy/geopy)是一个关于地理编码的python库。主要有以下几个功能：(需要联网)

1. 地理编码：将字符串转换为地理位置
2. 逆地理编码：用于将地理坐标转换为具体地址
3. 计算两个点的距离：经纬度距离和球面距离

## 安装

```
pip install geopy
```
## 使用

### 地理编码

```
>>> from geopy.geocoders import Nominatim
>>> geolocator = Nominatim()
>>> location = geolocator.geocode("天安门")
>>> print(location.address)
天安门, 东长安街, 崇文, 北京市, 东城区, 北京市, 100010, 中国
>>> print((location.latitude, location.longitude))
(39.9073285, 116.391242416486)
>>> print(location.raw)
{'class': 'building', 'boundingbox': ['39.9072282', '39.9075301', '116.3906498', '116.3918383'], 'place_id': '74005413', 'lon': '116.391242416486', 'osm_type': 'way', 'osm_id': '25097203', 'importance': 0.111, 'display_name': '天安门, 东长安街, 崇文, 北京市, 东城区, 北京市, 100010, 中国', 'type': 'yes', 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright', 'lat': '39.9073285'}
>>> 
```

![地理编码](http://img.blog.csdn.net/20171123190901853?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### 逆地理编码

```
>>> from geopy.geocoders import Nominatim
>>> geolocator = Nominatim()
>>> location = geolocator.reverse("34.224719, 108.9427484")
>>> print(location.address)
海底捞, 长安北路, 小寨, 雁塔区, 雁塔区 (Yanta), 西安市, 陕西省, 710061, 中国
>>> print((location.latitude, location.longitude))
(34.2253171, 108.9426205)
>>> print(location.raw)
{'lon': '108.9426205', 'display_name': '海底捞, 长安北路, 小寨, 雁塔区, 雁塔区 (Yanta), 西安市, 陕西省, 710061, 中国', 'boundingbox': ['34.2252171', '34.2254171', '108.9425205', '108.9427205'], 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright', 'address': {'county': '雁塔区 (Yanta)', 'country': '中国', 'road': '长安北路', 'state_district': '西安市', 'restaurant': '海底捞', 'neighbourhood': '小寨', 'country_code': 'cn', 'postcode': '710061', 'state': '陕西省', 'town': '雁塔区'}, 'place_id': '58165875', 'lat': '34.2253171', 'osm_id': '4516338791', 'osm_type': 'node'}
>>> 
```

![逆地理编码](http://img.blog.csdn.net/20171123191055643?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 计算距离
单位可以为

- meters 米(简写m)
- kilometers 千米(简写km)
- miles 英里(简写mi)
- nautical 海里(简写nm)
- feet 英尺(简写ft)

[具体可参考源代码](https://github.com/geopy/geopy/blob/master/geopy/distance.py)

### 计算经纬度距离[Vincenty distance](https://en.wikipedia.org/wiki/Vincenty's_formulae)

```
>>> from geopy.distance import vincenty
>>> tiananmen = (39.9073285, 116.391242416486)
>>> xiaozhai = (34.2253171, 108.9426205)
>>> print(vincenty(tiananmen, xiaozhai).meters)
913925.3164971869
>>> 
```

![计算经纬度距离](http://img.blog.csdn.net/20171123191145385?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### 计算球面距离[great-circle distance](https://en.wikipedia.org/wiki/Great-circle_distance)

```
>>> from geopy.distance import great_circle
>>> tiananmen = (39.9073285, 116.391242416486)
>>> xiaozhai = (34.2253171, 108.9426205)
>>> print(great_circle(tiananmen, xiaozhai).meters)
913913.5874054108
>>> 
```

![计算球面距离](http://img.blog.csdn.net/20171123191211890?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 参考

[geopy Github地址](https://github.com/geopy/geopy)
[geopy使用详解](https://www.cnblogs.com/giserliu/p/4982187.html)


  [1]: http://img.blog.csdn.net/20171123190901853?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast