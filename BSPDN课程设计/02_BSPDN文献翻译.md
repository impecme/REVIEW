# BSPDN 代表文献翻译与精读

## 1 原文信息

| 项目 | 内容 |
|---|---|
| 英文题目 | Backside Power Delivery With Relaxed Overlay for Backside Patterning Using Extreme Wafer Thinning and Molybdenum-Filled Slit Nano Through Silicon Vias |
| 中文题目 | 基于极薄晶圆减薄与钼填充长条形纳米硅通孔的低对准要求背面供电技术 |
| 作者 | P. Zhao, L. Witters, A. Jourdain, M. Stucchi, N. Jourdan, J. W. Maes, H. Bana, C. Zhu, R. Chukka, F. Sebaai, K. Vandersmissen, N. Heylen, D. Montero, S. Wang, K. D'have, F. Schleicher, J. De Vos, G. Beyer, A. Miller, E. Beyne |
| 期刊 | IEEE Transactions on Electron Devices |
| 年份 | 2024 |
| DOI | 10.1109/TED.2024.3487080 |
| 页数 | PDF 共 7 页 |
| 选择理由 | 该文是正式 IEEE TED 期刊论文，主题直接为 Backside Power Delivery / BSPDN，篇幅比 VLSI/IEDM 短论文更适合课程翻译，内容覆盖极薄晶圆减薄、背面图形化、overlay、BPR、nTSV、Mo 填充和电学测试，是说明 BSPDN 工艺落地难点的代表文献。 |

说明：本文档为课程设计用途的**全文覆盖式中文翻译与精读版**。全文覆盖原文的摘要、关键词、引言、制造流程、工艺开发经验、电学测试与分析、结论、致谢和图表说明。为避免未经授权逐字复刻整篇论文，以下采用“逐节翻译/意译 + 技术解释 + 图表说明翻译 + 术语/生词表”的方式呈现，但内容范围覆盖论文主体全文。

## 2 摘要翻译

背面供电网络（BSPDN）近年来受到广泛关注，因为它有潜力将信号布线和电源布线分开优化。本文使用长条形纳米级硅通孔（slit nTSV），在正面图形化的埋入电源轨（BPR）和晶圆背面正交图形化的金属电源轨之间形成高密度连接。这些 nTSV 在 BPR 上方原位图形化，并利用正面光刻实现自对准；同时，长条形通孔的长度可以调节。

这种设计可以放宽背面图形化对 overlay 的要求。传统背面图形化通常对 overlay 要求严格，因为晶圆键合会造成 wafer grid distortion，即晶圆网格形变。除此之外，本文通过优化晶圆减薄流程，在 10 nm 的 Si0.75Ge0.25 刻蚀停止层上实现极薄晶圆减薄，并获得良好的总厚度变化（TTV）控制。文章还首次展示了低电阻、无阻挡层的钼（Mo）填充 nTSV，相比传统 TiN/W 填充结构，Mo 填充显示出进一步缩放的潜力。

**摘要核心结论：**

1. BSPDN 能够把正面信号布线和背面电源布线分开优化。
2. 长条形 nTSV 可以连接正面 BPR 和背面金属轨。
3. nTSV 由正面光刻定义，能实现自对准并放宽背面 overlay 要求。
4. 优化后的极薄晶圆减薄流程可把 SiGe ESL 降到 10 nm。
5. Mo 填充 nTSV 电阻更低，且不需要传统 barrier，适合后续缩放。

## 3 关键词翻译

| 英文关键词 | 中文翻译 | 说明 |
|---|---|---|
| Backside power delivery network, BSPDN | 背面供电网络 | 将电源网络迁移到晶圆背面的供电架构 |
| Buried power rail, BPR | 埋入电源轨 | 靠近器件前端区域的局部电源轨 |
| Etch stop layer, ESL | 刻蚀停止层 | 用于控制刻蚀终点的薄膜 |
| Extreme wafer thinning | 极薄晶圆减薄 | 将晶圆背面减薄到极小厚度 |
| Nano through silicon via, nTSV | 纳米级硅通孔 | 连接晶圆背面和前端结构的纳米尺度通孔 |

## 4 引言部分翻译与精读

## 4.1 引言翻译

随着 pitch scaling 逐渐趋于饱和，先进逻辑技术的探索重点开始转向标准单元级别甚至更高层级的 scaling booster。BSPDN 是其中受到广泛关注的一项技术，因为它不仅能够带来功耗和性能收益，还能灵活支持标准单元面积缩小。

BSPDN 的核心思想是将电源布线放到晶圆背面，从而把信号布线和电源布线解耦。正面可以专门用于细间距 BEOL 信号布线，背面则可以利用相对宽松的关键尺寸来构建低电阻电源网络。这样不仅有助于降低电源网络电阻，还能够提高芯片面积使用效率。

目前已经提出多种 BSPDN 实现方式，这些方式可以根据背面布线和正面布线之间的连接结构，以及它们与有源器件共同集成的兼容性进行分类。其中，BPR-nTSV-last 方案已经被广泛研究。在该方案中，正面嵌入式 BPR 在正面工艺、晶圆键合和晶圆减薄之后，最终通过背面定义的 nTSV 连接。

已有研究已经缩小了 nTSV 尺寸，并探索了 Cu、W 等多种金属。但当 nTSV 尺寸持续缩小时，传统 TiN/W 结构中的 TiN 阻挡层会占据越来越大的比例，使有效金属填充体积下降，导致电阻上升。因此，需要探索更适合小尺寸 nTSV 的金属填充方案。

本文提出一种 nTSV-first 方案：nTSV 在正面工艺阶段被图形化，并与 BPR 自对准。通孔设计成长条形，尺寸约为 40 nm x 420 nm，可为 nTSV 和背面第一层金属 BSM1 之间提供约 100 nm 的 overlay margin。这样可以显著放宽背面金属图形化的 overlay 要求。

## 4.2 引言精读

这一部分实际上提出了全文的三个关键问题。

第一，**为什么需要 BSPDN**：因为先进节点中正面 BEOL 同时承担信号和电源布线，已经成为 PPA 瓶颈。

第二，**为什么需要 nTSV-first 和 slit nTSV**：传统背面定义通孔对背面对准要求高，而正面定义、自对准的 slit nTSV 可以把难题提前到正面工艺中解决。

第三，**为什么要研究 Mo 填充**：随着通孔尺寸缩小，传统 TiN/W 中的阻挡层会吃掉有效导电截面积，导致电阻增加；Mo 的无阻挡层填充可以减少这一问题。

## 5 制造流程部分翻译

## 5.1 正面工艺

论文中的制造流程如原文 Fig. 2 所示。首先，在体硅衬底上外延生长一层很薄的 Si0.75Ge0.25，厚度为 20 nm 或 10 nm。该层作为刻蚀停止层，用于补偿背面晶圆减薄过程中的厚度不均匀性。

随后进行 BPR 图形化。根据论文描述，BPR 图形化预计在 nanosheet 堆叠、图形化和浅沟槽隔离（STI）形成之后进行。BPR 的 pitch 设计为 105 nm，关键尺寸低于 36 nm，可兼容 N3 5-track 标准单元。BPR 刻蚀需要穿过约 200 nm 厚的 STI，并进一步进入硅衬底约 150 nm。

之后，工艺依次沉积 spin-on-carbon（SOC）和 spin-on-glass（SOG），作为 slit nTSV 图形化的硬掩膜。nTSV 打印之后，硬掩膜先被刻蚀到 BPR 底部，然后原位进行 nTSV 刻蚀，向 BPR 底部以下再刻蚀约 300 nm，实现与 BPR 的自对准。

这里需要注意：nTSV 的刻蚀深度必须超过 SiGe ESL。同时，均匀的 TSV 刻蚀深度对后续背面 knock-off CMP 工艺非常关键。之后，在 via 内沉积 SiO2 liner，再同时填充 BPR 和 nTSV。填充金属可以是 TiN/W，也可以是 Mo，最后通过对应的金属 CMP 完成双镶嵌结构。

## 5.2 背面工艺

正面工艺完成后，器件晶圆通过 SiCN-SiCN fusion bonding 与载片晶圆键合，用于后续背面工艺。器件晶圆的硅衬底需要先被减薄到约 3 微米，然后再进行最终的选择性硅湿法刻蚀。论文比较了不同晶圆减薄流程，并在后文详细分析。

为了暴露通孔，需要进行选择性硅湿法刻蚀，该刻蚀对 SiGe ESL 和 SiO2 via liner 具有良好选择性。随后去除 SiGe，并共形沉积 SiO2 介质层，以隔离硅衬底和背面第一层金属 BSM1。

在背面金属图形化之前，需要进行专门的 knock-off CMP，以去除表面形貌并暴露金属表面。最后，通过 Cu damascene 工艺形成 BSM1。这样，正面 BPR 就通过 nTSV 与背面 BSM1 建立连接。

## 5.3 制造流程精读

这一节说明 BSPDN 的工艺难点并不只是“在背面做金属”。真正的难点包括：

1. 正面 BPR 和 nTSV 必须在纳米尺度上对准；
2. 晶圆背面必须减薄到微米级甚至更薄；
3. 需要通过 SiGe ESL 控制刻蚀终点；
4. nTSV 必须穿过 ESL 并可靠连接 BPR；
5. 金属填充要同时满足低电阻、可填充性和可靠性。

## 6 工艺开发经验翻译

## 6.1 修正后的晶圆减薄流程

论文指出，虽然 SiGe ESL 在最初的正面工艺中已经生长，但实际所需 SiGe 厚度由背面晶圆减薄性能决定，尤其取决于最终选择性硅湿法刻蚀前的晶圆厚度均匀性。若 TTV 较大，就需要更厚的 SiGe ESL 以避免 punchthrough，即局部过刻穿透。

但是，较厚的 SiGe 层会因为 Si/SiGe 晶格失配而引入缺陷，并可能影响器件性能。因此，理想方案是使用足够薄但仍能发挥刻蚀停止作用的 ESL。

作者此前使用的晶圆减薄流程较复杂：先用 grinding 将硅衬底从 775 微米减薄到 50 微米，再进行 1 微米 CMP 以平坦化表面，随后用干法或湿法刻蚀减薄到 10 微米，再用单独湿法刻蚀减薄到 3 微米，最后进行选择性湿法刻蚀直至 SiGe ESL。

论文监测了整个减薄流程中的 TTV。结果显示，CMP 后 TTV 低于 2 微米，但后续干法/湿法刻蚀会显著恶化 TTV。为了补偿最终选择性硅湿法刻蚀前超过 3 微米的 TTV，原流程必须使用约 50 nm 的较厚 SiGe ESL。

为简化流程并改善 TTV，本文提出修正后的减薄流程。新流程使用带嵌入式 CMP 的 grinder，直接将晶圆从 775 微米减薄到 3 微米。在第一轮学习周期中，TTV 平均值约为 1.5 微米；第二轮中，TTV 平均值降低到 1 微米以下，最小 TTV 达到 0.4 微米。低 TTV 使得使用 20 nm 或 10 nm 的薄 SiGe ESL 成为可能。

对于使用 10 nm SiGe ESL 的晶圆，最终选择性湿法刻蚀后的 TEM 结果显示：晶圆中心仍剩余 9 nm SiGe，晶圆边缘仍剩余 3 nm SiGe，未检测到 punchthrough。

## 6.2 背面光刻和金属化

论文使用 scanner 测得 BSM1-BPR overlay vector map。结果显示，在不使用 HOCPE 的情况下，包括极端边缘在内，整个晶圆最大 overlay 小于 70 nm，低于前文设计的 100 nm alignment margin。

图中还可以看到，晶圆中心存在一个 overlay 较小的内部方形区域，而较大的 overlay 区域呈四个对称扇形分布在晶圆中部周围。论文进一步比较了键合后的 residual vector map，发现其矢量分布和大小与 BSM1-BPR overlay map 类似。这说明晶圆键合引起的 wafer grid distortion 是背面光刻与正面结构对准误差的主要来源。

对于 Mo 填充 via，由于暴露的 Mo 表面容易氧化，因此 BSM1 Cu 金属化需要特殊保护。作者在 knock-off CMP 后先沉积薄 SiCN 层保护 Mo；打开保护层后，进行表面清洗和 Ta 阻挡层沉积。TEM 和 EDS 分析显示，Mo via 与 Cu BSM1 的界面没有检测到氧信号，说明界面没有明显氧化。

对于 TiN/W 填充 via，虽然暴露 W via 的氧化风险较低，作者仍进行了类似 EDS 分析，也确认了无氧界面。最终 TEM 显示，nTSV 可以在两个正交方向上连接正面 BPR 和背面 BSM1。

## 6.3 工艺开发经验总结

这一节的关键贡献是：

1. 通过修正减薄流程，显著改善 TTV；
2. 将 SiGe ESL 从 50 nm 降到 10 nm；
3. 使用 slit nTSV 设计，把背面 overlay 要求控制在 100 nm margin 内；
4. 通过界面保护和 EDS 验证，证明 Mo-filled via 与 Cu BSM1 可形成无明显氧化的连接界面。

## 7 电学测试与分析翻译

## 7.1 测试对象

为了证明 nTSV-first 集成方案的可行性，论文对三类测试结构进行电学测量：

1. BPR；
2. 单个 nTSV；
3. BPR-TSV 连接链。

测试中还包含若干设计变化，例如关键尺寸和阻挡层厚度。作者指出，BPR/nTSV 电阻会直接影响 BSPDN 的 IR-drop，因此低电阻金属非常重要。Mo 作为低电阻、无阻挡层填充材料，被用于与传统 TiN/W 填充结构进行比较。

## 7.2 BPR 电阻

论文使用不同长度的 BPR 测试结构提取 BPR 电阻，BPR 长度包括 2 微米、10-100 微米等。作者比较了 Mo 填充和 TiN/W 填充的单位长度归一化电阻。

结果显示，Mo 填充晶圆的 BPR 电阻比 TiN/W 填充晶圆低 2-3 倍。同时，Mo 晶圆的数据分布更集中，说明 Mo 金属化工艺更稳定。相比之下，TiN/W 晶圆的数据分布更分散，主要与晶圆内阻挡层厚度变化有关。

作者还通过 TCR 测试提取电阻率和截面积。结果显示，Mo 的电阻率约比 TiN/W 低 30%。

## 7.3 单个 nTSV Kelvin 电阻

论文还比较了单个 nTSV 的 Kelvin 电阻。三片 Mo 填充晶圆的平均 nTSV 电阻为 5.3 欧姆，并表现出较紧的数据分布。相比之下，TiN/W 填充晶圆的 nTSV 电阻可达到 15 欧姆，部分异常点更高。

TiN/W nTSV 电阻分布较大的原因不仅与 TiN 阻挡层厚度有关，也与 TSV 刻蚀轮廓有关。为分析这一问题，作者建立了三维仿真模型，考虑 TiN 阻挡层厚度和 TSV 侧壁斜率角的变化。模型尺寸用 TEM 图像校准，电学参数与工艺数据库对齐。

仿真结果与实验趋势定性一致。若假设刻蚀侧壁角约为 88 度，TiN 厚度为 2.5 nm 和 5 nm 时，仿真电阻分别约为 9.1 欧姆和 11.6 欧姆，与实验中对应晶圆的中位电阻相符。这说明如果刻蚀轮廓足够直、阻挡层足够薄，TiN/W nTSV 电阻也可以降至 10 欧姆以下，但可靠性仍需进一步评估。

## 7.4 链路电阻

长链路电阻由多个单位链路电阻累加而成。每个单位链路电阻主要由两个部分组成：单个 nTSV 的电阻，以及与之串联的 BPR 片段电阻。由于 BSM1 线宽较大，其贡献可以忽略。因此，单位链路电阻可以近似表示为：

```text
R_chain ≈ R_BPR × L_BPR + R_nTSV
```

其中，`L_BPR` 是 BPR 片段长度。

论文测量了不同单位数的链路结构，单位数范围从 60 到 3800。归一化后的链路电阻结果表明，Mo 和 TiN/W 填充晶圆之间的对比与前面 BPR 和 nTSV 的结果一致。

论文最后还指出，未来如果要进一步推进该 nTSV-first 集成方案，需要建立更详细的工艺监测系统。该系统应关注不同制造步骤中的工艺波动，并把这些波动与最终电学性能联系起来。特别是在将 BPR-nTSV-first 方案与有源器件集成时，必须识别哪些工艺因素会影响最终器件性能。与此同时，继续探索更灵活的晶圆减薄流程和替代金属填充方案仍然很重要；不同金属填充 via 的可靠性评估也必不可少。

## 7.5 电学测试总结

电学测试部分的核心结论是：

1. Mo 填充 BPR 电阻显著低于 TiN/W；
2. Mo 填充 nTSV 平均 Kelvin 电阻约为 5.3 欧姆；
3. TiN/W 电阻较高且分布更宽，受阻挡层厚度和刻蚀轮廓影响；
4. 链路电阻测试验证了 BPR 和 nTSV 单项测试的趋势；
5. Mo-filled nTSV 具有作为低阻 BSPDN 垂直连接的潜力。

## 8 结论翻译

论文结论指出：通过在正面工艺中将自对准长条形 nTSV 图形化到 BPR 上，可以显著放宽背面金属布线的 overlay 要求，并且在背面图形化过程中不再需要 HOCPE。由于修正后的极薄晶圆减薄流程改善了 TTV，Si0.75Ge0.25 ESL 的厚度可以从 50 nm 降低到 10 nm。

从电学性能看，与 TiN/W 填充相比，Mo 填充晶圆在多种测试结构中表现出更低电阻和更紧的数据分布。总体而言，论文提出了一种从晶圆正面定义的 nTSV-to-BPR 替代连接方案，丰富了在 FinFET、nanosheet 或 CFET 中实现 BSPDN 的技术工具箱。

## 9 致谢与参考文献说明

## 9.1 致谢翻译

作者在致谢中感谢 imec 3-D system integration program 的成员和合作伙伴，感谢 imec pilot line、电学测量团队、材料表征分析团队以及 ICT 团队对本文工作的支持。

## 9.2 参考文献处理说明

原文参考文献主要用于支撑 BPR、BSPDN、PowerVia、FFET、晶圆键合、低阻金属化和电阻率测试等背景。课程翻译中不逐条翻译参考文献列表的全部题名，但在综述正文和译者总结中已经保留与本文主题最相关的技术脉络：BSPDN 作为 standard-cell/system scaling booster，依赖 BPR、nTSV、晶圆减薄、背面对准和低阻金属填充共同实现。

## 10 图表说明翻译

| 图号 | 原图主要内容 | 中文说明 |
|---|---|---|
| Fig. 1 | 两种 nTSV-BPR 连接方式示意 | 对比 nTSV-last 与 nTSV-first。nTSV-first 中 nTSV 在正面工艺中定义，可与 BPR 自对准，并通过 slit 形状放宽背面 overlay。 |
| Fig. 2 | 工艺流程和 Coventor 图像 | 展示正面工艺和背面工艺流程，灰色部分表示未来 nanosheet 器件制造步骤。 |
| Table I | 两种晶圆减薄流程对比 | 比较旧流程和修正流程，说明新流程简化并改善 TTV。 |
| Fig. 3 | 不同减薄流程的 TTV 对比 | 红色为旧流程，蓝色为新流程；新流程 TTV 更低。 |
| Fig. 4 | 两种减薄流程的 TTV profile | 旧流程 profile 起伏较大，新流程更平坦。 |
| Fig. 5 | 最终硅湿法刻蚀后的 TEM | 使用 10 nm SiGe ESL 后，中心和边缘仍有 SiGe 剩余，未发生 punchthrough。 |
| Fig. 6 | BSM1-BPR overlay map 和 bonding residual map | 说明 overlay 分布与晶圆键合形变相关，且最大 overlay 仍在 100 nm margin 内。 |
| Fig. 7 | Cu BSM1 与 Mo/TiN-W via 界面的 TEM/EDS | 说明界面未检测到氧信号，金属连接界面质量较好。 |
| Fig. 8 | FS-BS 连接 TEM | 展示 nTSV 如何桥接正面 BPR 和背面 BSM1。 |
| Fig. 9 | BPR 电阻对比 | Mo 填充 BPR 电阻低于 TiN/W，Mo 电阻率约低 30%。 |
| Fig. 10 | 单个 nTSV Kelvin 电阻与仿真 | Mo-filled nTSV 平均电阻低且分布紧；TiN/W 电阻受 barrier 厚度和侧壁角影响。 |
| Fig. 11 | 单位链路电阻累计分布 | 链路电阻结果与 BPR 和 nTSV 单项测试趋势一致。 |

## 11 术语表

| 英文术语 | 中文翻译 | 说明 |
|---|---|---|
| BSPDN | 背面供电网络 | 将电源网络放到晶圆背面的供电架构 |
| BPR | 埋入电源轨 | 位于器件附近的局部电源轨 |
| nTSV | 纳米级硅通孔 | 纳米尺度垂直连接通孔 |
| slit nTSV | 长条形纳米硅通孔 | 可提高 overlay 容差的长条形通孔 |
| FS | 正面 | frontside，晶体管和正面互连所在一侧 |
| BS | 背面 | backside，背面电源网络所在一侧 |
| BSM1 | 背面第一层金属 | backside metal 1 |
| ESL | 刻蚀停止层 | 用于控制刻蚀终点 |
| TTV | 总厚度变化 | total thickness variation，衡量晶圆厚度均匀性 |
| overlay | 套刻/对准误差 | 不同图形层之间的位置偏差 |
| wafer grid distortion | 晶圆网格形变 | 键合等过程导致的晶圆坐标变形 |
| fusion bonding | 熔融键合 | 晶圆级键合方法 |
| knock-off CMP | 去除凸起的 CMP | 用 CMP 去除表面形貌并暴露金属 |
| damascene process | 镶嵌工艺 | 先刻槽/孔再填金属的互连工艺 |
| barrier-free | 无阻挡层 | 不需要 TiN 等阻挡层 |
| Kelvin resistance | Kelvin 电阻 | 四端测量得到的精确电阻 |
| TCR | 电阻温度系数 | 用于提取电阻率和截面积 |
| punchthrough | 过刻穿透 | 刻蚀越过停止层造成穿透 |
| EDS | 能谱分析 | 检测元素分布，判断是否氧化 |
| HOCPE | 高阶芯片放置误差校正 | high-order chip placement error correction，用于补偿背面光刻中的网格形变 |
| TCR test | 电阻温度系数测试 | 通过温度相关电阻变化提取材料电阻率 |

## 12 面向初学者的英文生词表

| 英文词/短语 | 中文意思 | 在本文中的用法 |
|---|---|---|
| relaxed overlay | 放宽的套刻要求 | 指背面图形化不需要极高对准精度 |
| patterning | 图形化 | 光刻和刻蚀形成结构图形 |
| extreme wafer thinning | 极薄晶圆减薄 | 将晶圆减薄到微米级 |
| molybdenum-filled | 钼填充的 | 用 Mo 填充 nTSV/BPR |
| slit | 狭缝、长条形开口 | slit nTSV 指长条形通孔 |
| in situ | 原位 | 在同一流程或同一位置中完成 |
| self-alignment | 自对准 | 依赖结构本身实现对准 |
| stringent | 严格的 | stringent requirement 指要求很高 |
| grid distortion | 网格形变 | 晶圆坐标系统发生变形 |
| etch stop layer | 刻蚀停止层 | 控制刻蚀终点的材料层 |
| total thickness variation | 总厚度变化 | 晶圆厚度不均匀性 |
| counterpart | 对应物、对照对象 | TiN/W counterparts 指 TiN/W 对照样品 |
| pitch scaling | 间距缩小 | 器件/互连 pitch 持续减小 |
| standard cell | 标准单元 | 数字电路库中的基本逻辑单元 |
| critical dimension | 关键尺寸 | 工艺中关键线宽或结构尺寸 |
| hard mask | 硬掩膜 | 用于刻蚀转移图形的材料层 |
| conformally deposited | 共形沉积 | 沿结构表面均匀覆盖沉积 |
| selective etching | 选择性刻蚀 | 对某材料刻蚀快，对另一材料刻蚀慢 |
| over etch | 过刻 | 为保证刻蚀完全而额外刻蚀 |
| punchthrough | 刻穿 | 局部过刻导致穿透停止层 |
| residual vector map | 残余矢量图 | 表征对准残差的图 |
| oxidation | 氧化 | 金属表面与氧反应 |
| interface | 界面 | 两种材料接触区域 |
| distribution | 分布 | 数据或参数的分散情况 |
| outlier | 异常点 | 明显偏离主要数据的点 |
| sensitivity simulation | 敏感性仿真 | 改变参数观察结果变化 |
| slope angle | 侧壁倾角 | TSV 侧壁与垂直方向相关的角度 |
| chain link resistance | 链路电阻 | 多个单元串联后的电阻 |
| process variability | 工艺波动 | 制造过程中参数不一致 |
| feasibility | 可行性 | demonstrate the feasibility 指证明方案可行 |
| alternative | 替代的 | alternative scheme 指替代方案 |
| toolbox | 工具箱 | 比喻可供工艺实现选择的一组技术方案 |
| active device | 有源器件 | 晶体管等需要电源和偏置工作的器件 |

## 13 译者总结

这篇 IEEE TED 论文比 VLSI 短文更适合作为课程设计的“文献翻译”，原因是它篇幅更长，结构完整，并且直接围绕 BSPDN 工艺实现展开。文章不是泛泛介绍背面供电，而是解决 BSPDN 落地中的三个关键问题：

1. **背面对准问题**：通过正面定义的 self-aligned slit nTSV，使背面金属图形化获得约 100 nm 的 overlay margin。
2. **极薄晶圆减薄问题**：通过修正减薄流程，把 TTV 控制到 1 微米以下，并使 SiGe ESL 厚度从 50 nm 降到 10 nm。
3. **低阻垂直连接问题**：通过 Mo-filled nTSV/BPR 降低电阻，Mo 填充结构相比 TiN/W 具有更低电阻和更紧的数据分布。

本文对 BSPDN 课程设计的支撑作用非常直接：它说明 BSPDN 不只是“把电源放到背面”的概念，而是包含 BPR、nTSV、晶圆减薄、背面对准、金属填充、电阻测试和可靠性评估的一整套工艺集成问题。对于综述正文而言，该文可重点支撑“BPR 与 nTSV 路线”“晶圆减薄与背面对准”“nTSV 刻蚀与金属化”“BSPDN 工艺实现挑战”等章节。

可用于报告中的标准表述：

Zhao 等在 IEEE Transactions on Electron Devices 发表的研究表明，通过在正面工艺中形成 self-aligned slit nTSV，并将其与 BPR 集成，可以显著放宽背面金属图形化的 overlay 要求；同时，修正后的极薄晶圆减薄流程可将 SiGe ESL 厚度降低至 10 nm，Mo-filled nTSV/BPR 结构则表现出比 TiN/W 更低的电阻和更稳定的数据分布。这说明 BSPDN 的工程化关键不只是背面供电网络设计，还包括背面对准、极薄晶圆减薄、低阻垂直连接和金属化可靠性等完整工艺链条。
