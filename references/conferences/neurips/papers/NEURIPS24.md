# NEURIPS24 · Attention Is All You Need

- Ashish Vaswani、Noam Shazeer、Niki Parmar、Jakob Uszkoreit、Llion Jones、Aidan N. Gomez、Łukasz Kaiser、Illia Polosukhin；NIPS 2017。沿用依据：[PyTorch官方Transformer参考实现](https://docs.pytorch.org/docs/stable/generated/torch.nn.Transformer.html)。
- 来源：[正式记录](https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)。读取该正式PDF全部11页叙述、图1–2、表1–3及图注；检视第3、4页图。此版本未附正文所指注意力可视化附录，也未含后来版本的解析实验；不借记忆补读这些内容。

摘要同时给架构替换、质量、并行性和训练代价。引言第1–2页从RNN既有成果转到样本内顺序依赖；第2节区分卷积的路径长度与自注意力已有应用，增量限定为不用序列对齐RNN或卷积的transduction架构。第3节先保留编码器—自回归解码器总接口，再解释stack、缩放点积、多头及三处注意力应用，避免把标题理解成整个网络只有一个注意力操作。

图1给数据流和mask位置，图2展开缩放与并行head。第3.3–3.5节补前馈、embedding与位置，位置编码的长度外推是动机而非已证明收益；表3中学习位置编码结果近似相同。第4节把复杂度、顺序操作数、最长路径分开，且指出序列长度小于表示维度时的计算比较条件。训练并行与推断仍逐token生成必须分清。

第5节单列数据、硬件、优化和正则化。表2区分base/big、语言任务及单模型/ensemble；训练FLOPs按时长、GPU数和估计吞吐计算，非统一硬件实测算子计数。第6.1节报告checkpoint平均及beam/长度惩罚，第6.2节消融则不用checkpoint平均，不能直接把表3的dev数和最终test数相减。label smoothing降低困惑度表现却提升BLEU，说明代理指标可能反向变化。

结尾回扣翻译和速度，把局部注意力、其他模态、减少生成顺序性列为未来问题。可迁移“关键计算约束—结构性替代—接口与部件—复杂度分量—实际预算和消融”。适用于架构替换；长序列下二次注意力成本、原版post-norm、编码器—解码器配置均不能悄悄替换为后续LLM架构并归于原文。
