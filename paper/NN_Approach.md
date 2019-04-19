# MetaInfo
- title: A neural network approach to context-sensitive generation of conversation responses

- author: Sordoni


# Contribution
- train end-to-end on unstructured Twitter data.
- using NN to address sparsity problem when integrating context.
- dynamic-context generative model.
- data-driven.

**First Application of a neural network model to open-domain response
generation.**

- a multi-reference extraction technique that shows promise for 
automated evaluation. (Metrics)

# Background
- vast quantities of conversational exchanges become available on social media
such as Twitter and Reddit, giving rise to data-driven models.

# Related Works
- Ritter 2011 constructs a statistical machine translation system  from Twitter Corpus to generate response from a status post.
- Drawback: responses are *not* sensitive to context. (not context-sensitive)

# What is a context
- Linguistic context, *not* physical one.

# Benefits
- Context is important: 
    * the ability to take into account previous utterances is key to building dialog systems that can keep conversations active and engaging.
- Embedding-based model:
    * model the transition between consecutive utterances.
    * capture long-span dependency.
    
# Challenges
- Context info is hard for the MT model to capture.
- Naive injection of context is unmanageable due to data sparsity.

# Solutions
- Using embeddings for words and phrases. (Benefits of Word Embeddings)
    * compactly encode semantic and syntactic similarity.
    * address the sparsity problem.

# Models
- simple, context-sensitive, response-generation models.
- first encode past info into continuous representation and then decode
it using RLM.
- completely data-driven.
- no human annotation is needed.
- As opposed to: typical complex task-oriented multi-modular dialog
system.

   
*a line of though:* Although the training is nearly free of human annotation, the evaluation of such system relies heavily on human evaluation. The training of task-oriented system relies on human annotation but its evaluation is more supervised. One cannot gain both sides of goodness.

## Recurrent Language Model (RLM)
- benefits of using an RLM:
    * plausible
    * fluent
    * contextual relevant
- proposer: Mikolov 2010, Recurrent neural network based language model.
    
## Multi-modular Dialog System
* Young 2002 (Talking to machine)
* Stent and Bangalore 2014 (book: Natural Language Generation in Interactive Systems)
* requires human annotation.
* task-oriented.
* complex.

