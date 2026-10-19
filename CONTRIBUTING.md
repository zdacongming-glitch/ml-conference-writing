# 贡献指南

欢迎贡献公开论文的原创阅读分析、术语核验、写作规范及反例。可以从一篇已读论文开始，操作细节见[社区协议](references/community-contributions.md)。

## 材料与证据

- 以会议、方向、贡献类型组织档案，明确适用轨道。每个方向包含 `profile.md`、`corpus.json` 和 `terms.json`，字段见[语料协议](references/corpus-protocol.md)。
- 规范包含具体写作动作、论文 ID、章节或页码、适用条件和反例；不同条件下的相反观察可以并存。
- 阅读卡基于实际全文叙述、图表图注和必要附录，记录实际版本和范围；摘要、下载或记忆不计已读。不得复制论文段落。
- 按正式论文身份与别名去重，复用已有 ID 和卡片。DOI 可以缺少；arXiv、OpenReview 修订和终稿不重复计数。
- 不足十个匹配工作时保留 `provisional`。同会、同方向、同轨道与贡献类型的十篇已读全文，加上类型依据，才支持完整方向档案。
- 不把获奖、被录用、高引用或单篇特殊安排直接提升为全会规范。官方要求、论文观察与编辑建议分开。

只共享公开元数据和有权公开的原创分析。原论文、完整提取文本、稿件、未发表结果、数据、缓存、个人配置与凭据留在本地。贡献者在公开前检查具体差异。

## 通过 Codex 贡献

安装者本人明确开启后，在技能目录运行：

```bash
python scripts/collaborate.py enable --enable-public-contributions
python scripts/collaborate.py status
```

只在本机记录选择，不继承其他技能的授权。准备真实方向及关联卡：

```bash
python scripts/collaborate.py prepare --path references/conferences/icml/topics/representation-learning--methods
```

加 `--apply` 创建独立贡献副本并暂存差异，不上传。审阅文件和差异，校验后准备技能之外的 UTF-8 PR 正文文件。先预览：

```bash
python scripts/collaborate.py submit --title "补充 ICML 表征学习写作观察" --body-file /path/to/pr-body.md
```

本人开启且本次公开内容已在授权范围内时，加 `--apply` 才提交、创建或复用个人 fork、推送及发起 PR。需配置本人 Git 身份并登录 `gh`；无官方写权限也可贡献。没有 `gh` 时手动 fork 和创建 PR，证据要求相同。

自动白名单只含三会方向目录中的 Markdown、JSON 及同会 `papers/*.md`。核心库替换、会议总指南、指令、脚本和仓库配置走普通维护 PR。未知基线不覆盖已有路径；冲突保留双方，不强推。

## 校验和评审

仓库根目录运行：

```bash
python scripts/check_resources.py --require-complete
```

PR 和主分支 CI 检查资源及 Python 语法；该选项保护每会35篇核心和初始近期库，不要求所有临时方向凑满十篇。脚本不能证明已经阅读全文或规则合理，维护者仍需审阅：

1. 正式归属、轨道、版本与原文定位是否准确。
2. 方向及类型是否匹配，术语是否定义等价，规则范围是否超过证据。
3. 是否补充独立来源或反例，与现有规则如何合并。
4. 是否为原创、可公开内容，是否误改技术含义。

证据可以缩小或替代旧规则，记录原因与来源。CI 通过不自动合并；同一准备分支重试可返回已有 PR，新准备轮次产生新分支，应避免重复投稿。

## 更新本地

在技能目录运行 `python scripts/update_installation.py` 预览，再加 `--apply` 更新。Git/fork 安装要求干净且可快进；复制式安装依据外部基线保护修改与新增材料。版本不明或冲突时保存成果并协调，不硬重置。合并 PR 不会自动消除安装中的本地改动，具体处理见[社区协议](references/community-contributions.md#安装更新)。

更新不会开启公开贡献。停止贡献执行 `python scripts/collaborate.py disable`。
