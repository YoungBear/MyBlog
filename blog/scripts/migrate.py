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

# 注意：override 的值不含 .md 扩展（kebab() 会剥离，override 不会）
NAME_OVERRIDES = {
    'AndroidInterView.md': 'android-interview',
    # md_files 根级旧副本与 md_files/java/ 下新版同名，旧副本加 -old 后缀避免路径冲突
    'ListContainsPerformance.md': 'list-contains-performance-old',
}

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

# 历史链接笔误修复：旧 URL 指向的路径不存在，实际文章在别处（迁移时顺带修正为有效站内链接）
URL_ALIASES = {
    'md_files/python/geopy.md': 'md_files/python/md_files/geopy.md',
}


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


def yaml_quote(s: str) -> str:
    """将字符串写成 YAML 双引号标量。

    必要性：部分标题以 YAML 指示符开头（如 `[Demo源代码地址][6]` 的 '['、
    `` `insert` 语句 `` 的反引号），未加引号时 frontmatter 解析失败，构建中断。
    """
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


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
    # 注意：正则只匹配 URL 本身（不含外层的 ](...)），故只替换 URL，保留原有链接语法
    def blob_repl(m):
        if m.group(1) == 'files':
            return m.group(0)
        old_rel = f'md_files/{m.group(2)}'
        old_rel = URL_ALIASES.get(old_rel, old_rel)
        target = mapping.get(old_rel)
        return f'/{target}' if target else m.group(0)
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
    fm += f'title: {yaml_quote(title)}\n'
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
            f'---\ntitle: {yaml_quote(cat_name)}\ndate: {today}\ntags: []\n---\n\n'
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
