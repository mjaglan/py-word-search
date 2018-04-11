import datetime
from word_search import word_search_hashset as hs
from word_search import word_search_trie as ts

class ClientExample(object):
    """
    Test class for WordSearch
    """

    def __init__(self, filename, cols, rows):
        """
        Initialize objects.
        :return:
        """
        self.ROWS = rows
        self.COLS = cols
        self.filename = filename

    def demo_using_hashset(self):
        self.hws = hs.WordSearch(self.COLS, self.ROWS)
        self.hws.buildSet(self.filename)
        self.hws.generateBoard()
        result_set_hash = self.hws.getValidWords()
        print ("HASH: total %d words found -" % (len(result_set_hash)))
        print (sorted(result_set_hash))

    def demo_using_trie(self):
        self.tws = hs.WordSearch(self.COLS, self.ROWS)
        self.tws.buildSet(self.filename)
        self.tws.generateBoard()
        result_set_trie = self.tws.getValidWords()
        print ("TRIE: total %d words found -" % (len(result_set_trie)))
        print (sorted(result_set_trie))


def demo():
    """
    Program Entry Point.
    :return:
    """
    filename="res/input/words.txt"
    rows=15
    cols=15
    ce = ClientExample(filename, cols, rows)

    start_time_using_hashset = datetime.datetime.now()
    ce.demo_using_hashset()
    end_time_using_hashset = datetime.datetime.now()
    duration_using_hashset = "HASH SET Execution Time (HH:MM:SS): %s" % (end_time_using_hashset - start_time_using_hashset)

    start_time_using_trie = datetime.datetime.now()
    ce.demo_using_trie()
    end_time_using_trie = datetime.datetime.now()
    duration_using_trie = "TRIE SET Execution Time (HH:MM:SS): %s" % (end_time_using_trie - start_time_using_trie)

    print ("%s%s%s%s%s" % ("\n",duration_using_hashset,"\n",duration_using_trie,"\n"))


if __name__ == '__main__':
    demo()
