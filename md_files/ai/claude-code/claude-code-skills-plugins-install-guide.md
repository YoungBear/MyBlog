# Claude Code 插件和技能安装指南

## 安装方式概述

### 方式1：Marketplace 安装（推荐）

```bash
# 添加市场（github owner/repo 格式）
/plugin marketplace add owner/repo

# 安装技能
/plugin install skill-name@marketplace-name
```

### 方式2：Marketplace 安装（SSH 格式）

```bash
# 添加市场（SSH格式）
/plugin marketplace add git@github.com:owner/repo.git

# 安装技能
/plugin install skill-name@marketplace-name
```

### 方式3：从源码安装

```bash
# 克隆仓库
git clone https://github.com/owner/repo.git

# 从本地路径安装
/plugin install skill-name@/absolute/path/to/local/repo
```

### 方式4：直接指定 GitHub URL

```bash
/plugin install skill-name@github:owner/repo
```

---

## 一、Superpowers 系列技能

GitHub: [https://github.com/superpowers](https://github.com/superpowers)

Superpowers 是一套 Claude Code 开发流程最佳实践技能集。

### 1. brainstorming - 头脑风暴

**仓库**: superpowers/brainstorming

**功能**: 在进行创意工作（创建功能、构建组件、添加功能或修改行为）之前，必须使用此技能。探索用户意图、需求和设计。

**安装**:
```bash
/plugin marketplace add superpowers/superpowers
/plugin install brainstorming@superpowers
```

### 2. writing-plans - 编写计划

**仓库**: superpowers/writing-plans

**功能**: 当有规范或需求的多步骤任务时，在编写代码之前使用。帮助制定实施计划。

**安装**:
```bash
/plugin install writing-plans@superpowers
```

### 3. executing-plans - 执行计划

**仓库**: superpowers/executing-plans

**功能**: 执行实施计划，管理和协调各个步骤。

**安装**:
```bash
/plugin install executing-plans@superpowers
```

### 4. receiving-code-review - 接收代码审查

**仓库**: superpowers/receiving-code-review

**功能**: 在实现建议之前接收代码审查反馈，特别是当反馈不清晰或技术上存疑时。需要技术严谨性和验证，而不是盲目接受。

**安装**:
```bash
/plugin install receiving-code-review@superpowers
```

### 5. requesting-code-review - 请求代码审查

**仓库**: superpowers/requesting-code-review

**功能**: 在完成任务、实现主要功能或合并之前验证工作是否满足要求。

**安装**:
```bash
/plugin install requesting-code-review@superpowers
```

### 6. systematic-debugging - 系统化调试

**仓库**: superpowers/systematic-debugging

**功能**: 在遇到任何错误、测试失败或意外行为时使用。进行系统性调试分析。

**安装**:
```bash
/plugin install systematic-debugging@superpowers
```

### 7. test-driven-development - 测试驱动开发

**仓库**: superpowers/test-driven-development

**功能**: 实现任何功能或错误修复时，在编写实现代码之前使用 TDD 方法。

**安装**:
```bash
/plugin install test-driven-development@superpowers
```

### 8. finishing-a-development-branch - 完成开发分支

**仓库**: superpowers/finishing-a-development-branch

**功能**: 当完成功能分支开发时使用，确保所有工作正确完成。

**安装**:
```bash
/plugin install finishing-a-development-branch@superpowers
```

### 9. subagent-driven-development - 子代理驱动开发

**仓库**: superpowers/subagent-driven-development

**功能**: 在当前会话中执行具有独立任务的实施计划。

**安装**:
```bash
/plugin install subagent-driven-development@superpowers
```

### 10. verification-before-completion - 完成前验证

**仓库**: superpowers/verification-before-completion

**功能**: 在宣布任务完成之前进行验证检查。

**安装**:
```bash
/plugin install verification-before-completion@superpowers
```

### 11. using-git-worktrees - 使用 Git Worktrees

**仓库**: superpowers/using-git-worktrees

**功能**: 在开始需要与当前工作空间隔离的功能开发之前使用，确保存在隔离的工作空间。

**安装**:
```bash
/plugin install using-git-worktrees@superpowers
```

### 12. dispatching-parallel-agents - 并行代理分发

**仓库**: superpowers/dispatching-parallel-agents

**功能**: 当面临 2 个或更多可以无共享状态或顺序依赖地工作的独立任务时使用。

**安装**:
```bash
/plugin install dispatching-parallel-agents@superpowers
```

### 13. using-superpowers - 使用 Superpowers

**仓库**: superpowers/using-superpowers

**功能**: 介绍如何使用技能的基础技能。

**安装**:
```bash
/plugin install using-superpowers@superpowers
```

### 14. writing-skills - 编写技能

**仓库**: superpowers/writing-skills

**功能**: 创建和编写新的 Claude Code 技能。

**安装**:
```bash
/plugin install writing-skills@superpowers
```

---

## 二、UI/UX 相关技能

### ui-ux-pro-max

**仓库**: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

**功能**: 网页和移动端 UI/UX 设计智能。包含 50+ 样式、161 调色板、57 字体搭配、161 产品类型、99 UX 指南和 25 种图表类型。覆盖 React、Next.js、Vue、Svelte、SwiftUI、React Native、Flutter、Tailwind、shadcn/ui 和 HTML/CSS 等技术栈。

**安装**:

方法1 - Marketplace:
```bash
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

方法2 - SSH:
```bash
/plugin marketplace add git@github.com:nextlevelbuilder/ui-ux-pro-max-skill.git
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

### frontend-design

**仓库**: nextlevelbuilder/frontend-design-skill

**功能**: 创建独特、 production-grade 的前端界面，具有高设计质量。用于构建网页组件、页面或应用程序。

**安装**:
```bash
/plugin marketplace add nextlevelbuilder/frontend-design-skill
/plugin install frontend-design@frontend-design-skill
```

---

## 三、代码审查相关技能

### code-review

**仓库**: nextlevelbuilder/code-review-skill

**功能**: 审查 Pull Request 是否符合项目指南、风格规范和最佳实践。

**安装**:
```bash
/plugin marketplace add nextlevelbuilder/code-review-skill
/plugin install code-review@code-review-skill
```

### review-pr

**仓库**: pr-review-toolkit/review-pr

**功能**: 使用专业代理进行全面的 PR 审查。

**安装**:
```bash
/plugin marketplace add pr-review-toolkit/review-pr
/plugin install review-pr@pr-review-toolkit
```

---

## 四、其他常用技能

### skill-creator

**官方技能**: Anthropic 官方提供的技能创建工具

**功能**: 创建新的 Claude Code 技能。

**安装**:
```bash
/plugin install skill-creator
```

### update-config

**功能**: 配置 Claude Code 的 settings.json，包括权限、环境变量、钩子等。

**安装**:
```bash
/plugin install update-config@superpowers
```

### keybindings-help

**功能**: 自定义键盘快捷键、重新绑定按键、添加和弦绑定等。

**安装**:
```bash
/plugin install keybindings-help@superpowers
```

### simplify

**功能**: 审查更改的代码以实现复用性、质量和效率，然后修复发现的问题。

**安装**:
```bash
/plugin install simplify@superpowers
```

### fewer-permission-prompts

**功能**: 扫描常见只读 Bash 和 MCP 工具调用，然后添加到项目 .claude/settings.json 的允许列表中以减少权限提示。

**安装**:
```bash
/plugin install fewer-permission-prompts@superpowers
```

### loop

**功能**: 按固定间隔重复运行提示或斜杠命令（如每 5 分钟检查一次部署）。

**安装**:
```bash
/plugin install loop@superpowers
```

### claude-api

**仓库**: anthropics/claude-api-sdk

**功能**: 构建、调试和优化 Claude API / Anthropic SDK 应用。使用提示缓存。

**安装**:
```bash
/plugin marketplace add anthropics/claude-api-sdk
/plugin install claude-api@claude-api-sdk
```

### init

**功能**: 初始化新的 CLAUDE.md 文件，包含代码库文档。

**安装**:
```bash
/plugin install init@superpowers
```

### security-review

**功能**: 安全审查，检查代码中的安全漏洞。

**安装**:
```bash
/plugin install security-review@superpowers
```

---

## 五、Marketplace 管理命令

```bash
# 列出已添加的市场
/plugin marketplace list

# 安装技能
/plugin install skill-name@marketplace

# 卸载技能
/plugin uninstall skill-name

# 搜索技能
/plugin search keyword
```

---

## 六、一键安装所有 Superpowers

如果想安装所有 Superpowers 技能：

```bash
# 添加 superpowers 市场
/plugin marketplace add superpowers/superpowers

# 依次安装各个技能
/plugin install brainstorming@superpowers
/plugin install writing-plans@superpowers
/plugin install executing-plans@superpowers
/plugin install receiving-code-review@superpowers
/plugin install requesting-code-review@superpowers
/plugin install systematic-debugging@superpowers
/plugin install test-driven-development@superpowers
/plugin install finishing-a-development-branch@superpowers
/plugin install subagent-driven-development@superpowers
/plugin install verification-before-completion@superpowers
/plugin install using-git-worktrees@superpowers
/plugin install dispatching-parallel-agents@superpowers
/plugin install using-superpowers@superpowers
/plugin install writing-skills@superpowers
```
