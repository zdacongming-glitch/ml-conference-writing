# NEURIPS-C02 · Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?

- Yang Yue（乐洋）、Zhiqi Chen、Rui Lu、Andrew Zhao、Zhaokai Wang、Yang Yue（乐阳）、Shiji Song、Gao Huang；NeurIPS 2025主轨；[官方2025 Runner-Up](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)。两位Yang Yue是不同作者，不能自动去重。校准当年负结果写法，非长期认可证明。
- 来源：[正式记录](https://papers.nips.cc/paper_files/paper/2025/hash/537d5aa768c2d534016a4d06f87bc8fb-Abstract-Conference.html)。读正式36页PDF第1–11页完整主文与作者贡献、图1–9和表1–2；检视第2、4、6–10页。另读第16–29页A–F附录文字、图注、表3–6、两篇CoT及提示；补充曲线未全部视觉核查，不宣称独立验证推理轨迹。

摘要给出流行解释、替代问题、覆盖指标、跨模型证据与方向；引言先承认低采样预算收益，再问它来自新策略还是既有分布重加权。第2节定义zero-RL与非zero起点、pass@k及其不同于Best-of-N的目的，主动处理碰巧答对风险。这里pass@k是给定提示、解码、预算和验证器的可解覆盖代理，不是无限支持集或部署效用。

第3节按数学、代码、视觉推理扩展，表1集中列模型起点/算法/任务，正文说明相同零样本提示与采样参数。图2、4主要显示曲线交叉；图3（第6页）的DeepCoder在已画区间仍略高，图9前沿模型在大k差距缩小，不应一概改写成“每条曲线都被反超”。人工CoT检查覆盖难题小子集，AIME24还启发式过滤猜测题，不能证明全部正确末答案都有可靠过程。

第4节以正确率直方图、可解题集合、困惑度解释，再对照蒸馏、算法、训练步数、rollout/KL/熵与规模。图5区分零命中与高命中质量；表2/附录D.7承认有限预算下少量RL独有命中，并提高基础模型采样查找。图6仅两个题的生成轨迹困惑度，附录D.4再扩到十题，支持经验解释，不能证明所有新轨迹不可能。图8的采样效率差距把base pass@256当参照代理，非已证最优上界；六算法近似并列亦有训练样本成本差异。

第5节精确定位与已有观察的增量，第6节和附录C把探索困难、先验及多轮环境互动作为解释与未来研究。可迁移“承认现有效果—定义不同研究对象—跨设置重现—互补诊断—干预替代解释—保留范围”。适用于质疑机制解释的实证研究；全文的强“bounded/all”措辞不应照搬成理论断言，当前单轮RLVR结果也不能外推所有算法、规模、算力和未来交互范式。
