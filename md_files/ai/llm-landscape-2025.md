# 2025 年全球大模型全景汇总

> **编写时间：** 2025-08-02  
> **数据截止：** 2025 年 8 月初（部分模型信息更新至发布时的最新状态）  
> **说明：** 本文汇总国内外主流大模型的核心信息，包括模型名称、版本、参数规模、所属公司、性能评测、官方文档等，供大模型应用开发者参考。

---

## 目录

- [一、国际大模型](#一国际大模型)
  - [1.1 OpenAI — GPT / o 系列](#11-openai--gpt--o-系列)
  - [1.2 Anthropic — Claude 系列](#12-anthropic--claude-系列)
  - [1.3 Google — Gemini 系列](#13-google--gemini-系列)
  - [1.4 Meta — Llama 系列](#14-meta--llama-系列)
  - [1.5 xAI — Grok 系列](#15-xai--grok-系列)
  - [1.6 Mistral AI — Mistral 系列](#16-mistral-ai--mistral-系列)
- [二、国内大模型](#二国内大模型)
  - [2.1 深度求索 — DeepSeek 系列](#21-深度求索--deepseek-系列)
  - [2.2 阿里巴巴 — 通义千问 Qwen 系列](#22-阿里巴巴--通义千问-qwen-系列)
  - [2.3 百度 — 文心一言 ERNIE 系列](#23-百度--文心一言-ernie-系列)
  - [2.4 智谱 AI — GLM 系列](#24-智谱-ai--glm-系列)
  - [2.5 字节跳动 — 豆包 Doubao 系列](#25-字节跳动--豆包-doubao-系列)
  - [2.6 月之暗面 — Kimi 系列](#26-月之暗面--kimi-系列)
  - [2.7 腾讯 — 混元 Hunyuan 系列](#27-腾讯--混元-hunyuan-系列)
  - [2.8 科大讯飞 — 星火 Spark 系列](#28-科大讯飞--星火-spark-系列)
  - [2.9 MiniMax — MiniMax-01 系列](#29-minimax--minimax-01-系列)
  - [2.10 百川智能 — Baichuan 系列](#210-百川智能--baichuan-系列)
  - [2.11 零一万物 — Yi 系列](#211-零一万物--yi-系列)
- [三、核心评测基准说明](#三核心评测基准说明)
- [四、主要模型性能横评](#四主要模型性能横评)
- [五、总结与趋势](#五总结与趋势)
- [六、参考链接](#六参考链接)

---

## 一、国际大模型

### 1.1 OpenAI — GPT / o 系列

**公司：** OpenAI（美国）  
**官网：** [https://openai.com](https://openai.com)  
**API 文档：** [https://platform.openai.com/docs](https://platform.openai.com/docs)

#### 主要模型一览

| 模型 | 发布时间 | 参数规模 | 上下文窗口 | 最大输出 | 输入价格 | 输出价格 |
|------|----------|----------|-----------|----------|----------|----------|
| GPT-4o | 2024-05 | 未公开 | 128K | 16,384 | $2.50/M | $10.00/M |
| GPT-4o mini | 2024-07 | 未公开 | 128K | 16,384 | $0.15/M | $0.60/M |
| GPT-4.1 | 2025-04 | 未公开 | 1M | 32,768 | $2.00/M | $8.00/M |
| GPT-4.1 mini | 2025-04 | 未公开 | 1M | 32,768 | $0.40/M | $1.60/M |
| GPT-4.1 nano | 2025-04 | 未公开 | 1M | 32,768 | $0.10/M | $0.40/M |
| GPT-4.5 Preview | 2025-02 | 未公开 | 128K | — | $75.00/M | $150.00/M |
| o1 | 2024-12 | 未公开 | 200K | 100,000 | $15.00/M | $60.00/M |
| o1-mini | 2024-09 | 未公开 | 128K | 65,536 | $1.10/M | $4.40/M |
| o3-mini | 2025-01 | 未公开 | 200K | 100,000 | $1.10/M | $4.40/M |
| o3 | 2025-04 | 未公开 | 200K | 100,000 | $10.00/M | $40.00/M |
| o4-mini | 2025-04 | 未公开 | 200K | 100,000 | $1.10/M | $4.40/M |

> 注：价格单位为美元/百万 tokens。OpenAI 未公开 GPT-4 系列及 o 系列模型的具体参数量。

#### 关键性能与评测

**GPT-4.1 系列亮点（2025 年 4 月发布）：**

- **SWE-bench Verified：** GPT-4.1 得分 **54.6%**（GPT-4o 为 33.2%，提升 21.4 个百分点）
- **指令遵循（MultiChallenge）：** 38.3%（比 GPT-4o 高 10.5%）
- **指令遵循（IFEval）：** 87.4%（GPT-4o 为 81.0%）
- **长视频理解（Video-MME，无字幕）：** 72.0%
- **代码编辑（Aider Polyglot）：** 52-53%（GPT-4o 为 18-31%，约 2 倍提升）
- **前端编码：** 人类评估者 80% 偏好 GPT-4.1 超过 GPT-4o
- **不必要代码编辑：** 从 GPT-4o 的 9% 降低到 **2%**
- GPT-4.1 mini 在 MultiChallenge 和 MMMU 上超越完整版 GPT-4o
- GPT-4.1 nano MMLU 得分 **80.1%**，GPQA **50.3%**
- 推理速度比 GPT-4o 快 40%

**o3 / o4-mini（2025 年 4 月发布）：**

- **o3 SWE-bench Verified：** **69.1%**（不使用自定义脚手架），Thinking 模式 **74.9%**
- **o4-mini SWE-bench Verified：** **68.1%**
- **o3 GPQA Diamond：** **93.3%**（high compute）
- **o3 AIME 2024：** ~97%（high compute）
- **o4-mini HumanEval：** **99.3%**（high compute）
- o3/o4-mini 具备工具使用能力（Python 执行、网页搜索、文件分析），首次在推理过程中整合 Agent 行为

**GPT-4.5 Preview：**

- MMLU **90.8%**，强调对话流畅性和情感智能
- 定价极高（$75/$150），已于 2025 年 7 月 14 日从 API 下线，被 GPT-4.1 替代

---

### 1.2 Anthropic — Claude 系列

**公司：** Anthropic（美国）  
**官网：** [https://www.anthropic.com](https://www.anthropic.com)  
**API 文档：** [https://docs.anthropic.com](https://docs.anthropic.com)

#### 主要模型一览

| 模型 | 发布时间 | 参数规模 | 上下文窗口 | 最大输出 | 输入价格 | 输出价格 |
|------|----------|----------|-----------|----------|----------|----------|
| Claude 3.5 Sonnet | 2024-10 | 未公开 | 200K | 8,192 | $3.00/M | $15.00/M |
| Claude 3.5 Haiku | 2024-10 | 未公开 | 200K | 8,192 | $0.80/M | $4.00/M |
| Claude 3.7 Sonnet | 2025-02 | 未公开 | 200K | 64,000 | $3.00/M | $15.00/M |
| Claude Opus 4 | 2025-05 | 未公开 | 200K | 32,000 | $15.00/M | $75.00/M |
| Claude Sonnet 4 | 2025-05 | 未公开 | 200K | 64,000 | $3.00/M | $15.00/M |

> Anthropic 未公开任何 Claude 模型的具体参数量。Claude 4 系列支持扩展思考（Extended Thinking）。

#### 关键性能与评测

**Claude Opus 4（2025 年 5 月发布）：**

| 评测 | 基础 | 扩展思考 | 并行测试时计算 |
|------|------|----------|---------------|
| SWE-bench Verified | 72.5% | — | 79.4% |
| GPQA Diamond | 74.9% | 79.6% | 83.3% |
| MMLU | 91.0 | — | — |
| MATH | 86.0 | — | — |
| HumanEval | 88.4 / 94.5% | — | — |

**Claude Sonnet 4（2025 年 5 月发布）：**

| 评测 | 基础 | 扩展思考 | 并行测试时计算 |
|------|------|----------|---------------|
| SWE-bench Verified | 72.7% | — | 80.2% |
| GPQA Diamond | 70.0% | 75.4% | 83.8% |
| HumanEval | 85.2 / 95.1% | — | — |

**Claude 3.7 Sonnet（2025 年 2 月发布）：**

- SWE-bench Verified：**62.3%**
- HumanEval：**93.8%**
- 多语言基准：8 种语言中 6 种夺冠或并列第一
- 输出速度 ~78 tokens/s

**特点总结：**

- Claude 系列在 SWE-bench 编码评测中表现突出，Sonnet 4 基础分数 **72.7%** 处于行业领先
- Claude 3.5 Sonnet 在学术评测、多语言、指令遵循等精细化评估中长期领先
- Claude Opus 4 输出速度约 54 tok/s，价格是 Claude 3.7 Sonnet 的 5 倍
- Claude 4 系列引入 Summarized Thinking（用于安全审查）、思考与工具使用交替执行、一小时 Prompt 缓存等新能力

---

### 1.3 Google — Gemini 系列

**公司：** Google DeepMind（美国）  
**官网：** [https://deepmind.google](https://deepmind.google)  
**API 文档：** [https://ai.google.dev](https://ai.google.dev)

#### 主要模型一览

| 模型 | 发布时间 | 参数规模 | 上下文窗口 | 特点 |
|------|----------|----------|-----------|------|
| Gemini 1.5 Pro | 2024-05 | 未公开 | 2M | 多模态，长上下文 |
| Gemini 1.5 Flash | 2024-05 | 未公开 | 1M | 轻量快速版 |
| Gemini 2.0 Flash | 2025-02 | 未公开 | 1M | 新一代轻量模型 |
| Gemini 2.5 Pro | 2025-03 | 未公开 | 1M | 旗舰推理模型 |
| Gemini 2.5 Flash | 2025-07 | 未公开 | 1M | 新一代推理轻量版 |

> Gemini 2.5 Pro 为"思考模型"，推理阶段可展示思维过程。

#### 关键性能与评测

| 评测 | Gemini 2.5 Pro | Gemini 1.5 Pro | Gemini 2.0 Flash |
|------|---------------|---------------|------------------|
| SWE-bench Verified | ~63.8% | — | — |
| MMLU-Pro | 86.3% (HELM GPQA) | 76.3% | — |
| GPQA Diamond | 74.9% (估计) | 61.1% | — |
| HellaSwag | — | 92.2 | — |
| HumanEval | — | 71.9% | — |

- **Gemini 2.5 Pro** 在 SWE-bench 上得分 **63.8%**，领先 GPT-4.1，仅次于 Claude Sonnet 4
- **Gemini 1.5 Pro** 在 ScalingEval 跨类别综合评测中表现最佳
- Gemini 2.5 Pro 支持原生的多模态推理和工具使用
- Google 提供最具竞争力的免费额度（Gemini 2.5 Flash 免费层）

---

### 1.4 Meta — Llama 系列

**公司：** Meta（美国）  
**官网：** [https://llama.meta.com](https://llama.meta.com)  
**模型下载：** [https://huggingface.co/meta-llama](https://huggingface.co/meta-llama)

#### 主要模型一览

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 开源 |
|------|----------|--------|----------|------|--------|------|
| Llama 3.1 8B | 2024-07 | 8B | 8B | Dense | 128K | 开源 |
| Llama 3.1 70B | 2024-07 | 70B | 70B | Dense | 128K | 开源 |
| Llama 3.1 405B | 2024-07 | 405B | 405B | Dense | 128K | 开源 |
| Llama 3.3 70B | 2024-12 | 70B | 70B | Dense | 128K | 开源 |
| Llama 4 Scout | 2025-04 | 109B | 17B | MoE (16 专家) | 10M | 开源 |
| Llama 4 Maverick | 2025-04 | 400B | 17B | MoE (128 专家) | 1M | 开源 |
| Llama 4 Behemoth | 预览 | ~2T | 288B | MoE (16 专家) | — | 预览 |

#### 关键性能与评测

| 评测 | Llama 4 Maverick | Llama 3.1 405B | Llama 4 Scout |
|------|-----------------|----------------|---------------|
| MMLU | 85.5~89.4% | 88.6% | 79.6% |
| MMLU Pro | 80.5% | 73.2% | 74.3% |
| HumanEval | 87.9% | 89.0% | — |
| GPQA Diamond | — | 50.7% | — |
| LiveCodeBench | 43.4% | — | 32.8% |
| LMArena ELO | 1417 | — | — |

**Llama 4 Maverick 特点：**

- 活跃参数仅 17B（不到 DeepSeek V3 的一半），但在多项评测上超越 GPT-4o 和 Gemini 2.0 Flash
- 原生多模态（文本 + 图像 + 视频 + 音频）
- 推理和编码能力接近 DeepSeek V3
- 性价比在同类中突出

**Llama 4 Scout 特点：**

- **10M token 上下文窗口**，行业最长
- 可在单张 NVIDIA H100 上运行

**Llama 4 Behemoth（预览，仍在训练中）：**

- 活跃参数 288B，在多项 STEM 基准上超越 GPT-4.5、Claude Sonnet 3.7、Gemini 2.0 Pro

---

### 1.5 xAI — Grok 系列

**公司：** xAI（美国，Elon Musk 创立）  
**官网：** [https://x.ai](https://x.ai)  
**API 文档：** [https://docs.x.ai](https://docs.x.ai)

#### 主要模型一览

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 输入价格 | 输出价格 |
|------|----------|--------|----------|------|--------|----------|----------|
| Grok 2 | 2024-08 | 未公开 | 未公开 | MoE | 128K | — | — |
| Grok 3 | 2025-02 | ~600B | ~120B | MoE (16 专家) | 128K | $3.00/M | $15.00/M |
| Grok 3 mini | 2025-02 | 未公开 | 未公开 | MoE | 128K | $0.30/M | $1.50/M |

#### 关键性能与评测

| 评测 | Grok 3 | 说明 |
|------|--------|------|
| AIME 2024 | **93%** | 推理版，奥赛级别数学 |
| AIME 2025 | **93%** | 同上 |
| GPQA | **84.6%** | 研究生级科学推理 |
| LiveCodeBench | **79.4%** | 代码生成与修复 |
| MMLU | **89.0%** | 大规模多任务语言理解 |
| GSM8K | **95.0%** | 数学问题求解 |
| HumanEval | **70.0%** | 函数级代码生成 |
| Chatbot Arena | **1402 分** | 首个突破 1400 分的模型 |

**Grok 3 特点：**

- 使用 20 万张 GPU 训练（122 天 + 92 天两个阶段），训练算力是 Grok 2 的 10 倍
- 支持推理模式（Thinking/Big Brain），展示完整思维链
- DeepSearch 深度搜索功能对标 OpenAI Deep Research
- Chatbot Arena 排行榜首个突破 1400 分的模型
- Andrej Karpathy 评价：接近 o1-pro 水平，略优于 DeepSeek-R1

**局限：**

- xAI 未发布详细技术报告，所有评测分数均为自报
- 承诺等 Grok 3 稳定后开源 Grok 2
- HumanEval 仅 70.0%，编码能力在同类模型中偏弱

---

### 1.6 Mistral AI — Mistral 系列

**公司：** Mistral AI（法国）  
**官网：** [https://mistral.ai](https://mistral.ai)  
**API 文档：** [https://docs.mistral.ai](https://docs.mistral.ai)

#### 主要模型一览

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 开源协议 | 输入价格 | 输出价格 |
|------|----------|--------|----------|------|--------|----------|----------|----------|
| Mistral Large 2 | 2024-07 | 123B | 123B | Dense | 128K | Research License | $2.00/M | $6.00/M |
| Mistral Large 3 | 2025-12 | 675B | 41B | MoE (128 专家) | 256K | Apache 2.0 | $0.50/M | $1.50/M |

#### 关键性能与评测

| 评测 | Mistral Large 3 | Mistral Large 2 |
|------|----------------|-----------------|
| MMLU | ~85.5% | 84.0% |
| MMLU-Pro | 73.11% | — |
| MATH-500 | 93.6% | 71.5% (MATH) |
| HumanEval | — | 92.0% |
| GSM8K | — | 93.0% |
| 多语言 MMLU（中文） | — | 74.8% |

**Mistral Large 3 特点：**

- 总参数 675B 但每次仅激活 41B（MoE），推理成本大幅降低
- 首次在旗舰模型中支持原生多模态（文本 + 图像），含 2.5B 视觉编码器
- API 价格约为 Large 2 的 **1/6**
- 采用 **Apache 2.0 协议**，允许自由商业使用（Large 2 为限制性研究许可）
- 开源非推理模型 LMArena 排行榜排名第 2

---

## 二、国内大模型

### 2.1 深度求索 — DeepSeek 系列

**公司：** 深度求索（DeepSeek，杭州）  
**官网：** [https://www.deepseek.com](https://www.deepseek.com)  
**API 文档：** [https://platform.deepseek.com/api-docs](https://platform.deepseek.com/api-docs)  
**模型下载：** [https://huggingface.co/deepseek-ai](https://huggingface.co/deepseek-ai)

#### 主要模型一览

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 开源 | API 输出价格 |
|------|----------|--------|----------|------|--------|------|-------------|
| DeepSeek-V2 | 2024-05 | 236B | 21B | MoE | 128K | 开源 | — |
| DeepSeek-V3 | 2024-12 | 671B | 37B | MoE (256 专家) | 128K | 开源 | $0.27/M |
| DeepSeek-R1 | 2025-01 | 671B | 37B | MoE (256 专家) | 128K | 开源 | $2.19/M |
| DeepSeek-V3.2 | 2025 | 671B | 37B | MoE | 128K | 开源 | — |

#### 架构创新

- **Multi-head Latent Attention（MLA）：** KV Cache 压缩至标准注意力的 1/2~1/7，大幅降低显存带宽需求
- **DeepSeekMoE：** 256 个路由专家 + 1 个共享专家，每个 token 仅激活 8+1 个专家
- **FP8 混合精度训练：** 业界首个在万卡集群上验证 FP8 训练的前沿模型
- **DualPipe 流水线：** 计算与通信重叠，补偿受限的硬件互联带宽
- **训练成本：** V3 约 $557 万，R1 约 $600 万

#### 关键性能与评测

| 评测 | DeepSeek-V3 | DeepSeek-R1 |
|------|------------|-------------|
| MMLU | 87.2~90.2% | — |
| MMLU-Pro | 76.3% | — |
| HumanEval | 88.4% | 80.2% |
| MATH-500 | — | **97.3%** |
| GPQA Diamond | 59.1% | — |
| LiveCodeBench | 45.8~49.2% | — |
| SuperCLUE 基础模型 | 国内第 2（57.46 分） | — |
| Artificial Analysis 推理+知识 | 全球第 2 | — |

**DeepSeek-R1 特点：**

- 使用纯强化学习（GRPO）训练，无 SFT 预热，涌现出自我反思、自我纠正等长思维链行为
- MATH-500 得分 **97.3**，与 OpenAI o3-pro 同档
- 推理成本仅约 $6/百万 tokens，约为 o3-pro 的 **1/10**
- 蒸馏版覆盖 1.5B~70B，小模型即具备强推理能力
- SuperCLUE 幻觉控制 **81.71 分**（国内最高）

**DeepSeek-V3.2 特点：**

- 平衡推理与输出长度，面向日常问答和通用 Agent
- V3.2-Speciale 将开源推理能力推向极致

**综合评价：** "性价比革命"的代表，以约 1/30 的推理成本匹配 GPT-4 级性能，永久改变了前沿 AI 的经济学模型。

---

### 2.2 阿里巴巴 — 通义千问 Qwen 系列

**公司：** 阿里巴巴（Alibaba，杭州）  
**官网：** [https://tongyi.aliyun.com](https://tongyi.aliyun.com)  
**模型下载：** [https://huggingface.co/Qwen](https://huggingface.co/Qwen)  
**API 文档：** [https://help.aliyun.com/zh/model-studio](https://help.aliyun.com/zh/model-studio)

#### 主要模型一览

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 开源 |
|------|----------|--------|----------|------|--------|------|
| Qwen2.5-72B | 2024-09 | 72B | 72B | Dense | 128K | 开源 |
| Qwen2.5-Max | 2025-01 | 未公开 | 未公开 | MoE | 32K | 闭源 |
| QwQ-32B | 2025-03 | 32B | 32B | Dense | 131K | 开源 |
| Qwen3-8B | 2025-04 | 8B | 8B | Dense | 32K | 开源 |
| Qwen3-32B | 2025-04 | 32.8B | 32.8B | Dense | 32K | 开源 |
| Qwen3-30B-A3B | 2025-04 | 30.5B | 3.3B | MoE | 32K | 开源 |
| Qwen3-235B-A22B | 2025-04 | 235B | 22B | MoE | 130K | 开源 |
| Qwen3-Max | 2025-09 | 未公开 | 未公开 | 未公开 | 262K | 闭源 |
| Qwen3-Coder | 2025 | 未公开 | 未公开 | MoE | — | 开源 |

#### 关键性能与评测

**Qwen3-235B-A22B-Instruct-2507：**

- SuperCLUE 基础模型 **60.79 分**，**国内第 1、全球第 1**
- 数学推理 **64.57 分**（GPT-4o 仅 29.77 分，高出 34.8 分）
- 代码生成 **78.42 分**
- Agent 能力 **80.97 分**

**QwQ-32B（推理模型）：**

- LiveBench 综合得分 **92.3**，超越 GPT-4.5
- 参数仅为 DeepSeek-R1 的 1/21，推理速度高达 1200 tokens/s

**Qwen2.5-Max：**

- Chatbot Arena 盲测全球第 7，超越 DeepSeek-V3 和 o3-mini
- 数学与编程斩获单项冠军

**Qwen3-110B：**

- HumanEval+ 得分 **94.1**，刷新开源纪录

**Qwen 系列特点：**

- 模型矩阵最完整：从 0.5B 到 235B，全尺寸覆盖（Apache 2.0 全开源）
- 所有 Qwen3 模型支持双模式（思考/非思考），无需单独推理模型
- 预训练数据翻倍至 **36T tokens**（Qwen2.5 为 18T+）
- 支持 100+ 语言，针对 Agent 和 MCP 工作流优化
- "开源 + 云" 双轮驱动，多模态 Qwen2.5-VL 万物皆可 Token 化

---

### 2.3 百度 — 文心一言 ERNIE 系列

**公司：** 百度（Baidu，北京）  
**官网：** [https://yiyan.baidu.com](https://yiyan.baidu.com)  
**API 文档：** [https://cloud.baidu.com/doc/WENXINWORKSHOP/index.html](https://cloud.baidu.com/doc/WENXINWORKSHOP/index.html)

#### 主要模型一览

| 模型 | 发布时间 | 参数规模 | 上下文 | 开源 |
|------|----------|----------|--------|------|
| 文心大模型 4.0 Turbo | 2024 | 未公开 | — | 闭源 |
| 文心大模型 X1 | 2025-01 | 未公开 | — | 闭源 |
| 文心大模型 X1 Turbo | 2025 | 未公开 | — | 闭源 |
| ERNIE 4.5-8B | 2025 | 8B | — | 开源 |
| ERNIE 4.5-30B | 2025 | 30B | — | 开源 |

#### 关键性能与评测

- **X1 Turbo** C-Eval STEM **89.4 分**，结合亿级知识图谱使事实性问答错误率仅 **3.1%**（低于 GPT-5 的 4.7%）
- **ERNIE 4.5 30B** GSM8K 得分 **95.1**，创国产开源模型数学推理新高；FLOPs 利用率达 47%
- 2025 年 4 月起文心一言全面免费，深度搜索功能同步免费开放

**特点总结：**

- 搜索引擎积累的亿级知识图谱为核心护城河，事实性问答可靠性领先
- 中华文化内容生成能力突出
- "最懂行业的大模型"，在金融、教育、油气、电力、钢铁等行业深度优化

---

### 2.4 智谱 AI — GLM 系列

**公司：** 智谱 AI（Zhipu AI，北京，清华系）  
**官网：** [https://open.bigmodel.cn](https://open.bigmodel.cn)  
**模型下载：** [https://huggingface.co/THUDM](https://huggingface.co/THUDM)

#### 主要模型一览

| 模型 | 发布时间 | 参数规模 | 上下文 | 开源 |
|------|----------|----------|--------|------|
| GLM-4 / GLM-4-Plus | 2024 | 未公开 | 128K | 闭源 |
| GLM-4V-Plus | 2024 | 未公开 | — | 闭源（支持 2h 长视频理解） |
| GLM-Zero-Preview | 2025 | 未公开（推理模型） | — | 闭源 |
| GLM-4.5 | 2025 | 未公开 | — | 开源 |
| GLM-4.7 | 2025 | 未公开 | — | 开源 |

#### 关键性能与评测

- **GLM-4.5** Hugging Face 总榜**登顶全球开源第 1**，融合推理、编码和 Agent 能力
- **GLM-4.7** Vals Index 编程榜单**开源模型第 1**，Design Arena 胜率和 Elo 评分紧追 Gemini
- 参数规模从 5 万亿 → 10 万亿级翻倍增长，推理精度提升至 98.5%

**特点总结：**

- 清华系背景，中文理解能力极为出色（古典文学到网络用语全覆盖）
- 国内首个支持视频通话的千亿参数模型
- 学术审稿助手功能独特
- GLM-4-Plus-Web 支持联网搜索和代码解释器

---

### 2.5 字节跳动 — 豆包 Doubao 系列

**公司：** 字节跳动（ByteDance，北京）  
**官网：** [https://www.doubao.com](https://www.doubao.com)  
**API 文档：** [https://www.volcengine.com/docs/82379](https://www.volcengine.com/docs/82379)

#### 主要模型一览

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 |
|------|----------|--------|----------|------|--------|
| Doubao-1.5-pro | 2025 | 490B | 7B | MoE (稀疏) | 32K/256K |
| Doubao-Seed-1.6-thinking | 2025 | 未公开 | 未公开 | 未公开 | — |
| 豆包实时语音大模型 | 2025 | 未公开 | 未公开 | 未公开 | — |

#### 关键性能与评测

- **Doubao-Seed-1.6-thinking-250715** SuperCLUE 中文综合能力全球第 3（仅次于 OpenAI o3 和 o4-mini），代码生成 36.9 分
- **豆包 1.5-pro** 中文 C-Eval 得分 **86.9**，超 GPT-5 中文 1.8 分
- 利用稀疏 MoE 架构，仅激活 1/7 参数即打平等效 Dense 模型，性能杠杆达 **7 倍**，训练成本降 62%
- 实时语音模型端到端延迟 **320ms**，情感识别 F1=0.81，比 GPT-4o 高 6 个百分点
- MMLU、GSM8K 等多项评测超越 GPT-4o 与 Claude 3.5 Sonnet

**商业数据：**

- 日均 Token 使用量突破 **50 万亿**，中国第 1、全球第 3
- 截至 2025 年 11 月 MAU 达 **1.47 亿**，仅次于 ChatGPT 全球第 2

**特点总结：**

- "流量 → 数据 → 模型" 闭环最完整
- 多模态能力突出（视觉 + 语音 + 控制三模态融合）
- 国内唯一不靠卖云即可盈利的大模型

---

### 2.6 月之暗面 — Kimi 系列

**公司：** 月之暗面（Moonshot AI，北京）  
**官网：** [https://kimi.moonshot.cn](https://kimi.moonshot.cn)  
**模型下载：** [https://huggingface.co/moonshotai](https://huggingface.co/moonshotai)

#### 主要模型一览

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 开源 |
|------|----------|--------|----------|------|--------|------|
| moonshot-v1 系列 | 2024 | 未公开 | 未公开 | — | 128K | 闭源 |
| k1.5 多模态思考 | 2025-01 | 未公开 | 未公开 | — | — | 闭源 |
| Kimi K2-Instruct | 2025-07 | 1T | 32B | MoE (384 专家) | 128K | 开源 (MIT) |
| Kimi K2-Instruct-0905 | 2025-09 | 1T | 32B | MoE | 256K | 开源 (MIT) |
| Kimi K2 Thinking | 2025-11 | 1T | 32B | MoE | 256K | 开源 (MIT) |

#### 关键性能与评测

| 评测 | K2-0905 | K2-0711 | 对比参考 |
|------|---------|---------|---------|
| SWE-bench Verified | **69.2%** | 65.8% | Claude Sonnet 4: 72.7% |
| SWE-bench Multilingual | **55.9%** | 47.3% | Qwen3-Coder: 54.7% |
| Terminal-Bench | **44.5%** | 37.5% | Claude Opus 4: 43.2% |
| SWE-Dev | **66.6%** | 61.9% | Claude Sonnet 4: 67.1% |
| Multi-SWE-bench | **33.5%** | 31.3% | Claude Sonnet 4: 35.7% |

**Kimi K2 Thinking：**

- Humanity's Last Exam **44.9%**，超越 GPT-5 和 Claude Sonnet 4.5
- BrowseComp 自主网络浏览 **60.2%**，刷新纪录
- τ-Bench Telecom Agent 工具使用 **93%**

**特点总结：**

- Kimi K2 为国内代码和 Agent 能力最强模型之一（SWE-bench 仅次于 Claude Sonnet 4）
- 超长上下文处理标杆（K2 支持 256K，早期版本支持 200 万汉字）
- 自研 MuonClip 优化器，训练零崩溃
- MIT 协议开源，允许免费商业使用
- "模型即 Agent" 设计理念，K2 Thinking 可执行 200-300 次连续工具调用

---

### 2.7 腾讯 — 混元 Hunyuan 系列

**公司：** 腾讯（Tencent，深圳）  
**官网：** [https://hunyuan.tencent.com](https://hunyuan.tencent.com)  
**模型下载：** [https://huggingface.co/tencent](https://huggingface.co/tencent)

#### 主要模型一览

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 开源 |
|------|----------|--------|----------|------|--------|------|
| Hunyuan-Large 389B | 2025-03 | 389B | 52B | MoE | 256K | 开源 |
| Hunyuan 0.5B~7B 系列 | 2025-07 | 0.5B~7B | 0.5B~7B | Dense | 256K | 开源 |
| Tencent HY 2.0 | 2025-12 | 406B | 32B | MoE | 256K | 闭源 |

#### 关键性能与评测

**Hunyuan-Large 389B：**

- 开源中参数规模最大的 MoE Transformer
- 7T tokens 预训练（含 1.5T 高质量合成数据）
- 基座模型在多个数据集上领先 Llama 3.1-405B 和 DeepSeek-V2

**Hunyuan 7B-Instruct：**

| 评测 | 分数 |
|------|------|
| MMLU | 79.82 |
| AIME 2024 | **81.1**（超越 o1-mini 和 Qwen3-8B） |
| MATH | 93.7 |
| LiveCodeBench | 57.0 |
| GPQA Diamond | 60.1 |

**Tencent HY 2.0（2025 年 12 月旗舰）：**

- IMO-AnswerBench、HMMT2025、HLE、ARC-AGI 等权威测试国内第一梯队
- 引入长度惩罚策略，单位 token "智能密度" 业界领先
- RLVR+RLHF 双阶段强化学习，文本创作告别 "AI 味"
- 已在元宝、ima 等腾讯应用接入

**特点总结：**

- 形成 0.5B 到 406B 的完整模型矩阵
- 小模型端侧部署能力强，7B 在数学推理上超越 o1-mini
- 原生 256K 超长上下文，旗舰模型量化后性能几乎无损

---

### 2.8 科大讯飞 — 星火 Spark 系列

**公司：** 科大讯飞（iFlytek，合肥）  
**官网：** [https://xinghuo.xfyun.cn](https://xinghuo.xfyun.cn)  
**API 文档：** [https://www.xfyun.cn/doc/spark](https://www.xfyun.cn/doc/spark)

#### 主要模型一览

| 模型 | 发布时间 | 参数规模 | 上下文 | 开源 |
|------|----------|----------|--------|------|
| 星火 4.0 Turbo | 2024-10 | 未公开（万亿参数训练平台） | — | 闭源 |
| 星火深度推理 X1 | 2025-01 | 70B（另有 175B 说法） | — | 闭源 |

#### 关键性能与评测

- 斯坦福 HAI 2025 报告 MixEval-Hard 基准中，**唯一入围前十的国产大模型**（第 10 名）
- 14 项主流测试集中 **9 项超越 GPT-4o**、Claude 3.5 Sonnet、Gemini 1.5 Pro
- 数学能力提升 10.5%，超越 GPT-4o；C++ 编码能力超越 GPT-4o
- 知识回复错误率降低 40%，句子级知识溯源准确率 **90%**
- X1 深度推理模型以 70B 参数追平 o1 和 DeepSeek-R1
- **全部在国产算力平台（飞星一号/二号，联合华为打造）上实现训练**

**特点总结：**

- "最懂行业的大模型"，在金融、油气、电力、钢铁、航司等行业综合能力提升超 10%
- 全栈国产自主可控（算力 + 框架 + 模型）
- 文档理解速度提升 10 倍以上（500 页扫描到解析仅需 2 分钟）

---

### 2.9 MiniMax — MiniMax-01 系列

**公司：** MiniMax（上海）  
**官网：** [https://www.minimaxi.com](https://www.minimaxi.com)  
**模型下载：** [https://github.com/MiniMax-AI](https://github.com/MiniMax-AI)

#### 主要模型

| 模型 | 发布时间 | 总参数 | 活跃参数 | 架构 | 上下文 | 开源 | API 输入 | API 输出 |
|------|----------|--------|----------|------|--------|------|----------|----------|
| MiniMax-01 | 2025-01 | 456B | 45.9B | MoE (32 专家) | 4M | 开源 | ¥1/M | ¥8/M |

#### 关键性能与评测

- 在大多数主流文本和多模态理解任务上，追平 GPT-4o-1120 和 Claude 3.5 Sonnet
- **400 万 token 上下文窗口**，是 GPT-4o 的 32 倍、Claude 3.5 Sonnet 的 20 倍
- Needle-In-A-Haystack 400 万 token 全绿检索
- 随输入长度增加，性能衰减最慢（优于 Google Gemini）
- H20 GPU 上 MFU 达 75%

**架构创新：**

- 业内**首次将线性注意力（Lightning Attention）大规模部署**到商用模型级别
- 每 8 层中 7 层使用线性注意力 + 1 层传统 Softmax 注意力
- 打破传统 Transformer 的 O(n²) 复杂度瓶颈，接近线性复杂度

---

### 2.10 百川智能 — Baichuan 系列

**公司：** 百川智能（Baichuan Intelligence，北京，王小川创立）  
**官网：** [https://www.baichuan-ai.com](https://www.baichuan-ai.com)  
**模型下载：** [https://huggingface.co/baichuan-inc](https://huggingface.co/baichuan-inc)

#### 主要模型

| 模型 | 发布时间 | 参数规模 | 定位 | 开源 |
|------|----------|----------|------|------|
| Baichuan-M1 | 2025-01 | 14B | 医疗增强推理模型 | 开源 |
| Baichuan-M2 | 2025-08 | 32B | 医疗增强推理旗舰 | 开源 |

#### 关键性能与评测

**HealthBench 标准版（5000 条多轮对话）：**

| 排名 | 模型 | 得分 |
|------|------|------|
| 1 | GPT-5-Thinking | 67.2 |
| **2** | **Baichuan-M2 (32B)** | **60.1** |
| 3 | Qwen3-235B-A22B-Thinking | 55.2 |
| 4 | Grok 3 | 54.3 |
| 5 | DeepSeek-R1-0528 | 53.6 |

**HealthBench Hard（1000 高难度样本）：**

- Baichuan-M2 得分 **34.7**，全球第二款超 32 分的模型（GPT-5 为第一款）
- 超越 o3、Grok 3、Gemini 2.5 Pro、GPT-4.1 等所有闭源模型

**部署优势：**

- 支持 RTX 4090 单卡部署（4bit 量化），成本降至 DeepSeek-R1 H20 双节点的 **1/57**
- MTP 版本推理速度提升 74.9%
- 已完成国产主流芯片适配

---

### 2.11 零一万物 — Yi 系列

**公司：** 零一万物（01.AI，北京，李开复创立）  
**官网：** [https://www.01.ai](https://www.01.ai)  
**API 文档：** [https://platform.01.ai](https://platform.01.ai)

#### 主要模型

| 模型 | 发布时间 | 参数规模 | 架构 | 上下文 | 开源 |
|------|----------|----------|------|--------|------|
| Yi-Lightning | 2024-10 | 未公开 | MoE + 混合注意力 + 动态 Top-P 路由 | 32K | 闭源 |
| Yi-Lightning 34B MoE | 2024 | 34B | MoE（蒸馏版） | — | 开源 |

#### 关键性能与评测

- **LMSYS Chatbot Arena 全球总排名第 6，中国第 1**（发布时），首个超越 GPT-4o 的国产大模型
- Arena 得分 **1287 分**，与 GPT-4o-0513 持平
- 中文能力第 2、多轮对话第 3、数学推理第 3、编程第 4
- API 定价 **¥0.99/百万 tokens**（输入和输出），性价比极高

| 评测 | 分数 |
|------|------|
| MATH | 76.4 |
| HumanEval | 83.5 |
| IFEval | 81.9 |
| Arena-Hard | 91.8 |

**特点总结：**

- 训练成本仅约 300 多万美元（约 2000 张 GPU，1.5 个月）
- 跨层 KV 缓存共享技术使长文本内存需求降低 82.8%
- 2025 年战略转向：全面拥抱 DeepSeek，提供企业级一站式部署平台

---

## 三、核心评测基准说明

| 基准名称 | 全称 | 评测维度 | 说明 |
|----------|------|----------|------|
| **MMLU** | Massive Multitask Language Understanding | 多任务知识理解 | 涵盖 57 个学科的多选题评测，测试模型的世界知识广度 |
| **MMLU-Pro** | MMLU Professional | 专业知识推理 | MMLU 升级版，题目更难，区分度更高 |
| **GPQA Diamond** | Graduate-Level Google-Proof Q&A | 研究生级科学推理 | 生物/物理/化学博士级题目，Google 搜索也难以直接找到答案 |
| **HumanEval** | Human Evaluation | 代码生成 | 164 道 Python 函数补全题，Pass@1 评分 |
| **HumanEval+** | HumanEval Plus | 增强代码评测 | HumanEval 增强版，测试用例更严格 |
| **MATH** | Mathematics Aptitude Test of Heuristics | 数学推理 | 竞赛级数学题目（MATH-500 为精选子集） |
| **GSM8K** | Grade School Math 8K | 中小学数学 | 8,500 道小学数学应用题 |
| **AIME** | American Invitational Mathematics Exam | 奥赛数学 | 美国数学邀请赛真题，难度极高 |
| **SWE-bench Verified** | Software Engineering Benchmark | 软件工程 | 真实 GitHub Issue 的 bug 修复任务，评测端到端编程能力 |
| **LiveCodeBench** | Live Code Benchmark | 代码竞赛 | 近期的编程竞赛题目，数据污染风险低 |
| **C-Eval** | Chinese Evaluation | 中文综合能力 | 面向中文的多学科评测 |
| **SuperCLUE** | Super Chinese Language Understanding Evaluation | 中文综合能力 | 国内权威中文大模型评测榜单 |
| **HLE** | Humanity's Last Exam | 终极推理 | 当前最难的前沿评测，涵盖极难题目 |
| **Chatbot Arena** | LMSYS Chatbot Arena | 人类偏好 | 基于人类盲测投票的 ELO 评分排行榜 |

---

## 四、主要模型性能横评

### 4.1 国际模型核心评测对比

| 模型 | MMLU | GPQA Diamond | HumanEval | MATH | SWE-bench Verified |
|------|------|-------------|-----------|------|-------------------|
| OpenAI o3 (high) | — | **93.3** | 98.1 | 83.4* | 69.1 / 74.9† |
| OpenAI o4-mini (high) | — | 90.3 | **99.3** | 81.3* | 68.1 |
| GPT-4.5 Preview | **90.8** | 69.5 | 88.6 | 87.1 | — |
| GPT-4.1 | 90.2 | 66.3 | 94.5 | 82.1 | 54.6 |
| GPT-4o (Nov 2024) | 85.7 | 46.0 | 90.2 | 68.5 | 33.2 |
| Claude Opus 4 | 91.0 | 74.9~83.3‡ | 88.4~94.5 | 86.0 | 72.5 / 79.4‡ |
| Claude Sonnet 4 | — | 70.0~83.8‡ | 85.2~95.1 | — | 72.7 / 80.2‡ |
| Claude 3.7 Sonnet | 89.5 | 59.4 | 93.8 | 83.0 | 62.3 |
| Gemini 2.5 Pro | 86.3† | 74.9 | — | — | ~63.8 |
| Grok 3 | 89.0 | 84.6 | 70.0 | — | — |
| Llama 4 Maverick | 85.5~89.4 | — | 87.9 | — | — |
| Llama 3.1 405B | 88.6 | 50.7 | 89.0 | 73.8 | — |

> `*` = MATH-500 评分。`†` = MMLU-Pro 评分。`‡` = 基础分数 / 扩展思考或并行测试时计算分数。  
> 空格表示该模型无权威第三方评测数据。分数可能因评测方法（few-shot、CoT 等）不同而有差异。

### 4.2 国内模型核心评测对比

| 模型 | SuperCLUE | 关键亮点 |
|------|-----------|---------|
| Qwen3-235B-A22B | **60.79**（国内第1） | 数学推理 64.57，代码 78.42，Agent 80.97 |
| DeepSeek-V3-0324 | 57.46（国内第2） | 幻觉控制 81.71（国内最高） |
| Kimi-K2-0711 | 56.90（国内第3） | 代码生成 80.00（国内最高） |
| DeepSeek-R1 | — | MATH-500 97.3，推理全球顶级 |
| QwQ-32B | — | LiveBench 92.3，超越 GPT-4.5 |
| ERNIE 4.5 30B | — | GSM8K 95.1，国产开源数学新高 |
| Doubao-Seed-1.6-thinking | 全球第3（中文综合） | 代码生成 36.9 |
| Yi-Lightning | Arena 1287/全球第6 | 首个超越 GPT-4o 的国产模型 |

### 4.3 开源模型综合对比（Hugging Face / LMArena 排行榜参考）

| 排名 | 模型 | 亮点 |
|------|------|------|
| 1 | GLM-4.5 | Hugging Face 总榜登顶 |
| 2 | Qwen3-235B-A22B | SuperCLUE 全球第 1，模型矩阵最完整 |
| 3 | DeepSeek-V3 | 性价比之王，671B MoE，全球开源最有影响力 |
| 4 | Kimi K2 | SWE-bench 开源最强之一，MIT 协议 |
| 5 | Llama 4 Maverick | 400B MoE，原生多模态 |

---

## 五、总结与趋势

### 5.1 2025 年大模型核心趋势

1. **MoE 架构全面普及：** 从 DeepSeek-V3 到 Qwen3、Llama 4、Kimi K2、Mistral Large 3，混合专家架构已成为模型标准配置，以更少的活跃参数实现更强性能
2. **推理模型成为新赛道：** OpenAI o 系列、DeepSeek-R1、QwQ-32B、Kimi K2 Thinking、GLM-Zero 等推理/思考模型纷纷涌现，通过强化学习和测试时计算大幅提升复杂问题解决能力
3. **性价比竞争白热化：** DeepSeek 以约 1/30 的成本匹配 GPT-4 级性能，倒逼全行业降价；GPT-4.1 比 GPT-4o 成本降 26%，Mistral Large 3 价格仅为前代的 1/6
4. **超长上下文成为标配：** MiniMax-01 支持 400 万 tokens，Llama 4 Scout 支持 10M tokens，GPT-4.1 全系支持 1M tokens
5. **Agent 能力深度整合：** o3/o4-mini 原生支持工具调用，Kimi K2 "模型即 Agent"，Qwen3 针对 MCP 优化——Agent 能力正在从外挂变成模型内在能力
6. **中国大模型全面崛起：** Qwen3-235B 登顶 SuperCLUE 全球第一，DeepSeek 改变全球 AI 经济学，Kimi K2 编码能力紧追 Claude，多个国内模型在各自优势领域达到或超越国际顶尖水平
7. **开源生态蓬勃发展：** 从 Meta、Alibaba、DeepSeek 到 Kimi、Baidu、Tencent，几乎所有主流厂商都在拥抱开源（Apache 2.0 / MIT 等宽松协议）

### 5.2 选型建议（面向开发者）

| 场景 | 推荐国际模型 | 推荐国内模型 |
|------|-------------|-------------|
| **通用对话与内容生成** | Claude Sonnet 4、GPT-4.1 | Qwen3-235B、DeepSeek-V3 |
| **复杂推理与数学** | OpenAI o3、Claude Opus 4 | DeepSeek-R1、QwQ-32B |
| **代码生成与软件工程** | Claude Sonnet 4、o4-mini | Kimi K2、Qwen3-Coder |
| **超长上下文处理** | Gemini 2.5 Pro (1-2M) | MiniMax-01 (4M)、Kimi K2 (256K) |
| **高性价比 API 调用** | GPT-4.1 nano、Gemini 2.5 Flash | DeepSeek-V3、Yi-Lightning |
| **端侧/小模型部署** | Llama 3.1 8B | Qwen3-8B、Hunyuan 7B |
| **中文场景** | Claude 3.5 Sonnet | Qwen3、DeepSeek、GLM-4.5 |
| **垂直领域（医疗等）** | GPT-4.1 + RAG | Baichuan-M2 |
| **全栈国产自主可控** | — | 讯飞星火、DeepSeek（国产芯片适配） |

---

## 六、参考链接

### 评测平台与排行榜

- [LMSYS Chatbot Arena](https://chat.lmsys.org/) — 人类盲测 ELO 排行榜
- [SuperCLUE](https://www.cluebenchmarks.com/superclue.html) — 中文大模型权威评测
- [Artificial Analysis](https://artificialanalysis.ai/) — 模型质量/速度/价格综合对比
- [OpenRouter Rankings](https://openrouter.ai/rankings) — 开源/商业模型使用排行
- [Hugging Face Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) — 开源模型评测
- [SWE-bench](https://www.swebench.com/) — 软件工程评测
- [LiveBench](https://livebench.ai/) — 实时模型评测（防数据污染）
- [BenchGecko](https://benchgecko.ai/) — 多维度模型 Benchmark 查询

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
- 百川智能: [https://www.baichuan-ai.com](https://www.baichuan-ai.com)
- 零一万物: [https://www.01.ai](https://www.01.ai)

### 评测报告与数据来源

- 斯坦福 HAI 2025 AI Index Report
- JRC Technical Report — LLM Composite Index (PCA-based, 2025-02)
- Meta-analysis of LLMs: Benchmarking DeepSeek-R1 (Journal of Big Data, 2025)
- SuperCLUE 2025 上半年/7 月评测报告
- OpenAI simple-evals Repository
- TokenCalculator LLM Benchmarks (2026)

---

> **免责声明：** 本文数据来自公开评测报告、官方文档和第三方评测平台，模型参数、价格和评测分数可能随版本更新而变化。部分参数和评测分数因公司未公开或评测方法差异可能存在出入，仅供参考。
