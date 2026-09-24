# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 在此代码仓库中工作时提供指导。

## 概述

个人博客/学习笔记仓库：文章为 Markdown，由 VitePress 构建为静态站点，push 到 master 后 GitHub Actions 自动部署到自有 Linux 服务器（主）与 GitHub Pages（备）。

## 仓库结构

- **`blog/`**：站点项目根（package.json、new-post.sh、scripts/、deploy/）
- **`blog/docs/`**：全部文章，按分类目录组织（ai/、java/、android/、linux/、docker/、kubernetes/、nginx/、redis/、spring-boot/ 等）；`legacy/` 为历史文章归档（不再新增）；`pngs/` 存图片（文中用相对路径引用）；`public/` 存可下载静态文件
- **`blog/docs/.vitepress/`**：站点配置（config.mts 导航、sidebar.ts 自动侧边栏）
- **`files/`**：支持文件（Eclipse 设置、proguard 规则等），保持原位勿移动（文章中的 GitHub blob 链接指向此处）
- **`.github/workflows/deploy.yml`**：双部署工作流

## 写作与提交

- 新文章：`cd blog && ./new-post.sh <分类目录名> <文章标题>`，生成带 frontmatter（title/date/tags）的模板并自动登记到分类索引
- 新图片：放入 `blog/docs/pngs/<分类>/`，文中用相对路径引用
- 本地预览：`cd blog && npm run docs:dev`
- 提交风格：`[add|update|fix] <简短描述>`，每个 commit 末尾加 `Co-Authored-By: MiniMax-M2.7-highspeed <noreply@anthropic.com>`
- 发布：push 到 master 即自动部署；不要在 `legacy/` 下新增文章
