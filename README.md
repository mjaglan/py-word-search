# Word Search

Python package that searches a 2D grid of randomly generated letters (a-z only) for valid English words. Words can be found along any diagonal, forwards, upwards, downwards or backwards and cannot ‘wrap’ between edges. To check if a word is valid, a list of words at [res/input/words.txt](res/input/words.txt) is used as a reference dictionary.


### Project Highlights

- Run source
```bash
# cd PROJECT_ROOT
# python  <module-filename>                    <word-list-file>      <cols>   <rows>
python    word_search/word_search_hashset.py   res/input/words.txt   15       15
python    word_search/word_search_trie.py      res/input/words.txt   15       15
```

- Run unit test
```bash
# cd PROJECT_ROOT
python -m unittest discover word_search/
```

