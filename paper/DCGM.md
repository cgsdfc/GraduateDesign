# MetaInfo
- title: A neural network approach to context-sensitive generation of conversation responses
- author: Sordoni

# Contribution
- train end-to-end on unstructured Twitter data.
- using NN to address sparsity problem when integrating context.
- dynamic-context generative model.
- data-driven.

**First Application of a neural network model to open-domain response generation.**

- a multi-reference extraction technique that shows promise for 
automated evaluation. (Metrics)

# Background
- vast quantities of conversational exchanges become available on social media
such as Twitter and Reddit, giving rise to data-driven models.

# Related Works
- [Ritter 2011](../bib_db/model/ritter/Ritter2011.bib) constructs a statistical machine translation system  from Twitter Corpus to generate response from a status post.
- Drawback: responses are *not* sensitive to context. (not context-sensitive)

# What is a context
- Linguistic context, *not* physical one.

# Benefits
- Context is important: 
    * the ability to take into account previous utterances is key to building dialog systems that can keep conversations active and engaging.
- Embedding-based model:
    * model the transition between consecutive utterances.
    * capture long-span dependency.
- Robustness to sparsity:
    * capture context info while avoiding unmanageable growth of model parameters.
   
# Challenges
- Context info is hard for the MT model to capture.
- Naive injection of context is unmanageable due to data sparsity.

# Solutions
- Using embeddings for words and phrases. (Benefits of Word Embeddings)
    * compactly encode semantic and syntactic similarity.
    * address the sparsity problem.

# Models
- simple, context-sensitive, response-generation models.
- first encode past info into continuous representation and then decode it using RLM.
- completely data-driven.
- no human annotation is needed.
- As opposed to: typical complex task-oriented multi-modular dialog system.

   
*a line of though:* Although the training is nearly free of human annotation, the evaluation of such system relies heavily on human evaluation. The training of task-oriented system relies on human annotation but its evaluation is more supervised. One cannot gain both sides of goodness.

## Recurrent Language Model (RLM)
- benefits of using an RLM:
    * plausible
    * fluent
    * contextual relevant
- proposer:[Mikolov 2010](../bib_db/basic/mikolov/MikolovKBCK10.bib), Recurrent neural network based language model.
    
## Multi-modular Dialog System
* [Young 2002](../bib_db/model/traditional_dialog/young/Young02.bib) (Talking to machine)
* [Stent and Bangalore 2014](../bib_db/model/traditional_dialog/stent/SB2014.bib) (book: Natural Language Generation in Interactive Systems)
* requires human annotation.
* task-oriented.
* complex.

# Related Works
## Radical paradigm shift
- Accomplish both task jointly.
- latent dialog state.
- optimize directly to end-to-end performance.
- data-driven.

## Traditional Dialog System
- tease apart dialog management from response generation. (Young, Stent).
- hand-coded many components.
- labels and attributes defining dialog states.

## Previous uses of ML
- response generation, [Walker 2003]()
- dialog state tracking,[Young 2010]()
- user modeling, [Georgila 2006]()

## Application of word embeddings
- IR:
    * [Huang 2013]()
    * [Shen 2014]()
    * 
- Online Recommendation: [Gao 2014b]()
- MT:
    * [Auli 2013]()
    * [Cho 2014]()
    * [Kalchbrenner and Blunsom 2013]()
    * [Sutskever 2014](../bib_db/model/sutskever/SutskeverVL14.bib)
    * 
- Language Modeling LM:
    * [Bengio 2003]()
    * [Collobert and Weston 2008]()


