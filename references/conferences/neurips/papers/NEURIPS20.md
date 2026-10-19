# NEURIPS20 · Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks

- Shaoqing Ren、Kaiming He、Ross Girshick、Jian Sun；NIPS 2015；[2025官方 Test of Time认可](https://blog.neurips.cc/2025/11/26/announcing-the-test-of-time-paper-award-for-neurips-2025/)。
- 来源：[正式记录](https://papers.nips.cc/paper_files/paper/2015/hash/14bfa6bb14875e45bba028a21ed38046-Abstract.html)。读取正式PDF第1–9页全部叙述、损失及四步训练说明、表1–5、图1–2和图注；检视第3、8页图。未以较长后续版本替换本次阅读。

摘要同时交代瓶颈、共享特征的RPN、训练方式、完整速度与检测精度。引言前两段把Fast R-CNN的已有加速作为新瓶颈出现的原因，第三段直接承认CPU提议与GPU检测的比较并不对称，再解释共享计算为何超出简单GPU重实现。这样的限定使速度论证可核查。

第2节比较定位与共享计算两条相关线索；第3节按滑动网络、anchor、标签与损失、优化、共享训练、实现顺序展开。图1左侧用两个输出头解释位置与objectness，右侧是可处理尺度的例证。此版本采用四步交替训练；第4–5页明确把同时改变提议的联合优化留待以后，不能将“RPN可端到端训练”改写成整系统当时已一次联合训练。

第4节优先最终mAP而非提议召回代理。表1先给完整系统再在固定检测器下拆除分类、回归及NMS；须保留训练/测试提议不一致这个消融条件。表2–3区分数据组合与共享状态，73.2用07+12训练；表4分列卷积、提议、region-wise与总耗时，并标注SS在CPU，10ms是共享后的额外提议时间。图2诊断不同提议数量下的召回；第7页明确该代理与最终检测精度只松散相关。表5是特定实现下的单/两阶段对照，不能推出所有未来单阶段方法都差。

结尾只回扣共享、提议质量与5–17fps，不引入新的泛化定理。可迁移“已有加速暴露瓶颈—可共享机制—训练闭环—真实终点与分项成本”。适用于流水线改造；若硬件、训练集或backbone不同，不能只取最高mAP和最快fps拼成一个配置。
