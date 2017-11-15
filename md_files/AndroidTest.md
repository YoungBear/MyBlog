# Android 单元测试

[GoogleSample单元测试](https://github.com/googlesamples/android-testing/)

## AndroidJunitRunnerSample

- CaculatorTest 
- CalculatorInstrumentationTest
- OperationHintInstrumentationTest
- OperationHintLegacyInstrumentationTest

## BasicSample

- EmailValidatorTest Email有效性测试(单元测试)
- SharedPreferencesHelperTest 测试SharedPreferencesHelper的操作(Mock测试)

### Mockito 方法

- `Mockito.verify()` 验证Mock对象的方法是否被调用。
- `Mockito.times()` 调用Mock对象的方法次数。
- `Mockito.atMost(count) , Mockito.atLeast(count) , Mockito.never() ` 最多次数，最少次数，永远调用。
- `Mockito.anyInt() , Mockito.anyLong() , Mockito.anyDouble()等等` 参数设置-任意的Int类型，任意的Long类型。。。等。

[参考](http://www.jianshu.com/p/6334d1e2babf)

