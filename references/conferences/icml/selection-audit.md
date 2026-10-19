# ICML 核心语料选择与阅读审计

检索与阅读截止：2026-10-19。核心目标为 35 篇 2000 年以来 ICML 正式主会论文；另取最近已完成届次 ICML 2026 的两篇 Outstanding Paper 校准当前写法。实际核心年份为 2001–2020，近期校准为 2026。核心库不要求每年一篇，也不把近期获奖作品当作已经历时间检验的经典。

## 选择依据和边界

这是结合官方 Test of Time 认可、引用持续性、方法后续使用和写作场景覆盖形成的经典样本。它不声称存在客观唯一的“最经典 35 篇”排序。官方奖项较适合提供独立长期认可，但数量不足以覆盖全部方向；引用用于发现和交叉检查候选，不能取代归属核验或全文学习。

逐篇 JSON 保存 `recognition_evidence`。取得 OpenAlex 对应记录的论文另存检索日总量和 `counts_by_year`，可以检查 2021–2025 年实际记录；没有伪造早年检索快照或引用增长曲线。2026 是未完全年且可能索引滞后的记录，不与完整年度做增长率比较。不同版本、重印和同名期刊论文不相加。CRF 等早期来源优先作者出版清单与大学托管会议版本；PMLR 时期逐条核对 `citation_conference_title`、作者、年份及 PDF 首页。主轨均排除 workshop 和 position 记录。

覆盖图模型、半监督学习、SVM/排序优化、NLP 多任务、表征学习、生成模型、推断、不确定性、公平、迁移、元学习、RL/bandit 及理论。主贡献标签为 methods 27 篇、theory 4 篇、empirical-study 3 篇、negative-results 1 篇；这些标签服务于检索，并非否认一篇论文包含多种证据。作者与研究方向仍有重叠，年代集中在 2013–2018；系统、数据集、核方法与较新 foundation-model 工作没有充分代表。因此本库不能替代“会议 × 方向 × 贡献类型 × 轨道”的任务专属检索，未来应优先补充这些缺口的方向档案。

## 真实阅读与版本控制

35 篇核心 PDF 共 321 页，2 篇校准 PDF 共 51 页，已连续读完正确会议版本的主文叙述、算法和定理陈述、图表及图注、结尾和参考文献。每篇另渲染关键图表/公式页查看版面，笔记记录 PDF 页码及章节。ICML10、ICML13 的内附附录已读；两篇 2026 论文的内附附录分别 A–D 和 A–F 全读。阅读数学证明叙述不等于逐式独立验证，也没有复现实验。

另合法取得 22 份独立官方补充 PDF：11 份全部读完，6 份按需要选读，5 份仅取得。每份的来源、页数、源字节 SHA256、`status` 与实际 `read_pages` 独立记录在相应论文 `supplementary_texts`；绝不把取得、自动提取或页首索引当成已读。主文 `status=read` 表示完整主文叙述及图表阅读，不能解读为所有外部附件都已读。共享资源只收原创分析、规范、文献元数据及源散列；原 PDF 和全文提取保留在本地研究缓存。

### 候选纠错记录

| 候选或版本问题 | 核验结果与处理 |
| --- | --- |
| Understanding the difficulty of training deep feedforward neural networks | AISTATS 2010；剔除，核心以真实 ICML 2010 Hessian-free Optimization 等工作补充优化方向。 |
| Deep Boltzmann Machines | AISTATS；不作为 ICML 核心。纳入真实 ICML RankNet 扩充任务覆盖。 |
| DAgger: A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning | AISTATS 2011；剔除，采用 ICML 2004 Apprenticeship Learning。 |
| FedAvg: Communication-Efficient Learning of Deep Networks from Decentralized Data | AISTATS 2017；剔除，采用 ICML 2015 Unsupervised Domain Adaptation by Backpropagation。 |
| Highway Networks | ICML 2015 workshop；不能算作正式主轨核心，以 ICML 2015 Normalizing Flows 等正式论文补充。 |
| beta-TCVAE / Isolating Sources of Disentanglement in VAEs | NeurIPS 2018；剔除，纳入真实 ICML 2018 FactorVAE。 |
| LIME / Adam | 分别为 KDD / ICLR，未混入 ICML。 |
| Deep Adaptation Networks | 属于真实 ICML 2015；为减少域适应重复，初选后以 TRPO 替换，并未因无效归属剔除。 |
| ICML-C01 初次下载的 `ni26a` | 题名不符；没有将错误 PDF 阅读计入完成数。改核 `ni26e`，下载并连续读完正确 16 页版本后才记 read。 |
| Pegasos 同名期刊扩展 | 引用标题搜索优先返回 Mathematical Programming 2010/2011 记录；改按 ICML 2007 DOI 查询，只用会议记录引用量。实际阅读作者托管 8 页会议短版。 |
| Unified NLP 短标题目录记录 | 正式 PDF 主标题加副标题；目录记录以短标题收录，按会议 DOI 和作者年份核对，不接受最初的主题近似搜索结果。 |
| arXiv 年份早于正式会议 | DeCAF、MC dropout、DANN、Locatello、linear Thompson Sampling 等目录元数据可能采用首个作者稿年份；主记录坚持正式 ICML 年份，标注差异，不把每个版本算作另一篇。 |
| SGLD 目录年份 2012 | 对应来源指向 WelTeh2011a 作者稿；正式 PDF 为 ICML 2011。目录快照年份不改写会议年份。 |
| GP-UCB 标题变化 | 短会议版、早期 arXiv 与后续较长版本题名不完全一致；核心读 ICML 2010 正式短版，以 ICML 2020 官方长期奖为认可证据，没有把不同版本引用数字直接合并。 |
| 2024 年后重印记录 | 标题相同不代表新经典或新会议年；BN、diffusion、SimCLR 等重印的独立引用记录不相加。 |

## 作品身份与去重

`id`（ICML01 等）只用于库内定位。`work_id` 优先采用真实 DOI、ACM 文章号、PMLR 卷/篇标识或旧 ICML archive 的实际 paper 号。早期没有取得可核验独立出版 ID 的论文，使用已核验的作者稿/机构单篇记录 canonical URI 作为 fallback（ICML02、06、10）；它是来源身份，未来若新增 DOI 别名需合并同一作品，不能另计一篇。ICML01 的单篇出版记录为 ACM 655813；CMU 作者出版清单仅作归属辅助，实际全文来自 Columbia 大学课程托管副本，未称托管者为作者。

## 逐篇目录

完整作者、正式来源、阅读范围、SHA256、引用快照和入选理由见两份 JSON；下表用于快速定位原创笔记。

| ID | 年份 | 论文与阅读笔记 | PDF 页数 |
| --- | --- | --- | --- |
| ICML01 | 2001 | [Conditional Random Fields: Probabilistic Models for Segmenting and Labeling Sequence Data](papers/ICML01.md) | 8 |
| ICML02 | 2003 | [Semi-Supervised Learning Using Gaussian Fields and Harmonic Functions](papers/ICML02.md) | 8 |
| ICML03 | 2007 | [Pegasos: Primal Estimated sub-GrAdient SOlver for SVM](papers/ICML03.md) | 8 |
| ICML04 | 2008 | [A Unified Architecture for Natural Language Processing: Deep Neural Networks with Multitask Learning](papers/ICML04.md) | 8 |
| ICML05 | 2008 | [Extracting and Composing Robust Features with Denoising Autoencoders](papers/ICML05.md) | 8 |
| ICML06 | 2005 | [Learning to Rank using Gradient Descent](papers/ICML06.md) | 8 |
| ICML07 | 2010 | [Gaussian Process Optimization in the Bandit Setting: No Regret and Experimental Design](papers/ICML07.md) | 8 |
| ICML08 | 2010 | [Deep Learning via Hessian-free Optimization](papers/ICML08.md) | 8 |
| ICML09 | 2010 | [Rectified Linear Units Improve Restricted Boltzmann Machines](papers/ICML09.md) | 8 |
| ICML10 | 2004 | [Apprenticeship Learning via Inverse Reinforcement Learning](papers/ICML10.md) | 8 |
| ICML11 | 2011 | [Bayesian Learning via Stochastic Gradient Langevin Dynamics](papers/ICML11.md) | 8 |
| ICML12 | 2013 | [Learning Fair Representations](papers/ICML12.md) | 9 |
| ICML13 | 2013 | [Deep Canonical Correlation Analysis](papers/ICML13.md) | 9 |
| ICML14 | 2013 | [On the importance of initialization and momentum in deep learning](papers/ICML14.md) | 9 |
| ICML15 | 2014 | [Stochastic Backpropagation and Approximate Inference in Deep Generative Models](papers/ICML15.md) | 9 |
| ICML16 | 2014 | [DeCAF: A Deep Convolutional Activation Feature for Generic Visual Recognition](papers/ICML16.md) | 9 |
| ICML17 | 2015 | [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](papers/ICML17.md) | 9 |
| ICML18 | 2015 | [Deep Unsupervised Learning using Nonequilibrium Thermodynamics](papers/ICML18.md) | 10 |
| ICML19 | 2015 | [Show, Attend and Tell: Neural Image Caption Generation with Visual Attention](papers/ICML19.md) | 10 |
| ICML20 | 2015 | [Variational Inference with Normalizing Flows](papers/ICML20.md) | 9 |
| ICML21 | 2016 | [Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning](papers/ICML21.md) | 10 |
| ICML22 | 2016 | [Asynchronous Methods for Deep Reinforcement Learning](papers/ICML22.md) | 10 |
| ICML23 | 2017 | [Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks](papers/ICML23.md) | 10 |
| ICML24 | 2017 | [On Calibration of Modern Neural Networks](papers/ICML24.md) | 10 |
| ICML25 | 2017 | [Wasserstein Generative Adversarial Networks](papers/ICML25.md) | 10 |
| ICML26 | 2018 | [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](papers/ICML26.md) | 10 |
| ICML27 | 2018 | [Disentangling by Factorising](papers/ICML27.md) | 10 |
| ICML28 | 2018 | [Which Training Methods for GANs do actually Converge?](papers/ICML28.md) | 10 |
| ICML29 | 2019 | [Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](papers/ICML29.md) | 11 |
| ICML30 | 2020 | [A Simple Framework for Contrastive Learning of Visual Representations](papers/ICML30.md) | 11 |
| ICML31 | 2015 | [Unsupervised Domain Adaptation by Backpropagation](papers/ICML31.md) | 10 |
| ICML32 | 2015 | [Trust Region Policy Optimization](papers/ICML32.md) | 9 |
| ICML33 | 2015 | [Optimizing Neural Networks with Kronecker-factored Approximate Curvature](papers/ICML33.md) | 10 |
| ICML34 | 2013 | [Thompson Sampling for Contextual Bandits with Linear Payoffs](papers/ICML34.md) | 9 |
| ICML35 | 2017 | [Minimax Regret Bounds for Reinforcement Learning](papers/ICML35.md) | 10 |
| ICML-C01 | 2026 | [The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models](papers/ICML-C01.md) | 16 |
| ICML-C02 | 2026 | [High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions](papers/ICML-C02.md) | 35 |
