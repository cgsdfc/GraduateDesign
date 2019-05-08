# Conclusions
- Recall plays a more important role than precision in obtaining
high-levels of correlation with human judgement.
- Current level of correlation at the sentence level are still rather low.

# Contributions
- previous analysis focused on correlation on *system level*.
We focus on improving correlation on *segment level*.

# Future Work
- In the process of exploring several further enhancements to the current metric.

# Weakness in BLEU
- Main principle: the measurement of the overlap in unigrams (single words) and
higher order n-grams of words, between a translation and a set of references.
- Main component: n-gram precision: the proportion of the matched n-grams out of the total number of n-grams in the *evaluated translation*.

* The Lack of Recall

Brevity penalty does not compensate for the lack of recall

* Use of Higher Order N-grams

BLEU uses higher order n-grams to indirectly measure
the level of grammatical well-formedness.
Grammaticality (or word order) should be measured explicitly.

- Lack of Explicit Word-matching Between Translation and Reference
- Use of Geometric Averaging of N-grams

This problem was observed when I am working on its impl.
This section shares a lot of common though with me on the illness of BLEU.

# Importance of Recall
- Recall is the proportion of the matched n-grams out of the total number of
the n-grams in *the reference translation*.
- it reflects to what degree the translation covers the entire content of the translated sentence.

# Details of Meteor
- based on explicit word-to-word matches between the translation and a reference translation.
- If more than one reference translation is available, the given translation is scored against each reference independently, and the best score is reported.
- create an alignment between two strings.
- This alignment is incrementally produced
through a series of stages, each stage consisting of
two distinct phases.

# Flexibility
- Number of stages.
- Actual external mapping module used for each stage.
- Order in which the stages are run.

# Default Config
1. exact
2. porter stem
3. WN synonymy

[Turian 2003]()

# Final Score Formula

# Code!!
http://www.cs.cmu.edu/~alavie/METEOR/

https://github.com/mjdenkowski/meteor.git

https://github.com/cmu-mtlab/meteor.git

Document:
http://www.cs.cmu.edu/~alavie/METEOR/README.html

# Bundle with nlg-eval
https://github.com/cgsdfc/nlg-eval.git
