# 文本生成模型

语言生成模型采用的是**GPT-3模型**，它可以理解并生成自然语言。根据任务场景和功能强度分为四个可选子模型。其中`Davinci `功能最强大，而`Ada `响应速度最快。

| 模型名称         | 描述                                                         | 最大tokens   | 训练数据       |
| ---------------- | ------------------------------------------------------------ | ------------ | -------------- |
| text-davinci-003 | 最强大的GPT-3模型。<br />具有更高的输出质量、<br />更长的输出内容<br />和更好的语言理解能力。<br />还支持文本插入功能。 | 4,000 tokens | 截至2021年6月  |
| text-curie-001   | 功能强大，<br />但比`Davinci`速度更快，价格也更便宜。        | 2,048 tokens | 截至2019年10月 |
| text-babbage-001 | 能够完成简单任务，速度快，成本低。                           | 2,048 tokens | 截至2019年10月 |
| text-ada-001     | 能够完成非常简单的任务，<br />通常是GPT-3系列中速度最快的，成本最低的。 | 2,048 tokens | 截至2019年10月 |

尽管通常来讲`Davinci`最强大，但其他型号的模型在某些特定场景和任务下，具有明显的速度或成本优势。例如，`Curie`可以执行许多与`Davinci`相同的任务，但速度更快，成本仅为`Davinci`的1/10。

建议在实验时使用`Davinci`，因为它产生的结果最好。一旦实验完成，建议尝试一下其他模型的效果，看看是否能以更低的延迟或成本获得同样或近似的效果。同时还可以通过在特定任务上对其他模型进行微调来提高它们的性能。

## Davinci

`Davinci`是GPT-3系列中最强大的模型，可以在很少指引的情况下完成其他模型能完成的任何任务。对于需要大量理解内容的应用，如针对特定受众的摘要生成和创造性内容生成，`Davinci`的产生效果最佳好。当然，这些优势需要更多的计算资源，因此`Davinci`每次API调用的成本更高，而且速度也不如其他模型。

`Davinci`的另一个亮点是理解文本的意图。`Davinci`非常擅长解决各种逻辑问题，并解释其中角色的动机。`Davinci`已经能够解决一些涉及因果关系的最具挑战性的人工智能问题。

擅长领域：**复杂意图理解、因果关系发现及理解、针对性摘要总结**

## Curie 

`Curie`也非常强大，同时速度也非常快。虽然`Davinci`在分析复杂文本时更具优势，但`Curie`在情感分类和总结摘要等许多细致任务上表现出色。`Curie`还非常擅长回答问题，因此非常适合作通用服务聊天机器人。

擅长领域：**翻译、摘要、复杂分类、文本情感**

## Babbage 

`Babbage`可以执行分类等简单任务。当涉及到语义搜索时，它也可以很好地对文档与搜索查询的匹配程度进行排序。

擅长领域：**文本分类、语义搜索分类**

## Ada 

`Ada`通常是速度最快的模型，可以执行解析文本、地址更正和粗放的分类任务。可以通过提供更多上下文来提升`Ada`的表现。

擅长：**文本解析、简单分类、地址更正、关键字提取**

> ⚠注意：高级模型都能完成低级模型能完成的任务，例如Ada能完成的工作，Curie和Davinci都能完成。
>
> GPT-3模型是非确定性的，这意味着相同的输入可以产生不同的输出。将`temperature` 设置为0将使输出大部分具有确定性，但仍可能存在少量可变性。
