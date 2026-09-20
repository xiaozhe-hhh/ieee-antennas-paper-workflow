# IEEE Antennas Paper Workflow：IEEE 天线论文全流程 Skill

这是一个面向 Codex 的 **IEEE 天线论文全流程编排 Skill**，重点服务于 `IEEE Transactions on Antennas and Propagation`（TAP）和 `IEEE Antennas and Wireless Propagation Letters`（AWPL）。它用于从天线研究问题定义、文献调研和论文精读，一直推进到 HFSS/实验/SAR 证据规划、英文论文写作、IEEEtran LaTeX 排版、审稿修改、语言润色和投稿检查。

本 Skill 的默认领域是天线与传播，默认稿件语言是英文。它负责识别当前阶段、调用合适的专用 Skill，并保持“天线论文主张 - 仿真/测量/理论/文献证据 - 来源位置”之间的可追溯关系。对于 TAP、AWPL 以外的 IEEE 期刊或会议，必须以对应 venue 的最新官方作者指南和模板为准。

本仓库只包含工作流编排层，不捆绑第三方 Skill、出版商模板、论文 PDF、用户稿件、HFSS 工程或实验数据。

## 主要功能

整个科研论文工作流被划分为 11 个阶段：

1. 研究问题定义
2. 文献检索
3. 论文精读
4. 科研思路发展
5. 证据与实验规划
6. 论文撰写
7. 科研图片制作
8. LaTeX 排版与编译
9. 技术、引用和格式审查
10. 技术内容冻结后的语言润色
11. 汇报材料制作与项目归档

Skill 会从最近一个有效成果和检查点继续工作，而不是每次从头开始。每个阶段都会记录输入、输出、所用 Skill、证据缺口、作者待确认事项和下一阶段。

## 核心原则

- 不编造文献、数据、尺寸、公式、实验条件、创新点或实验结果。
- 明确区分仿真、测量、理论计算和文献来源的证据。
- 写作前先把关键论断映射到对应证据和来源位置。
- 缺失事实使用 `[TO BE PROVIDED]` 标记，不根据常识擅自补全。
- 科研思路和预期结果在获得实际证据前只能标记为“待验证假设”。
- 技术内容冻结后才能进行语言润色，润色后必须复核事实是否被改变。
- 人工材料按当前任务逐步索取，不要求作者一次提交所有文件。

## 安装方法

### Windows PowerShell

可以直接从 GitHub 克隆到 Codex Skills 目录：

```powershell
$codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
New-Item -ItemType Directory -Force (Join-Path $codexRoot 'skills') | Out-Null
git clone https://github.com/xiaozhe-hhh/ieee-antennas-paper-workflow.git (Join-Path $codexRoot 'skills\ieee-antennas-paper-workflow')
```

如果已经下载了本仓库，也可以在仓库的上一级目录中复制安装：

```powershell
$codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
New-Item -ItemType Directory -Force (Join-Path $codexRoot 'skills') | Out-Null
Copy-Item -Recurse -Force '.\ieee-antennas-paper-workflow' (Join-Path $codexRoot 'skills')
```

### Linux 或 macOS

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/xiaozhe-hhh/ieee-antennas-paper-workflow.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/ieee-antennas-paper-workflow"
```

安装完成后，请重新启动 Codex 或新建一个会话，以刷新 Skill 发现结果。

## 使用方法

可以显式调用该 Skill：

```text
使用 $ieee-antennas-paper-workflow 判断我的 IEEE 天线论文当前处于哪个阶段，并从最近的有效成果继续推进。
```

常见任务示例：

```text
使用 $ieee-antennas-paper-workflow 阅读这些 TAP/AWPL 论文，并建立天线文献对比矩阵。
```

```text
使用 $ieee-antennas-paper-workflow 检查稿件中每项天线性能和机理主张需要哪些证据。
```

```text
使用 $ieee-antennas-paper-workflow 逐条处理这些审稿意见，不要编造缺失实验。
```

```text
使用 $ieee-antennas-paper-workflow 把当前 Word 稿件整理为 AWPL 的 IEEEtran LaTeX 项目。
```

论文正文默认使用英文；研究规划、阅读笔记和与作者的沟通可以使用中文。

## 人工材料如何提交

当论文工作依赖作者提供资料时，Skill 不会直接列出一份庞大的总清单，而是根据当前被阻塞的论断或阶段，请求一个最小材料包。

每轮材料请求会区分：

- **现在必须**：缺少后无法继续当前任务的材料；
- **有则更好**：能够提高分析质量，但暂时不阻塞工作的材料；
- **投稿前必须**：当前可以暂缓，但正式投稿前必须补齐的材料。

完整指南见[作者材料逐步交接指南](references/author-material-guide.md)。其中包含研究任务、文献、设计、仿真、测量、图表、稿件和审稿修改八类材料包，以及专门针对 IEEE 天线与 SAR 论文的清单。

## IEEE 天线与 SAR 核心能力

配合 `ieee-antennas-reader` 和 `ieee-antennas-writing` 使用时，本 Skill 可以支持 TAP、AWPL 等 IEEE 天线论文工作，包括：

- TAP/AWPL 文献检索、论文精读与 Paper Card；
- 天线结构、机理、工作频段和设计演化梳理；
- S 参数、效率、增益、方向图、ECC 和 SAR 证据规划；
- HFSS/AEDT 仿真条件与结果追溯；
- 单端口及多端口激励功率、幅相和终端条件检查；
- 体模、组织参数、平均质量、测试距离和 SAR 归一化检查；
- AWPL/TAP LaTeX 模板路由、编译和版面检查；
- 审稿意见逐条解释、补充实验规划、稿件修改和回复证据整理。

自由空间电流图只能用于相应的自由空间机理分析，不能单独证明 SAR 合规、多端口精确相位关系或人体模型中的场分布。

## 可选的专用 Skills

本 Skill 可以路由到独立安装的专用 Skills，例如：

- `research-paper-writing`
- `nature-academic-search` 和 `nature-literature-pipeline`
- `nature-paper-card` 和 `nature-reader`
- `ieee-antennas-reader` 和 `ieee-antennas-writing`
- `nature-figure` 和 `scibox-diagram`
- `nature-reviewer` 和 `nature-ref-verifier`
- `humanizer`
- PowerPoint 或其他演示文稿工具

这些 Skills 是可选组件，不会复制到本仓库。即使某个专用 Skill 未安装，工作流仍会按照相同的成果约定执行后备流程。具体路由规则见[Skill 路由表](references/skill-routing.md)。

## 仓库结构

```text
ieee-antennas-paper-workflow/
|-- SKILL.md                         # Skill 入口与核心约束
|-- README.md                        # 中文使用说明
|-- agents/
|   `-- openai.yaml                  # Codex 界面元数据
`-- references/
    |-- artifact-contracts.md        # 各阶段成果的数据约定
    |-- author-material-guide.md     # 作者材料逐步交接指南
    |-- quality-gates.md             # 质量门禁
    |-- skill-routing.md             # 专用 Skill 路由规则
    |-- skill-sources.md             # 外部 Skill 来源与安装说明
    `-- workflow-sop.md              # 全流程标准操作程序
```

## 成果与检查点

常用成果包括：

- Research Brief：研究问题、对象、约束、假设和成功标准；
- Paper Card：单篇论文的来源化精读记录；
- Literature Matrix：多篇论文的结构化比较矩阵；
- Claim-Evidence Map：逐项论断及其证据状态；
- Figure Brief：图片信息、数据来源、尺寸和导出要求；
- Manuscript Handoff：稿件、LaTeX、图片、引用和待办事项交接；
- Checkpoint：当前阶段、状态、输入、输出、缺口和下一阶段。

检查点状态使用：

- `complete`：当前阶段已完成；
- `partial`：已产生有效成果，但仍有证据缺口；
- `blocked`：缺少关键作者材料，当前结论无法继续。

## 质量门禁

出现以下情况时，不应把论文标记为可投稿：

- 引用或定量结论尚未核验；
- 图片无法追溯到原始数据；
- 仿真和测量条件不足以支持公平比较；
- LaTeX 存在未解析引用、缺失图片或明显版面问题；
- 稿件仍包含 `[TO BE PROVIDED]`；
- 语言润色改变了数值、公式、限定条件或技术含义；
- 审稿问题尚未解决，也未由作者明确接受为风险。

相关文档：

- [全流程 SOP](references/workflow-sop.md)
- [成果约定](references/artifact-contracts.md)
- [质量门禁](references/quality-gates.md)
- [Skill 路由表](references/skill-routing.md)

## 隐私与公开范围

请勿向本 Skill 仓库提交以下内容：

- 未公开论文和审稿意见；
- 无再分发权限的论文 PDF 或出版商模板；
- 私有实验数据、仿真工程和样机资料；
- 密钥、令牌、账号信息和本机绝对路径；
- 含作者隐私或合作单位保密信息的材料。

实际科研项目的证据、稿件和数据应保存在独立项目目录中，本仓库只保留通用工作流规则。

## 许可证

本仓库目前尚未选择开源许可证。在添加 `LICENSE` 文件前，第三方可以查看仓库内容，但默认不获得复制、修改或再分发授权。
