# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 在此代码仓库中工作时提供指导。

## 概述

这是一个个人博客/学习笔记仓库，包含各种技术主题的 Markdown 文件。仓库结构如下：

- **根目录**：包含主要主题文件及历史文章
- **`md_files/`**：按类别组织的结构化笔记（java/、android/、linux/、docker/、kubernetes/、nginx/、redis/、spring-boot/ 等）
- **`pngs/`**：博客文章中使用的图片
- **`files/`**：支持文件，包括配置示例和 Eclipse 设置

## 内容结构

`README.md` 是所有主题的索引。关键主题领域包括：

- **Java**：日期时间、线程（AsyncTask、Handler、ThreadPool）、JVM、设计模式（单例、装饰器、观察者）
- **Android**：Activity 生命周期、运行时权限、MVP、FileProvider、RecyclerView、LeakCanary、StrictMode
- **Linux**：grep、tar、sed、ps、find、openssl 命令
- **基础设施**：Docker、Kubernetes、nginx、redis
- **数据库**：MySQL、MyBatis
- **工具**：IntelliJ IDEA 快捷键、Eclipse 设置、adb 命令

## 在此仓库中工作

这是一个文档仓库——没有构建命令、测试或编译步骤。

添加新内容时：
- 使用清晰、有描述性的标题创建 Markdown 文件
- 将相关内容放置在适当的 `md_files/` 子目录中
- 按照现有模式在 `README.md` 索引中添加条目
- 图片放在 `pngs/` 目录中，使用有意义的名称

提交风格遵循格式：`[update|add|fix] <简短描述>`
