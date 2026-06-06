# 先进逻辑制程中背面供电网络 BSPDN 技术研究综述

## 摘要

随着先进逻辑制程进入 FinFET 后期和 GAAFET/nanosheet 阶段，晶体管结构缩放带来的性能收益逐渐受到后段互连、电源完整性和热管理问题的制约。传统正面供电网络（frontside power delivery network, FSPDN）中，电源线、地线、时钟线和信号线共同占用晶圆正面后段金属层，使先进节点面临 IR drop 增大、布线拥塞加剧、标准单元高度难以继续缩放等问题。背面供电网络（backside power delivery network, BSPDN）通过将电源分配网络转移到晶圆背面，实现供电网络与正面信号互连的部分解耦，被认为是 2 nm 及后续逻辑节点的重要技术方向。本文基于 2024-2025 年发表的 BSPDN 相关文献，综述其研究背景、基本结构、主要技术路线、代表性研究进展、技术创新点、关键挑战和发展趋势。现有研究表明，BSPDN 的研究重点已经从单纯改善供电压降，扩展到 direct backside contact、buried power rail、nano-TSV、背面布线、热管理以及 DTCO/STCO 协同优化等方向。BSPDN 并非晶体管结构本身，而是与 GAAFET、CFET、3D IC 和先进封装共同演进的供电与互连架构创新。

**关键词**：背面供电网络；BSPDN；IR drop；nanosheet；GAAFET；buried power rail；nano-TSV；direct backside contact

## 1 引言

集成电路先进制程长期依赖晶体管尺寸缩小和器件结构演进实现性能提升。平面 MOSFET、FinFET 和 GAAFET/nanosheet 的演进主线，实质上是通过增强栅极对沟道的控制能力来抑制短沟道效应并提高晶体管密度。然而，进入 3 nm、2 nm 及后续节点后，芯片级 PPA（power, performance, area）并不只由前端器件决定。后段互连电阻、电源分配网络阻抗、局部电压跌落、标准单元布线资源和封装散热能力，逐渐成为先进逻辑制程继续缩放的主要限制因素。

在传统正面供电网络中，电源由封装端进入芯片后，需要通过多层 BEOL 金属和大量通孔传递到晶体管附近。由于先进节点金属线宽和通孔尺寸不断减小，供电路径电阻上升，电源压降和动态 voltage droop 更加严重。同时，电源线和信号线共同使用正面 BEOL 资源，导致布线拥塞、信号绕线增加和寄生 RC 增大。对于高性能计算和人工智能芯片，瞬态电流大、功率密度高，这类供电和互连问题更加突出。因此，仅依靠 GAAFET 等前端晶体管创新，难以完全转化为芯片级性能收益。

BSPDN 的提出正是为了缓解上述矛盾。其基本思路是将电源分配网络从晶圆正面转移到背面，通过背面金属层、埋入电源轨（buried power rail, BPR）、纳米级硅通孔（nano-through-silicon via, nTSV）或直接背面接触（direct backside contact, DBC）向器件供电。这样可以减少电源线对正面 BEOL 资源的占用，使正面金属层更多用于信号互连，并缩短部分供电路径。Xie 等在 2024 年 VLSI 论文中指出，面向 2 nm 之后 nanosheet 技术的 BSPDN 研究已经不再只是关注 IR drop，而是进一步关注不同背面接触方案对标准单元级缩放的影响[1]。

本文按照正式文献综述的写法，对近两年 BSPDN 相关论文进行归纳分析。全文首先介绍 BSPDN 的技术背景和基本结构，然后比较主要实现路线，接着对代表性文献进行评述，最后总结其创新点、挑战和发展趋势。

## 2 BSPDN 的技术背景与结构基础

## 2.1 正面供电网络的缩放瓶颈

传统 FSPDN 的核心问题在于电源网络与信号网络同时依赖正面 BEOL。随着技术节点缩小，BEOL 金属线宽减小、层间通孔尺寸下降、互连电阻上升，使供电网络阻抗不断增加。供电路径上的电阻会造成 IR drop，导致晶体管实际获得的工作电压低于理想电压，进而影响频率裕量、时序收敛和可靠性。

另一方面，电源线占用正面布线轨道，会压缩信号互连空间。先进标准单元通常需要在有限 cell height 内同时布置电源轨、信号引脚、局部互连和晶体管连接。当电源轨仍保留在正面时，标准单元高度继续缩放会受到明显限制。Thomas 在 Nature Electronics 的研究亮点中指出，背面供电方案的价值不仅在于提升供电效率，也在于为 nanosheet CMOS 的进一步缩放释放正面面积资源[2]。

因此，BSPDN 的研究背景可以概括为两个层面：一是电源完整性问题，即如何降低供电路径阻抗和 IR drop；二是面积和布线问题，即如何减少正面电源网络对标准单元和 BEOL 信号布线的占用。

## 2.2 BSPDN 的基本结构

BSPDN 通过晶圆键合、晶圆减薄和背面加工，在晶圆背面形成电源分配网络。典型结构包括背面金属层、BPR、nTSV、DBC、绝缘层和背面接触结构。其中，BPR 用于将电源轨靠近晶体管区域布置，nTSV 用于连接背面金属网络和前端/中段结构，DBC 则进一步尝试从背面直接连接局部电源节点或源漏区域。

表 1 总结了 BSPDN 中常见结构单元及其功能。

| 结构单元 | 主要功能 | 技术意义 |
|---|---|---|
| 背面金属层 | 在晶圆背面形成低阻 VDD/VSS 网络 | 降低长距离供电阻抗 |
| BPR | 将电源轨埋入器件附近 | 减少正面电源轨占用 |
| nTSV | 连接背面电源网络和 BPR/局部节点 | 建立背面到前端的垂直连接 |
| DBC | 从背面直接连接源漏或局部供电区域 | 缩短供电路径并支持 cell scaling |
| SABC | 自对准背面接触 | 缓解背面对准误差 |

需要强调的是，BSPDN 不是 FinFET 或 GAAFET 这样的晶体管结构，而是供电与互连架构。它与 GAAFET/nanosheet 的关系是协同关系：GAAFET 提升前端器件栅控能力，BSPDN 则改善供电、布线和面积缩放条件。

## 3 BSPDN 主要技术路线

## 3.1 BPR 与 nTSV 路线

BPR + nTSV 是 BSPDN 的典型实现路线。其基本思路是先将电源轨埋入晶体管附近，再通过从背面形成的 nTSV 将背面电源网络连接到 BPR。该路线的优势在于结构清晰，可以将电源轨从正面 BEOL 中移出，从而释放正面布线资源并缩短电源路径。

不过，该路线的工艺难度较高。首先，nTSV 尺寸需要与先进逻辑标准单元相匹配，通孔深宽比、刻蚀选择比和侧壁形貌都会影响连接电阻和可靠性。其次，背面加工前需要进行晶圆键合和极薄晶圆减薄，减薄厚度均匀性和 etch stop 控制会影响后续通孔形成。Wang 等研究了 BSPDN 中 nano-TSV 的刻蚀和 Ru 金属化问题，指出平滑侧壁、高选择比和热循环稳定性是实现可靠 nTSV 的关键因素[5]。

## 3.2 DTV 与 SFVBP 路线

DTV 类路线通过深沟槽通孔连接背面电源网络和正面或局部电源结构。与 BPR + nTSV 路线相比，DTV 的结构概念较直观，但通孔尺寸、电阻和面积占用可能限制其标准单元级缩放收益。Xie 等比较了 DTV-based、SFVBP 和 DBC-based 等方案，指出多数 DTV-based BSPDN 方案并不必然提供明显 cell-level scaling benefit；SFVBP 方案虽然可能改善部分几何约束，但 via resistance 仍可能成为瓶颈[1]。

因此，DTV 路线更适合从“电源路径后移”的角度理解 BSPDN，而如果目标是最大化标准单元缩放，则需要进一步采用 DBC 或更紧凑的背面接触方案。

## 3.3 Direct Backside Contact 路线

DBC 是近两年文献中最值得关注的 BSPDN 路线之一。该路线试图减少传统正面 power contact 和深沟槽通孔占用，通过背面直接连接器件源漏或局部电源区域。与 DTV 相比，DBC 供电路径更短，对正面标准单元面积占用更小。

Xie 等认为 DBC-based schemes 在 cell-level scaling 方面最有潜力，并展示了 SABC 结构以降低背面对准误差影响[1]。Thomas 对该研究的评述进一步指出，在固定 nanosheet 宽度和 n/p 间距的条件下，DBC 相比 frontside power delivery 可实现约 25% cell height reduction[2]。这说明 DBC 的价值不仅是改善供电阻抗，更是使 BSPDN 成为后 FinFET/GAAFET 节点的标准单元缩放助推器。

## 3.4 背面布线路线

BSPDN 的早期目标主要是供电网络后移，但 2025 年相关文献已经开始讨论 backside routing 的更广泛用途。Subramani 等在 VLSI 2025 论文中指出，背面层的使用对象可能从 power 扩展到 clock 和特定 signal，设计实现时需要在不同网络之间分配背面资源，以最大化 PPA[3]。

这意味着 BSPDN 后续可能从单一供电技术发展为背面互连平台。对于物理设计而言，这会影响标准单元库、时钟树综合、电源完整性分析、布线资源分配和 PDK 规则定义。换言之，BSPDN 的后续研究不只属于制造工艺问题，也属于 EDA 和设计-工艺协同优化问题。

## 4 近两年代表性文献评述

## 4.1 面向 2 nm 之后 nanosheet 技术的 BSPDN 集成

Xie 等的 VLSI 2024 论文是近两年 BSPDN 研究中较具代表性的工作[1]。该文献面向 2 nm 之后 nanosheet transistor 技术，比较了多种 BSPDN 集成方案对器件和标准单元缩放的影响。其重要贡献在于：作者没有停留于“BSPDN 能降低 IR drop”的一般判断，而是进一步分析不同背面供电结构是否真正有助于 cell-level scaling。

该文献的核心结论是，DTV-based 方案并非都能带来明显 cell scaling benefit，SFVBP 可能受 via resistance 限制，而 DBC-based 方案在标准单元缩放方面更具潜力[1]。此外，文献提出的 self-aligned backside contact 结构，针对背面对准困难这一核心工艺问题给出了解决思路。该研究表明，BSPDN 的评价指标应包括供电能力、器件影响、标准单元面积、接触电阻和工艺可制造性等多个维度。

## 4.2 Direct Backside Contact 的研究意义

Thomas 在 Nature Electronics 发表的 “Powering from behind” 是对 DBC 相关工作的研究亮点评述[2]。该文献强调，BSPDN 可以改善 CMOS 电路的 power efficiency 和 performance，同时也可能提供 scaling benefit。文章指出，DBC 方案通过减少源漏上方 power contact 和深沟槽通孔需求，使 nanosheet 标准单元具备进一步缩放可能。

该文献的价值在于从更宏观的角度解释了 DBC 的技术意义。对于课程设计而言，它可以支撑以下论点：BSPDN 不是简单改变供电方向，而是通过释放正面面积资源，参与先进逻辑标准单元的结构重构。该观点与 Xie 等的 VLSI 2024 论文形成相互支撑[1-2]。

## 4.3 从背面供电到背面布线

Subramani 等的 VLSI 2025 论文进一步拓展了 BSPDN 的研究边界[3]。该文献关注 advanced node GAA devices 中 backside routing 的实现问题，认为背面层可以根据设计目标分配给 power、clock 或特定 signal。与前述主要关注电源网络的研究相比，该工作更接近设计实现和 DTCO 层面。

该研究说明，BSPDN 的未来形态可能不是“背面只放 VDD/VSS”，而是“背面成为新的布线资源层”。如果 clock 或长距离信号也能受益于背面布线，则芯片物理设计流程需要重新考虑前后两侧金属层的资源划分。该方向对 EDA、标准单元库设计和封装协同提出了新的研究需求。

## 4.4 面向背面对准的 slit nTSV 工艺

Zhao 等在 IEEE Transactions on Electron Devices 发表的论文研究了使用极薄晶圆减薄和 Mo-filled slit nTSV 的 BSPDN 方案[4]。该论文针对背面图形化中的 overlay 问题，提出利用 frontside lithography 在 BPR 上方原位定义 nTSV，从而放宽 backside patterning 对准要求。

这一研究的创新点在于把 BSPDN 的关键难题从架构层面落实到具体工艺层面。先进 BSPDN 工艺中，晶圆键合和背面加工会引入形变，背面对准误差会影响 nTSV 与 BPR 的连接可靠性。slit nTSV 通过增大某一方向的连接容差，可以降低 overlay 对工艺良率的影响。同时，Mo 填充也为小尺寸垂直互连提供了材料选择[4]。

## 4.5 nano-TSV 刻蚀与金属化可靠性

Wang 等研究了 BSPDN 中 nano-TSV 的平滑侧壁刻蚀和 Ru 金属化[5]。该论文表明，nTSV 并不是传统 TSV 的简单缩小版本。在纳米尺度下，刻蚀侧壁 scallop、liner 损伤、金属残留和填充电阻都会影响最终可靠性。论文采用多步刻蚀获得较平滑的高深宽比 nTSV，并研究 Ru-based interconnection 和高选择比 recess etch。

该研究对于 BSPDN 的意义在于，它说明垂直连接结构的加工质量会直接决定 BSPDN 的电学和可靠性表现。如果 nTSV 电阻过高或热循环后失效，即使背面金属层本身低阻，也无法实现理想供电效果。因此，nTSV 工艺是 BSPDN 从概念验证走向量产的核心环节之一。

## 4.6 BSPDN 的热管理问题

Xie、Chen 和 Wei 在 ECTC 2024 论文中研究了 BSPDN 的热缓解策略[6]。该文献指出，BSPDN 虽然能够增强供电能力并缓解正面信号布线拥塞，但也会引入新的热管理问题。其原因在于 FEOL 发热区域到冷却端之间包含 BEOL、键合氧化层和极薄硅层，使等效热阻增大，横向热扩散能力下降。

作者提出利用 BEOL airgap 构建嵌入式微通道冷却，并与芯片顶部 jet cooling 结合形成双面冷却方案。仿真结果表明，在一定水冷入口条件下，芯片最高温度可降低 20% 以上，约 20 摄氏度[6]。该文献的意义在于，它提醒 BSPDN 不能只从供电和互连角度评价，还必须纳入热管理、封装和系统级可靠性。

## 5 BSPDN 技术创新点分析

## 5.1 架构创新：电源与信号解耦

BSPDN 最根本的创新是将电源分配网络从正面 BEOL 转移到晶圆背面，使电源网络和信号互连在空间上部分解耦。传统 FSPDN 中，电源线占用正面金属层，会与信号线、时钟线和局部互连竞争布线资源。BSPDN 通过背面低阻金属层承担主要供电功能，使正面 BEOL 可以更多用于信号互连，从而缓解先进节点中的布线拥塞问题。

## 5.2 面积创新：支持标准单元缩放

现有文献表明，BSPDN 的价值不仅是降低供电压降，还包括标准单元缩放。Xie 等和 Thomas 的文献均强调 DBC 对 cell-level scaling 的作用[1-2]。当传统正面 power contact 和 power rail 被减少或移除后，标准单元高度可以进一步压缩。因此，BSPDN 应被视为 advanced logic cell scaling 的组成部分。

## 5.3 工艺创新：nTSV、SABC 和新金属

BSPDN 引入了极薄晶圆减薄、nTSV 高深宽比刻蚀、SABC、自对准图形化、Ru/Mo 金属填充等新工艺模块。Zhao 等和 Wang 等的研究分别从 Mo-filled slit nTSV 与 Ru-based nTSV 角度说明，小尺寸垂直互连的材料、形貌和对准能力是 BSPDN 的关键[4-5]。

## 5.4 设计方法创新：从 DTCO 到 STCO

BSPDN 的收益依赖器件、标准单元、正面 BEOL、背面金属、封装和散热共同优化。Subramani 等对 backside routing 的研究说明，背面层未来可能服务于 power、clock 和特定 signal[3]。这意味着 BSPDN 需要从设计-工艺协同优化（DTCO）进一步扩展到系统-工艺协同优化（STCO）。

## 5.5 热管理创新：电-热-封装协同

传统 BSPDN 讨论更关注电源完整性，而 Xie 等的 ECTC 2024 论文表明，BSPDN 会改变芯片热路径并可能增加热点风险[6]。因此，先进 BSPDN 设计必须将供电收益与热阻、封装散热和冷却结构同时考虑。嵌入式微通道和双面冷却代表了 BSPDN 热管理的一个研究方向。

## 6 BSPDN 面临的关键挑战

## 6.1 制造工艺挑战

BSPDN 需要晶圆键合、极薄晶圆减薄、背面图形化、nTSV 刻蚀和金属填充等复杂步骤。每个步骤都可能影响良率和可靠性。例如，晶圆减薄过程中的厚度均匀性会影响 nTSV 深度控制；nTSV 侧壁粗糙会导致电场集中或金属填充缺陷；BPR 过刻蚀则可能破坏局部电源连接结构[4-5]。

## 6.2 背面对准和接触可靠性挑战

背面加工通常发生在晶圆键合和减薄之后，晶圆形变会增加 backside overlay 难度。SABC 和 slit nTSV 是降低对准敏感性的有效思路，但其长期可靠性、工艺窗口和大面积均匀性仍需要进一步验证[1,4]。对于量产而言，接触电阻、热循环、电迁移和机械应力都必须纳入可靠性评估。

## 6.3 热管理挑战

BSPDN 改变了传统芯片的热扩散路径。极薄衬底虽然有利于背面连接，但削弱了硅衬底的横向热扩散能力；BEOL 和键合氧化层则可能增加垂直热阻。Xie 等指出，BSPDN 可能导致热点问题加剧，需要通过嵌入式微通道冷却或双面冷却进行缓解[6]。

## 6.4 EDA 与设计实现挑战

如果背面层仅用于 VDD/VSS，设计流程相对清晰；但如果背面层进一步用于 clock 或 signal，则现有 PDK、标准单元库、布线规则、时钟树综合和电源完整性分析都需要改变。Subramani 等提出的 backside routing 方向说明，BSPDN 的最终收益取决于设计实现流程是否能够有效利用背面资源[3]。

## 7 发展趋势

未来 BSPDN 的发展可能呈现以下趋势。

第一，BSPDN 将与 GAAFET/nanosheet 同步演进。GAAFET 解决前端器件栅控问题，BSPDN 解决供电和互连瓶颈，二者协同才能实现先进节点的芯片级 PPA 改善。

第二，BSPDN 将从背面供电扩展到背面布线。背面层未来可能不仅用于电源和地，也可能用于时钟树、长距离全局信号或部分 SRAM 宏单元连接[3]。

第三，BSPDN 将与 CFET 和 3D IC 深度耦合。CFET 采用 nFET/pFET 垂直堆叠，3D IC 则进一步增加系统垂直集成密度，这些结构都需要更高效的背面连接、供电和散热能力。

第四，BSPDN 研究会更加重视热-电-机械-封装协同。未来评价 BSPDN 不能只看 IR drop 或 cell height，还应同时评价温度、可靠性、制造成本、封装复杂度和系统级收益。

## 8 结论

BSPDN 是先进逻辑制程中具有重要前景的供电与互连架构创新。其提出背景是：在 FinFET 和 GAAFET 节点继续缩放后，芯片性能越来越受限于正面 BEOL 布线拥塞、电源压降、标准单元高度和热管理问题。BSPDN 通过将电源网络迁移至晶圆背面，实现电源与信号网络的部分解耦，降低供电路径阻抗，并为标准单元面积缩放提供新的空间。

近两年文献表明，BSPDN 研究已经形成多个重点方向。Xie 等比较了面向 2 nm 之后 nanosheet 的多种 BSPDN 结构，强调 DBC 和 SABC 的 cell-level scaling 价值[1]；Thomas 从研究亮点角度阐明了 DBC 对 nanosheet CMOS 缩放的意义[2]；Subramani 等将 BSPDN 扩展到 backside routing 和设计实现层面[3]；Zhao 等和 Wang 等分别研究了 Mo-filled slit nTSV、Ru-based nTSV 等关键工艺模块[4-5]；Xie、Chen 和 Wei 则揭示了 BSPDN 的热管理挑战并提出双面冷却思路[6]。

总体而言，BSPDN 的创新性不仅体现在“从背面供电”，更体现在推动先进制程从单一器件缩放转向器件、互连、供电、封装、散热和设计方法的系统协同优化。其主要挑战包括晶圆减薄、背面对准、nTSV 刻蚀、金属填充、热管理、可靠性和 EDA flow。随着 GAAFET、CFET、3D IC 和先进封装继续发展，BSPDN 有望成为后 FinFET 时代先进逻辑技术平台的重要组成部分。

## 参考文献

[1] Xie R, Pancharatnam S, Miao L, et al. Backside power distribution for nanosheet technologies beyond 2nm[C]//2024 IEEE Symposium on VLSI Technology and Circuits. Honolulu: IEEE, 2024.

[2] Thomas S. Powering from behind[J]. Nature Electronics, 2024, 7: 518.

[3] Subramani K, et al. Backside routing enablement considerations for advanced node GAA devices[C]//2025 IEEE Symposium on VLSI Technology and Circuits. Kyoto: IEEE, 2025.

[4] Zhao P, et al. Backside power delivery with relaxed overlay for backside patterning using extreme wafer thinning and molybdenum-filled slit nano through silicon vias[J]. IEEE Transactions on Electron Devices, 2024, 71(12): 7963-7969. DOI: 10.1109/TED.2024.3487080.

[5] Wang Y, et al. Etch of nano-TSV with smooth sidewall and excellent selection ratio for backside power delivery network[J]. Microelectronic Engineering, 2024. DOI: 10.1016/j.mee.2024.112265.

[6] Xie F, Chen R, Wei T. Thermal mitigation strategy for backside power delivery network[C]//2024 IEEE 74th Electronic Components and Technology Conference. Denver: IEEE, 2024: 1485-1492. DOI: 10.1109/ECTC51529.2024.00241.
