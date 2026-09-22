---
title: "2026 年全球大模型全景汇总"
date: 2026-08-02
tags: []
---

# 2026 年全球大模型全景汇总

> **编写时间：** 2026-08-02  
> **数据截止：** 2026 年 7 月底（部分模型信息更新至发布时的最新状态）  
> **说明：** 本文汇总国内外主流大模型的核心信息，包括模型名称、版本、参数规模、所属公司、性能评测、官方文档等，供大模型应用开发者参考。  
> **历史版本：** 本文 2025 年版本可见 Git 历史 `deb7e7a` 之前的提交。

---

## 目录

- [一、2026 年大模型行业概览](#一2026-年大模型行业概览)
- [二、国际大模型](#二国际大模型)
  - [2.1 OpenAI — GPT-5 / 5.x 系列](#21-openai--gpt-5--5x-系列)
  - [2.2 Anthropic — Claude Opus 4.x / Fable 5 系列](#22-anthropic--claude-opus-4x--fable-5-系列)
  - [2.3 Google — Gemini 3 / 3.1 系列](#23-google--gemini-3--31-系列)
  - [2.4 Meta — Llama 4 系列](#24-meta--llama-4-系列)
  - [2.5 xAI — Grok 4 系列](#25-xai--grok-4-系列)
  - [2.6 Mistral AI — Mistral Large 3 系列](#26-mistral-ai--mistral-large-3-系列)
- [三、国内大模型](#三国内大模型)
  - [3.1 深度求索 — DeepSeek V4 / R1 系列](#31-深度求索--deepseek-v4--r1-系列)
  - [3.2 阿里巴巴 — 通义千问 Qwen 3.5 / 3.6 系列](#32-阿里巴巴--通义千问-qwen-35--36-系列)
  - [3.3 智谱 AI — GLM-5 系列](#33-智谱-ai--glm-5-系列)
  - [3.4 月之暗面 — Kimi K2.5 / K2.6 / K3 系列](#34-月之暗面--kimi-k25--k26--k3-系列)
  - [3.5 字节跳动 — 豆包 Doubao Seed 2.0 系列](#35-字节跳动--豆包-doubao-seed-20-系列)
  - [3.6 百度 — 文心 ERNIE 5.0 系列](#36-百度--文心-ernie-50-系列)
  - [3.7 MiniMax — M2.5 / M2.7 系列](#37-minimax--m25--m27-系列)
  - [3.8 腾讯 — 混元 HY 2.0 系列](#38-腾讯--混元-hy-20-系列)
  - [3.9 阶跃星辰 — Step 3.7 系列](#39-阶跃星辰--step-37-系列)
  - [3.10 科大讯飞 — 星火 4.0 系列](#310-科大讯飞--星火-40-系列)
  - [3.11 百川智能 — Baichuan-M2 系列](#311-百川智能--baichuan-m2-系列)
- [四、评测基准体系（2026 版）](#四评测基准体系2026-版)
- [五、主要模型性能横评](#五主要模型性能横评)
- [六、总结与趋势](#六总结与趋势)
- [七、参考链接](#七参考链接)

---

## 一、2026 年大模型行业概览

2026 年是大模型竞争白热化的一年，行业格局发生了几个关键变化：

1. **SWE-bench Verified 已于 2026 年 2 月被 OpenAI 宣布退役**（数据污染严重，分数普遍飙升至 80%+ 失去区分度），取而代之的是 **SWE-bench Pro**、**Terminal-Bench 2.x** 等更难的评测
2. **MMLU 和 HumanEval 基本饱和**——前沿模型分数集中在 88~95%+，分差已小于 prompt 格式差异，不再作为模型选型的主要依据
3. **推理预算取代模型选择**：GPT-5.5/5.6 的 `reasoning_effort` 参数使同一模型在不同预算下表现差异显著
4. **MoE + 极低激活率成为标配**：Qwen 3.5（397B/17B，4.3%）、MiniMax M2.5（229B/10B，4.4%）大幅降低推理成本
5. **开源与闭源差距急速缩小**：DeepSeek V4 Pro 的 SWE-bench 80.6% 仅比 GPT-5.5 低 8 个百分点，价格仅为其 1/12
6. **中国大模型全面崛起**：Kimi K3 登顶全球最大开源模型（2.8T），GLM-5.1 在 HLE 和 GPQA Diamond 上国产第一

---

## 二、国际大模型

### 2.1 OpenAI — GPT-5 / 5.x 系列

**公司：** OpenAI（美国）  
**官网：** [https://openai.com](https://openai.com)  
**API 文档：** [https://platform.openai.com/docs](https://platform.openai.com/docs)

#### 版本演进

| 模型 | 发布时间 | 上下文窗口 | 输入价格 | 输出价格 | 状态 |
|------|----------|-----------|----------|----------|------|
| GPT-5 | 2025-08 | 272K~400K | $1.25/M | $10.00/M | 已被替代 |
| GPT-5.1 | 2025-11 | 400K | $1.25/M | $10.00/M | 已被替代 |
| GPT-5.2 | 2025-12 | 400K | $1.75/M | $14.00/M | 已被替代 |
| GPT-5.4 | 2026-03 | 1.05M | $2.50/M | $15.00/M | 可用 |
| GPT-5.5 | 2026-04 | 1.05M | $5.00/M | $30.00/M | 可用 |
| GPT-5.6 Sol | 2026-07 | 1M | $5.00/M | $30.00/M | 最新旗舰 |
| GPT-5.6 Terra | 2026-07 | 1M | $2.50/M | $15.00/M | 均衡版 |
| GPT-5.6 Luna | 2026-07 | 1M | $1.00/M | $6.00/M | 轻量版 |

> OpenAI 从未公开 GPT-4/5 系列的具体参数量。GPT-5 于 2025 年 8 月首次发布，2026 年进入快速迭代期（5.1→5.2→5.4→5.5→5.6），节奏约为每 2~3 个月一个新版本。

#### 关键性能与评测

**GPT-5（2025 年 8 月发布，基准线）：**

| 评测 | 分数 |
|------|------|
| AIME 2025（无工具） | 94.6% |
| SWE-bench Verified | 74.9% |
| GPQA Diamond | 87.3% |
| MATH-500 | 99.6% |
| HumanEval | 96.0% |
| Chatbot Arena ELO | 1,450 |
| HLE | 42.0% |

**GPT-5.4（2026 年 3 月）：**

- 上下文窗口扩展至 **1.05M tokens**（GPT-5 的 3.9 倍）
- 原生 **Computer Use** 能力（OSWorld-Verified **75%**，超过人类平均水平 72.4%）
- 事实性错误比 GPT-5.2 减少 33%

**GPT-5.5（2026 年 4 月，旗舰推理模型）：**

- SWE-bench Verified **88.7%**（编码能力最强，但 SWE-bench 已退役仅供参考）
- GPQA Diamond **93.5%**（xhigh effort）
- 支持 `reasoning_effort` 参数调节（high / xhigh），预算越高推理越深
- GPT-5.5 Pro 变体 $30/$180 per MTok（6 倍基础价格）

**GPT-5.6 系列（2026 年 7 月，最新）：**

- 三档模型：Sol（旗舰）、Terra（均衡）、Luna（轻量）
- Agents' Last Exam（55 个领域）：Sol 得分 **53.6**，领先 Claude Fable 5 13.1 分
- Terminal-Bench 2.1：Sol Ultra 达到 **91.9%**
- 知识截止日期：2026 年 2 月

---

### 2.2 Anthropic — Claude Opus 4.x / Fable 5 系列

**公司：** Anthropic（美国）  
**官网：** [https://www.anthropic.com](https://www.anthropic.com)  
**API 文档：** [https://docs.anthropic.com](https://docs.anthropic.com)

#### 主要模型一览

| 模型 | 发布时间 | 上下文 | 最大输出 | 输入价格 | 输出价格 |
|------|----------|--------|----------|----------|----------|
| Claude Opus 4.5 | 2025-11 | 200K | — | $15.00/M | $75.00/M |
| Claude Opus 4.6 | 2026-02 | 1M | — | $5.00/M | $25.00/M |
| Claude Sonnet 4.6 | 2026-02 | 1M | — | $3.00/M | $15.00/M |
| Claude Opus 4.7 | 2026-04 | 1M | — | $5.00/M | $25.00/M |
| Claude Opus 4.8 | 2026-06 | 1M | — | $5.00/M | $25.00/M |
| **Claude Fable 5** | **2026-06** | 1M | 128K | $10.00/M | $50.00/M |

> Anthropic 未公开任何 Claude 模型的参数量。Opus 4.7 引入新 tokenizer 使同量文本多产生约 35% 的 token，实际使用成本约为标价的 1.35 倍。Fable 5 是 Anthropic 首个面向公众开放的 **Mythos 级**模型（与受限 Mythos 5 共享底层权重，通过安全分类器过滤敏感请求）。

#### 关键性能与评测

| 评测 | Fable 5 | Opus 4.8 | Opus 4.7 | Sonnet 4.6 |
|------|---------|----------|----------|------------|
| SWE-bench Verified | **95.0%** | 88.6% | 87.6% | 79.6% |
| SWE-bench Pro | **80.3%** | 69.2% | — | — |
| GPQA Diamond | 91.3% | — | **94.2%** | 89.9% |
| Terminal-Bench 2.0 | — | 82.7% | 69.4% | — |
| OSWorld-Verified | 85.0% | 83.4% | — | — |
| ARC-AGI-2 | — | — | — | — |
| HLE | 53.1% | — | — | — |
| GDPval-AA ELO | **1932** | 1890 | — | 1633 |
| Chatbot Arena ELO | **1507** | — | — | — |

**Claude Opus 4.6 亮点（2026 年 2 月）：**

- LMArena 综合榜 #1（发布时）
- Agent 能力多项第一（Terminal-Bench 65.4%、OSWorld 72.7%、BrowseComp 84.0%）

**Claude Sonnet 4.6 亮点（2026 年 2 月）：**

- 编码性价比之王——Opus 级别性能，Sonnet 级价格（Opus 的 60%）
- A-CODE-LLM Bench 综合第一（0.748），GDPval-AA ELO 1633 甚至超过 Opus 4.6（1606）

**Claude Fable 5 亮点（2026 年 6 月）：**

- SWE-bench Pro **80.3%**，比 Opus 4.8（69.2%）高出 11 个百分点
- FrontierCode Diamond **29.3%**（Opus 4.8 仅 13.4%）
- 安全分类器覆盖网络安全、生物/化学、模型蒸馏三大类（<5% 会话触发，回退到 Opus 4.8）
- 约 0.03% 流量触发静默降级（前沿 LLM 开发相关），引发透明度争议

---

### 2.3 Google — Gemini 3 / 3.1 系列

**公司：** Google DeepMind（美国）  
**官网：** [https://deepmind.google](https://deepmind.google)  
**API 文档：** [https://ai.google.dev](https://ai.google.dev)

#### 主要模型一览

| 模型 | 发布时间 | 上下文 | 输入价格 | 输出价格 |
|------|----------|--------|----------|----------|
| Gemini 2.5 Pro | 2025-03 | 1M | — | — |
| Gemini 2.5 Flash | 2025-07 | 1M | — | — |
| Gemini 3 Pro | 2025-11 | 1M | $2.00/M | $12.00/M |
| **Gemini 3.1 Pro** | **2026-02** | 1M~2M | $2.00/M | $12.00/M |
| Gemini 3.1 Flash | 2026 | 1M | $0.15/M | $0.60/M |

> 未公开参数量。Gemini 3 Pro 已于 2026 年 3 月被 3.1 Pro 替代。

#### 关键性能与评测

| 评测 | Gemini 3.1 Pro | Gemini 3 Pro |
|------|---------------|-------------|
| SWE-bench Verified | **80.6%** | 76.2% |
| GPQA Diamond | **94.3%** | 91.9% |
| ARC-AGI-2 | **77.1%** | 31.1% (+148%) |
| HLE（无工具） | 44.4% | 37.5% |
| HLE（有工具） | 51.4% | 45.8% |
| LiveCodeBench Pro ELO | **2887** | 2439 |
| Terminal-Bench 2.0 | 68.5% | 54.2% |
| BrowseComp | 85.9% | — |

**Gemini 3.1 Pro 亮点：**

- **科学推理与竞赛代码最强**——GPQA Diamond **94.3%**（全模型最高）、LiveCodeBench ELO **2887**（全模型最高）
- ARC-AGI-2 从 31.1% 跃升至 77.1%（+148%），为单代推理能力提升最大的一次
- 原生多模态（文本 + 图像 + 音频 + 视频 + 代码）
- Deep Think 模式支持多假设并行推理
- 价格仅为 Claude Opus 4.6 的 1/2.5（输入），性价比优异

---

### 2.4 Meta — Llama 4 系列

**公司：** Meta（美国）  
**官网：** [https://llama.meta.com](https://llama.meta.com)  
**模型下载：** [https://huggingface.co/meta-llama](https://huggingface.co/meta-llama)

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 开源 |
|------|----------|--------|----------|------|--------|------|
| Llama 4 Scout | 2025-04 | 109B | 17B | MoE (16 专家) | 10M | 开源 |
| Llama 4 Maverick | 2025-04 | 400B | 17B | MoE (128 专家) | 1M | 开源 |
| Llama 4 Behemoth | 2025 预览 | ~2T | 288B | MoE (16 专家) | — | — |

> 截至 2026 年 7 月，Llama 4 Behemoth 尚未正式发布。Meta 在 2026 年上半年没有发布新旗舰，Llama 4 Maverick 仍是其主力开源模型。

| 评测 | Llama 4 Maverick | Llama 3.1 405B |
|------|-----------------|----------------|
| MMLU | 85.5~89.4% | 88.6% |
| MMLU Pro | 80.5% | 73.2% |
| HumanEval | 87.9% | 89.0% |
| LiveCodeBench | 43.4% | — |
| LMArena ELO | 1417 | — |

---

### 2.5 xAI — Grok 4 系列

**公司：** xAI（美国，Elon Musk 创立）  
**官网：** [https://x.ai](https://x.ai)  
**API 文档：** [https://docs.x.ai](https://docs.x.ai)

| 模型 | 发布时间 | 总参数 | 活跃参数 | 上下文 | 输入价格 | 输出价格 |
|------|----------|--------|----------|--------|----------|----------|
| Grok 4 | 2026 初 | ~314B | ~22B | — | $8.00/M | $15.00/M |
| Grok 4.1 Fast | 2026 初 | ~314B | ~22B | — | $3.00/M | $15.00/M |
| Grok 4.3 | 2026-04 | 未公开 | 未公开 | 1M | $1.25/M | $2.50/M |
| Grok 4.5 | 2026-07 | 1.5T | 未公开 | 500K | $2.00/M | $6.00/M |
| Grok 4.6 | 2026-07（训练完成） | 2T | 未公开 | — | — | — |

**Grok 4.5 关键评测（2026 年 7 月）：**

- SWE-bench Pro：**64.7%**（高于 GPT-5.5 的 58.6%，低于 Claude Opus 4.8 的 69.2%）
- DeepSWE 1.1：53%
- Artificial Analysis Intelligence Index：54
- 定位：成本效率优先，Elon Musk 称其"大致与 Opus 4.7 相当但快得多"

**Grok 4.6（即将发布）：**

- 2 万亿参数，专门对标 Kimi K3，由 Colossus 2 超算集群训练
- Grok 5 级路线图：6~10 万亿参数

---

### 2.6 Mistral AI — Mistral Large 3 系列

**公司：** Mistral AI（法国）  
**官网：** [https://mistral.ai](https://mistral.ai)  
**API 文档：** [https://docs.mistral.ai](https://docs.mistral.ai)

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 开源 | 输入价格 | 输出价格 |
|------|----------|--------|----------|------|--------|------|----------|----------|
| Mistral Large 3 | 2025-12 | 675B | 41B | MoE (128 专家) | 256K | Apache 2.0 | $0.50/M | $1.50/M |

- MMLU **~85.5%**，MATH-500 **93.6%**，MMLU-Pro **73.11%**
- 首次在旗舰模型中支持原生多模态（文本 + 图像），含 2.5B 视觉编码器
- 开源非推理模型 LMArena 排行榜排名第 2

---

## 三、国内大模型

### 3.1 深度求索 — DeepSeek V4 / R1 系列

**公司：** 深度求索（DeepSeek，杭州）  
**官网：** [https://www.deepseek.com](https://www.deepseek.com)  
**API 文档：** [https://platform.deepseek.com/api-docs](https://platform.deepseek.com/api-docs)  
**模型下载：** [https://huggingface.co/deepseek-ai](https://huggingface.co/deepseek-ai)

#### 主要模型一览

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 开源 | API 输出价格 |
|------|----------|--------|----------|------|--------|------|-------------|
| DeepSeek-V3 | 2024-12 | 671B | 37B | MoE (256 专家) | 128K | 开源 | $0.27/M |
| DeepSeek-R1 | 2025-01 | 671B | 37B | MoE | 128K | 开源 | $2.19/M |
| DeepSeek-V3.2 | 2025 | 671B | 37B | MoE | 128K | 开源 | — |
| **DeepSeek V4-Flash** | **2026-04** | 284B | 13B | MoE | 1M | Apache 2.0 | $0.14/M（输入） |
| **DeepSeek V4-Pro** | **2026-04** | 1.6T | 49B | MoE (384+2 专家) | 1M | Apache 2.0 | $0.87/M |
| **DeepSeek-R1-0528** | 2025-05 | 671B | 37B | MoE | 128K | 开源 | — |

#### 架构创新（V4-Pro）

- **全栈昇腾 910C 训练**：首次在国产芯片上实现万亿级 MoE 模型训练
- 动态 Top-K 路由 + MLA（多头潜在注意力）
- 训练数据：33T tokens
- V4-Flash 推广价：输入 ¥12/百万 token（缓存命中 ¥1），输出 ¥24

#### 关键性能与评测

| 评测 | DeepSeek V4-Pro | DeepSeek-R1 | DeepSeek-V3 |
|------|----------------|-------------|-------------|
| MMLU-Pro | 84.2 | — | 76.3% |
| SWE-bench Verified | **80.6%** | 88.9% | — |
| LiveCodeBench v6 | 88.1 | — | 45.8~49.2% |
| GPQA Diamond | ~89% | — | 59.1% |

**核心定位：** 开源性价比之王。V4-Pro SWE-bench 80.6% 进入国际第一梯队，仅为 GPT-5.5 价格的 **1/12**。R1-0528 在 SWE-bench 上达到 88.9%。

---

### 3.2 阿里巴巴 — 通义千问 Qwen 3.5 / 3.6 系列

**公司：** 阿里巴巴（Alibaba，杭州）  
**官网：** [https://tongyi.aliyun.com](https://tongyi.aliyun.com)  
**模型下载：** [https://huggingface.co/Qwen](https://huggingface.co/Qwen)  
**API 文档：** [https://help.aliyun.com/zh/model-studio](https://help.aliyun.com/zh/model-studio)

#### 主要模型一览

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 开源 | 输入价格 |
|------|----------|--------|----------|------|--------|------|----------|
| Qwen3-235B-A22B | 2025-04 | 235B | 22B | MoE | 130K | 开源 | — |
| Qwen3-Max | 2025-09 | 未公开 | 未公开 | 未公开 | 262K | 闭源 | — |
| Qwen3.5-Plus | 2026-02 | 397B | 17B | MoE | 1M | 开源 | ¥0.8/M |
| Qwen3.6-Plus | 2026-04 | 397B | 17B | MoE | 1M | 开源 | — |
| Qwen3.6-Max-Preview | 2026-04 | 未公开 | 未公开 | MoE | 1M | 闭源 | — |

#### 关键性能与评测

- **C-Eval 88.5**（国产第一）
- MMLU-Pro **82.0**；SWE-bench Verified **71.8%**
- Qwen3.6-Plus：3970 亿总参数 / 170 亿激活
- 所有 Qwen3 系列模型支持思考/非思考双模式（同一模型内置，不加价）
- 全模态 Qwen3-Omni：215 项任务 SOTA
- HuggingFace 衍生模型超 **20 万个**，119 种语言覆盖

**核心定位：** 国产性价比之王（综合性价比 8.49），模型矩阵最完整（0.5B~397B 全尺寸），生态最丰富。

---

### 3.3 智谱 AI — GLM-5 系列

**公司：** 智谱 AI（Zhipu AI，北京，清华系，港交所上市：全球大模型第一股）  
**官网：** [https://open.bigmodel.cn](https://open.bigmodel.cn)  
**模型下载：** [https://huggingface.co/THUDM](https://huggingface.co/THUDM)

#### 主要模型一览

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 开源 | 输入价格 | 输出价格 |
|------|----------|--------|----------|------|--------|------|----------|----------|
| GLM-5 | 2026-02 | 未公布 | 未公布 | MoE | 1M | 开源 | — | — |
| GLM-5.1 | 2026-04 | 754B | 40B | MoE (256 专家) | 203K | MIT | ¥6/M | ¥24/M |
| GLM-5.2 | 2026 | 未公布 | 未公布 | MoE | — | 开源 | — | — |

#### 关键性能与评测

- **HLE 50.4**（国产第一）
- **GPQA Diamond 86.0**（国产第一）
- **AIME 2025 85.2**（国产推理之王）
- GLM-5.1 高速版 **400 tokens/s**，刷新全球大模型 API 速度上限
- 约 **10 万张昇腾 910B** 全流程训练，全栈国产自主可控
- MaaS ARR 达 17 亿元，年内三次提价调用量反增 400%

**核心定位：** 推理之王 + Agent 能力 + 政企合规。自研 GLM 架构（非 LLaMA 路线），MIT 许可证开源。

---

### 3.4 月之暗面 — Kimi K2.5 / K2.6 / K3 系列

**公司：** 月之暗面（Moonshot AI，北京）  
**官网：** [https://kimi.moonshot.cn](https://kimi.moonshot.cn)  
**模型下载：** [https://huggingface.co/moonshotai](https://huggingface.co/moonshotai)

#### 主要模型一览

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 开源 | 输出价格 |
|------|----------|--------|----------|------|--------|------|----------|
| Kimi K2-Instruct | 2025-07 | 1T | 32B | MoE (384 专家) | 128K | MIT | — |
| Kimi K2.5 | 2026 初 | 1T | 32B | MoE | 256K | MIT | — |
| Kimi K2.6 | 2026-04 | 1T | 32B | MoE (384 专家) | 256K | Modified MIT | ¥28/M |
| **Kimi K3** | **2026-07** | **2.8T** | ~16B | MoE (896 专家) | **1M** | Modified MIT | 中国模型最高价 |

#### 关键性能与评测

| 评测 | Kimi K3 | Kimi K2.6 | 对比参考 |
|------|---------|----------|---------|
| SWE-bench Pro | **58.6%** | — | 超过 GPT-5.4（开源第一） |
| SWE-bench Verified | — | 76.8% | Claude Fable 5: 95.0% |
| Terminal-Bench 2.0 | **66.7** | — | 击败 Claude Opus 4.6 |
| AAI 智能指数 | **54** | — | 开源第一 |
| HumanEval | — | **99.0%** | 全模型最高 |
| MMLU | — | 92.0% | — |
| MMLU-Pro | — | 87.1% | — |

**Kimi K3 亮点（2026 年 7 月）：**

- **全球最大开源模型**（2.8T 参数，896 专家，每次激活 16 个）
- LMArena 代码竞技场**登顶**
- 训练效率较 K2 提升 2.5 倍，自研 MuonClip 优化器
- ARR 从 4 月 2 亿美元增长至 6 月 3 亿美元

---

### 3.5 字节跳动 — 豆包 Doubao Seed 2.0 系列

**公司：** 字节跳动（ByteDance，北京）  
**官网：** [https://www.doubao.com](https://www.doubao.com)  
**API 文档：** [https://www.volcengine.com/docs/82379](https://www.volcengine.com/docs/82379)

| 模型 | 发布时间 | 参数 | 上下文 | 输入价格 | 输出价格 |
|------|----------|------|--------|----------|----------|
| Doubao-1.5-pro | 2025 | 490B/7B MoE | 256K | — | — |
| **Doubao-Seed-2.0-Pro** | **2026-02** | 未公布（约 65B+ MoE） | 256K | ¥3.41/M | ¥17.04/M |

#### 关键性能

- **SuperCLUE 74.5**（国产第一）
- **C-SimpleQA 80.2**（国产第一）
- SWE-bench Verified **72.3%**
- 国内唯一原生 VLM 编程模型（可看设计稿直接生成代码）
- 日均 Token 使用量超 **120 万亿**，中国 C 端最大用户基数

**核心定位：** C 端体验最佳、多模态创作、抖音/剪映生态深度集成。

---

### 3.6 百度 — 文心 ERNIE 5.0 系列

**公司：** 百度（Baidu，北京）  
**官网：** [https://yiyan.baidu.com](https://yiyan.baidu.com)  
**API 文档：** [https://cloud.baidu.com/doc/WENXINWORKSHOP/index.html](https://cloud.baidu.com/doc/WENXINWORKSHOP/index.html)

| 模型 | 发布时间 | 总参数 | 上下文 | 开源 | 定价 |
|------|----------|--------|--------|------|------|
| ERNIE 5.0 | 2025~2026 | ~1.8T MoE | 128K | 闭源 | ¥0.6/万 token（输入） |
| ERNIE 5.1（轻量） | 2026 | 未公开 | — | 闭源 | — |

- 知识增强架构（融合百度知识图谱）+ 昆仑芯 3 代 + 昇腾 910B 训练
- 中文理解深度、搜索整合、事实准确率提升 35%
- **核心定位：** 合规利器、企业级应用、搜索增强

---

### 3.7 MiniMax — M2.5 / M2.7 系列

**公司：** MiniMax（上海）  
**官网：** [https://www.minimaxi.com](https://www.minimaxi.com)  
**API 文档：** [https://platform.minimax.io/docs](https://platform.minimax.io/docs)

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 开源 | 输入价格 | 输出价格 |
|------|----------|--------|----------|------|--------|------|----------|----------|
| **MiniMax M2.5** | **2026-02** | 229B | ~10B | MoE | 128K | MIT | $0.30/M | $1.20/M |
| **MiniMax M2.7** | **2026-03** | 229B | ~10B | MoE | 200K | Modified-MIT | $0.30/M | $1.20/M |

#### 关键性能对比

| 评测 | M2.5 | M2.7 |
|------|------|------|
| SWE-bench Verified | **80.2%** | 78.0% |
| SWE-bench Pro | 55.4% | 56.2% |
| GPQA Diamond | 85.2% | 87.0% |
| HLE | 19.4 | 28.0 |
| GDPval-AA ELO | 1203 | **1495**（开源最高） |
| τ²-Bench Telecom | 97.8% | 85.0% |
| 幻觉率 | 88% | **34%** |

**M2.7 亮点：**

- 幻觉率从 88% 骤降至 34%（最大升级点）
- Agent 工具调用从 87% 提升至 93%
- 可自我迭代——自动化 30-50% 的内部强化学习研究流程
- **开源协议倒退**：从 MIT 变为 Modified-MIT，商业使用受限

**M2.5 定位：** 高吞吐、低成本通用推理，批量处理/RAG/多语言代码生成的首选。

---

### 3.8 腾讯 — 混元 HY 2.0 系列

**公司：** 腾讯（Tencent，深圳）  
**官网：** [https://hunyuan.tencent.com](https://hunyuan.tencent.com)

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 开源 |
|------|----------|--------|----------|------|--------|------|
| Hunyuan-Large 389B | 2025-03 | 389B | 52B | MoE | 256K | 开源 |
| Tencent HY 2.0 | 2025-12 | 406B | 32B | MoE | 256K | 闭源 |

- HY 2.0 在 IMO-AnswerBench、HMMT2025、HLE、ARC-AGI 等权威测试中位列国内第一梯队
- 引入长度惩罚策略，单位 token "智能密度" 业界领先
- RLVR+RLHF 双阶段强化学习，已在元宝、ima 等腾讯应用接入

---

### 3.9 阶跃星辰 — Step 3.7 系列

**公司：** 阶跃星辰（StepFun，上海）  
**官网：** [https://platform.stepfun.com](https://platform.stepfun.com)

| 模型 | 发布时间 | 总参数 | 活跃参数 | 上下文 | 开源 | 输入 | 输出 |
|------|----------|--------|----------|--------|------|------|------|
| **Step 3.7 Flash** | **2026-05** | 196B + 1.8B ViT | ~11B | 256K | Apache 2.0 | $0.20/M | $1.15/M |

#### 关键性能

- 最高生成速度 **400 tokens/s**（单卡 A100）
- ClawEval-1.1 **67.1**（多轮 Agent 执行一致性，大幅领先）
- τ²-bench Telecom **>98%**（三档难度全通过）
- SWE-bench Pro **56.3**
- 原生多模态（直接支持图像和视频输入）
- 支持 Claude Code、OpenClaw、vLLM、SGLang、llama.cpp 等框架

**核心定位：** 专为生产级 Agent 打造，面向高频、高并发的企业级多模态智能体工作流。

---

### 3.10 科大讯飞 — 星火 4.0 系列

**公司：** 科大讯飞（iFlytek，合肥）  
**官网：** [https://xinghuo.xfyun.cn](https://xinghuo.xfyun.cn)

| 模型 | 发布时间 | 参数 | 上下文 | 开源 |
|------|----------|------|--------|------|
| 星火 4.0 Turbo | 2024-10 | 未公开 | — | 闭源 |
| 星火深度推理 X1 | 2025-01 | 70B | — | 闭源 |

- 斯坦福 HAI 2025 MixEval-Hard 唯一入围前十的国产大模型
- 14 项主流测试中 9 项超越 GPT-4o
- 全部在国产算力平台（飞星一号/二号，联合华为打造）训练
- **核心定位：** 全栈国产自主可控、行业垂直场景（金融/油气/电力等）

---

### 3.11 百川智能 — Baichuan-M2 系列

**公司：** 百川智能（Baichuan Intelligence，北京）  

| 模型 | 发布时间 | 参数 | 定位 | 开源 |
|------|----------|------|------|------|
| Baichuan-M2 | 2025-08 | 32B | 医疗增强推理旗舰 | 开源 |

- HealthBench 标准版 **60.1 分**（仅次于 GPT-5-Thinking 67.2）
- 支持 RTX 4090 单卡部署（4bit），成本为 DeepSeek-R1 的 **1/57**
- 已完成国产主流芯片适配

---

## 四、评测基准体系（2026 版）

### 4.1 评测基准现状

| 基准 | 状态 | 说明 |
|------|------|------|
| **MMLU** | ⚠️ 已饱和 | 前沿模型得分 88~92.5%，分差小于 prompt 格式差异 |
| **HumanEval** | ⚠️ 已饱和+污染 | 164 道题已被广泛记忆，前沿模型 90~99% |
| **GSM8K** | ⚠️ 已饱和 | 小学数学题，前沿模型接近满分 |
| **SWE-bench Verified** | ❌ 已退役 | 2026-02-23 被 OpenAI 宣布退役（数据污染） |
| **SWE-bench Pro** | ✅ 活跃 | 更深度的工程任务，抗污染，前沿分数 23~80% |
| **GPQA Diamond** | ✅ 活跃 | 研究生级科学推理，仍有较好区分度 |
| **HLE** | ✅ 活跃 | Humanity's Last Exam，当前最难的前沿评测 |
| **LiveCodeBench** | ✅ 活跃 | 动态竞赛题，防数据污染 |
| **Terminal-Bench 2.x** | ✅ 活跃 | 命令行 Agent 评测 |
| **ARC-AGI-2** | ✅ 活跃 | 抽象视觉推理，3.1 Pro 77.1% 领先 |
| **GDPval-AA** | ✅ 活跃 | 44 种职业的结构化专业任务 |
| **Chatbot Arena** | ✅ 活跃 | 人类盲测 ELO 排行 |
| **SuperCLUE** | ✅ 活跃 | 中文综合能力权威评测 |
| **Agents' Last Exam** | ✅ 活跃 | 55 个领域的 Agent 评测，最新最严 |

### 4.2 基准说明

| 基准 | 全称 | 评测维度 | 说明 |
|------|------|----------|------|
| **GPQA Diamond** | Graduate-Level Google-Proof Q&A | 研究生级科学推理 | 博士级物化生题目，Google 无法直接搜到答案 |
| **HLE** | Humanity's Last Exam | 终极推理 | 涵盖多学科极难题目 |
| **SWE-bench Pro** | SWE-bench Professional | 软件工程（进阶） | 已验证版的抗污染升级版，真实 bug 修复 |
| **LiveCodeBench** | Live Code Benchmark | 代码竞赛 | 动态更新的竞赛题，防数据污染 |
| **ARC-AGI-2** | Abstraction & Reasoning Corpus | 抽象推理 | 视觉推理题，基准测试 AI 的真正推理能力 |
| **Terminal-Bench** | Terminal Benchmark | Agent 命令行 | 评测模型在终端环境中的多步操作能力 |
| **MMLU-Pro** | MMLU Professional | 专业知识 | 10 选 1 + CoT，比标准 MMLU 更难 |
| **SuperCLUE** | — | 中文综合能力 | 国内最权威的中文大模型评测 |

---

## 五、主要模型性能横评

### 5.1 国际旗舰模型核心评测

| 模型 | SWE-bench Pro | GPQA Diamond | HLE | Terminal-Bench 2.x | ARC-AGI-2 | Chatbot Arena |
|------|--------------|-------------|-----|--------------------|-----------|---------------|
| **Claude Fable 5** | **80.3%** | 91.3% | 53.1% | — | — | 1507 |
| Claude Opus 4.8 | 69.2% | — | — | 82.7% (2.1) | — | — |
| Claude Opus 4.7 | — | **94.2%** | — | 69.4% (2.0) | — | — |
| Claude Sonnet 4.6 | — | 89.9% | — | — | — | 1633 GDPval |
| **GPT-5.6 Sol** | — | — | — | **91.9%** (2.1) | — | — |
| GPT-5.5 | 58.6% | 93.5% | — | — | — | ~1480 |
| GPT-5.4 | — | — | — | — | — | ~1480 |
| **Gemini 3.1 Pro** | 54.2% | **94.3%** | 51.4% | 68.5% (2.0) | **77.1%** | 1486 |
| Grok 4.5 | 64.7% | — | — | — | — | — |
| Grok 4.3 | — | — | — | — | — | — |

> 空白表示该模型未公开权威第三方评测数据。

### 5.2 国内旗舰模型核心评测

| 模型 | SWE-bench Pro | GPQA Diamond | HLE | MMLU-Pro | SuperCLUE | 核心定位 |
|------|--------------|-------------|-----|----------|-----------|---------|
| **DeepSeek V4-Pro** | ~55% | ~89% | — | 84.2 | — | 开源性价比之王 |
| DeepSeek-R1-0528 | — | — | — | — | — | 推理专项开源 |
| **Qwen 3.6-Plus** | — | — | — | 82.0 | — | 国产性价比第一、生态最全 |
| **GLM-5.1** | — | **86.0** | **50.4** | — | — | 推理之王、Agent |
| **Kimi K3** | **58.6%** | — | — | — | — | 全球最大开源、代码第一 |
| Kimi K2.5 | — | — | — | 87.1 | — | 开源编码标杆 |
| **Doubao-Seed-2.0** | — | — | — | — | **74.5** | C端体验、多模态 |
| **MiniMax M2.5** | 55.4% | 85.2% | — | — | — | 低幻觉、Agent |
| **Step 3.7 Flash** | 56.3% | — | — | — | — | 生产级 Agent |

### 5.3 性价比对比（价格 / SWE-bench Pro 得分）

| 模型 | 输出价格 (per 1M) | SWE-bench Pro | 性价比 |
|------|-------------------|--------------|--------|
| **DeepSeek V4-Pro** | $0.87 | ~55% | 极优 |
| **Gemini 3.1 Flash** | $0.60 | — | 极优 |
| Gemini 3.1 Pro | $12.00 | 54.2% | 优 |
| Claude Sonnet 4.6 | $15.00 | — | 优 |
| Grok 4.5 | $6.00 | 64.7% | 优 |
| Claude Opus 4.8 | $25.00 | 69.2% | 中 |
| GPT-5.5 | $30.00 | 58.6% | 中 |
| Claude Fable 5 | $50.00 | 80.3% | 较低 |

---

## 六、总结与趋势

### 6.1 2026 年核心趋势

1. **推理预算取代模型选择：** GPT-5.5/5.6 的 `reasoning_effort` 参数使"选什么模型"逐渐变成"花多少推理预算"，同一模型在 high 与 xhigh 档位下表现差异显著
2. **MoE + 极低激活率成为标配：** 4~5% 的激活率已成行业标准，推理成本大幅降低。Kimi K3 仅激活 16B/2.8T（0.57%）
3. **开源与闭源差距急速缩小：** DeepSeek V4-Pro 以 1/12 价格接近 GPT-5.5 性能，Kimi K3 SWE-bench Pro 超越 GPT-5.4
4. **评测基准大洗牌：** SWE-bench Verified 退役，MMLU/HumanEval 饱和，SWE-bench Pro、Terminal-Bench、HLE、Agents' Last Exam 成为新标准
5. **Agent 能力深度整合：** 从"写代码"到"做工程"的范式跃迁——Claude Code 在 1250 万行代码库中连续自主工作 7 小时，精度 99.9%
6. **中国大模型全面崛起：** Kimi K3 登顶全球最大开源模型，GLM-5.1 在 HLE/GPQA 上国产第一，DeepSeek 改变全球 AI 经济学
7. **国产芯片适配加速：** DeepSeek V4-Pro 全栈昇腾 910C、智谱 GLM-5.1 10 万张昇腾 910B，全栈自主可控成为国产模型的独特竞争力
8. **76% 研究者认为 Scaling Law 已见顶：** 下一轮飞跃预期来自架构创新（稀疏架构、推理优化）而非简单扩大规模
9. **幻觉控制成为差异化焦点：** MiniMax M2.7 将幻觉率从 88% 降至 34%，幻觉控制成为产品可用性的关键指标

### 6.2 选型建议（面向开发者，2026 年 7 月）

| 场景 | 推荐国际模型 | 推荐国内模型 |
|------|-------------|-------------|
| **生产级编码（预算不限）** | Claude Fable 5、GPT-5.5 | Kimi K3 |
| **生产级编码（预算敏感）** | Claude Sonnet 4.6 | DeepSeek V4-Pro、Qwen 3.6-Plus |
| **竞赛级算法题** | Gemini 3.1 Pro | DeepSeek V4-Pro |
| **科学推理与数学** | Gemini 3.1 Pro | GLM-5.1 |
| **Agent / 工具调用** | Claude Opus 4.8 | Step 3.7 Flash、GLM-5.1 |
| **超长上下文处理** | Gemini 3.1 Pro (2M) | MiniMax M2.7、DeepSeek V4 (1M) |
| **高性价比 API** | GPT-5.6 Luna、Gemini Flash | DeepSeek V4-Flash、Qwen 3.5-Plus |
| **端侧/小模型部署** | Llama 4 Scout | Qwen3-8B、Hunyuan 7B |
| **中文场景** | Gemini 3.1 Pro | Qwen 3.6、DeepSeek、GLM-5.1 |
| **低幻觉要求** | Claude Fable 5 | MiniMax M2.7（34% 幻觉率） |
| **全栈国产自主可控** | — | 讯飞星火、DeepSeek V4、GLM-5.1 |
| **医疗垂直领域** | GPT-5.6 + RAG | Baichuan-M2 |
| **多模态 / VLM** | Gemini 3.1 Pro | Doubao-Seed-2.0-Pro |

---

## 七、参考链接

### 评测平台与排行榜

- [LMSYS Chatbot Arena](https://chat.lmsys.org/) — 人类盲测 ELO 排行榜
- [SuperCLUE](https://www.cluebenchmarks.com/superclue.html) — 中文大模型权威评测
- [Artificial Analysis](https://artificialanalysis.ai/) — 模型质量/速度/价格综合对比
- [SWE-bench](https://www.swebench.com/) — 软件工程评测（Verified 已退役，Pro 活跃）
- [LiveCodeBench](https://livecodebench.github.io/) — 动态代码竞赛评测
- [BenchGecko](https://benchgecko.ai/) — 多维度模型 Benchmark 查询
- [Vals AI](https://www.vals.ai/) — 独立第三方评测
- [BenchLM](https://benchlm.ai/) — 215 模型综合评测

### 各公司官方文档

- OpenAI: [https://platform.openai.com/docs](https://platform.openai.com/docs)
- Anthropic: [https://docs.anthropic.com](https://docs.anthropic.com)
- Google Gemini: [https://ai.google.dev](https://ai.google.dev)
- Meta Llama: [https://llama.meta.com](https://llama.meta.com)
- xAI Grok: [https://docs.x.ai](https://docs.x.ai)
- Mistral AI: [https://docs.mistral.ai](https://docs.mistral.ai)
- DeepSeek: [https://platform.deepseek.com/api-docs](https://platform.deepseek.com/api-docs)
- 阿里 Qwen: [https://help.aliyun.com/zh/model-studio](https://help.aliyun.com/zh/model-studio)
- 百度文心: [https://cloud.baidu.com/doc/WENXINWORKSHOP/index.html](https://cloud.baidu.com/doc/WENXINWORKSHOP/index.html)
- 智谱 GLM: [https://open.bigmodel.cn](https://open.bigmodel.cn)
- 字节豆包: [https://www.volcengine.com/docs/82379](https://www.volcengine.com/docs/82379)
- Kimi: [https://kimi.moonshot.cn](https://kimi.moonshot.cn)
- 腾讯混元: [https://hunyuan.tencent.com](https://hunyuan.tencent.com)
- 讯飞星火: [https://xinghuo.xfyun.cn](https://xinghuo.xfyun.cn)
- MiniMax: [https://www.minimaxi.com](https://www.minimaxi.com)
- 阶跃星辰: [https://platform.stepfun.com](https://platform.stepfun.com)

### 评测报告与数据来源

- 斯坦福 HAI 2026 AI Index Report
- TokenCalculator LLM Benchmarks (2026)
- ofox.ai — AI Model Rankings (May 2026)
- Vals AI — Independent Model Evaluations
- Eden AI — Claude Fable 5 Benchmark Comparison
- Artificial Analysis — Grok 4.5 / MiniMax M2.7 / Gemini 3.1 Pro 分析

---

> **免责声明：** 本文数据来自公开评测报告、官方文档和第三方评测平台。模型参数、价格和评测分数可能随版本更新而变化。部分参数因公司未公开可能存在出入。SWE-bench Verified 已于 2026 年 2 月退役，本文引用的 Verified 分数仅供参考历史对比。评测分数可能因评测方法（few-shot、CoT、推理预算设定等）不同而有差异。
