# ICML-C02 — High-Accuracy Sampling（近期校准）

Fan Chen, Sinho Chewi, Constantinos Daskalakis and Alexander Rakhlin (ICML 2026). [正式会议全文](https://proceedings.mlr.press/v306/chen26p.html)，PDF 35 页。2026-10-19 逐页阅读主文、算法、定理与证明叙述、附录 A–F，另核第 4、8 页版面。阅读不等同独立验证每步证明；未实现算法。官方 Outstanding Paper 仅作近期校准依据。

## 摘要与引言

摘要同时报告精度、维度和 score 误差依赖。第 1–2 页用“仅有梯度而无密度值时能否高精度采样”提出明确问题，逐层比较以往 oracle、数据假设和精度阶，贡献分成扩散与 log-concave 两个应用，未用空泛影响填充。

## 构造与理论顺序

第 2 节统一反向核与误差，第 3 节先在一维例子中由积分和 Poisson 随机化构造 FORS，再推广 Gaussian tilt（第 3–5 页）。第 4 节按最少假设、较好维度依赖、内在维度逐层实例化，分别注明加强假设和误差代价（第 6–7 页）；第 5 节复用同子程序到 proximal sampler。

## 证据、附录与结尾

无性能实验图表；算法、定理、oracle 查询量和证明是证据。附录 A 精确比较同期工作，B 集中工具，C–E 展开主构造与误差，F 给应用（第 12–35 页）。结尾第 8 页将理论改进与尚未证明的实际速度收益区分，列多次 score 调用、保守步长和 ODE 扩展问题。

## 可迁移规则和反例

共用技术支撑多结果时，先讲最小随机构造，再给抽象子程序和按假设排序的推论；附录按依赖分层。反例：一步少不表示总 score 查询更少，渐近高精度保证不等于现成可竞争的图像采样器；KL/TV 与 bounded Lipschitz、early stopping 与原数据误差不可互换。出版版注明另有改进预印本，引用须固定版本。
