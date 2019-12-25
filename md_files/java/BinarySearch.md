# 二分查找

```java
package com.ysx.common;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2019/12/25 22:00
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description
 */
public class BinarySearchUtils {

    /**
     * 二分查找
     * @param nums 整型数组
     * @param target 目标值
     * @return 查找匹配的下标，如果没有匹配的则返回-1
     */
    public static int binarySearch(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        int begin = 0;
        int end = nums.length - 1;
        int result = -1;
        while (begin <= end) {
            // 这种写法是防止begin+end溢出
            int middle = begin + (end - begin) / 2;
            if (nums[middle] == target) {
                return middle;
            } else if (nums[middle] > target) {
                end = middle - 1;
            } else {
                begin = middle + 1;
            }
        }
        return result;
    }

    /**
     * 二分查找
     *
     * @param nums   整型数组
     * @param target 目标值
     * @return 查找第一个匹配的元素，成功返回下标，失败返回-1
     */
    public static int binarySearchFirst(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        int begin = 0;
        int end = nums.length - 1;
        int result = -1;
        while (begin <= end) {
            // 这种写法是防止begin+end溢出
            int middle = begin + (end - begin) / 2;
            if (nums[middle] == target) {
                result = middle;
                end = middle - 1;
            } else if (nums[middle] > target) {
                end = middle - 1;
            } else {
                begin = middle + 1;
            }
        }
        return result;
    }

    /**
     * 二分查找
     *
     * @param nums   整型数组
     * @param target 目标值
     * @return 查找最后一个匹配的元素，成功返回下标，失败返回-1
     */
    public static int binarySearchLast(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        int begin = 0;
        int end = nums.length - 1;
        int result = -1;
        while (begin <= end) {
            // 这种写法是防止begin+end溢出
            int middle = begin + (end - begin) / 2;
            if (nums[middle] == target) {
                result = middle;
                begin = middle + 1;
            } else if (nums[middle] > target) {
                end = middle - 1;
            } else {
                begin = middle + 1;
            }
        }
        return result;
    }
}

```

