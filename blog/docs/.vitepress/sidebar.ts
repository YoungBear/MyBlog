import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const DOCS = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')

const GROUPS: { label: string; dirs: string[] }[] = [
  { label: 'AI 与模型', dirs: ['ai', 'deepseek'] },
  { label: 'Java', dirs: ['java', 'kotlin'] },
  { label: 'Android', dirs: ['android', 'baidu', 'greendao'] },
  { label: '后端', dirs: ['spring-boot', 'mysql', 'redis'] },
  { label: '运维与网络', dirs: ['linux', 'docker', 'kubernetes', 'nginx', 'communication'] },
  { label: 'Python 与数据', dirs: ['python'] },
  { label: '工具与杂项', dirs: ['tools', 'windows', 'config', 'onomastion', 'others'] },
  { label: '面试', dirs: ['interview'] },
  { label: '历史文章', dirs: ['legacy'] }
]

const DIR_LABELS: Record<string, string> = {
  ai: 'AI 与模型', android: 'Android', baidu: '百度地图',
  communication: '网络通信', config: '配置', deepseek: 'DeepSeek',
  docker: 'Docker', greendao: 'GreenDAO', interview: '面试',
  java: 'Java', kotlin: 'Kotlin', kubernetes: 'Kubernetes',
  linux: 'Linux', mysql: 'MySQL', nginx: 'nginx',
  onomastion: '命名学', others: '其他', python: 'Python 与数据分析',
  redis: 'Redis', 'spring-boot': 'Spring Boot', tools: '工具与杂项',
  windows: 'Windows', legacy: '历史文章'
}

interface Item { text: string; link?: string; items?: Item[]; collapsed?: boolean }

function readMeta(file: string): { title: string; date: string } {
  let text = ''
  try { text = fs.readFileSync(file, 'utf-8') } catch { return { title: '', date: '' } }
  const title = text.match(/^title:\s*(.+)$/m)?.[1]?.trim().replace(/^["']|["']$/g, '') ?? ''
  const date = text.match(/^date:\s*(\S+)/m)?.[1] ?? ''
  return { title, date }
}

function scanDir(dir: string): Item[] {
  const abs = path.join(DOCS, dir)
  const items: { item: Item; date: string }[] = []
  for (const name of fs.readdirSync(abs).sort()) {
    const p = path.join(abs, name)
    const stat = fs.statSync(p)
    if (stat.isDirectory()) {
      const sub = scanDir(path.join(dir, name))
      const idx = fs.existsSync(path.join(p, 'index.md')) ? `/${dir}/${name}/` : undefined
      if (sub.length || idx) items.push({ item: { text: name, link: idx, items: sub, collapsed: true }, date: '9999' })
    } else if (name.endsWith('.md') && name !== 'index.md') {
      const rel = path.join(dir, name).replace(/\.md$/, '')
      const { title, date } = readMeta(p)
      items.push({ item: { text: title || name.replace(/\.md$/, '').replace(/-/g, ' '), link: `/${rel}` }, date })
    }
  }
  return items.sort((a, b) => (a.date === b.date ? 0 : a.date < b.date ? 1 : -1)).map(x => x.item)
}

export function getSidebar(): Item[] {
  return GROUPS.filter(g => g.dirs.some(d => fs.existsSync(path.join(DOCS, d)))).map(g => ({
    text: g.label,
    collapsed: false,
    items: g.dirs.filter(d => fs.existsSync(path.join(DOCS, d))).map(d => ({
      text: DIR_LABELS[d] ?? d,
      link: `/${d}/`,
      items: scanDir(d),
      collapsed: true
    }))
  }))
}
