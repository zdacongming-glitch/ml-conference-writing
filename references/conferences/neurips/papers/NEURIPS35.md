# NEURIPS35 · Direct Preference Optimization: Your Language Model is Secretly a Reward Model

- Rafael Rafailov、Archit Sharma、Eric Mitchell、Stefano Ermon、Christopher D. Manning、Chelsea Finn；NeurIPS 2023；[官方Outstanding Main Track Runner-Up](https://blog.neurips.cc/2023/12/11/announcing-the-neurips-2023-paper-awards/)，非Test of Time。
- 来源：[正式记录](https://papers.nips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html)。读正式PDF第1–10页全部主文、图1–3及表1–2，检视第2、7、8页；另读官方补充第1–13页（印刷页15–27）A–D，包括证明、实现、评估提示、失败样文和人类研究协议。

摘要把行为控制问题、RLHF复杂管线、奖励与策略重参数化、分类损失及任务证据连起来。引言先区分知识能力与期望行为，再解释相对偏好易于收集和多模型训练开销。图1（第2页）承担流程对比，不承担理论等价证明。第2节相关工作提前定位语言对齐及离线偏好学习；第3节完整说明SFT、奖励模型与KL约束RL，读者才有条件理解第4节消去配分函数。

第4–5节从非参数最优策略推奖励比值，相同prompt的偏好对使归一化项抵消，再给带动态权重的分类梯度；未加权unlikelihood的退化作为必要反例。定理1及补充A要求正beta和参考策略全支持，并采用Bradley–Terry偏好模型。奖励等价类与最优策略的表达结论，不等于有限神经网络、有限离线数据和实际优化已精确求解所有RLHF问题。

第6节按受控情感、摘要、对话递进。图2左比较奖励与KL前沿，而非只取更高奖励；情感“ground truth”是指定分类器。右图与图3由GPT-4判胜、带采样温度；对话未获得可用PPO模型，Best-of-128只是强代理，不能写成同设定PPO直接比较。CNN/DailyMail迁移表中绝对胜率仍低于0.5，收益是相对所比方法。

第6.4节和补充C.2/D.3把评估器变成研究对象：gpt-4-0314、回答次序随机化、简洁提示与原提示、人类比较及温度均交代。补充表7–10保留冗长事实错误与GPT-4误判；人类样本主要来自Stanford STEM群体，不能推出普遍人群偏好一致。第7节以开放问题和局限结束，涉及分布转移、过优化、超过6B的规模与评估提示依赖。

可迁移“复述目标及约束—可核查变量替换—实现简化—受控前沿—实际任务—评估器验证”。适用于替换复杂训练管线；理论、实现和偏好评价须分别给证据。无显式奖励模型不代表无参考模型、无偏好假设或无评估偏差。
