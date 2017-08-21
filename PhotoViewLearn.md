# 使用静态方法来startActivity

## 使用PhotoView来显示一个图片


PhotoActivity.java

```
    private static final String IMAGE_PATH = "image_path";
    private static final String IMAGE_URI = "image_uri";

    public static void startPhotoActivity(Context context, String path) {
        Intent intent = new Intent(context, PhotoActivity.class);
        intent.putExtra(IMAGE_PATH, path);
        context.startActivity(intent);
    }

    public static void startPhotoActivity(Context context, Uri imageUri) {
        Intent intent = new Intent(context, PhotoActivity.class);
        intent.putExtra(IMAGE_URI, imageUri);
        context.startActivity(intent);
    }

```

调用方式：

**传递String值，即图片文件路径，可在调用照相机后将保存到指定文件中：**

```
private static final String TAKE_PHOTO_FILE_PATH =
            Environment.getExternalStorageDirectory().getAbsolutePath()
                    + "/" + "test_take_picture.jpg";
PhotoActivity.startPhotoActivity(this, TAKE_PHOTO_FILE_PATH);
```

**传递Uri值，即图片的Uri，在调用图片选择器返回时得到Uri使用：**

```
PhotoActivity.startPhotoActivity(this, mPickPictureImageUri);
```

源代码地址：

https://github.com/YoungBear/PhotoViewLearn