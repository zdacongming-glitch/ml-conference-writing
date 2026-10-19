# NEURIPS30 · Are GANs Created Equal? A Large-Scale Study

- Mario Lucic、Karol Kurach、Marcin Michalski、Olivier Bousquet、Sylvain Gelly；NeurIPS 2018。
- 来源：[正式记录](https://papers.nips.cc/paper_files/paper/2018/hash/e46de7e1bcaaced9a54f1e9d0d2f800d-Abstract.html)。读取正式PDF第1–10页全部主文、图1–5、表1–2及图注；检视第4–8页。另读官方补充PDF第11页A搜索范围及B说明，其他大量scatter与样图库未全读；未重跑研究。

摘要给“充分搜索后许多模型可达相似分数”的条件结果，没有证明所有GAN等价。引言用选择算法与识别实际增量两种用途说明比较为何重要，再定位概率不可算和指标缺陷。第2节先解释指标，第3节把受比较的损失和约束并排，第4节承认公平比较没有单一答案，列出架构、参数、种子、数据和预算五个可变维度；这比先给排行榜更适合经验研究。

第5节先校验FID自身的偏差、方差、mode dropping与编码，再构造有可算流形距离的多边形任务。图1支持的是所检验编码和数据范围；图2用四种精确/覆盖组合解释指标，距离靠非凸优化近似而非无误oracle。第6节统一大部分架构但保留BEGAN例外，附录A公开wide/narrow分布，narrow由Fashion-MNIST搜索选择。

图3画给定搜索预算下最佳FID的重采样分布，5000 bootstrap来自100次运行，不是5000独立训练；图4呈现搜索分布而非只挑最好。表2对选中配置50次新初始化统计且排除失败离群点，星号标出模式坍缩，故均值不能脱离失败率引用。原协议还每5epoch用test FID选点；这是应被现代验证集选择流程替换的历史做法。图5用95%均值置信区间，而图3是一标准差，两种误差棒不可互换。

第7–8节明确架构分辨率、优化与指标的范围，承认未探索条件下仍可能有模型胜出。[ICML2019后续研究](https://proceedings.mlr.press/v97/kurach19a/kurach19a.pdf)直接沿用代码并扩展正则化与架构，支持影响依据。可迁移“比较对象—可选公平标准—指标自检—预算分布—失效范围”；适用于benchmark和复核研究。未发现统治者不是统计等价，足够调参的结果不能取代同预算部署选择。
