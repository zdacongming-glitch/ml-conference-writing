# 全文语料、方向规范与增量维护

## 核心语料与正式归属

本轮为 ICML、ICLR、NeurIPS 各35篇经典，另加各2篇近期校准，共105篇经典与6篇校准。ICML、NeurIPS 核心从2000年起选，ICLR 从2013年起；不得把其他会议或 workshop 的论文计入主轨配额。

经典选择结合官方 Test-of-Time 认可、独立后续沿用、长期影响和可核验引用轨迹，兼顾方向、贡献类型、年代与作者群体。引用量用于发现候选，不单独决定入选；当年最佳论文奖也不等于已经历长期验证。保存入选依据和排除、替换理由，不声称客观唯一的最经典排名。

近期校准使用正式归属已确认的近年代表作，不计经典数；本轮为2023年起的已正式发表或获接收最终版本，每会至少两篇。其作用是校准特定写作观察，不代表已经概括整个当代会议。历史校准记录保留日期，后续按实际新证据补充，不用滚动年份修改过去的事实。

ICML 优先正式 proceedings；NeurIPS 使用逐篇官方条目；ICLR 使用官方 proceedings、接受记录和对应 OpenReview 最终版本。较早论文可以通过官方档案核验归属，作者公开稿用于实际阅读时如实记录版本。PMLR 也收录其他会议；带会议名称的 workshop 或 proceedings 卷名不证明论文属于主轨。逐篇核验题目、作者、年份、正式会议、轨道和稿型。

## 身份与版本

`work_id` 表示一个研究工作，`id` 为本库引用 ID；两者在版本变化时保持稳定。优先采用正式条目标识，如 `pmlr:v37/ioffe15`、`openreview:<forum-id>`、`neurips:<year>:<paper-hash>`。较早无此类标识时采用经核验的正式档案身份。

`identifiers` 关联 DOI、OpenReview forum ID、arXiv 基础 ID 和 proceedings URL；没有 DOI 不构成缺陷。arXiv 版本号另存实际版本，不用不同标题、上传版本或 camera-ready 凑数。标题变化或疑似期刊扩展需检查内容和版本关系后确定身份；不能只因标题近似就自动合并。

引用已存在论文时复用 ID、元数据及阅读卡。跨方向可直接引用已登记的额外论文，不重复建立一份相同工作。跨会议参考材料允许使用，但不计入目标会议的十篇门槛。

`publication_url` 和 `identifiers.proceedings_url` 指向单篇记录。整年接收清单只用作正式归属证据，放入 `track_evidence` 或来源说明；不能把同一清单当成多篇论文的身份。早期缺单篇正式条目时，可用已核验的单篇原始文献记录，并另列确认会议、年份和轨道的官方证据。

## 获取与实际阅读

优先获取正式全文，其次匹配的作者或机构公开版本。下载后检查标题、作者、主文起止、图表和末尾，排除封面、摘要、勘误、讨论回复和访问拦截页。扫描件可 OCR，专名、公式与图形回看原页。查询关联更正或撤回，旧论文的历史解释也可能需要修正。

只有实际阅读全文叙述、图表及图注，并读完理解主要论证所需的附录后，才设 `full_text.status: read`。逐式证明核验或实验复现不是默认承诺；记录实际范围。获取失败、下载完成、摘要阅读和记忆均不能代替全文阅读。既有十二篇重点阅读笔记只按原记录复用，补足阅读后才能升级状态。

每篇原创分析标真实章节或 PDF 页码，记录：摘要信息选择；引言段落功能；定义、直觉、方法、算法和理论的信息顺序；图表、比较和实验分别支持的判断；讨论和结尾作用；可迁移写作动作、适用条件及反例。不复制正文段落到技能包。

原 PDF、完整提取文本、OCR 图像和下载日志放在技能之外的研究缓存。共享资源只含公开题录、原创分析和规范。优先保存源文件字节的 SHA256；仅通过网页工具完整阅读而无法取得原字节时，`sha256` 留空，保存实际完整提取文本的 `extracted_text_sha256`，标 `hash_scope: extracted_text`。不得混淆两种散列。

## 会议语料格式

每会保存 `core-corpus.json`、`calibration-corpus.json`、`guide.md`、`selection-audit.md` 和 `papers/`。

语料对象包含 `schema_version`、`conference_id`、`conference`、`checked_at`、`selection_policy`、`papers`。每篇包含：

- `id`、`work_id`、`title`、`authors`、正式发表 `year`、`conference_id`、`publication_url`、`identifiers`。
- `track`：稳定值 `main`、`position`、`datasets-benchmarks`、`workshop` 或 `other`；实际官方轨道名可另存。
- `contribution_type`：主类型 `methods`、`theory`、`empirical-study`、`negative-results`、`datasets-benchmarks`、`systems` 或 `position`；多类型经核验后另用 `contribution_types`，不以出现定理或数据就推断类型。
- `topics`、`selection_reason`、`recognition_evidence`；每项认可证据含真实 `url`、准确说明 `note`，可以另存种类、核验日期与引用快照。题录页面只能核验归属，不能冒充领域共识证据。
- `full_text`：实际 URL、版本、格式、页数、散列、`read_scope`、`read_at`、真实状态。
- `note`：相对当前会议目录的阅读卡路径；例如 `papers/ICML01.md`。

正文中的来源关系和类型依据仍须人工或助手核验；字段齐全不能证明已经阅读或概括正确。

## 方向档案与十篇门槛

长期经验按“会议 × 方向 × 贡献类型”匹配，并标明适用轨道。方向 ID 表达稳定研究问题和边界；同方向不同类型可用复合 ID，例如 `representation-learning--methods`。维护方向定义、关键词、同义名称和排除项。

首次建档强制定向检索目标会议、本方向和匹配类型，优先经典、最近邻与必要近期校准。至少十个不同研究工作、同会同方向、匹配轨道与贡献类型、实际已读全文，档案才能 `complete`。核心及近期记录可复用；其他方向、其他会议或 workshop 只能作补充。数量不足记录检索范围与缺口，状态保持 `provisional`，继续有依据的改稿。

每个 `topics/<topic-id>/` 保存：

- `profile.md`：具体写作动作、支持论文及定位、适用条件和反例。
- `corpus.json`：`schema_version`、`conference_id`、方向定义、查询式与日期、`status`、目标 `track`、`contribution_type`、`paper_ids`、`supplementary_paper_ids`、`additional_papers`、`type_evidence` 及更新记录。
- `type_evidence` 按论文 ID 保存 `{contribution_type, basis}`，`basis` 指向原文或阅读卡位置及类型判断。论文类型标签、轨道和目标会议必须实际匹配，才计入十篇。
- `additional_papers` 保存同上论文格式，额外条目的 `note` 相对当前方向目录；共享卡在同一会议 `papers/` 时用 `../../papers/<id>.md`。已在其他方向登记的论文可直接引用其 ID。
- 补充论文的 `conference_id` 保留真实会议，例如 `iclr` 或 `aistats`，不能改成目标会议；新增跨会条目也可在本方向登记，放入 `supplementary_paper_ids`，不计目标十篇。
- `terms.json`：按[术语协议](terminology-protocol.md)保存已核验概念。

官方规则单独按“会议 × 届次 × 轨道 × 阶段”保存，不因换一年就重建十篇方向库。已有年度规则摘要是历史快照；页数、匿名、声明、补充材料和回复规则按目标届次官方原始来源复核。

## 从观察形成规则

单篇安排先记为观察。提出方向建议前检查独立作者群体、重复证据和反例；会议层建议还需跨方向支持。每条规则写明证据定位及适用条件。合理但不同的组织方式可并存，不用人为刻板风格制造三会差别。

区分官方要求、官方审稿标准、论文观察与编辑建议。经典论文的强标题、首图、贡献列表或被录用本身不证明所有稿件都应照做。条件与反例优先于脱离语境的模仿。

## 增量维护与同步

每个新的实质写作任务加载档案并执行定向增量检索，覆盖新文章、先前遗漏的经典、来源版本变化、更正与反证。按工作身份和别名去重，只深读新增相关材料或受影响规则；同轮连续改稿复用检索。无可复用新证据不改文件，不为进化而例行提交。

新证据仅影响部分规则时修订相关部分；足够独立反证或方向边界、贡献类型变化才重审整个方向。保留替代关系和原因。经典库用于写作组织，当前 SOTA、模型版本、数据污染、工具权限与评估协议另查当时一手来源。

运行 `scripts/check_resources.py`；本轮完整建库验收加 `--require-complete`，可用 `--cache-root` 核对真实源散列。脚本只检验完整性，不能认证阅读或学术判断。

维护者配置放在技能之外的 `skill-maintenance/ml-conference-writing.json`；社区配置及安装基线分别使用本技能自己的文件名。公开贡献、白名单、个人开启、PR 审核和安装更新见[社区协议](community-contributions.md)。不继承统计期刊技能的个人授权或仓库配置；只同步公开元数据、原创分析与规范，不上传稿件、数据、未发表结果或全文缓存。
