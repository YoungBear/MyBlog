# YoungBear's Blog

个人技术博客，由 [VitePress](https://vitepress.dev) 构建。

- 线上站点：https://youngbear.github.io/MyBlog/ （GitHub Pages，另有自有服务器部署）
- 文章源文件：本仓库 `blog/docs/` 目录，按分类组织

## 目录结构

- `blog/`：站点源码（VitePress 配置、构建脚本、新文章脚手架）
- `blog/docs/`：全部文章（分类目录 + `legacy/` 历史文章 + `pngs/` 图片）
- `files/`：支持文件（Eclipse 设置、proguard 规则、nginx 样例等）
- `.github/workflows/`：push 到 master 自动构建并部署到服务器与 GitHub Pages

## 写新文章

```bash
cd blog
./new-post.sh <分类目录名> <文章标题>
npm run docs:dev   # 本地预览 http://localhost:5173
```

确认无误后提交并推送，GitHub Actions 自动部署。

## 历史

- 2016-2019 年文章归档于 `blog/docs/legacy/`
- 2020-2026 年文章原位于 `md_files/`，2026-09 整体迁移至 `blog/docs/`
