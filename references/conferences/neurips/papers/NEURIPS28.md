# NEURIPS28 · Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles

- Balaji Lakshminarayanan、Alexander Pritzel、Charles Blundell；NIPS 2017。
- 来源：[正式记录](https://papers.nips.cc/paper_files/paper/2017/hash/9ef2ed4b7fd2c810847ffa5fa85bce38-Abstract.html)。读取正式PDF第1–9页全部主文、算法1、图1–6及表1；检视第6–9页图。另读官方补充第1–2页A及B.1，查看校准图7和架构图8–9；B.2样图库只读文字与图注，未全检。未复现。

摘要提出近似贝叶斯之外的易用基线，引言先说明过度自信后明确评价对象：准确率、校准和域外反应不同。第2页将已知集成与对抗训练重新定位为不确定性估计配方，承认组件已存在；其历史首创措辞不能不经复核当作今天的全景判断。

第2节按概率输出、proper scoring rule、局部平滑、集成顺序展开。回归每个网络同时预测均值和方差，最终是均匀Gaussian混合，再为计算便利作矩匹配Gaussian近似；不能等同“几个点预测的样本方差”。独立初始化与数据打乱负责随机性，所有网络可用完整训练数据；原文报告bootstrap反而退化。算法1明确对抗训练可选。

第3节从toy方差图、实际回归、分类、未知类到置信阈值决策递进。表1并排RMSE/NLL并保留部分RMSE更差，补充A与校准图7解释为何学方差优于只看网络间差异。图2随网络数变化并显示对抗训练对SVHN大集成收益消失；相同M下MC-dropout样本与独立网络并不表示同等训练/内存成本。图3与图5的未知类熵是特定shift检验，图6阈值曲线不自动给任意新分布上的错误率保证。

第4节承认M倍参数与蒸馏机会，并把集成和对抗训练各自效果分开。[NeurIPS2019一手评估](https://papers.nips.cc/paper/9547-can-you-trust-your-models-uncertainty-evaluating-predictive-uncertainty-under-dataset-shift.pdf)继续将其作为shift基线，支持沿用依据，不新增本库计数。可迁移“先定义质量，再给简配方与分量消融，最后测决策后果”；适用于可靠性方法。有限shift成功不能写成OOD安全保证，低NLL也不能单独替代所有校准和辨识度诊断。
