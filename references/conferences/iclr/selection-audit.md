# ICLR 语料选择与阅读审计

核验日期：2026-10-19。

## 选择口径

经典核心保持35个不同的正式主会工作，近期校准另列2个。检索窗口从ICLR创办的2013年至核验日；经典实际入选年份为2014–2020，优先长期认可和持续沿用，未为填满年份将新作称为test-of-time。此清单是供写作分析使用的精选库，不声称客观、唯一的“最经典前35名”。

长期认可使用三类互补线索：官方Test of Time；经身份匹配的OpenAlex多年引用轨迹；后续原始研究或官方实现对方法的实际采用、扩展与比较。引用数只用于发现和佐证，未按数字单列排序。正式接收信息只证明venue归属，不能单独证明长期认可。

6篇具有官方Test of Time主奖或runner-up证据：AEVB和Intriguing Properties（2024），Adam和NMT alignment（2025），DCGAN和DDPG（2026）。Deep Compression在2016官方页面获best paper，当年奖项与长期认可分别记录。所有奖项均给实际官方来源。2篇2026校准作品获得当年Outstanding Paper，分属理论和经验研究；没有把近期奖项写成Test of Time。

## 覆盖与偏差

入选覆盖变分推断、对抗鲁棒性、优化、泛化、图学习、生成/flow、强化学习、密集预测、离散潜变量、解耦表示、自监督、记忆QA、架构搜索、压缩及语言预训练；包括方法、理论与经验研究。理论稿用量词、上界和构造推进，经验稿用观察、控制和范围推进，防止只从模型架构稿归纳统一文风。

这不是对全部ICLR方向的均匀抽样。早期深度学习与视觉/生成/优化权重较大，Google/DeepMind与MILA相关作者出现较多，数据集、系统和position稿覆盖不足。NAS有两篇但原始RL控制器和可微双层搜索在结构与成本论证上有独立价值。新任务须执行方向检索，不能把本库偏好当成所有ICLR审稿偏好。

## 正式归属和版本

2014三篇使用[官方旧站conference proceedings清单](https://iclr.cc/archive/2014/old-site/conference-proceedings.html)，与workshop清单明确分开；旧的2014.html路径不可用，未用该失效地址充当已核验来源。2015/2016使用[2015官方会议清单](https://iclr.cc/archive/www/2015.html)和[2016官方会议清单](https://iclr.cc/archive/www/2016.html)。2017起保留正式OpenReview forum identity，结合正式页眉及作者公开记录核对。OpenReview直接PDF/API在本轮多次返回challenge，因此优先使用可取得的匹配作者全文；未把任意arXiv投稿当成主会接受稿。

35篇经典各有实际完整PDF。多数读取arXiv作者稿，版本及日期逐条记录，其中若干是会议后修订，DCGAN、IWAE、FFJORD和NAS文件仍有Under review页眉；主会归属另核，未声称这些字节已经与终稿逐页匹配。AEVB实际为2022修订、Adam为2017修订、DDPG为2019修订等，不能把这些布局称为原年终稿标准。

beta-VAE的OpenReview全文不可直取，经公开GitHub收藏取得带少量阅读高亮的22页原始会议PDF；题目、8位作者、ICLR2017正式页眉吻合。来源、实际SHA-256和镜像性质均明确记录；没有声称已与OpenReview字节独立比对。高亮属于取得版本现状，不用于规范生成。

原35号候选Ravi与Larochelle的Optimization as a Model for Few-Shot Learning，经OpenReview、作者主页和公开存档寻找仍未取得完整论文；作者主页ICLR演讲是slides，未冒充全文。该候选未计已读或入库，改用ICLR2019正式DARTS（OpenReview S1eYHoC5FX）。相关旧检索缓存不作为DARTS证据。

两篇近期校准均读取ICLR2026官方proceedings完整终稿：Transformers are Inherently Succinct（21页），LLMs Get Lost In Multi-Turn Conversation（41页）。后者先读的36页2025预印本仅供版本对照，不另计一个work；终稿主文、关键定义、人工核验和行为分析已重新阅读并更新定位。

## 阅读状态及证据边界

37篇均实际读完主文叙述、主要公式/定义、正文图表与图注，另按需要阅读相关附录；逐卡列具体范围。对关键结构与图表作页面渲染核验。下载或提取文本不自动等于read。这里的read不表示逐式证明认证、完整复现实验或每项补充画廊均逐图分析。

37个SHA-256都由实际取得的PDF字节计算，非URL、文件名或猜测值；没有使用源文件hash与文本hash混淆的例外。原PDF、提取全文、渲染页与检索快照只留研究缓存，公开skill仅包含元数据、原创阅读卡及归纳规范。正文笔记不是原文重印。

经典本身也有不宜学习的例子，阅读卡已保留：Adam原收敛分析被后续反例修正；beta-VAE指标丢弃底部50%运行；mixup白盒迭代攻击仍失败且LeNet语音结果变差；GIN表达能力不是泛化保证；DARTS搜索成本没有包含全部选型/训练；C02长度关联不是因果干预。这些限制防止将经典地位误当作每句话都正确。

## 引用数据异常排除

OpenAlex快照日期为2026-10-19。以完整标题、作者和arXiv基础ID或forum核身份，预印本年与正式会议年分开，引用量允许数据库聚合版本且受覆盖影响。时间异常或早于论文的索引记录未作为历史引用事实逐年解释；数值不建立唯一排名。

AEVB首个同名候选为2024工作，予以排除；NIN等采用身份匹配项。GIN带问号的初次查询失败后以去标点题名及作者、1810.00826核对。DARTS另查1806.09055及三作者，未沿用旧Ravi缓存。beta-VAE以题目、8作者、2017核对。

ALBERT初次候选为复现或Audio ALBERT，按DOI查询又出现preservation-copy错元数据；ELECTRA出现AraELECTRA及错题名/作者记录。这些计数均未纳入。两者改用Transformers[ALBERT官方实现文档](https://huggingface.co/docs/transformers/model_doc/albert)、[ELECTRA官方实现文档](https://huggingface.co/docs/transformers/model_doc/electra)中的原模型、集成日期与当前支持，作为持续实现沿用证据，不声称具体引用排名。ELECTRA正文还一手比较ALBERT，作为本库内部继承关系。

## 更新方式

逐篇原创卡片、规范的支持ID/章节、适用条件及反例构成本轮可复查产物。今后按会议×方向×文章类型检索至少10篇全文，已有核心可复用，同work不同版本只计一次。后续记录新证据、版本变化和反例再增量更新；没有新增材料不为“进化”改写规则。共享内容不得带入未发表稿件、项目数据、私有路径或论文原文附件。
