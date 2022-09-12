# Network Studies

This repository contains the report regarding the network of words. Every word has a definition, but only a few words are often needed to understand more complex definitions. As such, this project studies how the definitions of words are connected with one another using network theory. 

The definitions of words have been scraped using the BeautifulSoup library in Python, and the definitions of the words used in the definitions are again recursively scraped. This recursion has a depth of 50. If the definition of word A uses word B, then our network consists of a directed edge pointing from A to B (A -> B). The results are saved in a json file and plotted using a software for network studies known as Gephi. Definitions of words have been scraped off of vocabulary.com
Of course, words (prepositions) such as "the", "a", "an" and "of" are excluded as their definitions do not provide value to our study.

The project tries to apply our findings to design an English curriculum for foreign learners of the English language. Using common words which are necessary for performing in certain jobs which are highly concentrated in foreign workers, we try to design a way to discover which words are important to understanding these important vocabulary words. 
Some words are found to be important as many other words use it to define their meanings. Others find importance by being the bridge to understanding an important word.

You can read our findings in the file titled "Network of Words - Designing an English Curriculum".
