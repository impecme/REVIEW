# BSPDN 文献阅读矩阵与创新点

## 1. 近两年核心文献矩阵

| 序号 | 文献 | 年份 | 权威性 | 研究对象 | 核心结论 | 主要创新点 | 适合写入综述位置 |
|---|---:|---:|---|---|---|---|---|
| [1] R. Xie et al., “Backside Power Distribution for Nanosheet Technologies Beyond 2nm” | 2024 | IEEE VLSI / IBM Research | 2nm 之后 nanosheet BSPDN 集成路线 | DTV 类方案不一定带来 cell-level scaling；DBC 类方案最有利于单元级缩放；SABC 可降低背面对准风险 | 将 BSPDN 评价重点从 IR drop 扩展到 cell-level scaling；提出 self-aligned backside contact | 技术路线、核心文献精读、创新点 |
| [2] S. Thomas, “Powering from behind” | 2024 | Nature Electronics | IBM/Samsung DBC 研究亮点 | BSPDN 可改善 power efficiency、performance 和 scaling；DBC 可减少源漏上方 power contact 和深沟槽通孔需求 | 以研究亮点形式明确 DBC 对标准单元高度缩放的价值 | 引言、技术意义、DBC 案例 |
| [3] K. Subramani et al., “Backside Routing Enablement Considerations For Advanced Node GAA Devices” | 2025 | IEEE VLSI / IBM Research | advanced GAA 节点中的 backside routing | 背面层应根据 PPA 目标在 power、clock 和特定 signal 之间进行策略分配 | 将 BSPDN 扩展为 backside routing，研究设计实现 flow | 发展趋势、DTCO/STCO |
| [4] P. Zhao et al., “Backside Power Delivery With Relaxed Overlay...” | 2024 | IEEE Transactions on Electron Devices | Mo-filled slit nTSV、极薄晶圆、背面对准 | slit nTSV 可通过 frontside lithography 实现自对准并放宽 backside overlay；Mo 填充 nTSV 具备继续缩放潜力 | 面向量产痛点提出 overlay-relaxed backside patterning | 工艺挑战、nTSV、背面对准 |
| [5] Y. Wang et al., “Etch of nano-TSV with smooth sidewall...” | 2024 | Microelectronic Engineering | Ru-based nano-TSV 刻蚀与金属化 | 多步刻蚀可获得高深宽比、无 scallop 的 nTSV；Ru 金属化和高选择比 recess etch 有利于可靠互连 | 把 BSPDN 工艺瓶颈落实到侧壁形貌、选择比、Ru 金属化和热循环可靠性 | 工艺模块、可靠性 |
| [6] F. Xie et al., “Thermal Mitigation Strategy for BSPDN” | 2024 | IEEE ECTC | BSPDN 热管理和双面冷却 | BSPDN 增大热阻并加剧热点；BEOL 嵌入式微通道 + 顶部 jet cooling 可显著降低最高温度 | 从电源/互连研究扩展到热-封装协同；提出 BEOL airgap 微通道冷却 | 热管理、挑战、翻译文献 |
| [7] imec, “Backside power delivery” | 2024 访问版 | imec 技术文章 | BPR、nTSV、BSPDN 基本流程 | BSPDN 将电源和信号解耦；BPR+nTSV 可降低 IR drop、释放 BEOL 布线并支持标准单元缩放 | 系统化解释 BPR+nTSV 工艺流程和 DTCO 价值 | 原理、背景、技术路线 |
| [8] Intel Foundry, “Intel 18A” | 2026 访问版 | 厂商官方路线 | PowerVia + RibbonFET | PowerVia 将粗间距金属和 bump 迁到背面，并在标准单元中使用 nano-TSV；官方称 cell utilization 和 ISO-power performance 有提升 | 产业界最明确的 BSPDN 落地案例之一 | 产业案例 |
| [9] TSMC, “A16 Technology with Super Power Rail” | 2024 | 厂商官方新闻稿 | Super Power Rail + nanosheet | A16 将 SPR 与 nanosheet transistor 结合，面向复杂信号路由和密集供电的 HPC 产品 | 把 BSPDN 与 HPC/AI 产品需求绑定 | 产业趋势 |
| [10] Samsung, “SF2Z with optimized BSPDN” | 2024 | 厂商官方新闻稿 | SF2Z BSPDN | SF2Z 将 power rail 放到 wafer backside，以减少 power/signal bottleneck 并降低 IR drop | 说明 BSPDN 已进入多 foundry 节点路线图 | 产业趋势 |

## 2. 重点文献逐篇阅读结论

## 2.1 Xie et al., VLSI 2024

这篇文献是 BSPDN 课设中最重要的核心论文。它没有停留在“背面供电可以降低 IR drop”的一般叙述，而是面向 2nm 之后 nanosheet transistor，比较不同 BSPDN 集成路线对标准单元缩放的实际意义。文献指出，DTV-based BSPDN 方案并不必然带来单元级缩放优势，SFVBP 可能受到 via resistance 限制，而 DBC-based 方案在 cell-level scaling 上最具潜力。

可提炼创新点：

- 把 BSPDN 的评价指标从供电完整性扩展到标准单元高度缩放；
- 证明 DBC 不只是供电路径变化，也是 logic cell scaling booster；
- self-aligned backside contact 针对背面对准难题给出可行路线；
- 将 BSPDN 与 nanosheet transistor 直接结合，贴合 2nm 之后量产方向。

## 2.2 Thomas, Nature Electronics 2024

这篇 Nature Electronics 研究亮点适合作为综述引言材料。它用较短篇幅解释了为什么 BSPDN 会成为 nanosheet CMOS 的关键 scaling booster，并引用 IBM/Samsung DBC 方案说明，在固定 nanosheet width 和 n/p spacing 条件下，直接背面接触可带来约 25% cell height reduction。

可提炼创新点：

- 直观说明 BSPDN 的价值从 power efficiency 扩展到 area scaling；
- 将 direct backside contact 与 frontside power delivery 的器件行为进行对比；
- 提供了课程报告中最容易展示的定量结论：cell height reduction。

## 2.3 Subramani et al., VLSI 2025

这篇文献代表了 BSPDN 的下一阶段：从 backside power delivery 走向 backside routing。公开摘要强调，几家 foundry 已在 3nm 及之后节点提供背面布线特征，设计实现时需要决定哪些背面层用于 power、clock 或特定 signal，从而最大化 PPA。

可提炼创新点：

- BSPDN 不再只是电源网络，而是背面布线资源平台；
- clock tree、长距离信号和特定全局线可能成为背面层新用途；
- 后续需要 PDK、EDA、physical design flow 与工艺协同。

## 2.4 Zhao et al., IEEE TED 2024

这篇文献关注 BSPDN 工艺量产中的 overlay 问题。由于晶圆键合和背面加工会带来 grid distortion，背面图形化对准非常困难。论文使用长条形 slit nTSV，且 nTSV 在 BPR 上方通过 frontside lithography 原位图形化，实现自对准，从而放宽背面 patterning 要求。

可提炼创新点：

- 用 slit nTSV 增强背面连接容差；
- 用 Mo-filled nTSV 降低小尺寸互连阻值；
- 通过 SiGe etch stop layer 和极薄晶圆减薄控制 TTV；
- 把工艺创新直接对准 BSPDN 的 overlay bottleneck。

## 2.5 Wang et al., Microelectronic Engineering 2024

这篇文献把 BSPDN 连接结构落实到 nano-TSV 刻蚀和 Ru 金属化。BSPDN 需要大量高密度、小尺寸 nTSV，如果侧壁有 Bosch scallop、金属残留或过刻蚀，就会影响电可靠性和机械可靠性。该文献提出多步刻蚀和 Ru 干法 recess etch，以获得更平滑侧壁和高选择比。

可提炼创新点：

- 对比并解决 nTSV 刻蚀侧壁 scallop 问题；
- 使用 Ru 金属化适配更小尺寸互连；
- 通过高选择比刻蚀减少 liner 损伤和金属残留；
- 热循环后电阻变化小，说明可靠性可进一步验证。

## 2.6 Xie et al., ECTC 2024

这篇文献是热管理方向的代表论文，也是本课设文献翻译选用文献。它指出 BSPDN 改善供电和布线的同时，会因为 BEOL、键合氧化层和极薄硅层增加热阻，并导致 CPU hotspot area 增大。作者提出 BEOL 嵌入式微通道冷却，与芯片顶部 jet cooling 结合形成双面冷却系统。

可提炼创新点：

- 明确指出 BSPDN 是电-热-封装协同问题；
- 利用 BEOL airgap 构造嵌入式微通道，属于结构复用；
- 通过 FEA 和等效参数提取降低复杂 BSPDN 热仿真成本；
- 给出可量化热缓解结果：最高温度下降 20% 以上，约 20 摄氏度。

## 3. 创新点总表

| 创新类别 | 具体创新 | 对 BSPDN 发展的意义 | 支撑文献 |
|---|---|---|---|
| 架构创新 | 电源网络从正面迁移到背面 | 电源与信号解耦，释放正面 BEOL | [1], [2], [7] |
| 面积创新 | DBC 支持 cell height reduction | BSPDN 成为 standard cell scaling booster | [1], [2] |
| 连接创新 | BPR + nTSV | 形成背面电源到前端器件的高效通路 | [4], [5], [7] |
| 对准创新 | SABC、slit nTSV | 缓解背面图形化 overlay 难题 | [1], [4] |
| 材料创新 | Ru、Mo 金属化 | 适配小尺寸、高深宽比互连 | [4], [5] |
| 热管理创新 | BEOL 嵌入式微通道 + 双面冷却 | 处理 BSPDN 增加热阻和热点问题 | [6] |
| 设计方法创新 | backside routing for power/clock/signal | 从 BSPDN 走向完整背面布线平台 | [3] |
| 产业导入创新 | PowerVia、Super Power Rail、SF2Z | BSPDN 进入 foundry 路线图 | [8], [9], [10] |

## 4. 可作为课设“创新点”章节的表述

BSPDN 的创新性不仅体现在供电位置从正面转移到背面，更体现在先进逻辑制程的整体设计范式变化。首先，BSPDN 将电源和信号网络解耦，使正面 BEOL 金属层更多用于信号互连，从而缓解 advanced node 中的布线拥塞。其次，BSPDN 通过更短、更低阻的供电路径降低 IR drop，提高供电完整性。第三，direct backside contact 和 buried power rail 等结构能够减少传统 power rail 和 power contact 对标准单元高度的限制，使 BSPDN 成为后 FinFET/GAAFET 节点的面积缩放助推器。第四，BSPDN 引入 nTSV、self-aligned backside contact、Ru/Mo 金属化和极薄晶圆减薄等新工艺模块，推动前端、后端和背面工艺协同。最后，随着 backside routing 的提出，背面层可能进一步承担 clock 和特定全局信号布线功能，使 BSPDN 从单一供电技术演进为先进节点的背面互连平台。

## 5. 可作为课设“问题与挑战”章节的表述

BSPDN 的落地仍面临多方面挑战。工艺方面，极薄晶圆减薄要求严格控制总厚度变化，nTSV 高深宽比刻蚀需要同时保证侧壁平滑、避免 BPR 过刻蚀并控制金属残留。对准方面，晶圆键合后的 grid distortion 会提高背面图形化难度，因此需要 self-aligned contact 或 slit nTSV 等结构降低 overlay 敏感性。材料方面，传统 Cu/W 互连在纳米尺度下可能受到 barrier 占比和电阻上升限制，Ru、Mo 等新金属成为研究方向。热管理方面，BSPDN 中 BEOL、键合氧化层和极薄硅层会增加等效热阻并加剧热点，必须与双面冷却、微通道冷却和封装散热协同设计。设计方面，背面层用于 power、clock 还是 signal，需要通过 DTCO/STCO 和 EDA flow 共同确定。

## 6. 参考来源

[1] R. Xie et al., “Backside Power Distribution for Nanosheet Technologies Beyond 2nm,” IEEE VLSI Technology and Circuits, 2024. https://research.ibm.com/publications/backside-power-distribution-for-nanosheet-technologies-beyond-2nm

[2] S. Thomas, “Powering from behind,” Nature Electronics, 2024. https://www.nature.com/articles/s41928-024-01226-9

[3] K. Subramani et al., “Backside Routing Enablement Considerations For Advanced Node GAA Devices,” IEEE VLSI Technology and Circuits, 2025. https://research.ibm.com/publications/backside-routing-enablement-considerations-for-advanced-node-gaa-devices

[4] P. Zhao et al., “Backside Power Delivery With Relaxed Overlay for Backside Patterning Using Extreme Wafer Thinning and Molybdenum-Filled Slit Nano Through Silicon Vias,” IEEE Transactions on Electron Devices, 2024. DOI: 10.1109/TED.2024.3487080

[5] Y. Wang et al., “Etch of nano-TSV with smooth sidewall and excellent selection ratio for backside power delivery network,” Microelectronic Engineering, 2024. DOI: 10.1016/j.mee.2024.112265

[6] F. Xie, R. Chen, and T. Wei, “Thermal Mitigation Strategy for Backside Power Delivery Network,” IEEE ECTC, 2024. DOI: 10.1109/ECTC51529.2024.00241

[7] imec, “Backside power delivery.” https://www.imec-int.com/en/articles/how-power-chips-backside

[8] Intel Foundry, “Intel 18A.” https://www.intel.com/content/www/us/en/foundry/process/18a.html

[9] TSMC, “TSMC Celebrates 30th North America Technology Symposium with Innovations Powering AI with Silicon Leadership.” https://pr.tsmc.com/english/news/3136

[10] Samsung Semiconductor, “Samsung Showcases AI-Era Vision and Latest Foundry Technologies at SFF 2024.” https://semiconductor.samsung.com/us/news-events/news/samsung-showcases-ai-era-vision-and-latest-foundry-technologies-at-sff-2024/
