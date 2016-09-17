# Java 生成随机数 #
生成0~n的随机数，可使用Random.nextInt(n)

```
package com.example.random;

import java.util.HashSet;
import java.util.Random;
import java.util.Set;

public class Random2016 {

    // 10万个数里边随机取2016个数
    private static final int N = 100000;

    public static void main(String[] args) {
        //使用Set来保存，保证没有重复。
        Set<Integer> resultSet = new HashSet<Integer>();
        Random random = new Random();
        for (int i = 0; i < 2016;) {
            //随机数可能是0,1,2,...,N-1
            int temp = random.nextInt(N);
            if (resultSet.add(temp)) {
                System.out.println("i: " + i + ", temp: " + temp);
                i++;
            } else {
                System.out.println("already have this number, temp:" + temp
                        + ", i: " + i);
            }
        }
    }
}
```