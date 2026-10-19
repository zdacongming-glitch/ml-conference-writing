# NEURIPS15 · ImageNet Classification with Deep Convolutional Neural Networks

- Alex Krizhevsky、Ilya Sutskever、Geoffrey E. Hinton；NIPS 2012；[2022官方 Test of Time 认可](https://blog.neurips.cc/2022/11/21/announcing-the-neurips-2022-awards/)。
- 来源：[正式记录](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html)。读取正式 PDF 9 页全部叙述、图 1–4、表 1–2及图注；检视第 3、5、6、8 页所有图。更多补充检索示例未计已读，未复现实验。

摘要用任务规模、top-1/top-5 结果、网络与训练要素定位成果，并另报 2012 比赛的模型组合成绩。引言从数据规模、容量和图像先验三个必要条件讲到 GPU 可行性，再限定具体训练与实现成果；不能将成熟 CNN、ReLU 或 dropout 的全部起源归给本篇。

第 2 节先交代两届比赛标签可见性与预处理，第 3 节按作者认为的重要性讲 ReLU、多GPU、归一化和池化，再在 3.5 总结架构。此处总体架构后置仍可工作，反驳所有稿件都必须先图后组件的硬规则。第 4 节单列过拟合与增强、dropout，第 5 节给训练配置，随后才集中结果。

图 1 是 CIFAR-10 上到达训练误差的迭代比较，不能当 ImageNet 同倍实际耗时；图 2 解释两GPU连接，图 3 展示第一层核，图 4 是预测和特征检索诊断。表 1为2010，表 2区分2012的单网、五网与七网，并标额外大数据预训练；15.3%不能归给无额外预训练的单网。训练随机裁剪与测试十裁剪也不能省略。

讨论把深度移除后的变化与可能延伸分开，视频与无监督预训练是未来设想。可迁移的是把系统成绩接到规模、结构、优化及泛化控制的具体条件，并让表格标出额外数据与集成。历史验证/测试互用的措辞及对不同划分影响不大的判断不可照搬为现代评估规范；核图或近邻样例也不证明唯一表征机制。
