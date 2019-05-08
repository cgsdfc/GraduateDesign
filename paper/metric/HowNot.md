# Main Conclusions
Metrics adapted from MT suffer from:
- *very weak* correlation with human judgement on Twitter.
- *no* correlation at all on Ubuntu.

Note: these metrics generally compare a model's response to a single target response.


# Contribution
- highlight specific weaknesses in existing metrics.
- provide recommendations for future development of automatic metrics for dialogue system.

# Call to the Community
- shift away from these metrics.
- highlight the need for a new metric that correlates more strongly with human judgement.

# What is an unsupervised dialogue model
- supervised model: optimized for human-generated supervised signals, such as task-focused system.
- unsupervised model: supervised labels are unavailable, such as chatbot.

# Unsupervised Model
End-to-end training with neural networks:
- [Serban 2016](../../bib_db/model/serban/SerbanSBCP16%20HRED.bib)
- [Sordoni 2015](../../bib_db/model/sordoni/SordoniGABJMNGD15.bib)
- [Vinyals 2015](../../bib_db/model/vinyals/VinyalsL15.bib)

# Overlap-based Metrics
* MT
    - BLEU [papineni](../../bib_db/metric/BLEU.bib)
    - METEOR [Banerjee and Lavie](../../bib_db/metric/METEOR.bib)
* Summary
    - ROUGE [Lin](../../bib_db/metric/ROUGE.bib)

## Adopters of MT Metrics
- [Ritter et al., 2011](../../bib_db/model/ritter/Ritter2011.bib) 
- [Sordoni et al., 2015;](../../bib_db/model/sordoni/SordoniGABJMNGD15.bib) (a neural network approach) 
- [Li et al., 2015;](../../bib_db/model/jiwei/MMI.bib) (MMI)
- [Galley et al., 2015b;](../../bib_db/metric/DeltaBLEU.bib) 
- [Wen et al., 2015;](../../bib_db/dialog/wen/WenGMSVY15.bib) (applied LSTM to spoken dialog system)
- [Li et al., 2016;](../../bib_db/model/jiwei/persona.bib) (persona)

# Challenges
- automatically evaluate the quality of these models remains an open question.

# Benefits
- accelerate the deployment of unsupervised response generation systems.

# Components
- Studied Metrics
    - statistical word-overlap similarity metrics such as BLEU, METEOR and ROUGE.
    - word embedding metrics derived from `Word2Vec` [Mikolov 2013](../../bib_db/classic/mikolov/word2vec.bib)
- Datasets
    - chitchat oriented: Twitter dataset.
    - technical: Ubuntu Dialogue Corpus.
    
# Potential Problem of these Metrics
- These metrics assume valid responses have significant word overlap with the ground truth, which is too strong an assumption for dialogue systems.
- Significant diversity in the space of valid responses for dialogue systems.

# Related Work
- Word Perplexity 
    - the model generating the response also evaluate its quality.
    - not computed on a per-response basis.
    - [Serban 2015](../../bib_db/model/serban/SordoniBVLSN15.bib)
- Retrieval-based metrics (recall)
    - [Schatzmann 2005]()
    - [Lowe 2015]()
- Methods for supervised models
**Evaluation methods in the supervised setting have been well studied**.
    - [Walker 1997]()
    - [Moller 2006]()
    - [Jokinen and McTear 2009]()
    
# Problem Formulation
Given a dialogue context and a proposed response,
our goal is to automatically evaluate how appropriate the proposed response is to the conversation.

# Investigated Metrics
## Word based similarity metrics
Building block: the amount of _word-overlap_.

### BLEU
Studied by Galley in DeltaBLEU.


## Word-embedding based similarity metrics

# Statistical Analysis


# Qualitative Analysis

