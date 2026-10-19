# NEURIPS27 · Inductive Representation Learning on Large Graphs

- William L. Hamilton、Rex Ying、Jure Leskovec；NIPS 2017。持续沿用依据：[PyG官方SAGEConv接口](https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.nn.conv.SAGEConv.html)。
- 来源：[正式记录](https://papers.nips.cc/paper_files/paper/2017/hash/5dd9db5e033da9c6fb5ba83c7a7ebea9-Abstract.html)。读取正式PDF第1–11页全部主文、算法1、图1–2及表1，检视第2、7页；另读官方supplement full_paper/paper-graphsage.pdf第12–19页附录A–E的叙述、协议与证明组织。未逐式证明审计或复现。

摘要直接区分为每个节点存向量与学习生成向量的函数。引言先说明节点表示用途，再将变化图/跨图新节点变成目标，随后解释局部结构与特征的角色。第2节按因子分解、监督图学习和GCN比较，明确既有方法不适配的接口，而非宣称图神经网络首次出现。

第3节先写已训练模型如何生成embedding，再写参数训练和三类聚合器。算法1与图1给递归信息流，附录A反向展开所需采样节点、正向聚合，避免把S1/S2视为相同跳数；有放回抽样用于度数不足。mean/pool对称，随机顺序LSTM并不严格排列不变；不能把理想要求悄悄归给所有变体。

第4节用时间切分的citation/Reddit与全新PPI图分别检验两种归纳能力。表1区分监督/无监督，不能跨列比较而隐去标签。图2A分训练batch与全test推断，DeepWalk需对新节点额外SGD；附录C还说明不同硬件、边下采样和基线实现。图2B展示邻居数增加的性能/耗时取舍。六个数据集×训练方式设置的符号秩分析相关且样本小，不能视作六个独立大规模复现。

第5节聚类系数定理是分离节点特征、足够维度与4层的存在性；实际常用2层。附录E明确叫可识别性论证，维度最坏随节点数增长，且单图定理带transductive性质；不能据此声称SGD能高效学到或任意跨图泛化。结尾回到新节点与采样，提出非均匀采样扩展。

可迁移“泛化对象改变—推断接口—训练与模块选择—对应切分—表达力边界”。适用于归纳图学习；特征模式不同、邻接不可取得或分布变化时，需重新验证，不能把“新节点”一词代替真正隔离的评估设计。
