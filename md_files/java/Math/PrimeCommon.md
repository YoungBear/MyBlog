# 素数

## 1. 获取n以内素数列表

使用筛选法，生成正整数n以内素数列表。

**算法描述：**

初始设置BitSet从0到n的值均为true。

从2开始，由于2是素数，所以将所有2的倍数排除；然后下一个素数是3，则将所有3的倍数排除；下一个素数是

5，将所有5的倍数排除...

以此类推，直到n。

BitSet中剩余的值为true的index即为素数。

具体代码：

```java
    /**
     * 筛选法生成正整数n以内素数列表
     * 描述：
     * 初始设置BitSet从0到n的值均为true
     * 从2开始，由于2是素数，所以将所有2的倍数排除
     * 然后下一个素数是3，则将所有3的倍数排除
     * 下一个素数是5，将所有5的倍数排除
     * ...
     * 直到n
     * BitSet中剩余的值为true的index即为素数
     *
     * @param n 正整数
     * @return 素数表，用 BitSet 表示
     */
    public static BitSet genPrimeBitSet(int n) {
        BitSet primeBitSet = new BitSet(n);
        primeBitSet.set(0, n, true);
        primeBitSet.set(0, false);
        primeBitSet.set(1, false);
        for (int i = 2; i <= n; i++) {
            if (primeBitSet.get(i)) {
                for (int j = 2 * i; j <= n; j += i) {
                    primeBitSet.set(j, false);
                }
            }
        }
        return primeBitSet;
    }
```

测试代码：

```java
    public static void main(String[] args) {
        // 获取n以内的所有素数
        int n = 1000;
        long begin = System.currentTimeMillis();
        BitSet primeBitSet = genPrimeBitSet(n);
        StringBuilder sb = new StringBuilder();
        int num = 0;
        for (int i = 0; i <= n; i++) {
            if (primeBitSet.get(i)) {
                sb.append(i).append(",");
                num++;
            }
        }
        long end = System.currentTimeMillis();
        sb.delete(sb.toString().length() - 1, sb.toString().length());
        String desc = n + " 以内共 " + num + " 个素数，耗时 " + (end - begin) + "毫秒";
        sb.append(System.lineSeparator()).append(desc);
        System.out.println(sb.toString());
    }
```

以上代码输出为：

```
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997
1000 以内共 168 个素数，耗时 3毫秒
```