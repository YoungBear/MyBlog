# Claude Code 官方使用指南

本文档总结 Anthropic 官方提供的 Claude Code 内置功能、可安装技能和插件。

---

## 一、内置命令

Claude Code 内置以下命令，无需安装即可使用：

| 命令 | 功能 |
|------|------|
| `/review` | 审查 Pull Request |
| `/security-review` | 安全审查，检查代码中的安全漏洞 |
| `/init` | 初始化新的 CLAUDE.md 文件 |
| `/test` | 为代码编写和运行测试 |
| `/search` | 在代码库中搜索符号、文件或内容 |
| `/grep` | 在代码库中搜索特定文本模式 |
| `/edit` | 编辑特定文件或代码段 |
| `/read` | 读取并分析文件内容 |
| `/glob` | 使用 glob 模式搜索文件 |
| `/bash` | 执行 Shell 命令 |

### 使用示例

```bash
/review
/security-review
/init
/test
/search query
/grep pattern
/edit file.md
/read file.md
/glob **/*.md
/bash command
```

---

## 二、内置斜杠命令（Slash Commands）

| 命令 | 功能 |
|------|------|
| `/help` | 获取帮助信息 |
| `/clear` | 清除当前会话 |
| `/compact` | 压缩当前上下文 |
| `/config` | 配置 Claude Code 设置 |
| `/model` | 切换模型 |
| `/scientist` | 以科学家模式运行 |
| `/web` | 启用网页搜索 |

---

## 三、内置工具（Tools）

Claude Code 内置以下工具，可直接使用：

| 工具 | 功能 |
|------|------|
| `Read` | 读取文件 |
| `Edit` | 编辑文件 |
| `Write` | 写入文件 |
| `Bash` | 执行 Shell 命令 |
| `Glob` | 文件模式匹配 |
| `Grep` | 文本搜索 |
| `WebFetch` | 获取网页内容 |
| `WebSearch` | 网页搜索 |
| `Agent` | 启动子代理 |
| `TaskCreate` | 创建任务列表 |
| `TaskList` | 列出任务 |
| `TaskGet` | 获取任务详情 |
| `TaskUpdate` | 更新任务状态 |
| `TaskOutput` | 获取任务输出 |
| `TaskStop` | 停止任务 |
| `EnterPlanMode` | 进入计划模式 |
| `ExitPlanMode` | 退出计划模式 |
| `EnterWorktree` | 进入 Git Worktree |
| `ExitWorktree` | 退出 Git Worktree |
| `AskUserQuestion` | 询问用户 |
| `ScheduleWakeup` | 调度唤醒 |
| `CronCreate` | 创建定时任务 |
| `CronDelete` | 删除定时任务 |
| `CronList` | 列出定时任务 |
| `Skill` | 调用技能 |
| `NotebookEdit` | 编辑 Jupyter Notebook |

---

## 四、内置 MCP 服务器

Claude Code 支持 MCP（Model Context Protocol）服务器扩展：

### 内置 MCP 工具

- `mcp__desktop-commander__run_command` - 运行命令
- `mcp__desktop-commander__run_safely` - 安全运行命令
- `mcp__filesystem__read_file` - 读取文件
- `mcp__filesystem__write_file` - 写入文件
- `mcp__filesystem__list_directory` - 列出目录
- `mcp__search__search` - 搜索
- `mcp__search__search_files` - 搜索文件
- `mcp__search__read_file` - 读取文件

### 配置 MCP 服务器

在 `~/.claude/settings.json` 中配置：

```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-name"]
    }
  }
}
```

---

## 五、官方配置选项

### 模型选择

```bash
/model opus  # 最强模型
/model sonnet  # 平衡模型
/model haiku  # 快速模型
```

### 设置修改

```bash
/config set theme dark
/config set model sonnet
```

---

## 六、官方可安装技能

**GitHub**: [https://github.com/anthropics/skills](https://github.com/anthropics/skills)

### 安装方式

```bash
# 添加官方市场
/plugin marketplace add anthropics/skills

# 安装技能
/plugin install 技能名称@anthropic-agent-skills
```

### 技能列表

#### 文档处理类

| 技能 | 功能 | 安装命令 |
|------|------|----------|
| docx | Word 文档（.docx）的创建、读取、编辑和操作 | `/plugin install docx@anthropic-agent-skills` |
| pdf | PDF 文件处理（读取、合并、拆分、水印、表单等） | `/plugin install pdf@anthropic-agent-skills` |
| pptx | PowerPoint 演示文稿（.pptx）处理 | `/plugin install pptx@anthropic-agent-skills` |
| xlsx | Excel 电子表格（.xlsx、.xlsm、.csv、.tsv）处理 | `/plugin install xlsx@anthropic-agent-skills` |

#### 文档协作类

| 技能 | 功能 | 安装命令 |
|------|------|----------|
| doc-coauthoring | 文档协作 | `/plugin install doc-coauthoring@anthropic-agent-skills` |
| internal-comms | 内部沟通 | `/plugin install internal-comms@anthropic-agent-skills` |

#### 设计类

| 技能 | 功能 | 安装命令 |
|------|------|----------|
| brand-guidelines | 品牌指南 | `/plugin install brand-guidelines@anthropic-agent-skills` |
| canvas-design | Canvas 设计 | `/plugin install canvas-design@anthropic-agent-skills` |
| frontend-design | 前端设计 | `/plugin install frontend-design@anthropic-agent-skills` |
| theme-factory | 主题工厂 | `/plugin install theme-factory@anthropic-agent-skills` |

#### 创意类

| 技能 | 功能 | 安装命令 |
|------|------|----------|
| algorithmic-art | 算法艺术 | `/plugin install algorithmic-art@anthropic-agent-skills` |
| slack-gif-creator | Slack GIF 创建 | `/plugin install slack-gif-creator@anthropic-agent-skills` |
| web-artifacts-builder | Web 工件构建 | `/plugin install web-artifacts-builder@anthropic-agent-skills` |

#### 开发工具类

| 技能 | 功能 | 安装命令 |
|------|------|----------|
| claude-api | Claude API 相关 | `/plugin install claude-api@anthropic-agent-skills` |
| mcp-builder | MCP 构建器 | `/plugin install mcp-builder@anthropic-agent-skills` |
| webapp-testing | Web 应用测试 | `/plugin install webapp-testing@anthropic-agent-skills` |
| skill-creator | 技能创建 | `/plugin install skill-creator@anthropic-agent-skills` |

#### 其他类

| 技能 | 功能 | 安装命令 |
|------|------|----------|
| playground | 操场 | `/plugin install playground@anthropic-agent-skills` |

### Skill Set 快速安装

```bash
# 文档技能集（包含 docx、pdf、pptx、xlsx）
/plugin install document-skills@anthropic-agent-skills

# 示例技能集（包含所有示例技能）
/plugin install example-skills@anthropic-agent-skills
```

---

## 七、官方可安装插件

**GitHub**: [https://github.com/anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

### 安装方式

```bash
# 添加官方市场
/plugin marketplace add anthropics/claude-plugins-official

# 安装插件
/plugin install 插件名称@claude-plugins-official
```

### 常用插件

| 插件 | 功能 | 安装命令 |
|------|------|----------|
| code-review | 使用多个专业代理进行自动代码审查 | `/plugin install code-review@claude-plugins-official` |
| pr-review-toolkit | 全面的 PR 审查代理 | `/plugin install pr-review-toolkit@claude-plugins-official` |
| frontend-design | 前端设计技能 | `/plugin install frontend-design@claude-plugins-official` |
| skill-creator | 创建和优化技能 | `/plugin install skill-creator@claude-plugins-official` |
| mcp-server-dev | MCP 服务器开发 | `/plugin install mcp-server-dev@claude-plugins-official` |
| security-guidance | 安全指导 | `/plugin install security-guidance@claude-plugins-official` |

### LSP 语言服务器

| 插件 | 安装命令 |
|------|----------|
| clangd-lsp | `/plugin install clangd-lsp@claude-plugins-official` |
| gopls-lsp | `/plugin install gopls-lsp@claude-plugins-official` |
| jdtls-lsp | `/plugin install jdtls-lsp@claude-plugins-official` |
| pyright-lsp | `/plugin install pyright-lsp@claude-plugins-official` |
| typescript-lsp | `/plugin install typescript-lsp@claude-plugins-official` |
| rust-analyzer-lsp | `/plugin install rust-analyzer-lsp@claude-plugins-official` |

完整插件列表请参考：[Claude Code 官方插件完整列表](./claude-code-official-plugins.md)

---

## 八、创建自定义技能

技能结构简单，只需一个包含 `SKILL.md` 文件的文件夹：

```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Add your instructions here that Claude will follow when this skill is active]

## Examples
- Example usage 1
- Example usage 2

## Guidelines
- Guideline 1
- Guideline 2
```

### Frontmatter 必需字段

- `name` - 唯一标识符（小写，中划线分隔）
- `description` - 完整的技能描述和使用场景

---

## 九、获取帮助

```bash
# 获取帮助
/help

# 查看所有命令
/help commands

# 查看所有技能
/help skills
```

---

## 十、官方资源链接

- [什么是技能？](https://support.claude.com/en/articles/12512176-what-are-skills)
- [在 Claude 中使用技能](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [创建自定义技能](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Agent Skills 规范](https://agentskills.io)
- [Skills API 快速入门](https://docs.claude.com/en/api/skills-guide#creating-a-skill)
