# 社区贡献、个人开启与安装更新

用于公开分享可复用方向规范、原创阅读卡或术语纠正，以及获取上游更新。普通写作默认在本地积累；安装技能或登录 GitHub 不自动开启贡献。

## 开启与关闭

安装者在 Codex 明确说出自己的选择，例如：

```text
请为 ml-conference-writing 开启社区协作。以后允许把公开论文的原创阅读分析、
术语核验和可复用写作规范整理成 PR，提交前检查具体差异。
稿件、未发表结果、数据和个人配置留在本地。
```

在技能目录执行一次：

```bash
python scripts/collaborate.py enable --enable-public-contributions
python scripts/collaborate.py status
```

`enable` 只在技能之外保存当前安装者的选择，不创建 fork 或上传文件。使用独立的 `skill-maintenance/ml-conference-writing-community.json`；统计期刊技能的开关和维护者授权不会转移。已有明确授权可持续沿用，公开范围仍须覆盖本次具体材料。暂停公开贡献执行 `python scripts/collaborate.py disable`，本地积累继续可用。

本地整理需要 Python 3.10+ 与 Git。提交还需要个人 GitHub 账号、GitHub CLI `gh` 及已设置的 Git 提交身份。运行 `gh auth login` 登录本人账号；需要配置 HTTPS 推送凭据时运行 `gh auth setup-git`。首次提交才创建或复用个人 fork，无需官方仓库写权限。

## 范围与证据

自动流程只接收：

- `references/conferences/<conference>/topics/<topic-id>/` 下的 `.md`、`.json`。
- 同会 `papers/` 下单层的原创 `.md` 阅读卡。

`conference` 为 `icml`、`iclr`、`neurips`。方向按稳定研究问题和贡献类型组织，例如 `representation-learning--methods`；轨道另在档案中明确。贡献类型及字段见[语料协议](corpus-protocol.md)。

可以只贡献一篇实际读完的分析、术语纠正或规则反例。不足十篇时方向保持 `provisional`；十个独立工作、同会同方向、匹配贡献类型和轨道的已读全文及类型依据，才支持 `complete`。其他会议、邻近方向或 workshop 的材料可以作补充，不混计门槛。

先查正式论文身份及 DOI、OpenReview、arXiv 别名，复用已有 ID 与卡片。新论文 ID 用 `work-` 加规范 `work_id` 的 SHA256 前十二位；`work_id` 使用正式条目或 forum 的稳定身份，不能随题目或上传版本变化。新卡可放在同会 `papers/<id>.md`，方向中的 `note` 指向 `../../papers/<id>.md`。已登记的其他方向额外论文可以直接按 ID 引用。无 DOI 的论文照常贡献，不以不同版本凑数。

每条规范写明具体动作、支持论文及章节或页码、适用条件与反例。逐篇卡基于实际全文阅读，区分作者稿、接收稿和终稿；获取失败不能标为已读。单篇特殊写法先作为观察，不因获奖、被录用或高引用而直接变成全会通则。术语纠正须比较定义。

共享公开来源元数据及有权公开的原创分析。原论文、完整提取文本、稿件、数据、未发表结果、个人路径、凭据与配置留在本地；说明规则时用原创示例。发布前审阅具体差异，校验器不能识别所有私有研究内容。

## 准备和提交

先预览选定真实材料，路径相对技能根目录，`--path` 可以重复：

```bash
python scripts/collaborate.py prepare --path references/conferences/icml/topics/representation-learning--methods
```

确认范围后使用同一命令加 `--apply`，创建独立贡献工作副本、暂存差异并记录清单。安装目录保持原状；此步不提交、不推送。审阅输出的 worktree、文件清单及 `git diff --cached`。

脚本比较已安装基线、本地材料与官方最新版本，只传递选中的本地变化；非冲突部分三方合并，冲突时停止并保留双方。不会用旧整库覆盖上游。直接 Git 安装默认使用 HEAD；复制式安装使用外部安装基线。未知基线时，只能准备上游没有的新路径；修改已有文件需提供可信的 `--base-revision <commit>`。Git 或 fork 用户若已提交本地材料、HEAD 不属于官方历史，也可显式提供已知官方基线。

将 PR 正文存到技能之外的 UTF-8 文件，说明会议、方向、贡献类型、轨道、来源、阅读范围、反例、校验结果和缺口。先预览：

```bash
python scripts/collaborate.py submit --title "补充 ICML 表征学习方法稿写作观察" --body-file /path/to/pr-body.md
```

本人已开启且既有授权覆盖本次公开内容时，审阅后加 `--apply` 才提交、创建或复用 fork、推送并发起 PR。不自动合并；同一准备分支重试返回已有 PR。新的 `prepare --apply` 创建新分支，不更新旧 PR，准备前检查相关已有 PR，避免重复提交。失败时保留工作副本，不强推；修复认证或网络后按原清单重试。

没有 `gh` 时可以手动 fork、建立分支并提交相同范围的材料。核心库替换、会议总指南、技能指令、脚本和仓库配置超出自动白名单，走普通维护 PR 单独审阅。

## 校验与维护者审核

在仓库根目录运行 `python scripts/check_resources.py --require-complete`。CI 检查核心35篇/会、初始近期校准、身份与版本去重、阅读记录、来源散列格式、卡片、方向门槛、链接、Markdown 和 Python 语法。临时方向无需凑十篇。

脚本不能证明实际阅读、正式轨道判断或语义相关性，也不能判断规则是否概括过度。维护者审阅实际版本与定位、贡献类型、方向、适用条件、反例和原创性。相反观察在不同条件下可以并存；只有证据支持才扩大适用范围。去重后合并已有档案，保留替代关系及原因。

PR 合并进入官方库后，其他安装者更新本地安装才会获得变化。维护者自己的既有同步配置位于技能外 `skill-maintenance/ml-conference-writing.json`，不进入共享包。

## 安装更新

在技能目录先预览，再应用：

```bash
python scripts/update_installation.py
python scripts/update_installation.py --apply
```

更新从官方仓库获取版本，不推送内容，也不改变个人协作开关。

- 直接 Git 或 fork 安装只接受干净、可快进的分支，从官方版本更新并保留原 `origin`。本地改动、分叉提交、未跟踪或同名 ignored 文件冲突会阻止更新；保留成果后协调，不硬重置。
- 复制式安装按外部版本记录和文件散列核对；既有受管文件本地修改或删除时停止。新增本地方向和其他本地资源在不冲突时保留。
- 初次复制安装没有基线，受管内容与官方最新版一致时可建立基线；旧版需可信原提交 `--base-revision <commit>` 并通过比对。版本不明时先保存成果和人工核对，不猜测提交号。

安装状态在技能外 `skill-maintenance/ml-conference-writing-installation.json`，含版本和文本散列。贡献提交不自动消除安装中的改动；上游合并后仍可能需要人工协调或在保存成果后重新安装。
