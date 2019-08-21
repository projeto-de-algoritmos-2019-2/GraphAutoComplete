An autocompleter can only suggest words that it knows about. 
The suggested words come from a predefined vocabulary, for 
example all distinct words in Wikipedia or in the Oxford 
English Dictionary.

The heart of an autocompleter is a function that takes in the 
beginning of a word, or a prefix, and searches for vocabulary 
words that start with the given prefix.

Searches for vocabulary words implementations:

	-> A naive implementation would iterate sequentially over the 
	vocabulary words checking each in turn to see if it starts 
	with the given prefix.

	-> [Binary Search] A better implementation keeps the 
	vocabulary words sorted  in alphabetical order. Searching for 
	a prefix in an ordered  vocabulary is pretty fast with the 
	help of a binary search algorithm.

	-> [Prefix tree - TRie] Typically many vocabulary words begin with 
	the same prefix (broccoli, broker, brother and many other 
	words all start with bro-). It seems wasteful to have to 
	store the common prefix separately for each word.

	-> [Minimizing a prefix tree DFA] Handle shared word parts 
	efficiently

	-> [Most valuable completions first] This can be achieved by 
	including an integer weight, which represents the value of a 
	word, for each word in the vocabulary, and by showing the 
	completions with the highest weight first.

	-> [Tolerate small spelling errors] Following not only the 
	exact path defined by a given prefix but also some neighboring 
	paths with minor spelling variations.

	-> [Add user words] Modifying the full data structure might 
	be too expensive, however. A solution is to keep two data 
	structures: one with a fixed global vocabulary and another 
	with that user's words. The latter is much smaller and 
	therefore faster to update.

	-> [Phrases] The search string is broken into tokens 
	determined by whitespace (each non-whitespace "word" is a 
	token)


## Ideas
	- Phrase suggestion
	- Word Correction
	- Next Word prediction
	- Phonetic Algorithms [Index words by sound]

## Algorithms
	- Word-partials (ngrams, Pattern Partitioning)
	- Phrase-terms (shingles)
	- Word-proximity (word-clustering-index)
	- Ternary-search-tree (word lookup)
	- Trees (prefix tree, suffix tree, dawg)
	- Soundex (sounds familiar)
	- Levenshtein distance (Steps to reach another word)
	- BK Trees (finding near-matches)
	- Markov Chain (predict next word based on previous words)

## Links
	- https://medium.com/related-works-inc/building-an-autosuggest-corpus-part-1-3acd26056708
	- https://medium.com/related-works-inc/building-an-autosuggest-corpus-nlp-d21b0f25c31b
	- https://medium.com/related-works-inc/autosuggest-retrieval-data-structures-algorithms-3a902c74ffc8
	- https://www.futurice.com/blog/data-structures-for-fast-autocomplete/
	- http://blog.notdot.net/2007/4/Damn-Cool-Algorithms-Part-1-BK-Trees
	- http://blog.notdot.net/2010/07/Damn-Cool-Algorithms-Levenshtein-Automata
	- http://sujitpal.blogspot.com/2007/02/three-autocomplete-implementations.html
	- http://dhruvbird.blogspot.com/2010/09/very-fast-approach-to-search.html
	- [Trie]				https://www.youtube.com/watch?v=-urNrIAQnNo
	- [AUTOSUGGEST]			https://medium.com/@giokincade
	- [Peter Norvig]		https://www.youtube.com/watch?v=yvDCzhbjYWs
	- [SPELL CORRECTION]	http://norvig.com/spell-correct.html
	- [WORD PREDICTION] 	https://yurichev.com/blog/markov/
	- [SPELL CORRECTION] 	https://en.wikipedia.org/wiki/Fat-finger_error
	- [Ternary Search Tree]	https://lukaszwrobel.pl/blog/ternary-search-tree/
	- [Ternary Search Tree]	https://github.com/djtrack16/tst/blob/master/ternarysearchtree.py
	- [Ternary Search Tree]	https://gist.github.com/dpapathanasiou/58919e4813e05850e201d21329d0139f
	- [Treap]				https://gist.github.com/IvanIsCoding/0abbe10dc8dc7cf330e410cf49875593
	- [Treap]				https://gist.github.com/IvanIsCoding/0abbe10dc8dc7cf330e410cf49875593
	- [Treap]				https://gist.github.com/irachex/3922705
	- [Treap]				http://www.grantjenks.com/wiki/random/python_treap_implementation
	- [Treap]				https://pypi.org/project/treap/


## Similar projects
	- https://github.com/weihesdlegend/Autocomplete-System
	- https://github.com/npgall/concurrent-trees
	- https://github.com/vivekn/autocomplete
	- https://github.com/rodricios/autocomplete
	- https://github.com/rrenaud/Gibberish-Detector
	- https://github.com/ashwinmj/word-prediction
