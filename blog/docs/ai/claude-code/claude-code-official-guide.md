---
title: "Claude Code 官方使用指南"
date: 2026-05-19
tags: []
---

# Claude Code 官方使用指南

本文档总结 Anthropic 官方提供的 Claude Code 内置功能、可安装技能和插件，并整理日常使用中的常用操作。

> 本文内容基于 Claude Code v2.1.x 整理，不同版本命令可能略有差异。

## 目录

- [一、常用操作](#一常用操作)
- [二、内置斜杠命令](#二内置斜杠命令)
- [三、内置工具](#三内置工具)
- [四、MCP 服务器配置](#四mcp-服务器配置)
- [五、官方配置选项](#五官方配置选项)
- [六、官方可安装技能](#六官方可安装技能)
- [七、官方可安装插件](#七官方可安装插件)
- [八、创建自定义技能](#八创建自定义技能)
- [九、获取帮助](#九获取帮助)
- [十、官方资源链接](#十官方资源链接)

---

## 一、常用操作

### 1. 查看历史会话

- 会话内输入 `/resume`，打开交互式选择器，列出当前目录的历史会话；支持输入会话 ID 或关键词搜索（如 `/resume auth-refactor`），也支持粘贴 PR 链接
- 会话记录保存在本地：`~/.claude/projects/<编码后的项目路径>/<session-id>.jsonl`（路径中的非字母数字字符会替换为 `-`）

### 2. 继续上一次会话

| 命令 | 说明 |
|------|------|
| `claude -c`（`--continue`） | 继续当前目录最近一次会话 |
| `claude -r`（`--resume`） | 打开会话选择器；`claude -r <session-id>` 恢复指定会话 |
| `claude --from-pr <PR 号或链接>` | 恢复创建某个 PR 的会话 |
| `claude --fork-session` | 恢复会话时创建新的会话 ID（分支恢复，原会话不变），与 `-c`/`-r` 配合使用 |

### 3. 会话命名

- `claude -n <名称>`：启动时给会话命名（显示在提示框、`/resume` 选择器和终端标题）
- `/rename`：重命名当前会话

### 4. 回退到检查点

- `/rewind`：打开回退菜单，将对话或代码恢复到之前的检查点；输入框为空时双击 `Esc` 也可触发
- 支持恢复 `/clear` 之前的会话内容

### 5. 导出会话

- `/export`：将当前会话保存为文本文件或复制到剪贴板
- `/export <文件名>`：直接保存到指定文件（自动追加 `.txt` 后缀）

### 6. 上下文管理

| 命令 | 说明 |
|------|------|
| `/clear` | 清空当前上下文（会话记录文件仍保留） |
| `/compact` | 压缩上下文，在上下文窗口内继续对话 |
| `/context` | 查看上下文窗口占用情况 |
| `Ctrl+O` | 展开/收起完整对话记录（含详细思考过程） |

### 7. 会话统计

| 命令 | 说明 |
|------|------|
| `/status` | 查看设置、版本、模型、账号信息 |
| `/cost` | 查看当前会话的 Token 用量和费用 |
| `/usage` | 查看套餐和速率限制使用情况 |

### 8. 聊天内快捷操作

| 操作 | 说明 |
|------|------|
| `@文件路径` | 引用文件或目录（支持 Tab 补全），如 `@src/main.py` |
| `!命令` | 内联执行 Shell 命令；`` !`命令` `` 将命令输出注入提示词 |
| `/memory` | 编辑 CLAUDE.md 记忆文件（旧的 `#` 快捷方式已弃用） |

### 9. 键盘快捷键

| 快捷键 | 说明 |
|--------|------|
| `Esc Esc` | 输入框有内容时清空草稿；为空时打开回退（rewind）菜单 |
| `Shift+Tab` | 切换权限模式（default → acceptEdits → plan → 自定义），连按两次进入计划模式 |
| `Ctrl+C` | 中断当前操作（再次按下退出） |
| `Ctrl+D` | 退出 Claude Code |
| `?` | 查看当前会话快捷键面板 |

### 10. 无头模式（脚本/管道）

```bash
# 非交互执行并退出
claude -p "解释这个函数的作用"

# 从管道读取
cat error.log | claude -p "分析这个日志"

# JSON 输出
claude -p "列出所有 TODO" --output-format json
```

常用参数：`--output-format text|json|stream-json`、`--max-turns`、`--allowedTools`

### 11. 常用 CLI 启动参数

| 参数 | 说明 |
|------|------|
| `-c, --continue` | 继续当前目录最近一次会话 |
| `-r, --resume [id]` | 恢复会话（打开选择器或指定会话 ID） |
| `-n, --name <名称>` | 为会话设置显示名称 |
| `-p, --print` | 非交互模式，输出后退出 |
| `--model <模型>` | 指定模型（如 `sonnet`、`opus`） |
| `--from-pr [PR]` | 恢复创建某 PR 的会话 |
| `--fork-session` | 分支恢复会话（与 `-c`/`-r` 配合） |
| `--permission-mode <模式>` | 权限模式（default/acceptEdits/plan/bypassPermissions） |
| `--add-dir <目录>` | 添加工具可访问的额外目录 |
| `--dangerously-skip-permissions` | 跳过所有权限检查（仅建议在无网络的沙箱中使用） |
| `--mcp-config <文件>` | 从 JSON 文件加载 MCP 服务器 |
| `--settings <文件或 JSON>` | 加载额外设置 |
| `-w, --worktree [名称]` | 在 Git worktree 中启动会话 |
| `-v, --version` | 查看版本 |

### 12. 更新与认证

```bash
claude update       # 检查并安装新版本
claude install      # 安装指定版本，如 claude install 2.1.140
claude doctor       # 检查安装健康状态
claude auth login   # 登录认证（会话内可用 /auth login）
```

---

## 二、内置斜杠命令

Claude Code 官方内置的常用斜杠命令（在会话中输入 `/` 可查看完整列表）：

| 命令 | 功能 |
|------|------|
| `/help` | 获取帮助，查看所有命令 |
| `/clear` | 清除当前会话上下文 |
| `/compact` | 压缩当前上下文 |
| `/config` | 配置 Claude Code 设置 |
| `/model` | 切换模型 |
| `/resume` | 查看/恢复历史会话 |
| `/rewind` | 回退到历史检查点 |
| `/export` | 导出当前会话 |
| `/rename` | 重命名当前会话 |
| `/status` | 查看状态信息 |
| `/cost` | 查看 Token 用量和费用 |
| `/usage` | 查看套餐使用情况 |
| `/context` | 查看上下文窗口占用 |
| `/memory` | 编辑 CLAUDE.md 记忆文件 |
| `/permissions` | 配置工具权限规则 |
| `/add-dir` | 添加额外工作目录 |
| `/hooks` | 配置 Hooks |
| `/vim` | 切换 Vim 键位模式 |
| `/theme` | 选择主题 |
| `/agents` | 管理子代理 |
| `/todos` | 查看任务列表 |
| `/doctor` | 检查安装健康状态 |
| `/mcp` | 管理 MCP 服务器 |
| `/auth` | 管理认证（登录/登出） |
| `/update` | 检查软件更新 |
| `/upgrade` | 升级 Max 套餐 |
| `/init` | 初始化 CLAUDE.md（官方内置技能） |
| `/plugin` | 管理插件 |

> 注：`/review`、`/security-review`、`/test`、`/search` 等命令来自已安装的插件或自定义技能，并非官方内置命令；不同环境的可用命令不同，可用 `/help` 查看当前环境的完整列表。

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

## 四、MCP 服务器配置

Claude Code 通过 MCP（Model Context Protocol）扩展工具能力。官方不内置任何 MCP 服务器，需要自行连接第三方 MCP 服务器。

### 配置方式一：命令行（推荐）

```bash
# 添加到当前项目（写入 .mcp.json）
claude mcp add <名称> -- <命令> <参数>

# 示例：添加 filesystem 服务器
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem ~/Documents

# 添加到用户级（所有项目可用）
claude mcp add --scope user <名称> -- <命令> <参数>

# 查看/删除
claude mcp list
claude mcp remove <名称>
```

会话内可用 `/mcp` 管理已连接的服务器。

### 配置方式二：项目 .mcp.json

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"]
    }
  }
}
```

### 配置方式三：settings.json（用户级）

在 `~/.claude/settings.json` 中配置 `mcpServers`，格式与上述 `.mcp.json` 相同。

---

## 五、官方配置选项

### 模型选择

```bash
/model opus    # 最强模型（当前为 Opus 4.7）
/model sonnet  # 平衡模型（当前为 Sonnet 4.6）
/model haiku   # 快速模型（当前为 Haiku 4.5）
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

完整插件列表请参考：[Claude Code 官方插件完整列表](/ai/claude-code/claude-code-official-plugins)

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
# 查看所有命令和快捷键
/help

# 查看当前会话快捷键面板
?
```

---

## 十、官方资源链接

- [Claude Code 官方文档](https://code.claude.com/docs)
- [交互模式](https://code.claude.com/docs/en/interactive-mode)
- [会话管理](https://code.claude.com/docs/en/sessions)
- [CLI 参考](https://code.claude.com/docs/en/cli-reference)
- [什么是技能？](https://support.claude.com/en/articles/12512176-what-are-skills)
- [在 Claude 中使用技能](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [创建自定义技能](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Agent Skills 规范](https://agentskills.io)
- [Skills API 快速入门](https://docs.claude.com/en/api/skills-guide#creating-a-skill)
