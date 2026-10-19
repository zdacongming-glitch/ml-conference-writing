# 经典论文的论证与叙述阅读笔记

这是旧版的 12 篇重点阅读摘记。完整升级语料及逐篇阅读状态见[三会语料索引](conferences/index.md)；本页不额外计入篇数，也不替代新库的全文阅读记录。

核查日：2026-09-30。选择 12 篇已发表于三大会的代表性经典，每会 4 篇，覆盖方法、理论反例、经验研究与计算近似。这里的“经典”是为学习论证而作的选样，不是完整经典名单、引用量排名或录用偏好的统计推断。

均取得全文，并围绕写作目的重点精读摘要、引言、关键构造或结果、实验组织与结尾；以下不是逐式证明审计或实验复现。笔记是原创分析，不复制论文段落。读的是历史论文，不能把其当年的最佳结果、文献判断和评估惯例写成今天仍成立的事实。

## 按论证任务选读

| 需要学习的动作 | 论文 |
| --- | --- |
| 将具体困难转为可实现的设计 | M01 Batch Normalization；M05 AEVB |
| 把组件与设计理由接到证据 | M02 SimCLR；M06 GAT；M10 Transformer |
| 先精确定义学习目标和评估对象 | M03 MAML |
| 用反常观察提出经验问题 | M04 Calibration；M07 Rethinking Generalization |
| 用反例定位缺口，再给条件化修复 | M08 AMSGrad |
| 从计算成本引出近似及误差分析 | M09 Random Features |
| 分开直觉、理想分析和实际算法 | M11 GAN |
| 解释目标函数选择，并坦诚不同指标的权衡 | M12 DDPM |

范例不必来自目标会议；选与当前稿件的论证任务相近者。迁移的是组织逻辑，不是作者特殊句式或整篇固定章节数。

## M01 · Batch Normalization — ICML 2015

Sergey Ioffe、Christian Szegedy. *Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift*. PMLR 37:448–456。[出版记录](https://proceedings.mlr.press/v37/ioffe15.html)；[会议全文](https://proceedings.mlr.press/v37/ioffe15.pdf)。

- **定位**：摘要与 §1；§2 的困难；§3、§3.1；§4.2；§5。
- **论证链**：训练困难 → 归一化直觉 → 朴素做法的问题 → 可微的 mini-batch 构造 → 分开训练与推断 → 训练步数及识别效果。
- **可迁移动作**：解释设计时，逐项回答为何不直接用已有做法、为何需要可学习缩放、推断时怎样使用统计量。方法动机落实到算法操作。
- **边界**：论文提出的机制解释不能仅凭性能改善就当作完整因果证明；训练步数减少不等于同倍率的实际耗时减少，单模型与集成结果也须分开。

## M02 · SimCLR — ICML 2020

Ting Chen、Simon Kornblith、Mohammad Norouzi、Geoffrey Hinton. *A Simple Framework for Contrastive Learning of Visual Representations*. PMLR 119:1597–1607。[出版记录](https://proceedings.mlr.press/v119/chen20j.html)；[会议全文](https://proceedings.mlr.press/v119/chen20j/chen20j.pdf)。

- **定位**：摘要、§1–2 与框架图；§3、§4.2、§5.2；§6、§8。
- **论证链**：简洁框架 → 关键设计因素 → 分别检验增强、投影头及训练配置 → 汇总比较。
- **可迁移动作**：让实验标题回应引言中的具体判断；把实际观察和机制猜想分开，再用针对性实验研究猜想。说明使用投影前还是投影后的表示。
- **边界**：框架简洁不表示计算便宜；大 batch 与训练时长相关。linear evaluation、半监督微调及迁移不能混报成同一种性能。组件曾出现于前作，并不妨碍组合及系统认识成为贡献。

## M03 · MAML — ICML 2017

Chelsea Finn、Pieter Abbeel、Sergey Levine. *Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks*. PMLR 70:1126–1135。[出版记录](https://proceedings.mlr.press/v70/finn17a.html)；[会议全文](https://proceedings.mlr.press/v70/finn17a/finn17a.pdf)。

- **定位**：摘要、§1 和示意图；§2 的任务分布与适配目标；§5 开头；§6。
- **论证链**：少量新数据下的快速适配 → 学习容易适配的初始化 → 外层评价更新后的模型 → 跨任务实验回答预先提出的问题。
- **可迁移动作**：先用一句直觉说明优化的对象，再给内外层目标；区分支持数据、适配步骤和更新后的评价数据。
- **边界**：“model-agnostic”受梯度训练条件约束；少样本指新任务适配，不代表元训练总数据或计算很少，也不等于任意分布外泛化。

## M04 · Calibration — ICML 2017

Chuan Guo、Geoff Pleiss、Yu Sun、Kilian Q. Weinberger. *On Calibration of Modern Neural Networks*. PMLR 70:1321–1330。[出版记录](https://proceedings.mlr.press/v70/guo17a.html)；[会议全文](https://proceedings.mlr.press/v70/guo17a/guo17a.pdf)。

- **定位**：§1 与首图；§2 度量；§3；§4–5；§6。
- **论证链**：决策需要可靠置信度 → 精度和校准的差异 → 定义度量 → 研究相关因素 → 比较校准方法 → 留下机制问题。
- **可迁移动作**：在复杂方法之前用一个清楚的现象建立问题；结果段先区分不同评价维度，再解释改进。作者明确避免从因素比较直接声称因果。
- **边界**：较低经验校准误差不保证任意分布下校准，也不等于分类更准；简单修正有效，不代表成因已解释完毕。

## M05 · Auto-Encoding Variational Bayes — ICLR 2014

Diederik P. Kingma、Max Welling. *Auto-Encoding Variational Bayes*。[ICLR 2014 官方论文记录](https://iclr.cc/archive/2014/old-site/conference-proceedings.html)；实际阅读 [arXiv v10，2014-05-01](https://arxiv.org/pdf/1312.6114v10)，而非后来更新的摘要版本。

- **定位**：摘要、§1；§2.1 的问题条件、§2.3–2.4 的估计与重参数化；§6–7。
- **论证链**：难算的后验与大规模数据 → 可微随机估计 → 重参数化 → 识别网络实现摊销推断 → 潜变量模型实例。
- **可迁移动作**：将一般估计工具与具体应用区分；每个数学步骤都说明解除哪一个计算障碍，并用简单分布解释抽象变换。
- **边界**：可优化下界不是精确边际似然；近似后验不等于真实后验。连续潜变量及可微构造的条件不能删掉。

## M06 · Graph Attention Networks — ICLR 2018

Petar Veličković 等. *Graph Attention Networks*。[OpenReview 会议记录](https://openreview.net/forum?id=rJXMpikCZ)；实际阅读 [作者全文 v3，2018-02-04](https://arxiv.org/pdf/1710.10903v3)，页首标明发表于 ICLR 2018。

- **定位**：§1 的图数据需求与前作分类；§2 的单层构造、多头及性质；§3；§4。
- **论证链**：不规则邻域带来的要求 → 局部共享的注意力算子 → 多头组合 → 按 transductive／inductive 设置评价。
- **可迁移动作**：先列设计要满足的实际需求，再解释每项操作怎样满足；先讲单个可理解的算子，再扩展成网络。
- **边界**：邻域注意力仍需要相应图结构；注意力图不能自动视为因果解释。论文把更深入的解释性分析留作未来工作；历史上对谱方法的概括也不能直接套到今天。

## M07 · Rethinking Generalization — ICLR 2017

Chiyuan Zhang、Samy Bengio、Moritz Hardt、Benjamin Recht、Oriol Vinyals. *Understanding deep learning requires rethinking generalization*。[OpenReview 会议记录](https://openreview.net/forum?id=Sy8gdB9xx)；实际阅读 [作者全文 v2，2017-02-26](https://arxiv.org/pdf/1611.03530v2)。

- **定位**：摘要与 §1；randomization experiments；regularization 与 finite-sample expressivity 部分；结尾。
- **论证链**：高容量模型为何泛化 → 随机标签检验 → 拆开拟合能力、显式正则和优化作用 → 指出仍待解释的问题。
- **可迁移动作**：把笼统疑问变成能反驳某种解释的对照；用分层发现组织贡献，结尾准确保留未解之处。
- **边界**：能拟合随机标签不推出所有正则化无用，也不推翻全部统计学习理论；表达能力结果不是泛化保证。不要仅模仿标题的挑战性语气。

## M08 · Adam / AMSGrad — ICLR 2018

Sashank J. Reddi、Satyen Kale、Sanjiv Kumar. *On the Convergence of Adam and Beyond*。[OpenReview 会议记录](https://openreview.net/forum?id=ryQu7f-RZ)；实际阅读 [作者全文 v1，2019-04-19](https://arxiv.org/pdf/1904.09237v1)。该公开存档上传于 2019，论文页首及出版信息对应 **ICLR 2018**。

- **定位**：§1；自适应方法共同框架；§3 反例；§4 修正与遗憾界；实验和讨论。
- **论证链**：收敛疑问 → 统一更新形式 → 简单反例及直觉 → 长期记忆修复 → 条件化理论 → 实验。
- **可迁移动作**：先让读者看到故障如何发生，再说明修改为何针对该故障；定理之后解释其作用域。
- **边界**：存在不收敛问题不等于 Adam 总失败；凸在线优化的遗憾结论不等于非凸深网全局收敛。还应区分理论采用的参数日程与实践设置。

## M09 · Random Features — NIPS 2007

Ali Rahimi、Benjamin Recht. *Random Features for Large-Scale Kernel Machines*. NIPS 20。[出版记录](https://papers.nips.cc/paper_files/paper/2007/hash/013a006f03dbc5392effeb8f18fda755-Abstract.html)；[会议全文](https://papers.nips.cc/paper_files/paper/2007/file/013a006f03dbc5392effeb8f18fda755-Paper.pdf)。

- **定位**：摘要、§1–2；§3 随机特征与近似；实验；§6。
- **论证链**：核方法计算负担 → 显式随机映射 → 用线性学习器处理 → 核近似分析 → 速度与精度比较。
- **可迁移动作**：把主要改变说成对哪个对象作近似，再连接表示、计算与误差；不让“更快”脱离精度代价。
- **边界**：核函数的近似保证不能直接替代预测风险保证；条件决定适用核与输入范围。历史运行时间不能当作今天任何硬件上的普遍加速倍数。

## M10 · Transformer — NIPS 2017

Ashish Vaswani 等. *Attention Is All You Need*. NIPS 30。[出版记录](https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)；[会议全文](https://papers.nips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)。

- **定位**：§1–2；§3 架构图与组件；§4 对照表；§5；§6.1–6.2；§7。
- **论证链**：顺序计算的限制 → 注意力架构 → 用并行性、复杂度和路径长度解释选择 → 训练协议 → 任务结果与组件变化。
- **可迁移动作**：先给系统全貌，再拆组件；设计比较使用明确的评价轴，结果区分实际测量与估算成本。
- **边界**：自注意力的优势依赖序列长度等条件；训练并行不等于自回归生成完全并行。标题不表示网络没有前馈层等组件，也不构成跨所有任务的结论。

## M11 · GAN — NIPS 2014

Ian J. Goodfellow 等. *Generative Adversarial Nets*. NIPS 27。[出版记录](https://papers.nips.cc/paper_files/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html)；[会议全文](https://papers.nips.cc/paper_files/paper/2014/file/f033ed80deb0234979a61f95710dbe25-Paper.pdf)。

- **定位**：§1；§3 博弈目标及实际更新；§4.1–4.2；§5–7。
- **论证链**：生成学习的计算困难 → 对抗直觉 → 精确目标 → 理想条件下分析 → 实际交替训练 → 优点与限制。
- **可迁移动作**：用直觉降低进入门槛，随即给操作定义；解释实际训练为何调整原始损失。论文明确提醒理想分析并不直接适用于有限参数网络的实际优化。
- **边界**：最优判别器、足够容量等条件不可省；不要把理想分布空间结论写成实际 SGD 必然收敛。原文当年的评价方法也不是现代生成论文的通用规范。

## M12 · DDPM — NeurIPS 2020

Jonathan Ho、Ajay Jain、Pieter Abbeel. *Denoising Diffusion Probabilistic Models*. NeurIPS 33。[出版记录](https://proceedings.neurips.cc/paper_files/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html)；[会议全文](https://papers.nips.cc/paper_files/paper/2020/file/4c5bcfec8584af0d967f1ab10179ca4b-Paper.pdf)。

- **定位**：摘要与 §1；§2；§3.2、§3.4；§4.1–4.3；§5。
- **论证链**：扩散模型的样本质量问题 → 参数化与目标选择 → 与去噪的联系 → 消融 → 质量、似然与压缩解释。
- **可迁移动作**：围绕关键设计选择组织推导和实验；在介绍优势时主动承认另一指标不占优，避免“全面优越”的空泛结论。
- **边界**：简化目标改变了原变分目标的权重，不能写成无条件等同；样本质量指标不等于全部分布拟合能力，更不能把后来快速采样器的表现归给此文。

## 来源与版本使用方法

ICML、NeurIPS 使用会议出版全文；ICLR 使用官方会议记录核对归属，并读取上面锁定版本的作者全文。部分 OpenReview PDF 直接访问受限，所以没有声称逐页读取其站点上的版本。正式引用如需逐字引文、最终页码或定理编号，应再核对实际引用版本。

把卡片用于“当前段落缺少什么论证动作”的诊断。不要因某篇有强势标题、首图或贡献列表，就规定所有投稿都照做；不要以经典论文已被录用来证明其每一项写法或技术解释都无可改进。
