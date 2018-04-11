# -*- coding: utf-8 -*-

import unittest
import word_search_hashset as hs


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
        self.tws = hs.WordSearch(self.COLS, self.ROWS)

    def test_buildSet(self):
        """
        test method WordSearch::buildSet()
        :return:
        """

        print("\n")
        print ("TEST: word_search_hashset::WordSearch::buildSet()")

        filename='word_search/test/res/input/test_words.txt'
        self.tws.buildSet(filename)

        # Success
        self.expectedResult = {'aardvark', 'aardvarks', 'abaci', 'aback', 'abacus'}
        self.assertItemsEqual(self.expectedResult,self.tws.wordSet)

        # Failure
        self.expectedResult = set()
        self.assertNotEquals(self.expectedResult, self.tws.wordSet)

    def test_generateBoard(self):
        """
        test method WordSearch::generateBoard()
        :return:
        """

        print("\n")
        print ("TEST: word_search_hashset::WordSearch::generateBoard()")

        self.tws.generateBoard()
        twsROWS = len(self.tws.board)
        twsCOLS = len(self.tws.board[0])

        # Success
        self.assertEquals(self.ROWS, twsROWS)
        self.assertEquals(self.COLS, twsCOLS)
