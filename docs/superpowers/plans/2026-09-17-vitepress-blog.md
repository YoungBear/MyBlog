# VitePress 博客系统实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 MyBlog 仓库改造为 VitePress 博客站点：全部文章迁入 `blog/docs/`，GitHub Actions 自动双部署到自有 Linux 服务器（主）与 GitHub Pages（备）。

**Architecture:** 站点代码与文章同仓共存于 `blog/` 目录（`docs/` 为 VitePress 文档根）。一个 Python 迁移脚本完成「git mv + 文件名短横线化 + frontmatter 日期注入 + 链接/图片路径改写 + 分类索引生成」。CI 监听 master push（`blog/**` 路径），构建两份产物（服务器 base `/`、Pages base `/MyBlog/`）分别部署。

**Tech Stack:** VitePress 1.6.4（精确版本）、Node 20（本机 v20.20.2）、Python 3.12（迁移脚本）、GitHub Actions、nginx。

## Global Constraints

- **分支**：所有工作在新分支 `feature/blog-vitepress` 上进行，验收后合回 master；合回后 master push 触发自动部署
- **提交格式**（用户既有规范，每次提交必须遵守）：
  ```
  [add|update|fix] <简短描述>

  Co-Authored-By: MiniMax-M2.7-highspeed <noreply@anthropic.com>
  ```
- **VitePress 版本精确锁定** `1.6.4`（npm 最新版；Node ≥ 18，本机 Node v20.20.2 ✅）
- **目录约定**：站点项目根 = `blog/`；文档根 = `blog/docs/`；图片 = `blog/docs/pngs/`（非 public 目录，用相对路径引用）；`files/` 目录**保留在仓库根**（文章中指向它的 GitHub blob 链接依赖该路径，不迁移）
- **Pages base** = `/MyBlog/`（仓库 YoungBear/MyBlog）；服务器 base = `/`（通过 `BASE` 环境变量双构建）
- **一切迁移用 `git mv`** 保留历史；文件名统一短横线；根目录旧文章全部进 `legacy/` 不做主题归类；旧文章外链图床（CSDN）链接保持原样不修复
- **部署前提**（用户需准备的 secrets，见 Task 5 清单）：`SSH_HOST`、`SSH_USER`、`SSH_PRIVATE_KEY`、`DEPLOY_PATH`
- 仓库当前实际文章数：**140 篇**（md_files 97 + 根目录 40 + English 3），迁移后 `blog/docs/` 下 .md 总数 = 140 + 23 个分类索引 + 1 个首页 = **164**（用于验证断言）

---

## File Structure

```
blog/                                  # 站点项目根（新增）
├── package.json                       # 依赖与构建脚本
├── package-lock.json                  # npm install 生成
├── new-post.sh                        # 新文章脚手架（Task 4）
├── scripts/
│   └── migrate.py                     # 一次性迁移脚本（Task 2）
├── deploy/
│   └── nginx-myblog.conf              # 服务器 nginx 配置样例（Task 5）
├── dist/                              # 构建产物（gitignore，CI 用）
└── docs/                              # VitePress 文档根
    ├── index.md                       # 站点首页（Task 1 占位 / Task 3 完成）
    ├── .vitepress/
    │   ├── config.mts                 # 站点配置：nav、base、search（Task 1 最小 / Task 3 完整）
    │   └── sidebar.ts                 # 自动扫描分类生成侧边栏（Task 3）
    ├── pngs/                          # 原 pngs/ 整体迁入（Task 2）
    ├── public/                        # 静态资源（AllZoneIds.txt 迁入，Task 2）
    ├── legacy/                        # 43 篇旧文章归档（Task 2）
    ├── ai/ java/ android/ ...         # 原 md_files 分类目录（Task 2，约 22 个）
    └── <每个分类>/index.md            # 分类索引页（Task 2 生成，new-post.sh 维护）

.github/workflows/
└── deploy.yml                         # 双部署工作流（Task 5）

根目录（改造后）：blog/  files/  README.md  CLAUDE.md  LICENSE.txt  .github/  .gitignore
```

分类导航分组（9 组，侧边栏与顶部「分类」下拉共用）：

| 导航组 | 目录 |
|--------|------|
| AI 与模型 | ai, deepseek |
| Java | java, kotlin |
| Android | android, baidu, greendao |
| 后端 | spring-boot, mysql, redis |
| 运维与网络 | linux, docker, kubernetes, nginx, communication |
| Python 与数据 | python |
| 工具与杂项 | tools, windows, config, onomastion, others |
| 面试 | interview |
| 历史文章 | legacy |

---

## Task 0: 创建分支并提交本计划

**Files:**
- Create: `docs/superpowers/plans/2026-09-17-vitepress-blog.md`（本文件，已存在）

- [ ] **Step 1: 创建分支**

```bash
git checkout -b feature/blog-vitepress
```

- [ ] **Step 2: 提交计划文档**

```bash
git add docs/superpowers/plans/2026-09-17-vitepress-blog.md
git commit -m "$(cat <<'EOF'
[add] add vitepress blog implementation plan

Co-Authored-By: MiniMax-M2.7-highspeed <noreply@anthropic.com>
EOF
)"
```

---

## Task 1: 站点脚手架

**Files:**
- Create: `blog/package.json`
- Create: `blog/docs/index.md`（占位首页）
- Create: `blog/docs/.vitepress/config.mts`（最小配置）
- Modify: `.gitignore`

**Interfaces:**
- Produces: `blog/package.json` 的 scripts 被 Task 2/3/4/5 使用；`config.mts` 的 `process.env.BASE` 机制被 Task 5 的 CI 双构建使用

- [ ] **Step 1: 创建 package.json**

`blog/package.json`：

```json
{
  "name": "myblog",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "docs:dev": "vitepress dev docs",
    "docs:build": "vitepress build docs",
    "docs:preview": "vitepress preview docs",
    "build:server": "BASE='/' vitepress build docs --outDir dist/server",
    "build:pages": "BASE='/MyBlog/' vitepress build docs --outDir dist/pages"
  },
  "devDependencies": {
    "vitepress": "1.6.4"
  }
}
```

- [ ] **Step 2: 创建最小 config.mts**

`blog/docs/.vitepress/config.mts`：

```ts
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
```

- [ ] **Step 3: 创建占位首页**

`blog/docs/index.md`：

```markdown
# YoungBear's Blog

网站建设中。
```

- [ ] **Step 4: 更新 .gitignore**

`.gitignore` 追加：

```
node_modules/
blog/dist/
blog/docs/.vitepress/cache/
blog/docs/.vitepress/dist/
```

- [ ] **Step 5: 安装依赖并验证**

```bash
cd blog && npm install
npm run docs:build
```

预期：`build complete` 成功退出，产物在 `blog/docs/.vitepress/dist/`。

- [ ] **Step 6: 本地 dev 验证**

```bash
npm run docs:dev -- --port 5199
```

另开终端：`curl -s http://localhost:5199/ | grep -i "YoungBear"` 有输出后 Ctrl-C 停掉 dev server。

- [ ] **Step 7: 提交**

```bash
git add blog/package.json blog/package-lock.json blog/docs/index.md blog/docs/.vitepress/config.mts .gitignore
git commit -m "$(cat <<'EOF'
[add] scaffold vitepress site with minimal config

Co-Authored-By: MiniMax-M2.7-highspeed <noreply@anthropic.com>
EOF
)"
```

---

## Task 2: 迁移脚本与全部内容迁移

**Files:**
- Create: `blog/scripts/migrate.py`（完整代码见 Step 1）
- 迁移结果：`blog/docs/` 下 22 个分类目录 + `legacy/` + `pngs/` + `public/` + 23 个分类索引页

**Interfaces:**
- Consumes: Task 1 的 `blog/docs/`（脚本写往该目录）
- Produces: 全部文章新路径（供 Task 3 侧边栏扫描）；每篇 frontmatter 含 `title`/`date`（Task 3 排序、Task 4 模板同构）；分类索引页 `<!-- POSTS -->` 标记（Task 4 的 new-post.sh 依赖）

- [ ] **Step 1: 编写迁移脚本**

`blog/scripts/migrate.py`：

```python
#!/usr/bin/env python3
"""MyBlog 文章迁移：git mv + 短横线化 + frontmatter 注入 + 链接/图片改写 + 分类索引生成。

用法:
  python3 blog/scripts/migrate.py --dry-run   # 仅打印迁移计划并校验冲突
  python3 blog/scripts/migrate.py             # 执行迁移
"""
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DOCS = ROOT / 'blog' / 'docs'
PNGS_NEW = DOCS / 'pngs'

# 目录重命名/合并（md_files 内相对目录 → 新相对目录，最长前缀匹配）
DIR_RENAMES = {
    'Kotlin': 'kotlin',
    'SpringBoot': 'spring-boot',
    'DataAnalysis': 'python',
    'Kubernetes': 'kubernetes',
    'Others': 'others',
    'java/IDEA': 'java/idea',
    'java/JavaPatternReadme': 'java/java-pattern-readme',
    'java/Math': 'java/math',
    'python/md_files': 'python',
}

# md_files 根级散落文件 → 目标分类
LOOSE_FILES = {
    'AndroidTest.md': 'android',
    'Communication.md': 'communication',
    'FileProvider.md': 'android',
    'GitCommandLearn.md': 'tools',
    'GitHub_API.md': 'tools',
    'ListContainsPerformance.md': 'java',
    'ProguardLearn.md': 'android',
    'RecyclerViewLearn.md': 'android',
}

NAME_OVERRIDES = {'AndroidInterView.md': 'android-interview.md'}

CATEGORY_NAMES = {
    'ai': 'AI 与模型', 'android': 'Android', 'baidu': '百度地图',
    'communication': '网络通信', 'config': '配置', 'deepseek': 'DeepSeek',
    'docker': 'Docker', 'greendao': 'GreenDAO', 'interview': '面试',
    'java': 'Java', 'kotlin': 'Kotlin', 'kubernetes': 'Kubernetes',
    'linux': 'Linux', 'mysql': 'MySQL', 'nginx': 'nginx',
    'onomastion': '命名学', 'others': '其他', 'python': 'Python 与数据分析',
    'redis': 'Redis', 'spring-boot': 'Spring Boot', 'tools': '工具与杂项',
    'windows': 'Windows', 'legacy': '历史文章',
}

ROOT_EXCLUDE = {'CLAUDE.md', 'README.md', 'LICENSE.txt'}
GITHUB_BLOB = re.compile(
    r'https://github\.com/YoungBear/MyBlog/blob/master/(md_files|files)/(.+?\.md)')


def kebab(name: str) -> str:
    name = re.sub(r'\.md$', '', name).replace('_', '-')
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', name)
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1-\2', s)
    return s.lower()


def git_created_date(path: Path) -> str:
    out = subprocess.run(
        ['git', 'log', '--follow', '--format=%cs', '--diff-filter=A', '--', str(path)],
        cwd=ROOT, capture_output=True, text=True)
    lines = out.stdout.strip().splitlines()
    return lines[-1] if lines else ''


def apply_dir_renames(rel_dir: str) -> str:
    for old, new in sorted(DIR_RENAMES.items(), key=lambda kv: -len(kv[0])):
        if rel_dir == old or rel_dir.startswith(old + '/'):
            return new + rel_dir[len(old):]
    return rel_dir


def new_rel_for(old: Path) -> str:
    """返回新路径（相对 blog/docs，不含 .md 扩展）。"""
    if old.parent == ROOT or old.parent.name == 'English':
        name = NAME_OVERRIDES.get(old.name, kebab(old.name))
        return f'legacy/{name}'
    rel = old.relative_to(ROOT / 'md_files')
    parts = rel.parts
    if len(parts) == 1:
        cat = LOOSE_FILES[old.name]
        name = NAME_OVERRIDES.get(old.name, kebab(old.name))
        return f'{cat}/{name}'
    if parts[-1] == 'README.md':
        return f'{apply_dir_renames("/".join(parts[:-1]))}/index'
    return f'{apply_dir_renames("/".join(parts[:-1]))}/{kebab(parts[-1])}'


def collect_articles():
    items = []
    for p in sorted(ROOT.glob('*.md')):
        if p.name in ROOT_EXCLUDE:
            continue
        items.append(p)
    items += sorted((ROOT / 'English').glob('*.md'))
    items += sorted((ROOT / 'md_files').rglob('*.md'))
    mapping = {str(p.relative_to(ROOT)): new_rel_for(p) for p in items}
    assert len(mapping) == len(set(mapping.values())), '新路径存在冲突，请检查 NAME_OVERRIDES'
    return mapping


def extract_title(text: str, fallback: str) -> str:
    m = re.search(r'^title:\s*(.+)$', text, re.M)
    if m:
        return m.group(1).strip().strip('"\'')
    m = re.search(r'^#\s+(.+)$', text, re.M)
    if m:
        return m.group(1).strip()
    return fallback


def rewrite_content(text: str, old_path: Path, new_rel: str,
                    mapping: dict) -> str:
    # 1. 图片相对路径：任意层级的 ../pngs/ → 从新文件位置到 docs/pngs 的相对路径
    new_dir = DOCS / os.path.dirname(new_rel)
    img_rel = os.path.relpath(PNGS_NEW, new_dir)
    text = re.sub(r'\((?:\.\./)+pngs/', f'({img_rel}/', text)

    # 2. GitHub blob 链接（md_files 前缀）→ 站点内部链接；files/ 前缀保持不动
    def blob_repl(m):
        if m.group(1) == 'files':
            return m.group(0)
        old_rel = f'md_files/{m.group(2)}'
        target = mapping.get(old_rel)
        return f'](/{target})' if target else m.group(0)
    text = GITHUB_BLOB.sub(blob_repl, text)

    # 3. 相对 .md 链接 → 站点内部链接（按旧路径查映射）
    def mdlink_repl(m):
        target = m.group(1)
        if target.startswith(('http', '#')):
            return m.group(0)
        resolved = (old_path.parent / target).resolve()
        try:
            old_rel = str(resolved.relative_to(ROOT))
        except ValueError:
            return m.group(0)
        new_target = mapping.get(old_rel)
        return f'](/{new_target})' if new_target else m.group(0)
    text = re.sub(r'\]\(([^)]+\.md[^)]*)\)', mdlink_repl, text)

    # 4. frontmatter：已有则补 date，没有则前置
    date = git_created_date(old_path)
    if text.startswith('---\n'):
        head_end = text.find('\n---', 4)
        if head_end != -1:
            head = text[4:head_end]
            if not re.search(r'^date:', head, re.M) and date:
                text = text[:4] + f'date: {date}\n' + text[4:]
            return text
    title = extract_title(text, os.path.basename(new_rel).replace('-', ' ').title())
    fm = '---\n'
    fm += f'title: {title}\n'
    if date:
        fm += f'date: {date}\n'
    fm += 'tags: []\n---\n\n'
    return fm + text


def generate_indexes():
    today = subprocess.run(['date', '+%F'], capture_output=True,
                           text=True).stdout.strip()
    for cat_dir in sorted(p for p in DOCS.iterdir()
                          if p.is_dir() and p.name not in ('.vitepress', 'pngs', 'public')):
        entries = []
        for f in sorted(cat_dir.rglob('*.md')):
            if f.name == 'index.md':
                continue
            rel = f.relative_to(DOCS)
            text = f.read_text(encoding='utf-8')
            date = re.search(r'^date:\s*(\S+)', text, re.M)
            title = extract_title(text, f.stem.replace('-', ' ').title())
            entries.append((date.group(1) if date else '', str(rel.with_suffix('')), title))
        entries.sort(key=lambda e: e[0], reverse=True)  # 日期降序，无日期排最后
        lines = [f'- [{t}](/{r})' + (f' — {d}' if d else '')
                 for d, r, t in entries]
        index = cat_dir / 'index.md'
        cat_name = CATEGORY_NAMES.get(cat_dir.name, cat_dir.name)
        index.write_text(
            f'---\ntitle: {cat_name}\ndate: {today}\ntags: []\n---\n\n'
            f'# {cat_name}\n\n<!-- POSTS -->\n\n' + '\n'.join(lines) + '\n',
            encoding='utf-8')


def main():
    dry = '--dry-run' in sys.argv
    mapping = collect_articles()
    print(f'共 {len(mapping)} 篇文章')
    for old, new in sorted(mapping.items()):
        print(f'  {old}  ->  {new}')
    if dry:
        return

    moved = 0
    for old_s, new_rel in sorted(mapping.items()):
        old_p = Path(old_s)
        new_p = DOCS / f'{new_rel}.md'
        new_p.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(['git', 'mv', str(old_p), str(new_p)], cwd=ROOT, check=True)
        text = new_p.read_text(encoding='utf-8')
        new_p.write_text(rewrite_content(text, old_p, new_rel, mapping),
                         encoding='utf-8')
        moved += 1
    print(f'git mv 完成 {moved} 篇')

    # 图片与数据文件
    subprocess.run(['git', 'mv', 'pngs', str(PNGS_NEW)], cwd=ROOT, check=True)
    (DOCS / 'public' / 'java').mkdir(parents=True, exist_ok=True)
    subprocess.run(['git', 'mv', 'md_files/java/datetime/AllZoneIds.txt',
                    str(DOCS / 'public' / 'java' / 'AllZoneIds.txt')],
                   cwd=ROOT, check=True)

    generate_indexes()
    # 清理空的旧目录（git 不跟踪空目录）
    for d in ('md_files', 'pngs', 'English'):
        subprocess.run(['rm', '-rf', str(ROOT / d)], check=True)
    print('迁移完成')


if __name__ == '__main__':
    main()
```

- [ ] **Step 2: Dry-run 校验**

```bash
python3 blog/scripts/migrate.py --dry-run
```

预期：打印 140 行 `旧路径 -> 新路径`，无断言错误（新路径冲突会在此暴露）。抽查：`legacy/` 共 43 篇（40 根目录 + 3 English）、`md_files/SpringBoot/SpringBoot-9-MultipyEnv.md -> spring-boot/spring-boot-9-multipy-env`、`md_files/python/md_files/geopy.md -> python/geopy`。

- [ ] **Step 3: 执行迁移**

```bash
python3 blog/scripts/migrate.py
```

预期：输出 `git mv 完成 140 篇` 与 `迁移完成`。

- [ ] **Step 4: 结构断言**

```bash
find blog/docs -name '*.md' | wc -l
```

预期：`164`（140 文章 + 23 分类索引 + 1 首页）。若不符，停下检查 `git status`。

- [ ] **Step 5: 链接残留检查**

```bash
grep -rn '(\.\./)+pngs/' blog/docs && echo "FAIL: 仍有旧图片路径" || echo OK
grep -rn 'github.com/YoungBear/MyBlog/blob/master/md_files' blog/docs && echo "FAIL: 仍有旧 GitHub 链接" || echo OK
grep -rn '](\./SpringBoot-' blog/docs && echo "FAIL: 仍有旧相对链接" || echo OK
```

预期：三条 `OK`。`md_files` 作为纯文字出现在正文中（非链接）是允许的，上面只检查链接形态。

- [ ] **Step 6: 图片引用完整性校验**

```bash
cd blog/docs && python3 - <<'EOF'
import re, sys
from pathlib import Path
missing = []
for f in Path('.').rglob('*.md'):
    for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)', f.read_text(encoding='utf-8')):
        src = m.group(1)
        if src.startswith(('http', '/', '#')):
            continue
        if not (f.parent / src).resolve().exists():
            missing.append((str(f), src))
print('\n'.join(f'{f}: {s}' for f, s in missing) if missing else 'ALL OK')
sys.exit(1 if missing else 0)
EOF
```

预期：`ALL OK`（外链图床 http 开头不检查；`/` 开头是 Task 3 配置后才出现的链接，此时应没有）。

- [ ] **Step 7: 构建验证**

```bash
cd blog && npm run docs:build
```

预期：`build complete`，构建产物含 164 个页面；无死链报错（VitePress 构建时对失效的内部 md 链接会报 dead link，若有则按报错修正对应文件后重跑）。

- [ ] **Step 8: 预览冒烟**

```bash
cd blog && npm run docs:preview -- --port 5199
```

另开终端验证页面可访问（HTTP 200 + 内容抽查）：

```bash
curl -s -o /dev/null -w '%{http_code}\n' http://localhost:5199/legacy/why-write-blog   # 预期 200
curl -s http://localhost:5199/nginx/ | grep -q "nginx" && echo OK                        # 分类索引页
curl -s http://localhost:5199/ai/claude-code/claude-code-install-guide | grep -q "Claude" && echo OK
```

预期：`200` + 两条 `OK`（legacy 文章标题可能是中文，故只查状态码）。验证后停掉 preview。

- [ ] **Step 9: 提交**

```bash
git add -A blog/ .gitignore
git status  # 确认删除项包含 md_files/ pngs/ English/，新增项包含 blog/docs/
git commit -m "$(cat <<'EOF'
[update] migrate all 140 articles into blog/docs with kebab-case names and frontmatter

Co-Authored-By: MiniMax-M2.7-highspeed <noreply@anthropic.com>
EOF
)"
```

---

## Task 3: 站点配置、自动侧边栏与首页

**Files:**
- Modify: `blog/docs/.vitepress/config.mts`（完整版）
- Create: `blog/docs/.vitepress/sidebar.ts`
- Modify: `blog/docs/index.md`（正式首页）

**Interfaces:**
- Consumes: Task 2 生成的目录结构与 frontmatter（`title`/`date`）
- Produces: `sidebar.ts` 导出的 `getSidebar()` 供 config.mts 使用；导航分组定义与 Task 2 的 CATEGORY_NAMES 一致

- [ ] **Step 1: 编写 sidebar.ts**

`blog/docs/.vitepress/sidebar.ts`：

```ts
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
  const title = text.match(/^title:\s*(.+)$/m)?.[1]?.trim() ?? ''
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
```

- [ ] **Step 2: 编写完整 config.mts**

覆盖 `blog/docs/.vitepress/config.mts`：

```ts
import { defineConfig } from 'vitepress'
import { getSidebar } from './sidebar'

export default defineConfig({
  base: process.env.BASE || '/',
  lang: 'zh-CN',
  title: "YoungBear's Blog",
  description: 'YoungBear 的技术博客',
  cleanUrls: true,
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
```

- [ ] **Step 3: 编写正式首页**

覆盖 `blog/docs/index.md`：

```markdown
---
title: YoungBear's Blog
date: 2026-09-17
---

# YoungBear's Blog

技术学习笔记与博客：Java、Android、Spring Boot、Linux、Docker、Kubernetes、AI 等。

- 通过顶部「分类」菜单或左侧边栏浏览全部文章
- 「历史文章」归档了 2016-2019 年的早期笔记（部分图床外链可能失效）
- 本站由 [VitePress](https://vitepress.dev) 构建，文章源文件在 [GitHub 仓库](https://github.com/YoungBear/MyBlog) 中

## 写新文章

```bash
cd blog
./new-post.sh <分类目录名> <文章标题>
npm run docs:dev   # 本地预览
git push           # 推送到 master 即自动发布
```
```

- [ ] **Step 4: 构建验证**

```bash
cd blog && npm run docs:build
```

预期：`build complete` 成功。若有 dead link 报错，按报错修正后重跑。

- [ ] **Step 5: 双 base 构建验证**

```bash
cd blog && npm run build:server && npm run build:pages
```

预期：`blog/dist/server/` 与 `blog/dist/pages/` 各自构建成功。抽查 Pages 产物 HTML 中资源前缀为 `/MyBlog/`：

```bash
grep -o 'src="/MyBlog/[^"]*"' dist/pages/ai/index.html | head -1
grep -o 'href="/MyBlog/legacy/[^"]*"' dist/pages/index.html | head -1
```

预期：各有输出（说明 base 生效）。另抽查服务器产物不含 `/MyBlog/` 前缀：

```bash
grep -c 'src="/MyBlog/' dist/server/ai/index.html
```

预期：`0`。

- [ ] **Step 6: 提交**

```bash
git add blog/docs/.vitepress/ blog/docs/index.md
git commit -m "$(cat <<'EOF'
[update] add auto sidebar, nav groups and homepage

Co-Authored-By: MiniMax-M2.7-highspeed <noreply@anthropic.com>
EOF
)"
```

---

## Task 4: 新文章脚手架 new-post.sh

**Files:**
- Create: `blog/new-post.sh`

**Interfaces:**
- Consumes: Task 2 生成的分类索引页中的 `<!-- POSTS -->` 标记
- Produces: 分类目录下带 frontmatter 模板的新文章 + 索引页自动插入链接

- [ ] **Step 1: 编写脚本**

`blog/new-post.sh`：

```bash
#!/usr/bin/env bash
# 用法: ./new-post.sh <分类目录名> <文章标题> [英文slug]
# 示例: ./new-post.sh java "Java 日期时间用法"
set -euo pipefail
cd "$(dirname "$0")"

CAT="${1:?用法: ./new-post.sh <分类目录名> <文章标题> [英文slug]}"
TITLE="${2:?缺少标题}"
SLUG="${3:-}"
DATE=$(date +%F)

if [ -z "$SLUG" ]; then
  if [[ "$TITLE" =~ ^[A-Za-z0-9\ _-]+$ ]]; then
    SLUG=$(echo "$TITLE" | tr 'A-Z ' 'a-z-' | tr -s '-')
  else
    SLUG="$DATE"
  fi
fi

FILE="docs/$CAT/$SLUG.md"
mkdir -p "docs/$CAT"

cat > "$FILE" <<EOF
---
title: $TITLE
date: $DATE
tags: []
---

# $TITLE

EOF

if [ -f "docs/$CAT/index.md" ]; then
  LINK="- [$TITLE](/$CAT/$SLUG) — $DATE"
  sed -i "/<!-- POSTS -->/a\\
$LINK" "docs/$CAT/index.md"
fi

echo "已创建: $FILE"
echo "本地预览: npm run docs:dev"
```

- [ ] **Step 2: 赋予执行权限并测试**

```bash
chmod +x blog/new-post.sh
./new-post.sh ai "脚手架测试文章" test-post
```

预期输出：`已创建: docs/ai/test-post.md`。检查：

```bash
cat blog/docs/ai/test-post.md
grep -A1 '<!-- POSTS -->' blog/docs/ai/index.md
```

预期：frontmatter 含 `title: 脚手架测试文章`、`date: <今天>`；索引页 `<!-- POSTS -->` 下一行是 `- [脚手架测试文章](/ai/test-post) — <今天>`。

- [ ] **Step 3: 清理测试文章**

```bash
rm blog/docs/ai/test-post.md
git checkout -- blog/docs/ai/index.md
```

（索引页未被 commit 前用 checkout 还原；若已 commit 则手工删掉插入行后再 add。）

- [ ] **Step 4: 提交**

```bash
git add blog/new-post.sh
git commit -m "$(cat <<'EOF'
[add] add new-post.sh scaffold for writing new articles

Co-Authored-By: MiniMax-M2.7-highspeed <noreply@anthropic.com>
EOF
)"
```

---

## Task 5: GitHub Actions 双部署与 nginx 配置

**Files:**
- Create: `.github/workflows/deploy.yml`
- Create: `blog/deploy/nginx-myblog.conf`

**Interfaces:**
- Consumes: Task 1 的 `build:server` / `build:pages` scripts（`BASE` 环境变量）；Task 2 的产物结构
- Produces: master push（`blog/**`）自动双部署；`nginx-myblog.conf` 供服务器一次性配置

- [ ] **Step 1: 编写工作流**

`.github/workflows/deploy.yml`：

```yaml
name: Deploy

on:
  push:
    branches: [master]
    paths: ['blog/**']
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - name: Install dependencies
        run: npm ci
        working-directory: blog
      - name: Build for server (base /)
        run: npm run build:server
        working-directory: blog
      - name: Build for GitHub Pages (base /MyBlog/)
        run: npm run build:pages
        working-directory: blog
      - name: Upload server artifact
        uses: actions/upload-artifact@v4
        with:
          name: server-dist
          path: blog/dist/server
      - name: Upload pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: blog/dist/pages

  deploy-pages:
    needs: build
    if: github.ref == 'refs/heads/master'
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4

  deploy-server:
    needs: build
    if: github.ref == 'refs/heads/master'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: server-dist
          path: dist
      - uses: webfactory/ssh-agent@v0.9.0
        with:
          ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}
      - name: Deploy via rsync
        run: |
          mkdir -p ~/.ssh
          ssh-keyscan -H "${{ secrets.SSH_HOST }}" >> ~/.ssh/known_hosts
          rsync -az --delete dist/ "${{ secrets.SSH_USER }}@${{ secrets.SSH_HOST }}:${{ secrets.DEPLOY_PATH }}"
```

- [ ] **Step 2: 编写 nginx 配置样例**

`blog/deploy/nginx-myblog.conf`：

```nginx
# 放到服务器 /etc/nginx/conf.d/myblog.conf 后 nginx -s reload
server {
    listen 80;
    server_name _;               # 有域名时改为你的域名

    root /var/www/myblog;        # 与 GitHub Actions secrets 中 DEPLOY_PATH 一致
    index index.html;

    location / {
        try_files $uri $uri/ $uri.html /404.html;
    }

    # 可选：gzip
    gzip on;
    gzip_types text/plain text/css application/javascript application/json image/svg+xml;
}
```

- [ ] **Step 3: 准备清单（需用户一次性操作，不写代码）**

在仓库 Settings → Secrets and variables → Actions 添加 4 个 secrets：
- `SSH_HOST`：服务器公网 IP 或域名
- `SSH_USER`：SSH 用户（如 root）
- `SSH_PRIVATE_KEY`：可登录该服务器的私钥（对应公钥已加入服务器 `~/.ssh/authorized_keys`）
- `DEPLOY_PATH`：部署目录，如 `/var/www/myblog`

在服务器上一次性执行：

```bash
mkdir -p /var/www/myblog
# 安装 nginx 后，把 blog/deploy/nginx-myblog.conf 放入 /etc/nginx/conf.d/ 并 nginx -s reload
# 可选：certbot --nginx 配置 HTTPS
```

GitHub 仓库 Settings → Pages → Source 选择 **GitHub Actions**（一次性）。

- [ ] **Step 4: 验证工作流语法**

```bash
ruby -e "require 'yaml'; YAML.load_file('.github/workflows/deploy.yml'); puts 'YAML OK'"
```

预期：`YAML OK`。（无 ruby 则用 `python3 -c "import yaml,sys; yaml.safe_load(open('.github/workflows/deploy.yml')); print('YAML OK')"`，PyYAML 不可用时跳过，靠 Task 7 首次运行验证。）

- [ ] **Step 5: 分支上试跑（可选但推荐）**

push 本分支后在 Actions 页面手动触发 `Deploy` workflow（`workflow_dispatch`）。预期：`build` 成功、两个部署 job 因 `if: github.ref == 'refs/heads/master'` 跳过——这验证了构建链路。**注意**：Pages 部署只会在 master 上真实发生，此试跑不会影响任何线上环境。

- [ ] **Step 6: 提交**

```bash
git add .github/workflows/deploy.yml blog/deploy/nginx-myblog.conf
git commit -m "$(cat <<'EOF'
[add] add dual-deploy workflow to server and GitHub Pages

Co-Authored-By: MiniMax-M2.7-highspeed <noreply@anthropic.com>
EOF
)"
```

---

## Task 6: 更新 README.md 与 CLAUDE.md

**Files:**
- Modify: `README.md`（整体重写）
- Modify: `CLAUDE.md`（整体重写）

- [ ] **Step 1: 重写 README.md**

覆盖 `README.md`：

```markdown
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
```

- [ ] **Step 2: 重写 CLAUDE.md**

覆盖 `CLAUDE.md`：

```markdown
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
```

- [ ] **Step 3: 提交**

```bash
git add README.md CLAUDE.md
git commit -m "$(cat <<'EOF'
[update] rewrite README and CLAUDE.md for the vitepress blog structure

Co-Authored-By: MiniMax-M2.7-highspeed <noreply@anthropic.com>
EOF
)"
```

---

## Task 7: 验收、合并 master 与首次部署

**Files:** 无新代码。删除 `docs/superpowers/plans/`（合并前询问用户）。

- [ ] **Step 1: 用户验收清单（在分支上）**

```bash
cd blog && npm run docs:dev
```

请用户逐项确认：首页正常、分类下拉可点、侧边栏分类完整、抽查 3-5 篇文章（含 1 篇 legacy、1 篇含图片的文章、1 篇原 SpringBoot 系列含互链的文章）链接与图片正常。用户确认后继续。

- [ ] **Step 2: 推送分支并合并**

```bash
git push -u origin feature/blog-vitepress
```

若用户希望在 GitHub 上用 PR 合并则到此为止等用户操作；本地合并则：

```bash
git checkout master
git merge --no-ff feature/blog-vitepress -m "$(cat <<'EOF'
[update] launch vitepress blog site with dual deployment

Co-Authored-By: MiniMax-M2.7-highspeed <noreply@anthropic.com>
EOF
)"
git push origin master
```

- [ ] **Step 3: 验证首次部署**

1. GitHub Actions 页面确认 `Deploy` workflow 三个 job 全绿
2. 服务器验证：`curl -s http://<SSH_HOST>/ | grep -i YoungBear` 有输出
3. Pages 验证：浏览器打开 `https://youngbear.github.io/MyBlog/` 正常（首次启用 Pages 需等待约 1 分钟）

- [ ] **Step 4: 收尾**

询问用户后删除计划文档（可选）：

```bash
git rm -r docs/superpowers && git commit -m "[update] remove plan docs after launch"
```

（注意：本计划文件在 `docs/superpowers/` 下，位于 VitePress 文档根之外，不会被站点渲染。）

---

## Self-Review 记录

- **Spec 覆盖**：10 项锁定决策逐一映射——①新增目录维护站点→Task 1/2；②VitePress→全部任务；③自有服务器+Pages→Task 5；④Actions 双部署→Task 5/7；⑤139→140 篇全量迁移 git mv→Task 2；⑥目录布局与 pngs 迁入→Task 2（files/ 保留根目录系修复旧链接所需，已偏离原"根目录只剩 5 项"的表述并在 Task 2/6 注明）；⑦新分支→Task 0/7；⑧legacy 归档+短横线化→Task 2；⑨功能集（内置+日期注入）→Task 2/3；⑩写作工作流→Task 4/6
- **类型一致性**：`migrate.py` 生成 frontmatter 字段 `title`/`date`/`tags` 与 `sidebar.ts` 读取字段、`new-post.sh` 模板字段一致；`<!-- POSTS -->` 标记在 `generate_indexes()` 与 `new-post.sh` 中一致；`build:server`/`build:pages` 在 package.json 与 deploy.yml 中一致；base 值 `/MyBlog/` 在 config.mts、deploy.yml、Task 5 验证命令中一致
- **占位符扫描**：无 TBD；secrets 名（SSH_HOST 等）是用户提供的外部输入，非代码占位
