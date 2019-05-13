# Cornell Conversational Analysis Toolkit ([ConvoKit](http://convokit.cornell.edu/))
This toolkit contains tools to extract conversational features and analyze social phenomena in conversations.  Several large [conversational datasets](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit#datasets) are included together with scripts exemplifying the use of the toolkit on these datasets.

The toolkit currently implements features for:

- [Linguistic coordination](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/Coordination_README.md), a measure of linguistic influence (and relative power) between individuals or groups based on their use of function words (see the [Echoes of Power](https://www.cs.cornell.edu/~cristian/Echoes_of_power.html) paper). Example script [exploring the balance of power in the US Supreme Court](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/examples/coordination/examples.ipynb).

- [Politeness strategies](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/Politeness_README.md), a set of lexical and parse-based features correlating with politeness and impoliteness (see the [A computational approach to politeness](https://www.cs.cornell.edu/~cristian/Politeness.html) paper).  Example script for [understanding the (mis)use of politeness strategies in conversations gone awry on Wikipedia](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/examples/conversations-gone-awry/Conversations%20Gone%20Awry%20Prediction.ipynb).

- [Question typology](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/QuestionTypology_README.md), an unsupervised method for extracting surface motifs that recur in questions, and for grouping them according to their latent rhetorical role (see the [Asking too much](http://www.cs.cornell.edu/~cristian/Asking_too_much.html) paper).  Example scripts for extracting common question types in the [UK parliament](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/examples/question-typology/parliament_question_typology.py), on [Wikipedia edit pages](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/examples/question-typology/wiki_question_typology.py), and in [sport interviews](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/examples/question-typology/tennis_question_typology.py).

- [Conversational prompts](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/QuestionTypology_README.md), an unsupervised method for extracting types of conversational prompts (see the [Conversations gone awry](http://www.cs.cornell.edu/~cristian/Conversations_gone_awry.html) paper).  Example script for [understanding the use of conversational prompts in conversations gone awry on Wikipedia](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/examples/conversations-gone-awry/Conversations%20Gone%20Awry%20Prediction.ipynb).

- [Hypergraph conversation representation](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/hyperconvo_README.md) (beta), a method for extracting structural features of conversations through a hypergraph representation (see the [Patterns of Participant Interactions](http://www.cs.cornell.edu/~cristian/Patterns_of_participant_interactions.html) paper). Example script demonstrates [hypergraph creation and feature extraction, visualization and interpretation](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/examples/hyperconvo/demo.ipynb).

- Coming soon: Basic message and turn features, currently available here [Constructive conversations](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/tree/constructive/cornellversation/constructive)

## Datasets
These datasets are included for ready use with the toolkit:

- [Conversations Gone Awry Corpus](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/datasets/conversations-gone-awry-corpus/awry.README.v1.00.txt): a collection of conversations from Wikipedia talk pages that derail into personal attacks (1,270 conversations, 6,963 comments). `convokit.download("conversations-gone-awry-corpus")`

- [Tennis Corpus](http://www.cs.cornell.edu/~liye/tennis_README.txt): transcripts for tennis singles post-match press conferences for major tournaments between 2007 to 2015 (6,467 post-match press conferences). `convokit.download("tennis-corpus")`

- [Wikipedia Talk Pages Corpus](http://www.cs.cornell.edu/~cristian/Echoes_of_power_files/wikipedia.talkpages.README.v1.01.txt): collection of conversations from Wikipedia editors' talk pages. `convokit.download("wiki-corpus")`

- [Supreme Court Corpus](http://www.cs.cornell.edu/~cristian/Echoes_of_power_files/supreme.README.v1.01.txt): collection of conversations from the U.S. Supreme Court Oral Arguments. `convokit.download("supreme-corpus")`

- [Parliament Corpus](http://www.cs.cornell.edu/~cristian/Asking_too_much_files/paper-questions.pdf): parliamentary question periods from May 1979 to December 2016 (216,894 question-answer pairs). `convokit.download("parliament-corpus")`

- [Reddit Conversations Corpus](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/tree/master/datasets/reddit-corpus) (beta): 99,145 Reddit conversations sampled from 100 subreddits. `convokit.download("reddit-corpus")`

These datasets can be downloaded using the `convokit.download()` [helper function](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/convokit/util.py).  Alternatively you can access them directly [here](http://zissou.infosci.cornell.edu/socialkit/datasets/).

## Data format

To use the toolkit with your own dataset, it needs to be in a standard json [format](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit/blob/master/Data_format.md).

## Installation
This toolkit requires Python 3.

1. Download the toolkit: `pip3 install convokit`
2. Download Spacy's English model: `python3 -m spacy download en`

Alternatively, visit our [Github Page](https://github.com/CornellNLP/Cornell-Conversational-Analysis-Toolkit) to install from source.

## Usage

See the example ipython notebooks linked above to familiarize yourself with how to use the different modules of the toolkit.  The basic process is:

1. `import convokit` into your python3 project.
2. Load a corpus of conversations using `corpus = convokit.Corpus(filename=...)`; use your own corpus or one of the ones provided with the toolkit.
3. Use convokit functionality to extract features from the conversations, for example `ps = convokit.PolitenessStrategies(corpus)` extracts the politeness strategies used in all the conversations. 
4. Have fun analyzing coversations.

## Documentation
Documentation is hosted [here](http://zissou.infosci.cornell.edu/socialkit/documentation/).

The documentation is built with [Sphinx](http://www.sphinx-doc.org/en/1.5.1/) (`pip3 install sphinx`). To build it yourself, navigate to `doc/` and run `make html`. 

## Acknowledgements

Andrew Wang ([azw7@cornell.edu](mailto:azw7@cornell.edu))  wrote the Coordination code and the respective example script, wrote the helper functions and designed the structure of the toolkit.

Ishaan Jhaveri ([iaj8@cornell.edu](mailto:iaj8@cornell.edu)) refactored the Question Typology code and wrote the respective example scripts.

Jonathan Chang ([jpc362@cornell.edu](mailto:jpc362@cornell.edu)) wrote the example script for Conversations Gone Awry.


[ConvoKit](http://convokit.cornell.edu/)
