# NEURIPS23 · Learning to learn by gradient descent by gradient descent

- Marcin Andrychowicz、Misha Denil、Sergio Gómez Colmenarejo、Matthew W. Hoffman、David Pfau、Tom Schaul、Brendan Shillingford、Nando de Freitas；NIPS 2016。
- 来源：[正式记录](https://papers.nips.cc/paper_files/paper/2016/hash/fb87582825f9d28a8d42c5e5e5e8b23d-Abstract.html)。读取正式PDF第1–9页全部叙述、图1–9及图注；检视第2、4–8页。另读官方补充PDF第1–2页A预处理与B解释、查看图10，并读取图11–13图注；未将补充C全部样图计为已读。

摘要把学习更新规则定位为针对一类问题的特化。引言从梯度下降及人工曲率设计进入不同研究社区的优化器需求；第1.1节特意重新定义泛化为跨问题实例迁移，第1.2节承认早期元学习，增量落在可扩展的优化器架构，避免把“学习学习”本身声称为首次。

第2节先区分最终目标与轨迹加权训练代理，再说明截断反传和舍弃经梯度输入传播的二阶项；两项近似都改变实际训练，不能称完整精确元梯度。图2的实/虚边使停止梯度可见。第2.1节用逐坐标共享权重、各自隐状态化解维度问题，图3展示共享范围；补充A解释梯度幅度预处理，不能遗漏为无关实现细节。

第3节按二次函数、MNIST、CIFAR、图像风格递进。图4对比步数与超出训练步数的运行，图5–6检验架构迁移并展示sigmoid换ReLU失效；不是只选成功迁移图。CIFAR还需要将全连接和卷积参数拆成两套共享优化器，说明最初的单套机制不足。图8是目标对数曲线，图9是视觉质量例证；补充B把不同优化器放在LSTM同一轨迹下作条件诊断，不能解释成各自真实运行轨迹比较。

结尾主张同类结构迁移，未给任意目标收敛保证。后续[ICML2017研究](https://proceedings.mlr.press/v70/wichrowska17a/wichrowska17a.pdf)第2节及5.1节明确讨论和比较此优化器的迁移限制，提供研究影响依据，不新增本库计数。可迁移“先定义跨什么泛化，再按变化轴做压力测试”；适用于学习算法本身。按步更快还需报告元训练开销、每步时间和基线调参条件，不能由步数曲线直接宣布总计算更省。
