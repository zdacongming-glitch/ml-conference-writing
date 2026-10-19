# 前后改写示例

以下英文和数值均为**本技能原创的假想示例**，不摘抄经典论文，也不代表任何真实研究结果。只能在作者材料确实提供相同事实时使用相应表达，不能把示例数据带入稿件。

## 1. 将空泛动机改成具体困难

**给定事实**：研究表征学习；编码器在训练阶段更新、在线性评估阶段冻结；现有目标直接约束编码器表示，方法将一致性目标放在独立投影空间。尚无实验数字。

**原句**

> Representation learning has attracted tremendous attention. Existing methods have many limitations. We propose a novel and powerful framework to address these challenges.

**改写**

> An invariance objective can suppress information that remains useful for downstream prediction. We separate the representation used for prediction from the space in which invariance is enforced. The proposed objective acts on a learned projection while retaining the encoder representation for downstream tasks.

**修改理由**：具体说明矛盾和设计动作。此处没有结果，因此不加“更好”“最先进”或捏造提升；如果作者尚未支持第一句的机制判断，应写成待研究的风险或假设，而不是确定成因。

## 2. 把贡献列表改成有证据的摘要

**给定事实**：方法和基线使用相同编码器架构及初始化；训练时编码器参与更新，方法额外联合训练独立投影头；与身份投影的基线使用相同数据和更新次数；线性评估时分别冻结训练后的编码器，A、B、C 三个数据集分别增加 1.2、1.6、0.4 个准确率百分点；没有测试端到端微调，没有机制证明。

**原摘要**

> We propose a novel representation learning framework with a new projection module. Extensive experiments demonstrate superior generalization and validate the effectiveness of every component. Our method establishes a new state of the art.

**改写**

> We study whether separating the training-objective space from the encoder representation improves linear-evaluation accuracy. Our approach jointly trains the encoder and a projection head, then freezes the encoder and evaluates its representation before projection. With the same encoder architecture, initialization, training data, and number of updates, it improves accuracy over the identity-projection baseline by 1.2, 1.6, and 0.4 percentage points on datasets A, B, and C, respectively.

**修改理由**：贡献落到具体设置、操作和结果，不把三项比较称为机制验证或 SOTA。作用范围已经由 linear evaluation 和具体数据集限定，摘要不再追加“其他评估尚未做”的通用尾句；需要讨论的推广范围在对应位置说明。

## 3. 保住理论结论的量词与适用范围

**给定事实**：在有界凸域、有界梯度及指定学习率下，已证明在线算法的遗憾 $R_T\le C\sqrt{T}$；没有非凸结论。

**原句**

> We prove that the optimizer always converges to the global optimum, guaranteeing reliable training of deep neural networks.

**改写**

> For online convex optimization over a bounded domain, we establish an $O(\sqrt{T})$ regret bound under bounded gradients and the prescribed learning-rate schedule. The average regret therefore vanishes as $T$ grows. This result does not establish global convergence for nonconvex neural-network training.

**修改理由**：遗憾界、平均遗憾与非凸参数优化是不同结论。正式定理仍保留常数依赖和完整条件，不因摘要或解释段使用大 O 就删掉它们。

**另一种量词错误**

> Adam fails to converge.

若实际证据只是存在反例，应改成：

> We construct an online convex optimization problem on which Adam has nonvanishing average regret under the specified parameter settings.

不能从一句孤立原文猜出具体反例；只有作者材料确实提供时才这样写。

## 4. 消融下降不自动确定机制

**给定事实**：删模块后准确率从 80% 降到 78%，同时参数量降低 25%；无容量匹配的对照。

**原句**

> The ablation proves that the proposed attention mechanism is the cause of the improvement.

**改写**

> Removing the module reduces accuracy from 80% to 78% in this experiment. This comparison also reduces the parameter count by 25%, so it does not isolate the effect of the proposed attention mechanism from that of model capacity.

**修改理由**：报告实际观察，同时指出尚未分离的因素。可建议合适的容量匹配对照；不能直接补写该实验已经支持机制。

## 5. 区分训练步数、耗时与加速比

**给定事实 A**：达到同一准确率所需更新从 12,000 次减少到 6,000 次，未测耗时。

**原句**

> Our method trains twice as fast.

**改写**

> Our method reaches the target accuracy in 6,000 updates, compared with 12,000 for the baseline.

**给定事实 B**：另一个已测比较在相同硬件与评价条件下，基线用时 3 小时，新方法用时 2 小时。

**可以补写**

> Under the same hardware and evaluation conditions, runtime decreases from 3 to 2 hours, corresponding to a 1.5-fold speedup.

A 不能推出 B。若用耗时减少来表达，B 是约 33.3%，不是 50%。不要从相同硬件进一步推断 batch、精度或软件实现也相同，除非材料已给出。

## 6. 不把点估计写成显著性

**给定事实**：表中准确率为 82% 与 80%；没有独立运行数或不确定性说明。

**原句**

> Our method significantly outperforms the baseline by 2%.

**改写**

> In the reported experiment, our method achieves 82% accuracy, compared with 80% for the baseline, a difference of 2 percentage points.

**正文外提示作者**：确认运行数、汇总方式和不确定性；现有信息不足以判断统计显著性。不能自行把差值解释为均值差、置信区间或相对误差下降。

若材料确实提供“五次独立运行的均值与样本标准差”，再明确写 mean ± standard deviation over five independent runs；不要给所有论文默认加这句话。

## 7. 让负结果保持价值与范围

**给定事实**：在三个基准、已报告的调参范围和固定预算下，新组件没有稳定提高性能；没有不可能性证明。

**原句**

> Our experiments show that this entire class of methods is ineffective.

**改写**

> Across the three evaluated benchmarks, adding the component does not yield a consistent improvement within the tested hyperparameter range and training budget.

**修改理由**：测试范围已在这句中明确，无需再附“其他架构和预算仍未知”。是否需要另行讨论由论文的具体主张决定；不能因结论为负就淡化已有发现，也不把有限测试升级为不可能性。

## 8. 把回复写成可核查的直接回答

**审稿意见**：无法判断表中差异是否来自额外预训练数据。

**给定事实**：所有方法使用相同预训练 checkpoint，后续均不使用额外预训练数据；原文表注确实遗漏了这些信息；用户只请求起草回复，尚未修改或上传论文。

**原回复**

> The reviewer misunderstood our method. We have fixed all issues in the revised manuscript and conducted comprehensive new experiments.

**改写**

> All methods in Table 2 use the same pretrained checkpoint and receive no additional pretraining data. We agree that the original caption did not make this clear. We will specify the shared checkpoint and data usage in the caption when a manuscript revision is permitted.

**修改理由**：直接回答混杂疑问；只承诺真实可做的修改。不声称已改文件或做了新实验。若实际已修改且当年规则允许，再写完成时并给准确位置。

## 9. 格式与 AI 声明缺信息时怎样继续

**请求**：“帮我把这段英文润色成 ICLR 风格，顺便写一句没有使用 AI。”

**处理**：完成这段英文润色；没有研究全流程的信息，不能替作者写“没有使用 AI”。说明本次确实用了 AI 辅助编辑，并确认作者所指的投稿年份和需要声明的实际活动。

对 ICLR 2027，应按其专门 AI 政策区分各活动并填写所需声明；不能拿 NeurIPS 2026 对普通写作辅助的规则代替。对已完成的人工核查也只能报告事实，不能模板化承诺。

**请求**：“我投 ICML，把正文写到 9 页。”

**处理**：先从上下文确定年份和阶段。按本档案的 ICML 2026 规则，9 页对应终稿，初投正文上限是 8 页。可以继续压缩重复文字、改进结构，但在信息不足时不能宣称 9 页初稿合规。

这些场景展示如何处理事实与规则的边界，不要求普通段落润色都附上一份投稿检查报告。

## 10. 设置已清楚时删去重复解释

**上下文**：实验设置已说明线性评估会冻结编码器，表1列出三个数据集；使用投影头后，三个准确率分别提高1.2、1.6和0.4个百分点。

**原段**

> The projection head improves linear-evaluation accuracy on all three datasets in Table 1. It is important to note that the encoder is frozen during this evaluation. These results should therefore be interpreted in the context of linear evaluation, rather than as evidence about other evaluation protocols.

**独立无损删改后**

> The projection head improves linear-evaluation accuracy on all three datasets (Table 1).

**修改理由**：后两句重复已定义的设置，未纠正新的误解。删去后保留实际比较和适用协议；正文没有被升级为端到端微调结论。

## 11. 单个设计动作直接表达

**给定事实**：投影头仅在训练时使用，下游评估使用投影前的编码器表示；此句没有承担与某个具体前作比较的任务。

**原句**

> The projection head is not a component used at evaluation time, but rather a module that is employed only during training.

**改写**

> We use the projection head only during training.

**修改理由**：一句设计事实即可清楚表达，不需要先否定另一种说法。若上一段明确讨论推断时保留投影头的前作，则按比较任务决定是否保留对立。

## 12. 假设引用可以承接有效范围

**上下文**：定理2已经完整陈述条件与遗憾界，正文假设A1–A3定义凸域、梯度界和学习率；此处解释结果。

**原段**

> Under Assumptions A1–A3, Theorem 2 gives average regret of order $T^{-1/2}$. This statement requires the bounded convex domain, bounded gradients, and prescribed learning-rate schedule specified in these assumptions. It should not be interpreted as an unconditional guarantee for arbitrary neural-network training.

**独立无损删改后**

> Under Assumptions A1–A3, Theorem 2 gives average regret of order $T^{-1/2}$.

**修改理由**：假设和对象已经清楚，后文未提出神经网络全局优化的推广；无需重列条件和虚设反例。若正文确有这种推广声称，则必须修正对应声称，不能仅删除警告。

## 13. 已经准确的句子保持不变

**原句与终稿**

> We freeze the encoder and train a linear classifier on its representations.

**处理**：与给定实际协议一致、指代清楚且没有重复时保持原样。完成无损删改和语言清理并不要求每句留下修改。
