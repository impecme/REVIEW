# BSPDN 文献阅读矩阵与创新点

## 1 筛选说明

本矩阵围绕 BSPDN 主题组织 20 篇文献，分为三类：

1. **核心 BSPDN 文献**：直接研究背面供电、背面电源分配、背面布线、nTSV、背面对准和热管理。
2. **关键支撑文献**：研究 GAAFET/nanosheet、CFET、NanoStack、Flip FET 等后 FinFET 结构，因为 BSPDN 的导入对象正是这些先进器件平台。
3. **设计协同文献**：研究 DTCO、PPAC、双面互连、标准单元和系统级热分析。

企业官网、新闻稿和技术文章不进入引用体系。

## 2 20 篇文献矩阵

| 序号 | 文献方向 | 文献 | 与 BSPDN 的关系 | 可提炼创新点 |
|---|---|---|---|---|
| [1] | 核心结构 | Xie et al., VLSI 2024, Backside power distribution for nanosheet technologies beyond 2nm | 直接比较 BSPDN 集成路线 | DBC/SABC 支持 cell-level scaling |
| [2] | 背面布线 | Subramani et al., VLSI 2025, Backside routing enablement considerations for advanced node GAA devices | 从 BSPDN 扩展到 backside routing | 背面层可用于 power/clock/signal |
| [3] | nTSV/对准 | Zhao et al., IEEE TED 2024, Mo-filled slit nTSV | BSPDN 背面连接工艺 | slit nTSV 放宽 overlay |
| [4] | nTSV 刻蚀 | Wang et al., Microelectronic Engineering 2024 | BSPDN nano-TSV 可靠互连 | 平滑侧壁、Ru 金属化 |
| [5] | 热管理 | Xie, Chen and Wei, ECTC 2024 | BSPDN 热缓解 | 微通道和双面冷却 |
| [6] | 互连缩放 | Lanzillo et al., ASMC 2025 | NanoStack 互连与 BSPDN 约束 | AP/DFM/DTCO 协同 |
| [7] | 三维互连 | Banerjee et al., Proceedings of the IEEE 2001 | 垂直维度缓解互连瓶颈 | 3D IC interconnect |
| [8] | 晶圆键合 | Fan et al., Electrochemical and Solid-State Letters 1999 | 背面/三维连接的键合基础 | Cu wafer bonding |
| [9] | CFET inverter | Liao et al., IEDM 2024 | 垂直堆叠 CMOS 与背面连接需求 | monolithic CFET inverter |
| [10] | CFET inverter | Liao et al., IEDM 2023 | stacked nanosheet inverter 基础 | monolithic CFET |
| [11] | 2.5D 集成 | Zhang et al., Applied Physics Reviews 2015 | BSPDN 与 2.5D/3D 系统热互连背景 | silicon interposer |
| [12] | GAAFET 平台 | Yeap et al., IEDM 2024 | BSPDN 主要面向 nanosheet/GAA 平台 | 2 nm 平台器件-互连协同 |
| [13] | 多阈值 nanosheet | Bao et al., IEDM 2024 | BSPDN 导入对象的器件基础 | 多 Vt 与低功耗库 |
| [14] | pFET nanosheet | SiGe channel for scaled GAA nanosheet pFET, IEDM 2025 | 支撑 GAA 平台性能 | SiGe 沟道改善 pFET |
| [15] | CFET | Demuynck et al., VLSI 2024 | 后 GAAFET 垂直堆叠器件 | MDI 与 stacked contacts |
| [16] | CFET 接触 | Vega Gonzalez et al., IITC 2024 | CFET 中段接触集成 | MOL stacked contacts |
| [17] | CFET + 背面接触 | Vandooren et al., IEDM 2024 | 背面接触与 CFET 缩放 | direct backside contact for CFET |
| [18] | stacked inverter | Park et al., VLSI 2024 | 垂直堆叠 nanosheet inverter 与背面互连需求 | stacked complementary nanosheet |
| [19] | CFET 缩放 | Xiong and Wu, Nature Electronics 2024, Building inverters with stacked complementary nanosheet transistors | BSPDN 后续承接 CFET/垂直互连需求 | stacked complementary nanosheet inverter |
| [20] | 先进封装/热可靠性 | Sheikh et al., IEEE Solid-State Circuits Magazine 2021, 2.5D and 3D heterogeneous integration | BSPDN 与封装散热、异质集成耦合 | chiplet/heterogeneous integration 热管理 |

## 3 核心结论

## 3.1 BSPDN 的研究主线

现有文献表明，BSPDN 研究经历了三个层次。

第一层是**供电路径重构**。其核心问题是把电源网络从正面迁移到背面，以降低供电阻抗和释放正面布线资源。[1]、[3]、[4] 是这一层的代表。

第二层是**标准单元和背面布线协同**。BSPDN 不仅影响 IR drop，也影响 cell height、pin access、routing 和 block-level PPA。[2]、[7]、[9]、[10]、[18] 属于这一层。

第三层是**系统级协同**。BSPDN 与 GAAFET、CFET、3D IC、先进封装和热管理共同决定后 FinFET 节点的实际收益。[5]、[6]、[11]-[17] 属于这一层。

## 3.2 创新点归纳

| 创新类别 | 具体创新 | 支撑文献 |
|---|---|---|
| 架构创新 | 电源网络从正面迁移到背面 | [1] |
| 面积创新 | DBC/SABC 支持标准单元级缩放 | [1] |
| 工艺创新 | slit nTSV、Ru/Mo 金属化、平滑侧壁刻蚀 | [3], [4] |
| 背面布线创新 | 背面层从 power 扩展到 clock/signal | [2], [9], [10] |
| DTCO 创新 | BSPDN 纳入 PPAC pathfinding | [7], [18] |
| 热管理创新 | 微通道、双面冷却、非均匀功率图建模 | [5], [11] |
| 器件协同创新 | BSPDN 与 GAAFET、CFET、NanoStack 协同 | [12]-[17], [19] |

## 4 对综述写作的支撑

20 篇文献可支撑综述形成“核心问题-技术路线-工艺实现-设计协同-系统趋势”的论文结构：

- 第 1-2 节：用 [1]、[6]、[12] 说明 BSPDN 的提出背景。
- 第 3 节：用 [1]-[4] 分析 DTV、SFVBP、DBC、nTSV。
- 第 4 节：用 [3]、[4]、[8] 讨论背面对准、晶圆键合和垂直互连。
- 第 5 节：用 [2]、[7]、[9]、[10]、[18] 讨论 EDA/DTCO 和标准单元设计。
- 第 6 节：用 [5]、[11] 讨论热管理。
- 第 7 节：用 [12]-[17]、[19] 讨论 GAAFET/CFET/NanoStack 后续趋势。

## 5 使用说明

综述正文应优先围绕 [1]-[6] 展开核心论证；[7]-[11] 用于补充设计协同、双面互连、键合和热建模；[12]-[20] 用于支撑 GAAFET、CFET、NanoStack 和先进封装背景。这样可以保证文献数量达到 20 篇，同时避免把非核心文献误写成 BSPDN 本体论文。
