# NEURIPS11 · Online Learning for Latent Dirichlet Allocation

- Matthew D. Hoffman、David M. Blei、Francis Bach；NIPS 2010；[2021 官方 Test of Time Award](https://blog.neurips.cc/2021/11/30/announcing-the-neurips-2021-award-recipients/)。
- 来源：[正式记录](https://papers.nips.cc/paper_files/paper/2010/hash/71f6278d140af599e06ad9bf1ba03cb0-Abstract.html)。读取正式 PDF 9 页全部主文叙述、算法 1–2、自然梯度分析、图 1–2、表 1和图注；检视第 2、7 页。未读另附 supplement 的全部技术证明，未复现。

摘要前置在线 VB、自然梯度解释、变分目标上的局部保证及 330 万文档单遍实例。引言从层次模型的用途缩到后验不可算、近似推断的两类方法及 batch VB 每次全遍的瓶颈，再解释为什么流式算法对应真实需求；图 1 提前展示文档量、held-out 指标及主题演化。

第 2 节先恢复 LDA 与 batch VB 的必要定义，把全局与每文档变分参数分开；再以重复一篇文档形成临时全语料的直觉导出加权更新。mini-batch 和超参数调整紧随算法，2.3 才说明无显式求梯度的更新等于随机自然梯度。结论对象是所定义 ELBO 的驻点，不是精确后验或全局最优。

第 4 节区分参数选择、固定语料的时间比较和持续新文档的真正在线实例。表 1 给 batch 大小与学习参数组合，图 2 用 CPU 时间比较 held-out 指标；图 1 的横轴则是已处理文档，不能互换为相同耗时。理论要求衰减指数大于 0.5，实际实验包括 0.5，改写时须保留分析与实现范围差异。原文承认 perplexity 不等于主题可解释性，并交代下载和预处理成本。

结尾由 LDA 算法提炼向其他层次模型推广的思路，而非宣称每个模型都已验证。可迁移“已知 batch 方法—计算瓶颈—局部到全局更新—解释—两种现实场景”的顺序；适合可扩展推断稿。自然梯度解释与实测提速需要分别支持，不能只凭少数代码行宣称资源开销可忽略。
