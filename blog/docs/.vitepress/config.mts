import { defineConfig } from 'vitepress'

export default defineConfig({
  base: process.env.BASE || '/',
  lang: 'zh-CN',
  title: "YoungBear's Blog",
  description: 'YoungBear 的技术博客',
  cleanUrls: true,
  themeConfig: {
    nav: [{ text: '首页', link: '/' }],
    sidebar: []
  }
})
