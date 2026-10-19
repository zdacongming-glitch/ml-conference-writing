# ICML35 — Minimax Regret in RL

Mohammad Gheshlaghi Azar, Ian Osband and Rémi Munos (ICML 2017). [正式会议全文](https://proceedings.mlr.press/v70/azar17a.html)，PDF 10 页。2026-10-19 阅读全部主文、四份算法、定理及证明路线与参考文献，另核第 3–4 页版面。未作独立证明审计。

## 摘要与引言

摘要给有限时域 MDP、完整 regret 形式和两项分析关键，说明何种大样本条件下匹配下界。引言第 1–2 页从探索困境推进到 S/H 依赖，明确问题设置不同于 weakly communicating 系统；限制集中放在结果意义附近。

## 算法与结果层次

第 2 节统一环境、已知有界 reward、episode 与总时间。第 3 节用共同 UCBVI 骨架承载 CH/BF 两类 bonus；简单变体先展示状态维改进，经验方差变体再解释时域改进（第 3–4 页）。第 4 节按同一顺序列完整定理和渐近解释。

## 证据与结尾

没有实验图表，主要证据为可实现算法、非渐近界和第 5 节的分步证明。证明先指出数据依赖导致直接 concentration 无效，再分 correction、martingale、bonus 和 estimation；BF 部分复用共同步骤，仅讲改变（第 5–8 页）。结尾归纳两次依赖改进，并明确小 T 和低阶项仍可改进。

## 可迁移规则和反例

理论算法有两个创新时，让简单/精细两版本分别承载，定理、解释与证明顺序一致。反例：标题中的 minimax 不能删掉足够大 T、已知时域及有限状态等范围；不同总步数/episode 约定的界先换算再比较。证明路线够清楚时无需为装饰性完整而硬加实验节。
