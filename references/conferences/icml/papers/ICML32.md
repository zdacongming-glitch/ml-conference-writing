# ICML32 — Trust Region Policy Optimization

John Schulman, Sergey Levine, Philipp Moritz, Michael Jordan and Pieter Abbeel (ICML 2015). [正式会议全文](https://proceedings.mlr.press/v37/schulman15.html)，PDF 9 页。2026-10-19 阅读全部主文、算法、图表图注及参考文献，另核第 4、7 页图像。未做证明审计或复现。另读官方独立补充材料第 4, 5, 6, 7 页（CG、line search、参数化和实验配置）；其余页不计为已读，未作逐式证明审计。

## 摘要与引言

摘要直接区分有单调改进保证的方案与多次近似后的实用 TRPO。引言第 1 页以 policy iteration、policy gradient、无导数方法的实际差距界定动机，再预告两种采样实例，避免把“理论驱动”泛化为全部实现都有定理。

## 理论到近似链

第 2–3 节由性能差分恒等式、旧策略访问分布的局部 surrogate，到总变差/KL 界及理想算法（第 2–3 页）。第 4–6 节依次替换 penalty 为约束、最大 KL 为平均 KL、精确期望为样本及数值近似；第 5–6 页集中回顾近似和代价。single-path/vine 的可重置假设用图 1 解释。

## 证据与结尾

第 8 节先列三实验问题，再用消融、控制和视觉游戏回答。图 4 的站立参考分数防止误认学会前进。表 1（第 8 页）坦承 Atari 每任务仅一次运行，不能据它宣称统计稳定。讨论返回理论支撑与经验跨度，并提出更贵采样下的下一步。

## 可迁移规则和反例

理论启发算法适合显式列出“从保证到实现”的每次替换，集中解释一次而非全文反复设防。反例：平均 KL 约束不承继最大 KL 版本的原保证；simulator 可重置的 vine 不能作为任意真实机器人都可运行的协议。广泛任务演示与单次运行的不确定性须分别陈述。
