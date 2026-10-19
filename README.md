# ml-conference-writing

面向 ICML、ICLR 与 NeurIPS 的 Codex 写作技能。依据经典论文全文及方向档案安排论证，核验术语，独立无损删改，再调用本地统一去水印整理语言和保守清理 Unicode。

## 写作与语料

本轮核心库为三会各35篇经典，另各2篇近期校准，共105篇核心、6篇校准。逐篇原创阅读卡记录实际来源、版本、阅读范围、文件散列及章节或页码；完整性与当前阅读状态见各会语料文件。经典结合长期影响和领域沿用选样，不宣称客观唯一的前35排名。

ICML、NeurIPS 核心从2000年起，ICLR 从2013年起。正式论文身份关联 proceedings、OpenReview、arXiv 与 DOI；无 DOI 不影响记录，不把同一工作的多个版本重复计数。作者稿和正式版分别标记；阅读写作组织不等于逐行验证全部证明或复现实验。

按会议、方向、贡献类型及适用轨道匹配写作规范，保留来源、条件和反例。年度页数、匿名、声明、checklist、回复规则单独按届次、轨道与阶段核查；不会从经典版式推断当前要求。三会不被刻画为互斥的理论、架构、应用风格。

## 使用

```text
请使用 $ml-conference-writing，按 ICML 方法稿改写这份引言。
保留研究结果、技术条件与引用键，独立无损删改后执行统一去水印，
先给可用正文，再简要说明实质变化。
```

```text
请使用 $ml-conference-writing，检查这份 ICLR 经验研究稿的实验叙述。
明确比较协议和证据范围，删除重复解释，保留训练与测试的信息边界。
```

提供已有稿件、结果及目标会议即可。局部润色保留用户限定结构；结构改写可重排和合并。只使用给定结果，不编造定理、实验、数据和引文。审稿回复只依据真实证据与实际修改，发布由作者按指令执行。

核心术语首次引入时比较定义，核验后采用惯用名称。写完后独立检查可无损删去的内容，避免虚设对立；不设句长、压缩比例和禁词配额，成熟文字允许不改。技术核查完整进行，正文只保留当前位置必要的信息。

## 安装

已有同名目录时先保存本地成果。Windows PowerShell：

```powershell
git clone https://github.com/zdacongming-glitch/ml-conference-writing.git "$env:USERPROFILE\.codex\skills\ml-conference-writing"
```

macOS / Linux：

```bash
git clone https://github.com/zdacongming-glitch/ml-conference-writing.git ~/.codex/skills/ml-conference-writing
```

脚本依赖 Python 3.10+ 标准库；同步与安装更新还需要 Git。文件清理调用另装的 `watermarks-remover` 技能，缺失时按内置说明完成可做的忠实语言整理与技术核对，并说明未运行的工具步骤。不会自动安装外部重写服务，也不承诺通过 AI 检测。

## 持续学习与协作

首次完整方向档案至少需要十篇同会、同方向、匹配轨道和贡献类型的已读全文及类型依据。合格核心记录可复用；不足时保存为 `provisional`。新任务做定向增量检索，只深读新增、版本变化和反证；同轮连续改稿复用检索，没有新证据不例行改规范或提交。

默认本地积累。安装者使用自己的 GitHub 账号登录 `gh auth login`，需要设置 HTTPS 凭据时再执行 `gh auth setup-git`；Git 需配置本人的提交身份。然后在 Codex 说：

```text
请为 ml-conference-writing 开启社区协作。以后允许把公开论文的原创阅读分析、
术语核验和可复用写作规范整理成 PR，提交前检查具体差异。
稿件、未发表结果、数据和个人配置留在本地。
```

Codex 在技能目录执行一次：

```bash
python scripts/collaborate.py enable --enable-public-contributions
python scripts/collaborate.py status
```

该操作只记录本人选择，不上传内容。之后从具体方向和卡片准备独立差异，校验、审阅后按既有授权通过个人 fork 提交 PR，无需官方仓库写权限。维护者审核合并，不自动合并。可从一篇已读卡、术语纠正或反例开始，十篇完整门槛仍保留。只共享公开元数据和原创分析，原全文、稿件与私有研究留在本地。

操作细节见[社区协议](references/community-contributions.md)和[贡献指南](CONTRIBUTING.md)。停止公开贡献使用 `python scripts/collaborate.py disable`。

## 获取更新

在技能目录先预览，再应用：

```bash
python scripts/update_installation.py
python scripts/update_installation.py --apply
```

直接 Git 和 fork 安装只接受干净、可快进的分支，保留原 `origin`；复制式安装核对外部版本与散列，保护本地修改与新增方向材料，冲突停止。旧复制版初次缺少基线时，需要可信原版本 `--base-revision <commit>` 并通过比对。更新不上传内容，也不改变协作开关。

## 主要资源

| 文件 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | Codex 执行流程和完成标准 |
| [三会索引](references/conferences/index.md) | 会议指南、核心、校准与逐篇卡 |
| [语料协议](references/corpus-protocol.md) | 全文阅读、工作身份、方向建库及增量维护 |
| [术语协议](references/terminology-protocol.md) | 定义核验与首选名称 |
| [修改手册](references/revision-playbook.md) | 按论证任务组织修改 |
| [实验叙述](references/evidence-and-experiments.md) | 比较、归因、信息边界与不确定性 |
| [改写示例](references/worked-examples.md) | 纠正越界、删去重复和保留成熟句 |
| [终稿清理](references/final-cleanup.md) | 统一去水印与技术复核 |
| [社区协议](references/community-contributions.md) | 个人开启、fork PR、审核和更新 |
| [资源校验](scripts/check_resources.py) | 身份、阅读记录、方向门槛与 Markdown |
| [维护同步](scripts/sync_resources.py) | 维护者白名单预览与同步 |

投稿要求文件保留历史核查日期，实际投稿需复核目标届次官方来源。技能用于写作与编辑，不保证录用。
