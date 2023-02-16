# 频率惩罚

## 概要

频率惩罚介于-2.0和2.0之间，它影响**模型如何根据文本中词汇（token）的现有频率惩罚新词汇（token）**。

正值将通过惩罚已经频繁使用的新词汇来降低模型**一行中重复用词**的可能性。

存在惩罚是种一次性的附加效用，作用于至少采样一次的所有token；而频率惩罚则与特定token的采样频率成比例地发挥作用。

为了稍微减少输出中的重复词语，惩罚系数的合理值通常约为0.1至1。

如果目标是显著抑制重复，系数可以增加到2，但这可能会对输出的质量产生负面影响。

相反，使用负值可以增加重复的可能性。

## 频率惩罚对生成文本多样性和创意性的影响

频率惩罚参数控制GPT-3模型生成文本的“**多样性**”。通过该参数可以调节生成文本的**似然度**与**新颖度**。

GPT-3和其他语言模型一样，使用**概率分布**来预测给定提示的下一个词。频率惩罚参数修改该分布，使模型在其训练期间更频繁地看到的不同的词，从而鼓励模型生成新颖或不太常见的词。

实际工作中，频率惩罚作为缩放因子作用于模型预测的对数概率上，形式如下：

$$
(1 – frequency_penalty) * log_probability
$$

* 当频率惩罚为0时，模型的行为不受影响；
* 当频率惩罚为1时，训练过程中看到的任何词汇都不会用到，从而生成完全新颖的或随机的文本；
* 当频率惩罚介于0和1之间时，模型会在熟悉词和新颖词之前取得平衡。

通常，频率惩罚的默认值为0，当你希望生成与模型训练时使用的文本类似的文本时使用该值。

另一方面，如果你希望模型生成更多样化和更少重复的文本，你可以使用更大频率惩罚，这将鼓励模型减少常用词的使用，并降低生成常见短语的可能性。

## 与存在惩罚的区别

这两个参数之间的主要区别在于它们修改模型预测概率分布的方式不同。

频率惩罚参数修改概率分布，以生成模型在训练过程中不常见的词。这鼓励模型生成新颖或不太常见的词。它的工作原理是缩放模型在训练过程中常见词的对数概率，从而降低模型生成这些常见词的可能性。

而存在惩罚参数修改概率分布，以使输入提示中出现的词不太可能出现在输出中。这鼓励模型生成输入中没有的词。它的工作原理是缩放输入中存在词的对数概率，使模型不太可能生成输入中已经存在的单词。

简单地说，频率惩罚控制模型输出用词的新颖性，而存在惩罚控制模型谈论新主题的可能性。

总之，这两个参数都可以用于增加生成文本的多样性，并鼓励模型生成更多新颖或意外的词。但它们以不同的方式实现，并且取决于用例和具体要求，一个可能比另一个更有益，或者它们可以一起用于控制生成的文本多样性。