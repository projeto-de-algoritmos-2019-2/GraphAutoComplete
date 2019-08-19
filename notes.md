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

	-> [Prefix tree] Typically many vocabulary words begin with 
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

## Links
	- https://www.futurice.com/blog/data-structures-for-fast-autocomplete/
	- http://blog.notdot.net/2007/4/Damn-Cool-Algorithms-Part-1-BK-Trees
	- http://blog.notdot.net/2010/07/Damn-Cool-Algorithms-Levenshtein-Automata
	- http://sujitpal.blogspot.com/2007/02/three-autocomplete-implementations.html
	- http://dhruvbird.blogspot.com/2010/09/very-fast-approach-to-search.html