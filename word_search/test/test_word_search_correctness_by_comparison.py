# -*- coding: utf-8 -*-

import unittest
import word_search_hashset as hs
import word_search_trie as ts


class TestWordSearch(unittest.TestCase):
    """
    Test class for WordSearch
    """

    def setUp(self):
        """
        Initialize objects.
        :return:
        """
        self.ROWS = 5
        self.COLS = 7

        self.tws = ts.WordSearch(self.COLS, self.ROWS)
        self.hws = hs.WordSearch(self.COLS, self.ROWS)

        filename = 'word_search/test/res/input/test_words_large.txt'
        self.tws.buildSet(filename)
        self.hws.buildSet(filename)

        # Keep same N x M Grid
        self.tws.generateBoard()
        self.hws.board = self.tws.board

    def test_correctness_by_comparison(self):
        """
        Compare results of getValidWords() by each module: word_search_hashset and word_search_trie.
        :return:
        """
        print("\n")
        print ("TEST: word_search_trie vs word_search_hashset")

        result_set_hash = self.hws.getValidWords()
        result_set_trie = self.tws.getValidWords()

        self.assertItemsEqual(result_set_hash, result_set_trie)

        in_trie_set = set()
        in_hash_set = set()

        print("\n")
        print ("TRIE: total %d words found" % (len(result_set_trie)))
        print ("HASH: total %d words found" % (len(result_set_hash)))

        if result_set_trie != result_set_hash:
            in_trie_set = result_set_trie - result_set_hash
            in_hash_set = result_set_hash - result_set_trie

        if len(in_trie_set) > 0:
            print '{:15} {:10} {:10}'.format("WORD", "in-TRIESET", "in-HASHSET")
            for i in in_trie_set:
                print '{:15s} {:10} {:10}'.format(i, str(self.tws.isValid(i)), str(self.hws.isValid2(i)))

        if len(in_hash_set) > 0:
            print '{:15} {:10} {:10}'.format("WORD", "in-TRIESET", "in-HASHSET")
            for i in in_hash_set:
                print '{:15s} {:10} {:10}'.format(i, str(self.tws.isValid(i)), str(self.hws.isValid2(i)))
