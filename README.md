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

- Run unit test with code coverage using [Coverage.py](https://coverage.readthedocs.io/en/coverage-4.5.1/)
```bash
# cd PROJECT_ROOT
coverage run --source=word_search/ -m unittest discover word_search/
coverage report
```

- Code coverage results
```
Name                                                             Stmts   Miss  Cover
------------------------------------------------------------------------------------
word_search/__init__.py                                              0      0   100%
word_search/test/__init__.py                                         0      0   100%
word_search/test/test_word_search_correctness_by_comparison.py      36      8    78%
word_search/test/test_word_search_hashset.py                        24      0   100%
word_search/test/test_word_search_trie.py                           15      0   100%
word_search/word_search_hashset.py                                 190     27    86%
word_search/word_search_trie.py                                    224     29    87%
------------------------------------------------------------------------------------
TOTAL                                                              489     64    87%
```

- Create source distribution
```bash
# cd PROJECT_ROOT
python setup.py sdist
```

-  Install package from [pypi.org/project/word-search](https://pypi.org/project/word-search/)
    ```bash
    pip install word_search --user
    ```
    or
    ```bash
    pip install word-search --user
    ```

-  Install package from this repository
	- Normal Install
	```bash
	# cd PROJECT_ROOT
	pip install . --user
	```

	- Development Install
	```bash
	# cd PROJECT_ROOT
	pip install -e . --user
	```

- Check package installation
    ```bash
    pip --user freeze | grep word_search
    ```

-  Uninstall package
    ```bash
    pip uninstall word_search
    ```
    or
    ```bash
    pip uninstall word-search
    ```

- For package usage see [client/client_example.py](client/client_example.py)
    ```python
    from word_search import word_search_hashset as hs
    from word_search import word_search_trie as ts
    ```


### References
- [Implementing a Trie in Python - towardsdatascience.com](https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1)
- [What is the best project structure for a Python application? - stackoverflow.com](https://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application)
  - [According to Jean-Paul Calderone's Filesystem structure of a Python project](https://stackoverflow.com/a/5998845/2105028)
  - [Open Sourcing a Python Project the Right Way](https://stackoverflow.com/a/19871661/2105028)
- [Package And Distribute Python Applications - digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-package-and-distribute-python-applications)
- [Python Packaging User Guide, Tool recommendations - packaging.python.org](https://packaging.python.org/guides/tool-recommendations/)
- [pypi](https://pypi.python.org/pypi) and [testpypi](https://testpypi.python.org/pypi)

<br/>
