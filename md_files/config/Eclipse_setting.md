# eclipse 常用配置

## 1. 自动补全

**Windows->Preferences->Java->Editor->Content Assist**

将**Auto activation triggers for Java:** 后边的内容，将`.`改为`.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`

## 2. 保存自动格式化

**Windows->Preferences->Java->Editor->Save Actions**

选中**Perform the selected actions on save**和**Format source code**。

## 3. UTF-8编码及Unix文件格式

**Windows->Preferences->General->Workspace**

将底部的**Text file encoding**，不选择**Default**，而选择`Other->UTF-8`。

将**Next text file line delimiter**，不选择**Default**，而选择`Other->Unix`。

## 4. 空格替换Tab并显示空字符

**Windows->Preferences->General->Editors->Text Editors**

选中**Insert spaces for tabs** 和**show whitespace characters**。

**Windows->Preferences->Java->Code Style->Formatter**

编辑默认的profile，选择Indentation选项卡，将Tab policy的值改为`Spaces only`。

## 5. 文件浏览插件 Open Explorer

从github下载插件 [插件下载地址](https://github.com/samsonw/OpenExplorer/releases) `OpenExplorer_1.5.0.v201108051513.jar`

然后将.jar文件拷贝到eclipse安装目录下的`plugins`目录下，重启Eclipse即可生效。


