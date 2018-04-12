package: word_search

GitHub: https://github.com/mjaglan/py-word-search

Python package that searches a 2D grid of randomly generated letters (a-z only) for valid English words. Words can be found along any diagonal, forwards, upwards, downwards or backwards and cannot ‘wrap’ between edges. To check if a word is valid, a list of words at res/input/words.txt is used as a reference dictionary.


How to run?

from word_search import word_search_hashset as hs

from word_search import word_search_trie as ts

Refer client/client_example.py in GitHub at

https://github.com/mjaglan/py-word-search/blob/master/client/client_example.py

to see an example program.
