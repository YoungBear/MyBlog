# Java - List 的 contains 方法的性能

有一个需求，对一个List中的元素，获取的所有Record字段，**要求去重**，并作为List返回。现在有两个方案，一个是使用`ArrayList`(`LinkedList`类似)，另一个是使用`HashSet`，`ArrayList`使用其`contains()`方法来去重，`HashSet`调用`add()`方法自然会去重。具体实现如下：


```
package com.example.collection;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * @author youngbear
 * @email youngbear@aliyun.com
 * @date 2018/8/15 22:17
 * @blog https://blog.csdn.net/next_second
 * @github https://github.com/YoungBear
 * @description ArrayList 的contains方法的性能问题
 */
public class ContainsTest {

    public static final int COLUMNS = 30;
    public static final int NUMBERS = 10000;
    public static void main(String[] args) {
        List<Pair> pairs = generateData();
        System.out.println("pairs.size(): " + pairs.size());

        long beginList = System.currentTimeMillis();
        List<Long> recordUsingList = getRecordUsingList(pairs);
        long endList = System.currentTimeMillis();

        long beginSet = System.currentTimeMillis();
        List<Long> recordUsingSet = getRecordUsingSet(pairs);
        long endSet = System.currentTimeMillis();

        System.out.println("list: " + (endList - beginList) + " ms" + ", size: " + recordUsingList.size());
        System.out.println("set: " + (endSet - beginSet) + " ms" + ", size: " + recordUsingSet.size());

    }

    /**
     * 生成测试数据
     * @return
     */
    static List<Pair> generateData() {
        List<Pair> pairs = new ArrayList<Pair>();
        for (int i = 0; i < NUMBERS; i++) {
            for (int j = 0; j < COLUMNS; j++) {
                Pair pair = new Pair();
                pair.setRecord((long)i);
                pair.setName("name: " + i + ", " + j);
                pairs.add(pair);
            }
        }
        return pairs;
    }

    /**
     * 使用列表去重
     * @param list
     * @return
     */
    static List<Long> getRecordUsingList(List<Pair> list) {
        List<Long> results = new ArrayList<Long>();
        for (Pair pair : list) {
            if (!results.contains(pair.getRecord())) {
                results.add(pair.getRecord());
            }
        }
        return results;
    }

    /**
     * 使用Set去重
     * @param list
     * @return
     */
    static List<Long> getRecordUsingSet(List<Pair> list) {
        Set<Long> set = new HashSet<Long>();
        for (Pair pair : list) {
            set.add(pair.getRecord());
        }
        List<Long> results = new ArrayList<Long>(set);
        return results;
    }


    static class Pair{
        private Long record;
        private String name;

        public Long getRecord() {
            return record;
        }

        public void setRecord(Long record) {
            this.record = record;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }
}



```

输出结果为：

```
pairs.size(): 300000
list: 13908 ms, size: 10000
set: 31 ms, size: 10000
```

## 分析

### `List`
由于数据中存在重复元素，所以使用`contains()`方法，但是，`ArrayList`的`contains()`方法会调用其`indexOf()`方法，在`indexOf()`方法里边，有一个for循环，所以，`ArrayList`的`contains()`方法的时间复杂度是`O(n*n)`。

```
    public boolean contains(Object o) {
        return indexOf(o) >= 0;
    }

    public int indexOf(Object o) {
        if (o == null) {
            for (int i = 0; i < size; i++)
                if (elementData[i]==null)
                    return i;
        } else {
            for (int i = 0; i < size; i++)
                if (o.equals(elementData[i]))
                    return i;
        }
        return -1;
    }    
```

### `HashSet`
对于`HashSet`，它的`add()`方法会自动去重，它调用的是一个`map`的`put`方法，其时间复杂度是`O(1)`。

```
    public boolean add(E e) {
        return map.put(e, PRESENT)==null;
    }
```

## 结论
所以，在大量的数据的时候，不要使用`List`的`contains()`方法，其效率很低，可以考虑使用`Set`来实现。


## 参考
[HashSet vs. List performance](https://stackoverflow.com/questions/150750/hashset-vs-list-performance)

[HashSet vs ArrayList contains performance](https://stackoverflow.com/questions/32552307/hashset-vs-arraylist-contains-performance)

### [更多文章](https://github.com/YoungBear/MyBlog/blob/master/README.md)