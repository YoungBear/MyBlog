# 使用百度测距

要测量两个坐标之间的**距离**，可以使用百度地图提供的API :

```
DistanceUtil.getDistance(LatLng var0, LatLng var1)
```

**其返回结果是一个double值，单位是米。**

在日常的工作中，经常需要判断用户当前位置是否在目标位置，所以我写了一个辅助函数，用来判断用户是否在目标点：

```
package com.boco.baidusdk.utils;

import android.util.Log;

import com.baidu.mapapi.model.LatLng;
import com.baidu.mapapi.utils.DistanceUtil;

/**
 * 测距帮助类
 *
 * @author ysx
 * @date 2017/12/28
 * @description
 */

public final class DistanceHelper {
    private static final String TAG = "DistanceHelper";

    /**
     * 判断是否在位置点
     *
     * @param dest    目标位置点
     * @param current 当前位置点
     * @param radius  误差半径
     * @return
     */
    public static boolean isInPosition(LatLng dest, LatLng current, double radius) {
        double distance = DistanceUtil.getDistance(dest, current);
        Log.d(TAG, "isInPosition: dest: " + dest + ", current: " + current);
        Log.d(TAG, "isInPosition: distance: " + distance + ", radius: " + radius);
        return Math.abs(distance - radius) < 0;
    }
}
```
