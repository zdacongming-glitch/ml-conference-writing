# ICML09 — Rectified Linear Units Improve RBMs

Vinod Nair and Geoffrey E. Hinton (ICML 2010). [正式会议全文](https://icml.cc/Conferences/2010/papers/432.pdf)，PDF 8 页。2026-10-19 连续阅读全文、图表图注，另核第 5–6 页图像；无独立附录。未复现实验。

## 摘要与引言

摘要从共享权重的无限二值副本到 stepped sigmoid，再到 noisy ReLU 近似和两项任务，解释了新单元从何而来。第 1 节仅回顾构造需要的 RBM 学习及 Gaussian visible units，服务随后替换。

## 方法、性质与验证顺序

第 2 节定义近似，第 3 节严格区分 intensity equivariance 和经 cosine 获得的 invariance；第 4–6 节才给 NORB 与 LFW 设置及比较（第 2–7 页）。第 7 节补充指数多个线性区域的解释，最后摘要式结尾串回单元构造、判别与表示性质。

## 图表证据

图 1 对照近似曲线；滤波器图和激活直方图说明学到什么；表 1–2（第 5 页）将预训练与单元类型分开。第 7 页表 3 的 LFW 方差较大，正文拒绝作坚决胜负判断，并说明五折合并、裁背景及其他方法额外标签等比较差别。

## 可迁移规则与边界

组件稿可用“原对象—构造—可计算近似—相关性质—隔离比较”组织。条件：近似有明确来源。反例：本文 NReLU 的随机训练与判别时确定性 ReLU 不能混写；正齐次性要求零 bias 与无噪声（第 3、6 页），不对任意带偏置网络成立。图像滤波器只作诊断，不夸成语义理解证明。
