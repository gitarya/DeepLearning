<h3>Introduction</h3>
This project is all about operations on word vectors including cosine similarity, word analogy and debiasing word vectors.
该文件关注词向量相关的操作。包括计算cosine相似度，词分析和词向量去偏

<h3>Content</h3>
**Cosine similarity**
Cosine similarity help to measure how similar two words are. This idea comes from GloVe algorithm.
Cosine similarity是用来衡量两个单词之间的相似度的标准。这是来自GloVe算法中的概念。

The formula is:
$$\text{CosineSimilarity(u, v)} = \frac {u . v} {||u||_2 ||v||_2} = cos(\theta) \tag{1}$$



**Word analogy**
In the word analogy function, we complete the sentence "a is to b as c is to __". For example , man is to woman as boy is to girl.
词分析主要解决类比关系的关系。比如说，A跟B的关系关系好比C跟__的关系。__中的应该填的对应的词就是这个功能需要找到的内容。举例，男人与女人这对词对应的是男孩和女孩。


**Debiasing word vectors**