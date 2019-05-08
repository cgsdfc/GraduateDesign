# Name
Referenced metric and Unreferenced metric Blended Evaluation Routine

# Advantages
- Both generative and retrieval dialog system can be evaluated with high human correlation.
- Don't need any human annotation. Train in a unsupervised way. 
- Fair transferability over different open domain dataset.
- Significantly outperform existing automatic evaluation metrics.

# Setup
- Dataset: Douban, 1,449,218 samples, each of which consists of a
query-reply pair (in text)
- Embedding: In the referenced metric, we
train 50-dimensional word2vec embeddings on the
Douban dataset.
- optimizer: Adam
- 

# Formula
```latex

Sentence embedding of the referenced metric is:
\begin{align}
    \vec{v}_{max}\[i\] = \max \left\{ \vec{w}_1\[i\], \vec{w}_2\[i\], \cdots, \vec{w}_n\[i\]\right\}
\end{align}

Referenced metric is:
\begin{align}
    s_R(r, \hat{r}) = \cos\left( \vec{v}_r, \vec{v}_{\hat{r}} \right) = \frac{\vec{v}_r^T\vec{v}_{\hat{r}}}{||\vec{v}_r||\cdot||\vec{v}_{\hat{r}}||}
\end{align}

The forward RNN takes the form:
\begin{align}
    \[\vec{r}_r;\vec{z}_t\] &= \sigma\left( W_{r,z}\vec{x}_t + U_{r,z}\vec{h}^{\rightarrow}_{t-1} + \vec{b}_{r,z} \right) \\
    \tilde{\vec{h}}_t &= \tanh\left( W_h \vec{x}_t + U_h(\vec{r}_t \circ \vec{h}^{\rightarrow}_{t-1}) + \vec{b}_h \right) \\
    \vec{h}_t^{\rightarrow} = (1-\vec{z}_t) \circ \vec{h}^{\rightarrow}_{t-1} + \vec{z}_t \circ \tilde{\vec{h}}_t
\end{align}

Training objective of unreferenced metric:
\begin{align}
    J = \max{0, \Delta - s_U(q, r) + s_U(q, r^-)}
\end{align}

Normalize each metric to (0, 1)
\begin{align}
    \tilde{s} = \frac{s-\min(s')}{\max(s') - \min(s')}
\end{align}

Finally, 2 metrics are combined using heuristics including $\min$, $\max$, geometric averaging and arithmetic averaging.

```

# Our training data
