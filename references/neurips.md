# NeurIPS 写作与投稿档案

核查日：2026-09-30。规则快照：**NeurIPS 2026 Main Track Handbook，V2026.3**。历史会议名 NIPS 与 NeurIPS 对应同一会议系列；不要将其他会议的论文混入范例。

## 官方要求

| 项目 | 2026 主轨 |
| --- | --- |
| 初投稿正文 | 最多 9 页，含图表，使用当年样式 |
| 接收后的终稿正文 | 最多 10 页 |
| 页限之外 | 参考文献、可选技术附录及必需的 paper checklist |
| 附录 | 放在主文之后的同一 PDF；决定性证据不应仅放附录 |
| 匿名 | 初投与补充材料遵循双盲要求；初投不放致谢；已发表自引用第三人称 |

依据：[Main Track Handbook](https://neurips.cc/Conferences/2026/MainTrackHandbook) 和 [2026 官方格式压缩包](https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip)。不能将主轨规则直接用于 Evaluations & Datasets 或其他专门轨道；从 [Call for Papers](https://neurips.cc/Conferences/2026/CallForPapers) 进入对应要求。

主轨**不强制独立的 Broader Impacts 栏目**；适用的影响和伦理问题仍需讨论，可在正文或附录中按规则安排。不能挪用 ICML 的声明名称及免计页数安排。[Main Track Handbook](https://neurips.cc/Conferences/2026/MainTrackHandbook)

## 官方审稿标准：先识别贡献类型

2026 主轨使用 General、Theory、Use-Inspired、Concept & Feasibility、Negative Results 等 contribution types。这些是**主轨内的贡献类型**，不等同于另一个投稿轨道；选定后不能随意在评审期间更换。[Reviewer Guidelines](https://neurips.cc/Conferences/2026/ReviewerGuidelines)

同一指南分别讨论 quality、clarity、significance、originality。Theory 类型**不要求经验验证**；应该解释结果意义、关键假设和证明思想。负结果或概念可行性贡献仍需要充分论证其新知识与价值，不是降低证据要求。

据此给出的**编辑建议**：理论稿把结果的变化、条件与困难放前面；经验或 use-inspired 稿把真正的需求与评估协议说清；负结果稿明确检验对象、测试强度和失败范围。不要给所有稿件强加同一组实验章节。

## Checklist 怎样落实到文字

官方压缩包中的 [checklist.tex](https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip) 要求使用规定问题与回答格式，并给出解释。它检验主张与证据的一致性、局限、理论假设、复现、实验设置、不确定性、计算资源及适用的伦理事项。

**编辑建议**：回答应指向确有内容的章节或材料；不要全部自动填 Yes。No/NA 本身通常不是拒稿理由，但必须适用且解释真实。主张没有证据不能靠 checklist 的肯定答案补救。代码开放受到鼓励，但不能概括为每篇一律强制公开代码；仍需提供与贡献相称的复现或验证途径。

误差条说明随机性来源及 SD、SE、CI 的含义；计算报告区分单次运行和项目总投入。不强制把这些建议机械变成“必须五个数据集、三个随机种子”。详细编辑步骤见 [evidence-and-experiments.md](evidence-and-experiments.md)。

## AI 使用与当次核查

2026 规则要求说明成为核心方法中重要、原创或非标准组成部分的 LLM 使用；仅用于不影响核心方法的写作、编辑或格式处理，不要求相同披露。[Main Track Handbook](https://neurips.cc/Conferences/2026/MainTrackHandbook) 与官方 checklist 的 LLM 问题。

不要把这条写成其他届次或 ICLR 的通用规则；作者始终需要核实内容与引文。投稿前检查目标年模板、checklist、贡献类型、页数、补充材料和回复规则。

## 可学的论文路径

见 [阅读笔记](classic-papers.md)：M09 Random Features 用计算障碍连接构造与误差；M10 Transformer 用架构需求解释组件；M11 GAN 把直觉变成目标并区分理想分析与实现；M12 DDPM 解释目标选择并同时报告优势与代价。
