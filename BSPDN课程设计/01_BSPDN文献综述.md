# 先进逻辑制程中背面供电网络 BSPDN 技术研究综述

## 摘要

背面供电网络（backside power delivery network, BSPDN）是 2 nm 及后续先进逻辑节点中用于缓解电源压降、正面互连拥塞和标准单元缩放瓶颈的重要技术。随着晶体管结构由 FinFET 演进至 GAAFET/nanosheet，并进一步向 CFET、NanoStack 和三维异质集成发展，芯片性能提升的主要限制已由单一前端器件逐渐转向“器件-互连-供电-封装-散热”的系统协同。传统正面供电网络中，电源线与信号线共同占用晶圆正面 BEOL 金属层，导致 IR drop、voltage droop、路由拥塞和标准单元高度限制。BSPDN 通过将主要电源分配网络迁移至晶圆背面，并结合埋入电源轨（buried power rail, BPR）、纳米级硅通孔（nano-through-silicon via, nTSV）、直接背面接触（direct backside contact, DBC）和背面布线等技术，实现电源网络与信号互连的空间解耦。已有研究显示，BSPDN 的意义不能仅理解为“把电源放到背面”，更应放在标准单元缩放、背面连接、设计规则重构和热-电协同优化的框架中加以认识。笔者认为，BSPDN 的关键价值不仅在于降低供电阻抗，还在于支持标准单元缩放、释放正面布线资源，并为 GAAFET、CFET 和三维集成提供基础互连平台；其主要挑战包括背面对准、晶圆减薄、nTSV 刻蚀与金属化、热扩散受限、EDA flow 适配和可靠性验证。

**关键词**：BSPDN；背面供电；GAAFET；nanosheet；buried power rail；nano-TSV；direct backside contact；DTCO

## 1 引言

先进逻辑制程长期依赖晶体管尺寸缩小和器件结构演进获得性能与密度收益。从平面 MOSFET 到 FinFET，再到 GAAFET/nanosheet，器件结构演进的主线是增强栅极对沟道的控制能力，以抑制短沟道效应并提高晶体管密度。2 nm 平台和后续 nanosheet 技术论文表明，GAAFET 已成为 FinFET 之后先进逻辑节点的核心器件路线之一[12-14]。然而，随着器件尺寸继续缩小，芯片级 PPA（power, performance, area）并不只由晶体管决定。后段互连、电源完整性、局部供电压降、标准单元路由资源和封装散热能力，正在成为先进节点继续缩放的主要限制。

传统正面供电网络（frontside power delivery network, FSPDN）中，电源由封装侧进入芯片后，经由多层 BEOL 金属和通孔传递至晶体管附近。随着 BEOL 金属线宽和 via 尺寸不断缩小，电源路径阻抗上升，IR drop 和动态 voltage droop 加剧。同时，电源轨、时钟线和信号线共同使用正面金属资源，导致路由拥塞、寄生 RC 增大和时序收敛难度提升。对于高性能计算和人工智能芯片，瞬态电流和功率密度更高，传统正面供电网络的限制更明显。

BSPDN 的核心思想是将主要电源分配网络从晶圆正面迁移至背面，通过背面金属层、BPR、nTSV、DBC 或其他背面连接结构向前端器件供电。这样可以减少电源线对正面 BEOL 的占用，使正面金属层更多服务于信号互连，并缩短部分供电路径。Xie 等在 VLSI 2024 论文中指出，面向 2 nm 之后 nanosheet 的 BSPDN 研究已经从“能否降低 IR drop”发展到“不同背面供电结构是否真正支持 cell-level scaling”[1]。Subramani 等进一步将研究范围扩展到 backside routing，即背面层未来可能不仅用于 power，也可能用于 clock 或特定信号[2]。

围绕 BSPDN 的技术价值，笔者更关注三个问题：其一，背面供电为什么会在后 FinFET 节点成为必要选择；其二，不同 BSPDN 结构路线究竟解决了哪些互连和标准单元问题；其三，工艺、EDA、热管理和先进封装能否共同支撑这种架构进入可制造平台。下文据此从技术动因、结构路线、工艺实现、设计协同、热管理和发展趋势等方面展开讨论。

## 2 BSPDN 的技术动因

## 2.1 器件缩放后的互连和供电瓶颈

FinFET 向 GAAFET/nanosheet 的转变主要解决前端器件栅控问题。Yeap 等报道的 2 nm 平台技术表明，nanosheet 晶体管、互连和系统应用需要联合优化才能获得能效收益[12]。Bao 等关于 nanosheet 多阈值电压集成的研究也说明，先进节点的器件优化已经进入高度工程化阶段，单纯依赖器件结构变化并不足以解决全部 PPA 问题[13]。当晶体管栅长、接触间距和标准单元轨道数继续缩小，电源网络和局部互连对芯片性能的影响会被放大。

传统 FSPDN 的主要瓶颈有三类。第一是供电阻抗瓶颈。电源电流需要穿过多层正面金属和 via，路径长且逐层缩窄，导致 IR drop 和 voltage droop。第二是布线资源瓶颈。正面 BEOL 同时承担 power、ground、clock 和 signal，电源轨占用会挤压信号布线空间。第三是标准单元面积瓶颈。VDD/VSS rail 和 power contact 若仍位于正面，会限制 cell height 继续降低。BSPDN 正是针对这些问题提出的供电与互连架构创新。

## 2.2 BSPDN 与 GAAFET、CFET 的关系

BSPDN 不是一种晶体管，而是与后 FinFET 器件共同演进的供电架构。GAAFET/nanosheet 负责增强沟道栅控，BSPDN 负责降低供电和互连限制。进一步看，CFET 通过垂直堆叠 nFET 和 pFET 继续压缩标准单元面积，但也使上下器件接触、布线和供电更复杂。Demuynck 等关于 monolithic CFET 的工作展示了中间介质隔离和堆叠接触的重要性[15]，Vega Gonzalez 等则研究了 monolithic CFET 的中段堆叠接触集成[16]。这些研究说明，随着器件从平面布局走向三维堆叠，背面供电和背面连接会成为更重要的系统能力。

因此，BSPDN 应被理解为先进逻辑节点的平台型技术：它与 GAAFET 共同解决 2 nm 及后续节点的器件-供电协同问题，与 CFET 共同支撑更激进的标准单元缩放，并与 3D IC 和先进封装共同决定系统级能效和热可靠性。

![N2 nanosheet 平台与 NanoFlex 标准单元示意](figures/fig1_ref12_n2_nanoflex.png)

图 1 N2 nanosheet 平台与 NanoFlex 标准单元示意。来源：文献[12] Yeap G, et al., *2nm Platform Technology Featuring Energy-Efficient Nanosheet Transistors and Interconnects Co-Optimized with 3DIC for AI, HPC and Mobile SoC Applications*, Fig. 2 “N2 NanoFlex innovation modulates NS width for best PPA”。2 nm nanosheet 平台通过调节 nanosheet 宽度和标准单元高度实现 PPA 优化，表明后 FinFET 节点的性能提升已经从单一器件缩放转向器件结构、标准单元和互连资源的协同设计。BSPDN 正是在这一背景下成为 GAAFET/nanosheet 平台的重要供电与互连支撑技术。

## 3 BSPDN 的主要结构路线

## 3.1 BPR 与 nTSV 路线

BPR + nTSV 是 BSPDN 的基本实现路线之一。BPR 将电源轨从正面 BEOL 或标准单元内部转移到器件附近，nTSV 从晶圆背面连接背面金属电源网络与 BPR 或局部供电节点。该路线的优势是结构清晰，能够减少正面电源轨占用，同时缩短供电路径。

但 BPR + nTSV 的实现依赖复杂工艺。nTSV 需要在极薄衬底中形成高深宽比通孔，其刻蚀侧壁、选择比、金属填充和热循环可靠性都会影响最终电源路径。Wang 等研究了 BSPDN 中 nano-TSV 的平滑侧壁刻蚀和 Ru 金属化，指出无 scallop 侧壁、高选择比刻蚀和稳定金属化是可靠 nTSV 的关键[4]。Zhao 等进一步提出 Mo-filled slit nTSV，通过长条形通孔设计放宽背面图形化 overlay 要求[3]。

## 3.2 DTV、SFVBP 与 DBC 路线

DTV 类路线通过深沟槽通孔连接背面电源网络与正面或局部电源结构。该方案概念直观，但通孔电阻、面积占用和对准误差可能限制标准单元缩放收益。Xie 等比较了 DTV-based、SFVBP 和 DBC-based 等多种方案，指出 DTV 类方案并不必然带来明显 cell-level scaling benefit，SFVBP 可能受 via resistance 限制，而 DBC-based 方案在标准单元缩放方面更具潜力[1]。

DBC 的关键在于减少传统正面 power contact 和深沟槽通孔占用，使供电路径更短，同时释放正面单元面积。Xie 等提出的 self-aligned backside contact（SABC）针对背面对准误差提供解决思路[1]。从综述角度看，DBC 是 BSPDN 从“电源网络后移”向“器件-接触-标准单元协同缩放”发展的标志。

![FSPDN 与多种 BSPDN 标准单元结构对比](figures/fig2_ref1_bspdn_cell_architectures.png)

图 2 FSPDN 与多种 BSPDN 标准单元结构对比。来源：文献[1] Xie R, Pancharatnam S, Miao L, et al., *Backside Power Distribution for Nanosheet Technologies Beyond 2nm*, Fig. 1 “different cell architectures with frontside power distribution network (FSPDN) and BSPDN”。FSPDN、DTV-based BSPDN、SFVBP 和 DBC 等结构在标准单元中的布局差异表明，BSPDN 的核心变化是将电源网络从正面互连资源中分离出来。DTV 类方案主要通过垂直通孔建立背面到局部电源结构的连接，DBC 类方案则进一步减少正面 power contact 占用，因而更有利于标准单元缩放。

![不同 BSPDN 方案的标准单元高度缩放效果](figures/fig3_ref1_cell_height_scaling.png)

图 3 不同 BSPDN 方案的标准单元高度缩放效果。来源：文献[1] Xie R, Pancharatnam S, Miao L, et al., *Backside Power Distribution for Nanosheet Technologies Beyond 2nm*, Fig. 2 “Impact of cell height scaling with various power supply schemes at constant nanosheet width and N-P space”。在相同 nanosheet 宽度和 N-P 间距条件下，SFVBP、DBC 和 DBC-CEI 相比 FSPDN 具有不同程度的 cell height reduction。DBC 类路线通过更直接地释放正面单元面积，体现出 BSPDN 在标准单元缩放方面的结构优势。

## 3.3 背面布线路线

早期 BSPDN 主要关注 VDD/VSS 供电，但后续研究开始把背面层视为更广义的布线资源。Subramani 等提出，先进 GAA 节点中的背面层可能服务于 power、clock 或特定 signal，需要在设计实现流程中根据 PPA 目标进行资源分配[2]。Flip FET 和双面 pin 标准单元相关研究也表明，双面互连和双面信号路由可能改变标准单元设计与 block-level PPA[9-10]。

这意味着 BSPDN 的发展方向可能从“背面供电”扩展到“背面互连平台”。该变化对 PDK、标准单元库、布线规则、时钟树综合、电源完整性分析和 RC 提取都提出新要求。

## 4 BSPDN 工艺实现问题

## 4.1 晶圆减薄与背面对准

BSPDN 的背面加工通常需要晶圆键合、极薄晶圆减薄和背面光刻。晶圆键合会引入形变和局部应力，极薄晶圆又容易把这些形变传递到后续曝光和通孔加工中。早期 Cu wafer bonding 研究已经证明，晶圆级键合是三维互连和背面连接类技术的重要基础工艺[8]。因此，背面加工不是简单增加一层金属，而是涉及晶圆形貌、对准模型和工艺窗口的系统问题。

Zhao 等的 Mo-filled slit nTSV 研究正是面向背面对准这一痛点。其设计通过前端定义的 slit nTSV 增加连接容差，从而降低背面图形化 overlay 要求[3]。这一思路说明，BSPDN 工艺需要通过结构设计和工艺流程共同降低对准敏感性。

![BSM1-BPR 背面对准矢量图](figures/fig4_ref3_bsm1_bpr_overlay_vector_map.png)

图 4 BSM1-BPR 背面对准矢量图。来源：文献[3] Zhao P, et al., *Backside Power Delivery With Relaxed Overlay for Backside Patterning Using Extreme Wafer Thinning and Molybdenum-Filled Slit Nano Through Silicon Vias*, Fig. 6 “(a) BSM1-BPR overlay vector map. (b) Residual vector map post bonding”。背面金属 BSM1 与前侧 BPR 之间存在可观测的 overlay 分布，键合后仍会保留残余对准偏差。由此可见，背面图形化时的 overlay 控制是 BSPDN 制造中的关键问题，长条形 slit nTSV 通过增加连接容差降低了背面对准敏感性。

## 4.2 nTSV 刻蚀与金属化

nTSV 是 BSPDN 从背面金属层连接至前端供电节点的关键路径。与传统 TSV 相比，nTSV 尺寸更小、密度更高、与标准单元布局关系更紧密，因此不能简单套用传统 3D 封装 TSV 工艺。Wang 等关于 nTSV smooth sidewall 的研究表明，刻蚀侧壁粗糙、scallop、liner 损伤和金属残留会影响电阻和可靠性[4]。Ru、Mo 等金属材料被用于探索小尺寸互连中的低阻和可填充性问题[3-4]。

从可靠性角度看，nTSV 还需要承受热循环、电迁移和机械应力。若 nTSV 电阻过高，即使背面电源网低阻，整体供电收益也会被局部垂直连接抵消。因此，nTSV 是 BSPDN 量产可行性的核心工艺模块。

![优化 Bosch 工艺刻蚀的不同直径 nano-TSV](figures/fig5_ref4_optimized_bosch_ntsv.png)

图 5 优化 Bosch 工艺刻蚀的不同直径 nano-TSV。来源：文献[4] Wang Y, et al., *Etch of nano-TSV with smooth sidewall and excellent selection ratio for backside power delivery network*, Fig. 13 “Etching of different diameter nano-TSVs using optimized Bosch technology”。nano-TSV 尺寸小、深宽比高，刻蚀侧壁粗糙或形貌不稳定会影响后续金属填充和电阻可靠性。优化后的 Bosch 工艺能够在不同直径下形成较稳定的 nano-TSV 结构，为 BSPDN 垂直互连提供工艺基础。

## 4.3 与先进图形化和 DFM 的协同

Lanzillo 等从 NanoStack transistor era 的角度讨论了先进互连缩放挑战，指出后 FinFET 节点的互连问题需要先进图形化、design for manufacturing（DFM）和 DTCO 共同解决[6]。BSPDN 正属于这种复杂协同问题：其结构涉及 FEOL、MOL、BEOL 和背面层，任何局部设计规则变化都可能影响标准单元布局、路由资源和工艺可制造性。

因此，BSPDN 不能被视为单独的背面工艺模块，而应被纳入先进节点工艺平台和设计规则体系中统一优化。

## 5 设计协同与 PPA 影响

## 5.1 标准单元缩放

BSPDN 对 PPA 的直接贡献之一是标准单元缩放。Xie 等指出，DBC-based BSPDN 在 cell-level scaling 方面优于部分 DTV 类方案[1]。其原因在于 DBC 可以减少正面 power contact 和深沟槽通孔占用，使标准单元高度和局部互连布局具备进一步优化空间。

CFET inverter 和 stacked complementary nanosheet transistor 相关论文从另一角度展示了功能化晶圆背面对标准单元设计空间的扩展[9-10]。当 nFET/pFET 由平面并排走向垂直堆叠时，供电、接触和信号引脚不再只是正面二维布局问题，而会变成前后两侧资源共同分配的问题。虽然这些工作并非传统 BSPDN 结构本身，但其共同说明，背面层一旦从“仅供电”扩展为“功能互连面”，标准单元和物理实现方法会发生根本变化。

## 5.2 DTCO 与路径搜索

BSPDN 的收益高度依赖设计-工艺协同优化。Banerjee 等关于三维 IC 的经典论文指出，垂直维度可以缓解深亚微米互连瓶颈并为 SoC 集成提供新的结构自由度[7]；这一思想在 BSPDN 中体现为利用晶圆背面分担正面互连和供电压力。面向三维堆叠 FET 的 SA-DBC 与 BGC 研究也表明，当器件和互连走向垂直堆叠后，标准单元、局部接触和布线资源必须联合优化[18]。因此，BSPDN 是否值得引入不能只看单个器件或单根电源线，而需要在 PDK、标准单元库、placement、routing、功耗、性能和面积之间进行系统评估。

Subramani 等关于 backside routing 的论文进一步说明，背面资源如何分配给 power、clock 或 signal，是未来先进节点设计实现中的关键问题[2]。因此，BSPDN 的成熟需要 EDA 工具支持 backside-aware placement/routing、RC extraction、电源完整性分析和热分析。

## 6 热管理与可靠性

## 6.1 BSPDN 的热路径变化

BSPDN 改善供电和布线的同时，也会改变芯片热路径。传统 FSPDN 中，硅衬底较厚，横向热扩散能力较强；而 BSPDN 往往需要极薄硅层、键合氧化层和背面金属结构，可能增加等效热阻并削弱横向热扩散。Xie、Chen 和 Wei 的 ECTC 2024 论文指出，BSPDN 会带来新的热管理挑战，并提出 BEOL 嵌入式微通道和顶部 jet cooling 的双面冷却方案[5]。在 2.5D/3D 异质集成中，热耦合和封装互连也会影响芯片系统级可靠性，相关综述性论文显示先进封装中的功率密度和热管理问题需要与芯片互连共同考虑[20]。

2.5D/3D 集成研究表明，硅中介层、微凸点、TSV 和多芯粒封装会引入复杂的互连和热耦合问题[11,20]。这说明 BSPDN 热评估不能只停留在单器件或单标准单元层面，而应考虑 chiplet、interposer、封装和局部热点共同作用；对于高功率密度系统，过于简化的均匀热通量模型往往不足以支撑设计决策。

![BSPDN 微通道冷却前后温度分布对比](figures/fig6_ref5_temperature_distribution_microchannel.png)

图 6 BSPDN 微通道冷却前后温度分布对比。来源：文献[5] Xie F, Chen R, Wei T, *Thermal Mitigation Strategy for Backside Power Delivery Network*, Fig. 18 “Temperature distribution for BSPDN chip solid domain under water coolant cooling, inlet velocity = 0.06 m/s: (a) Temperature distribution for chip without microchannel cooling; (b) Temperature distribution for chip with microchannel cooling”。BSPDN 改善供电路径的同时会改变热扩散路径，水冷微通道引入后芯片固体区域温度分布发生明显变化。该结果表明，背面供电网络需要与先进封装散热和片上冷却结构协同设计。

## 6.2 可靠性问题

BSPDN 可靠性至少包括四个方面。第一是电可靠性，包括 nTSV 电阻、电迁移和接触电阻漂移。第二是热可靠性，包括热点、热循环和材料热膨胀失配。第三是机械可靠性，包括晶圆键合形变、薄硅翘曲和局部应力。第四是制造可靠性，包括背面对准、刻蚀残留和金属填充缺陷。Zhao 等和 Wang 等的工艺论文分别从 overlay-relaxed slit nTSV 和 smooth-sidewall nTSV 角度回应了部分可靠性问题[3-4]，但完整量产可靠性仍需更多长期数据。

## 7 发展趋势

第一，BSPDN 将与 GAAFET/nanosheet 共同导入先进逻辑节点。GAAFET 解决器件栅控问题，BSPDN 解决供电和互连瓶颈，两者协同才能在芯片级实现 PPA 改善[1,12]。

第二，BSPDN 将从背面供电走向背面布线。背面层未来可能服务于 VDD/VSS、clock、长距离 signal 或部分宏单元连接[2,9-10]。

第三，BSPDN 将与 CFET 和三维集成深度耦合。CFET、Flip FET 和 NanoStack 等技术均会增加垂直方向的器件和互连复杂度，从而提高背面连接和背面供电的重要性[15-19]。

第四，BSPDN 研究将更加重视热-电-机械-设计协同。未来评价 BSPDN 不能只看 IR drop 或 cell height，还应同时评价温度、可靠性、制造成本、设计规则、封装复杂度和系统级收益[5-6,11,20]。

## 8 结论

BSPDN 是后 FinFET 时代先进逻辑制程中具有重要前景的供电与互连架构创新。它通过将电源网络从晶圆正面迁移至背面，减少电源线对正面 BEOL 的占用，降低供电路径阻抗，并为标准单元缩放和背面布线提供新的技术空间。与单纯器件结构创新不同，BSPDN 的价值体现在器件、互连、标准单元、EDA、封装和热管理的系统协同。

归纳现有研究可以看到，当前 BSPDN 的技术演进主要集中在六条线索：一是面向 nanosheet 的 DTV、SFVBP、DBC 和 SABC 结构比较[1]；二是背面层从 power 向 clock/signal 扩展的 backside routing[2]；三是 slit nTSV、Ru/Mo 金属化和高深宽比刻蚀等关键工艺[3-4]；四是三维互连、键合和标准单元设计方法[7-11,18]；五是 BSPDN 带来的热管理和先进封装耦合问题[5,20]；六是与 GAAFET、CFET、NanoStack 和三维集成共同演进的系统趋势[12-17,19]。

总体来看，笔者更倾向于将 BSPDN 判断为先进节点的平台型技术，而不是单一供电模块。其研究难点不在于“是否可以把电源放到背面”这一简单问题，而在于如何在保持器件性能和可靠性的同时，实现低阻供电、可制造背面对准、高质量 nTSV、可用 EDA flow、可控热路径和可验证系统级收益。未来 BSPDN 的成熟程度，将直接影响 2 nm 之后逻辑芯片的 PPA 提升空间。

## 参考文献

[1] Xie R, Pancharatnam S, Miao L, et al. Backside power distribution for nanosheet technologies beyond 2nm[C]//2024 IEEE Symposium on VLSI Technology and Circuits. Honolulu: IEEE, 2024: 1-2. DOI: 10.1109/VLSITechnologyandCir46783.2024.10631449.

[2] Subramani K, et al. Backside routing enablement considerations for advanced node GAA devices[C]//2025 Symposium on VLSI Technology and Circuits. Kyoto: IEEE, 2025: 1-3. DOI: 10.23919/VLSITechnologyandCir65189.2025.11074879.

[3] Zhao P, et al. Backside power delivery with relaxed overlay for backside patterning using extreme wafer thinning and molybdenum-filled slit nano through silicon vias[J]. IEEE Transactions on Electron Devices, 2024, 71(12): 7963-7969. DOI: 10.1109/TED.2024.3487080.

[4] Wang Y, et al. Etch of nano-TSV with smooth sidewall and excellent selection ratio for backside power delivery network[J]. Microelectronic Engineering, 2025, 295: 112265. DOI: 10.1016/j.mee.2024.112265.

[5] Xie F, Chen R, Wei T. Thermal mitigation strategy for backside power delivery network[C]//2024 IEEE 74th Electronic Components and Technology Conference. Denver: IEEE, 2024: 1485-1492. DOI: 10.1109/ECTC51529.2024.00241.

[6] Lanzillo N A, et al. A perspective on interconnect scaling challenges in the NanoStack transistor era: AP/DFM: advanced patterning/design for manufacturing (design-technology co-optimization)[C]//2025 36th Annual SEMI Advanced Semiconductor Manufacturing Conference. Saratoga Springs: IEEE, 2025: 1-6. DOI: 10.1109/ASMC64512.2025.11010679.

[7] Banerjee K, Souri S J, Kapur P, Saraswat K C. 3-D ICs: a novel chip design for improving deep-submicrometer interconnect performance and systems-on-chip integration[J]. Proceedings of the IEEE, 2001, 89(5): 602-633. DOI: 10.1109/5.929647.

[8] Fan A, Rahman A, Reif R. Copper wafer bonding[J]. Electrochemical and Solid-State Letters, 1999, 2(10): 534-536. DOI: 10.1149/1.1390894.

[9] Liao S, et al. First demonstration of monolithic CFET inverter at 48nm gate pitch toward future logic technology scaling[C]//2024 IEEE International Electron Devices Meeting. San Francisco: IEEE, 2024: 1-4. DOI: 10.1109/IEDM50854.2024.10873334.

[10] Liao S, et al. Complementary field-effect transistor (CFET) demonstration at 48nm gate pitch for future logic technology scaling[C]//2023 IEEE International Electron Devices Meeting. San Francisco: IEEE, 2023: 1-4. DOI: 10.1109/IEDM45741.2023.10413672.

[11] Zhang X, Lin J K, Wickramanayaka S, et al. Heterogeneous 2.5D integration on through silicon interposer[J]. Applied Physics Reviews, 2015, 2(2): 021308. DOI: 10.1063/1.4921463.

[12] Yeap G, et al. 2nm platform technology featuring energy-efficient nanosheet transistors and interconnects co-optimized with 3DIC for AI, HPC and mobile SoC applications[C]//2024 IEEE International Electron Devices Meeting. San Francisco: IEEE, 2024: 1-4. DOI: 10.1109/IEDM50854.2024.10873475.

[13] Bao R, et al. Advanced multi-Vt enabled by selective layer reductions for 2nm nanosheet technology and beyond[C]//2024 IEEE International Electron Devices Meeting. San Francisco: IEEE, 2024: 1-4. DOI: 10.1109/IEDM50854.2024.10873425.

[14] Mochizuki S, Kumar S, Greene A, et al. SiGe channel for scaled gate-all-around nanosheet pFET transistor for advanced logic applications[C]//2025 IEEE International Electron Devices Meeting. San Francisco: IEEE, 2025: 1-4. DOI: 10.1109/IEDM50572.2025.11353609.

[15] Demuynck S, et al. Monolithic complementary field effect transistors (CFET) demonstrated using middle dielectric isolation and stacked contacts[C]//2024 IEEE Symposium on VLSI Technology and Circuits. Honolulu: IEEE, 2024: 1-2. DOI: 10.1109/VLSITechnologyandCir46783.2024.10631349.

[16] Vega Gonzalez N, et al. Front-side integration of middle-of-line stacked contacts for monolithic CFET[C]//2024 IEEE International Interconnect Technology Conference. San Jose: IEEE, 2024: 1-3. DOI: 10.1109/IITC61274.2024.10732165.

[17] Vandooren A, et al. Monolithic-CFET with direct backside contact to source/drain and backside dielectric isolation[C]//2024 IEEE International Electron Devices Meeting. San Francisco: IEEE, 2024: 1-4. DOI: 10.1109/IEDM50854.2024.10873520.

[18] Park J, Park J, Hwang K, et al. Highly manufacturable self-aligned direct backside contact (SA-DBC) and backside gate contact (BGC) for 3-dimensional stacked FET at 48nm gate pitch[C]//2024 IEEE Symposium on VLSI Technology and Circuits. Honolulu: IEEE, 2024: 1-2. DOI: 10.1109/VLSITechnologyandCir46783.2024.10631556.

[19] Xiong X, Wu Y. Building inverters with stacked complementary nanosheet transistors[J]. Nature Electronics, 2024, 7: 1072-1073. DOI: 10.1038/s41928-024-01329-3.

[20] Sheikh F, Nagisetty R, Karnik T, Kehlet D. 2.5D and 3D heterogeneous integration: emerging applications[J]. IEEE Solid-State Circuits Magazine, 2021, 13(4): 77-87. DOI: 10.1109/MSSC.2021.3111386.
