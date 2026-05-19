# Claude Code 官方插件指南

**GitHub**: [https://github.com/anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

## 安装方式

```bash
# 添加官方市场
/plugin marketplace add anthropics/claude-plugins-official

# 安装插件
/plugin install 插件名称@claude-plugins-official
```

---

## 插件列表

### 一、开发工具类

#### 1. code-review

**功能**: 使用多个专业代理进行自动代码审查，基于置信度评分

**安装**: `/plugin install code-review@claude-plugins-official`

#### 2. code-simplifier

**功能**: 代码简化和优化

**安装**: `/plugin install code-simplifier@claude-plugins-official`

#### 3. commit-commands

**功能**: Git 提交相关命令

**安装**: `/plugin install commit-commands@claude-plugins-official`

#### 4. feature-dev

**功能**: 功能开发工作流

**安装**: `/plugin install feature-dev@claude-plugins-official`

#### 5. mcp-server-dev

**功能**: 设计和构建 MCP 服务器的技能，指导部署模式（远程 HTTP、MCPB、本地）、工具设计模式、认证和交互式 MCP 应用

**安装**: `/plugin install mcp-server-dev@claude-plugins-official`

#### 6. plugin-dev

**功能**: 插件开发指南

**安装**: `/plugin install plugin-dev@claude-plugins-official`

#### 7. pr-review-toolkit

**功能**: 全面的 PR 审查代理，专注于评论、测试、错误处理、类型设计、代码质量和代码简化

**安装**: `/plugin install pr-review-toolkit@claude-plugins-official`

#### 8. security-guidance

**功能**: 安全指导

**安装**: `/plugin install security-guidance@claude-plugins-official`

#### 9. session-report

**功能**: 会话报告生成

**安装**: `/plugin install session-report@claude-plugins-official`

### 二、代码编辑与分析类

#### 10. agent-sdk-dev

**功能**: Agent SDK 开发

**安装**: `/plugin install agent-sdk-dev@claude-plugins-official`

#### 11. code-modernization

**功能**: 代码现代化改造

**安装**: `/plugin install code-modernization@claude-plugins-official`

#### 12. explanatory-output-style

**功能**: 解释性输出风格

**安装**: `/plugin install explanatory-output-style@claude-plugins-official`

#### 13. learning-output-style

**功能**: 学习输出风格

**安装**: `/plugin install learning-output-style@claude-plugins-official`

### 三、设计类

#### 14. frontend-design

**功能**: 前端设计技能，用于 UI/UX 实现

**安装**: `/plugin install frontend-design@claude-plugins-official`

### 四、Skill 创建类

#### 15. skill-creator

**功能**: 创建新技能、改进现有技能和衡量技能性能。当用户想要从头创建技能、更新或优化现有技能、运行评估测试技能或进行带方差分析的技能性能基准测试时使用

**安装**: `/plugin install skill-creator@claude-plugins-official`

### 五、Loop 类

#### 16. ralph-loop

**功能**: Loop 循环任务

**安装**: `/plugin install ralph-loop@claude-plugins-official`

### 六、其他工具类

#### 17. claude-code-setup

**功能**: Claude Code 安装配置

**安装**: `/plugin install claude-code-setup@claude-plugins-official`

#### 18. claude-md-management

**功能**: Markdown 文件管理

**安装**: `/plugin install claude-md-management@claude-plugins-official`

#### 19. playground

**功能**:  playgrounds

**安装**: `/plugin install playground@claude-plugins-official`

### 七、LSP 语言服务器类

#### 20. clangd-lsp

**安装**: `/plugin install clangd-lsp@claude-plugins-official`

#### 21. csharp-lsp

**安装**: `/plugin install csharp-lsp@claude-plugins-official`

#### 22. gopls-lsp

**安装**: `/plugin install gopls-lsp@claude-plugins-official`

#### 23. jdtls-lsp

**安装**: `/plugin install jdtls-lsp@claude-plugins-official`

#### 24. kotlin-lsp

**安装**: `/plugin install kotlin-lsp@claude-plugins-official`

#### 25. lua-lsp

**安装**: `/plugin install lua-lsp@claude-plugins-official`

#### 26. php-lsp

**安装**: `/plugin install php-lsp@claude-plugins-official`

#### 27. pyright-lsp

**安装**: `/plugin install pyright-lsp@claude-plugins-official`

#### 28. ruby-lsp

**安装**: `/plugin install ruby-lsp@claude-plugins-official`

#### 29. rust-analyzer-lsp

**安装**: `/plugin install rust-analyzer-lsp@claude-plugins-official`

#### 30. swift-lsp

**安装**: `/plugin install swift-lsp@claude-plugins-official`

#### 31. typescript-lsp

**安装**: `/plugin install typescript-lsp@claude-plugins-official`

### 八、第三方插件

位于 `external_plugins/` 目录下的第三方合作插件：

#### 32. algorithmic-art

**功能**: 算法艺术

#### 33. brand-guidelines

**功能**: 品牌指南

#### 34. canvas-design

**功能**: Canvas 设计

#### 35. claude-api

**功能**: Claude API 相关

#### 36. doc-coauthoring

**功能**: 文档协作

#### 37. docx

**功能**: Word 文档处理

#### 38. frontend-design

**功能**: 前端设计

#### 39. internal-comms

**功能**: 内部沟通

#### 40. mcp-builder

**功能**: MCP 构建器

#### 41. pdf

**功能**: PDF 处理

#### 42. playground

**功能**: 操场

#### 43. slack-gif-creator

**功能**: Slack GIF 创建

#### 44. theme-factory

**功能**: 主题工厂

#### 45. webapp-testing

**功能**: Web 应用测试

#### 46. web-artifacts-builder

**功能**: Web 工件构建

#### 47. xlsx

**功能**: Excel 表格处理

---

## 快速安装所有官方插件

```bash
# 添加市场
/plugin marketplace add anthropics/claude-plugins-official

# 安装常用插件
/plugin install code-review@claude-plugins-official
/plugin install frontend-design@claude-plugins-official
/plugin install pr-review-toolkit@claude-plugins-official
/plugin install skill-creator@claude-plugins-official
/plugin install mcp-server-dev@claude-plugins-official
/plugin install security-guidance@claude-plugins-official
```
