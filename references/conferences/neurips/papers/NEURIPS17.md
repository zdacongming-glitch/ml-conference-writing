# NEURIPS17 · Distributed Representations of Words and Phrases and their Compositionality

- Tomas Mikolov、Ilya Sutskever、Kai Chen、Greg Corrado、Jeffrey Dean；NIPS 2013；[2023官方 Test of Time认可](https://blog.neurips.cc/2023/12/11/announcing-the-neurips-2023-paper-awards/)。
- 来源：[正式记录](https://papers.nips.cc/paper_files/paper/2013/hash/9aa42b31882ec039965f3c4923ce901b-Abstract.html)。读取正式 PDF 9 页全部叙述、图1–2、表1–6及图注；检视第2、4页模型图与PCA投影。未复现。早期 Efficient Estimation of Word Representations 一文是 ICLR Workshop，不与本篇正式会议身份混淆。

摘要明确是对既有 Skip-gram 的训练和表征扩展，再用不具简单组合语义的短语解释第二个问题。引言先承认词向量历史和先前 Skip-gram，再用具体类比说明要评价的线性关系；后续段落分别引出 subsampling、negative sampling、短语 token 与加法现象。

第2节先定义附近词预测目标、层次 softmax，再给 NEG 和频词下采样，明确 NEG 只借鉴 NCE 并不保留相同似然性质。第3节先检验训练方法，第4节另定义短语提取和短语评估，第5节解释加法现象，第6节比较公开词向量。方法选择、语料扩大和短语构造没有被假定为同一变化。

图1说明预测方向，图2是国家首都关系的PCA例示；表1并报耗时和两类类比，表3保留 subsampling 后层次softmax优于NEG的短语结果，表4–6是近邻和加法示例。72%短语类比来自约330亿词、1000维与整句窗口，不是表3十亿词300维配置。公开基线语料和维度不同，表6不能孤立证明某训练目标唯一造成改善。

结尾直接说明最优训练算法和超参数依任务而异。可借鉴“既有构造的明确增量—分别回应子问题—保留任务交互”的写法。类比与少数近邻不构成完整语言理解保证；加法的解释也不能普遍等同形式组合语义，历史训练时间不应转写为现代框架速度。
