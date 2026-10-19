# NEURIPS34 · FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

- Tri Dao、Daniel Y. Fu、Stefano Ermon、Atri Rudra、Christopher Ré；NeurIPS 2022；[作者维护实现及后续FlashAttention-2/3](https://github.com/Dao-AILab/flash-attention)提供持续沿用线索，后续版本性能不归给原文。
- 来源：[正式记录](https://papers.nips.cc/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html)。读正式PDF第1–10页全部主文与影响说明，第16页checklist；检视第2、6、9页全部主图。官方补充第17–31页A–D与E.1–E.9的实验说明已读；第32页起密集计时表未逐格审计，补充曲线主要读取图注，未宣称复现实验。

摘要先给精确注意力的IO问题，再给分块、重计算及端到端结果。引言依长序列需求、FLOPs与真实速度脱节、硬件层级、已有IO技术转用推进；明确tiling和recomputation并非新发明。图1（第2页）同时解释内存层级、块循环和内核计时，7.6倍是该注意力内核的比较，不能写成全模型训练收益。

第2节先定义硬件与计算瓶颈，第3节才讲在线softmax和不物化注意力矩阵的算法。定理1保持二次FLOPs、降低额外内存；定理2的IO计数带SRAM范围条件。命题3（第6页）的下界是无法对所有SRAM大小同时渐近改进，不是每个固定内存规模均已证最优。图2把FLOPs、HBM读写、时间并列，显示多算仍可更快，也显示块变大后时间不再随IO下降。块稀疏变体另属近似，不能把其线性/稀疏收益贴到精确算法。

第4节先模型训练再内核测试。表1/补充E.1固定初始点、目标验证精度与8张A100，10次训练平均；表2的HuggingFace与Megatron基线优化程度不同。补充图4用重合验证曲线核查同配置计算等价；更长上下文改善质量是另一实验干预。Path-X/256还包含Path-64预训练和位置嵌入上采样。图3（第9页）展示精确计算时间仍二次增长，近似方法在长序列可越过其速度，不支持“所有长度最快”。

第5节直接以局限和未来方向收尾，没有单列Conclusion；CUDA工程、硬件迁移与多GPU约束都具体。补充E.6承认短序列128时较Apex FMHA略慢；E.9注明随机QKV、100次计时、不同精度与外部实现限制。可迁移写法是“瓶颈量—算法不变量—资源分析—内核诊断—端到端收益”，适用于系统算法；每个速度数字须带硬件、基线、序列、精度与计量层级。不能以FLOPs减少替代运行时间，也不能据一代GPU推通用最优。
