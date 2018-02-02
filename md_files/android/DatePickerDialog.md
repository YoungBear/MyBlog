# Android日期选择器DatePickerDialog的使用

使用DatePickerDialog来实现日期选择器。

### 使用方法

用一个Calendar对象来保存时间值，然后在回调函数中，可以根据用户的选择，设置日期值，最终使用该Calendar可以获取日期。结合时间格式化函数可以设置想要显示的时间格式。

具体代码：

```
        final Calendar calendar = Calendar.getInstance();
        mTvDate.setText(DateUtils.date2String(calendar.getTime(), DateUtils.YMD_FORMAT));
        DatePickerDialog dialog = new DatePickerDialog(DatePickerActivity.this,
                new DatePickerDialog.OnDateSetListener() {
                    @Override
                    public void onDateSet(DatePicker view, int year, int month, int dayOfMonth) {
                        LogUtils.d(TAG, "onDateSet: year: " + year + ", month: " + month + ", dayOfMonth: " + dayOfMonth);

                        calendar.set(Calendar.YEAR, year);
                        calendar.set(Calendar.MONTH, month);
                        calendar.set(Calendar.DAY_OF_MONTH, dayOfMonth);
                        mTvDate.setText(DateUtils.date2String(calendar.getTime(), DateUtils.YMD_FORMAT));
                    }
                },
                calendar.get(Calendar.YEAR),
                calendar.get(Calendar.MONTH),
                calendar.get(Calendar.DAY_OF_MONTH));
        dialog.show();
```

[完整Activity代码](https://github.com/YoungBear/Hello/blob/master/app/src/main/java/com/example/hello/activity/DatePickerActivity.java)

### 关于样式

用户可以传递一个theme，来设置具体的样式。默认情况下，在Android 4.4及以下，样式为：


![date_picker_android_4.4_api19](http://img.blog.csdn.net/20180202151605591?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

在Android 5.0，样式为：

![date_picker_android_5.0_api21](http://img.blog.csdn.net/20180202151641688?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

在Android 6.0，样式为：

![date_picker_android_6.0_api23](http://img.blog.csdn.net/20180202151731672?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTmV4dF9TZWNvbmQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)