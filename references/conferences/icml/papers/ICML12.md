# ICML12 — Learning Fair Representations

Richard Zemel, Yu Wu, Kevin Swersky, Toniann Pitassi and Cynthia Dwork (ICML 2013). [正式会议全文](https://proceedings.mlr.press/v28/zemel13.html)，PDF 9 页。2026-10-19 连续读全部正文与图表图注，另核第 7 页图像。未复现实验。另读官方独立补充材料全部 2 页（数据与模型选择、完整定量表），未作逐式证明审计。

## 摘要与引言

摘要先定义目标公平概念，再给保留信息与隐藏敏感组别的表示目标。引言第 1–2 页说明删除敏感属性仍有相关代理，区分 statistical parity 与 individual fairness，再定位给定距离和无法样本外推广的问题。

## 方法与论证顺序

第 2 节先给原型概率映射，再按 parity、重建、预测列损失；第 2.3 节解释两方组合系统和为何在表示上约束（第 2–4 页）。相关工作随后按改标签、正则化、fairness through awareness 连接目标差异。

## 图表、诊断与结尾

第 4 节先定义 accuracy、discrimination、局部 consistency 和验证选参，第 7 页图 1 同时展示两种选参准则，图 2测一致性，图 3测试敏感属性可预测性；第 8 页另检验迁移。结尾把 parity 目标局限和更丰富表示作为具体开放问题。

## 可迁移规则与反例

价值目标或多目标稿件须先固定操作定义，再用不同诊断分别评估，不把一个分数写成整个目标。条件：规范概念与测量可以对应。反例：局部 consistency 代理不是一般 individual fairness 保证，特定线性预测器难预测敏感属性不证明任意攻击者都无信息；不将 statistical parity 泛称唯一公平标准。正文应保留这种必要区别而删去空泛社会重要性重复。
