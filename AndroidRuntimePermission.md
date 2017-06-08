# AndroidRuntimePermission
# Android运行时权限

官网文档：

https://developer.android.com/about/versions/marshmallow/android-6.0-changes.html

https://developer.android.com/training/permissions/requesting.html?hl=zh-cn#perm-request

https://developer.android.com/training/permissions/best-practices.html?hl=zh-cn#testing



对于Android 6.0（API 级别 23）或更高版本为目标平台的应用，请务必在**运行时检查**和**请求权限**。

其中，检查权限使用函数

```
ContextCompat.checkSelfPermission() :
public static int checkSelfPermission(@NonNull Context context, @NonNull String permission)
```
返回值为0或者1，其含义分别为：
```
//PackageManager.java
public static final int PERMISSION_GRANTED = 0;//同意
public static final int PERMISSION_DENIED = -1;//拒绝
```

如果应用具有此权限，方法将返回 `PackageManager.PERMISSION_GRANTED`，并且应用可以**继续**操作。如果应用不具有此权限，方法将返回 `PackageManager.PERMISSION_DENIED`，且应用必须**明确**向用户要求权限。

## 请求权限
如果您的应用需要应用清单中列出的**危险权限**，那么，它必须**要求用户授予**该权限。Android 为您提供了多种权限请求方式。调用这些方法将显示一个标准的 Android 对话框，不过，您**不能**对它们进行自定义。

## 解释应用为什么需要权限

为了帮助查找用户可能需要解释的情形，Android 提供了一个实用程序方法，即 `shouldShowRequestPermissionRationale()`。如果应用**之前请求过**此权限**但用户拒绝**了请求，此方法将返回 true。

注：如果用户在过去拒绝了权限请求，并在权限请求系统对话框中选择了 `Don't ask again` 选项，此方法将返回 false。如果设备规范禁止应用具有该权限，此方法也会返回 false。

# 请求您需要的权限

如果应用尚无所需的权限，则应用必须调用一个 requestPermissions() 方法，以请求适当的权限。应用将传递其所需的权限，以及您指定用于识别此权限请求的整型请求代码。此方法异步运行：它会立即返回，并且在用户响应对话框之后，系统会使用结果调用应用的回调方法，将应用传递的相同请求代码传递到 requestPermissions()。

以下代码可以检查应用是否具备读取用户联系人的权限，并根据需要请求该权限：

```
// Here, thisActivity is the current activity
if (ContextCompat.checkSelfPermission(thisActivity,
                Manifest.permission.READ_CONTACTS)
        != PackageManager.PERMISSION_GRANTED) {

    // Should we show an explanation?
    if (ActivityCompat.shouldShowRequestPermissionRationale(thisActivity,
            Manifest.permission.READ_CONTACTS)) {

        // Show an expanation to the user *asynchronously* -- don't block
        // this thread waiting for the user's response! After the user
        // sees the explanation, try again to request the permission.

    } else {

        // No explanation needed, we can request the permission.

        ActivityCompat.requestPermissions(thisActivity,
                new String[]{Manifest.permission.READ_CONTACTS},
                MY_PERMISSIONS_REQUEST_READ_CONTACTS);

        // MY_PERMISSIONS_REQUEST_READ_CONTACTS is an
        // app-defined int constant. The callback method gets the
        // result of the request.
    }
}
```

注：当您的应用调用 requestPermissions() 时，系统将向用户显示一个标准对话框。您的应用**无法配置**或更改此对话框。如果您需要为用户提供任何信息或解释，您应在调用 `requestPermissions()` **之前**进行，如解释应用为什么需要权限中所述。

# 处理权限请求响应

当应用请求权限时，系统将向用户显示一个对话框。当用户响应时，系统将调用应用的 `onRequestPermissionsResult()` 方法，向其传递用户响应。您的应用必须替换该方法，以了解是否已获得相应权限。回调会将您传递的相同请求代码传递给 requestPermissions()。例如，如果应用请求 READ_CONTACTS 访问权限，则它可能采用以下回调方法：

```
@Override
public void onRequestPermissionsResult(int requestCode,
        String permissions[], int[] grantResults) {
    switch (requestCode) {
        case MY_PERMISSIONS_REQUEST_READ_CONTACTS: {
            // If request is cancelled, the result arrays are empty.
            if (grantResults.length > 0
                && grantResults[0] == PackageManager.PERMISSION_GRANTED) {

                // permission was granted, yay! Do the
                // contacts-related task you need to do.

            } else {

                // permission denied, boo! Disable the
                // functionality that depends on this permission.
            }
            return;
        }

        // other 'case' lines to check for other
        // permissions this app might request
    }
}
```

系统显示的对话框说明了您的应用需要访问的权限组；它不会列出具体权限。例如，如果您请求 `READ_CONTACTS` 权限，系统对话框只显示您的应用需要访问设备的联系人。用户只需要为每个权限组授予一次权限。如果您的应用请求**该组中的任何其他权限**（已在您的应用清单中列出），系统将**自动授予**应用这些权限。当您请求此权限时，系统会调用您的 `onRequestPermissionsResult()` 回调方法，并传递 PERMISSION_GRANTED，如果用户已通过系统对话框明确同意您的权限请求，系统将采用相同方式操作。

**注**：您的应用仍需要明确请求其需要的每项权限，即使用户已向应用授予该权限组中的其他权限。此外，**权限分组在将来的 Android 版本中可能会发生变化**。您的代码不应依赖特定权限属于或不属于相同组这种假设。

例如，假设您在应用清单中列出了 READ_CONTACTS 和 WRITE_CONTACTS。如果您请求 READ_CONTACTS 且用户授予了此权限，那么，当您请求 WRITE_CONTACTS 时，系统将立即授予您该权限，不会与用户交互。

如果用户拒绝了某项权限请求，您的应用应采取适当的操作。例如，您的应用可能显示一个对话框，解释它为什么无法执行用户已经请求但需要该权限的操作。

当系统要求用户授予权限时，用户可以选择指示系统不再要求提供该权限。这种情况下，无论应用在什么时候使用 requestPermissions() 再次要求该权限，系统都会立即拒绝此请求。系统会调用您的 onRequestPermissionsResult() 回调方法，并传递 PERMISSION_DENIED，如果用户再次明确拒绝了您的请求，系统将采用相同方式操作。这意味着当您调用 requestPermissions() 时，您不能假设已经发生与用户的任何直接交互。

# 权限最佳做法

用如果一味要求用户提供授权，可能会让用户无所适从。如果用户发现应用难以使用，或者担心应用会滥用其信息，他们可能不愿意使用该应用，甚至会将其完全卸载。以下最佳做法有助于避免此类糟糕的用户体验。

## 考虑使用 intent

许多情况下，您可以使用以下两种方式之一来让您的应用执行某项任务。您可以将应用设置为要求提供权限才能执行操作。或者，您可以将应用设置为使用 intent，让其他应用来执行任务。

例如，假设应用需要使用设备相机才能够拍摄照片。应用可以请求 CAMERA 权限，以便允许其直接访问相机。然后，应用将使用 Camera API 控制相机并拍摄照片。利用此方法，您的应用能够完全控制摄影过程，并支持您将相机 UI 整合至应用中。

不过，如果您无需此类完全控制，则可以使用 ACTION_IMAGE_CAPTURE intent 来请求图像。发送该 intent 时，系统会提示用户选择相机应用（如果没有默认相机应用）。用户使用选定的相机应用拍摄照片，该相机应用会将照片返回给应用的 onActivityResult() 方法。

同样，如果您需要拨打电话、访问用户的联系人或要执行其他操作，可以通过**创建适当的 intent** 来完成，或者您也可以请求相应的权限并直接访问相应的对象。每种方法各有优缺点。

### 两种方法的比较:

**如果使用权限**：

- 您的应用可在您执行操作时完全控制用户体验。不过，如此广泛的控制会增加任务的复杂性，因为您需要设计适当的 UI。
- 系统会在运行或安装应用时各提示用户提供一次权限（具体取决于用户的 Android 版本）。之后，应用即可执行操作，不再需要用户进行其他交互。不过，**如果用户不授予权限（或稍后撤销权限），您的应用将根本无法执行操作**。

**如果使用 intent**：

- 您无需为操作设计 UI。处理 intent 的应用将提供 UI。不过，这意味着您无法控制用户体验。用户可能与您从未见过的应用交互。
- 如果用户没有适用于操作的默认应用，则系统会提示用户选择一款应用。如果用户未指定默认处理程序，则他们每次执行此操作时都必须处理一个额外对话框。

## 仅要求您需要的权限

每次您要求权限时，实际上是在强迫用户作出决定。您应尽量减少提出这些请求的次数。如果用户运行的是 Android 6.0（API 级别 23）或更高版本，则每次用户尝试要求提供权限的新应用功能时，应用都必须中断用户的操作并发起权限请求。如果用户运行的是较早版本的 Android，则在安装应用时需要为应用的每一权限请求给予授权；如果列表过长或看起来不合适，用户可能会决定不安装该应用。为此，您应尽量减少应用需要的权限数。

例如，很多情况下应用可以通过使用 intent 来避免请求权限。如果某项功能并非应用的核心功能，不妨考虑将相关工作交给其他应用来执行，如考虑使用 intent 中所述。

## 不要让用户感到无所适从

如果用户运行的是 Android 6.0（API 级别 23）或更高版本，则用户**必须在应用运行时为其授权**。如果您的应用一次要求用户提供多项权限，用户可能会感到无所适从并因此退出应用。您应根据需要请求权限。

某些情况下，一项或多项权限可能是应用所必需的。在这种情况下，合理的做法是，在应用启动之后立即要求提供这些权限。例如，如果您运行摄影应用，应用需要访问设备的相机。在用户首次启动应用时，他们不会对提供相机使用权限的要求感到惊讶。但是，如果同一应用还具备与用户联系人共享照片的功能，您不应在应用首次启动时要求用户提供 READ_CONTACTS 权限，而应等到用户尝试使用“共享”功能之后，再要求提供该权限。

如果应用提供了教程，则合理的做法是，在教程结束时请求提供应用的必要权限。

## 解释需要权限的原因

系统在您调用 `requestPermissions()` 时显示的权限对话框将说明应用需要的权限，但不会解释为何需要这些权限。某些情况下，用户可能会感到困惑。因此，最好在调用 `requestPermissions()` **之前**向用户解释应用需要相应权限的原因。

例如，摄影应用可能需要使用位置服务，以便能够为照片添加地理标签。通常，用户可能不了解照片能够包含位置信息，并且对摄影应用想要了解具体位置感到不解。因此在这种情况下，应用最好在调用 requestPermissions() 之前告知用户此功能的相关信息。

告知用户的一种办法是将这些请求纳入应用教程。这样，教程可以依次显示应用的每项功能，并在显示每项功能时解释需要哪些相应的权限。例如，摄影应用的教程可以演示其“与您的联系人共享照片”功能，然后告知用户需要为应用授予权限才能查看用户的联系人。然后，应用可以调用 requestPermissions()，要求用户提供该访问权限。当然，并非所有用户都会按照教程操作，因此您仍需在应用的正常操作期间检查和请求权限。

## 测试两种权限模式

从 Android 6.0（API 级别 23）开始，用户是在运行时而不是在应用安装时授予或撤销应用权限。因此，您应在多种不同条件下测试应用。在低于 Android 6.0 的版本中，您可以认为如果应用得到运行，它就可以得到在应用清单中声明的全部权限。在新的权限模式中，这一推断不再成立。

以下提示可帮助您识别在运行 API 级别 23 或更高级别的设备上与权限有关的代码问题：

- 识别应用的当前权限和相关的代码路径。
- 在各种受权限保护的服务和数据中测试用户流程。
- 使用授予或撤销权限的各种组合进行测试。例如，相机应用可能会在清单中列出 `CAMERA`、`READ_CONTACTS` 和 `ACCESS_FINE_LOCATION`。您应在测试应用时逐一打开和关闭这些权限，确保应用可以妥善处理所有权限配置。**请记住，自 Android 6.0 起，用户可以打开或关闭任何应用的权限，即使面向 API 级别 22 或更低级别的应用也是如此**。
- 使用 adb 工具从命令行管理权限：
    按组列出权限和状态:
    `$ adb shell pm list permissions -d -g`
    授予或撤销一项或多项权限：
    `$ adb shell pm [grant|revoke] <permission-name> ...`
- 针对使用权限的服务对应用进行分析。

谷歌官方demo：

https://github.com/googlesamples/android-RuntimePermissions
