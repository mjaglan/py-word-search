# -*- coding: utf-8 -*-

import unittest
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

    def test_generateBoard(self):
        """
        test method WordSearch::generateBoard()
        :return:
        """

        print("\n")
        print ("TEST: word_search_trie::WordSearch::generateBoard()")

        self.tws.generateBoard()
        twsROWS = len(self.tws.board)
        twsCOLS = len(self.tws.board[0])

        # Success
        self.assertEquals(self.ROWS, twsROWS)
        self.assertEquals(self.COLS, twsCOLS)
