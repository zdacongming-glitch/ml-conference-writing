# NEURIPS18 · Generative Adversarial Nets

- Ian J. Goodfellow、Jean Pouget-Abadie、Mehdi Mirza、Bing Xu、David Warde-Farley、Sherjil Ozair、Aaron Courville、Yoshua Bengio；NIPS 2014；[2024官方 Test of Time认可](https://blog.neurips.cc/2024/11/27/announcing-the-neurips-2024-test-of-time-paper-awards/)。
- 来源：[正式记录](https://papers.nips.cc/paper_files/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html)。读取正式 PDF 9 页全部叙述、算法1、理想理论及解释、图1–3、表1–2和图注；检视第4、7页全部图。未逐式审计或复现。

摘要把生成与判别两模型的角色、minimax关系、无限容量情形与实际MLP训练分开。引言先从生成学习的概率计算困难提出需求，再用竞争直觉降低理解门槛；紧接着将本文实现限定为可微网络。第2节按概率表示、采样与训练所需计算比较相关工作；其中历史归属和关于其他模型的概括不能未经复核当作今天的通则。

第3节把直觉落实到噪声映射、判别概率及minimax目标，然后解释实际有限步交替更新与避免梯度饱和的另一生成损失。第4节先求固定生成器的最优判别器，再说明理想分布空间的目标与分布匹配；第5页末尾明确有限参数网络优化不受这些证明直接保证。相同均衡点不能自动说成两个实际损失全程等价。

图1是分布与映射的教学示意，表1是Parzen拟合密度的测试估计；正文坦承高维和方差问题。图2说明随机样本与最近训练例、图3展示潜坐标插值，但这些有限检查不是普遍无记忆证明。第6节明确同步训练和模式坍缩困难，表2按训练、推断、采样与密度评价分列代价；第7节把条件生成等留为扩展。

可迁移“直觉—操作定义—理想结果—实际差异—可行性证据及代价”。适用于新的学习框架；理想最优判别器与足够容量不可删，Parzen结果和样本图不能替代现代分布质量评价，也不能把后来GAN变体的能力归给原文。
