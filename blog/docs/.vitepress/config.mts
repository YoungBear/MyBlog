import { defineConfig } from 'vitepress'
import { getSidebar } from './sidebar'

export default defineConfig({
  base: process.env.BASE || '/',
  lang: 'zh-CN',
  title: "YoungBear's Blog",
  description: 'YoungBear 的技术博客',
  cleanUrls: true,
  // 保留此行：nginx 等文章中的 localhost 示例链接在构建时不应被当作死链
  ignoreDeadLinks: 'localhostLinks',
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      {
        text: '分类',
        items: [
          { text: 'AI 与模型', items: [{ text: 'AI 与模型', link: '/ai/' }, { text: 'DeepSeek', link: '/deepseek/' }] },
          { text: 'Java', items: [{ text: 'Java', link: '/java/' }, { text: 'Kotlin', link: '/kotlin/' }] },
          { text: 'Android', items: [{ text: 'Android', link: '/android/' }, { text: '百度地图', link: '/baidu/' }, { text: 'GreenDAO', link: '/greendao/' }] },
          { text: '后端', items: [{ text: 'Spring Boot', link: '/spring-boot/' }, { text: 'MySQL', link: '/mysql/' }, { text: 'Redis', link: '/redis/' }] },
          { text: '运维与网络', items: [{ text: 'Linux', link: '/linux/' }, { text: 'Docker', link: '/docker/' }, { text: 'Kubernetes', link: '/kubernetes/' }, { text: 'nginx', link: '/nginx/' }, { text: '网络通信', link: '/communication/' }] },
          { text: 'Python 与数据', items: [{ text: 'Python 与数据分析', link: '/python/' }] },
          { text: '工具与杂项', items: [{ text: '工具与杂项', link: '/tools/' }, { text: 'Windows', link: '/windows/' }, { text: '配置', link: '/config/' }, { text: '命名学', link: '/onomastion/' }, { text: '其他', link: '/others/' }] },
          { text: '面试', items: [{ text: '面试', link: '/interview/' }] }
        ]
      },
      { text: '历史文章', link: '/legacy/' },
      { text: 'GitHub', link: 'https://github.com/YoungBear/MyBlog' }
    ],
    sidebar: getSidebar(),
    search: { provider: 'local' },
    outline: { level: [2, 3] },
    docFooter: { prev: '上一篇', next: '下一篇' },
    lastUpdated: { text: '最后更新' }
  },
  lastUpdated: true
})
