# Main Conclusion
Metrics adapted from MT suffer from:
- *very weak* correlation with human judgement on Twitter.
- *no* correlation at all on Ubuntu.

Note: these metrics generally compare a model's response to a
single target response.

# Methodology
- quantitative results.
- qualitative results.

# Contribution
- highlight specific weaknesses in existing metrics.
- provide recommendations for future development of
automatic metrics for dialogue system.

# What is an unsupervised dialogue model
- supervised model: optimized for human-generated supervised signals, such as task-focused system.
- unsupervised model: supervised labels are unavailable, such as chatbot.

# Unsupervised Model
- end-to-end training with neural networks.
- Serban 2016
- Sordoni 2015
- Vinyals 2015

# Metrics
* MT
    - BLEU papineni
    - METEOR Banerjee and Lavie
* Summary
    - ROUGE Lin

## Adopters
- Ritter et al., 2011; 
- Sordoni et al., 2015; (a neural network approach) 
- Li et al., 2015; (MMI)
- Galley et al., 2015b; 
- Wen et al., 2015; (applied LSTM to spoken dialog system)
- Li et al., 2016; (persona)

# Challenges
- automatically evaluate the quality of these models remains an open question.

# Benefits
- accelerate the deployment of unsupervised response generation systems.
