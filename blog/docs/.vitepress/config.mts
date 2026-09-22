import { defineConfig } from 'vitepress'

export default defineConfig({
  base: process.env.BASE || '/',
  lang: 'zh-CN',
  title: "YoungBear's Blog",
  description: 'YoungBear 的技术博客',
  cleanUrls: true,
  // nginx-https 等文章正文中出现的 http(s)://localhost:PORT 是示例地址（非站内链接），
  // VitePress 默认会把它当作站内页面检查并报 dead link
  ignoreDeadLinks: 'localhostLinks',
  themeConfig: {
    nav: [{ text: '首页', link: '/' }],
    sidebar: []
  }
})
