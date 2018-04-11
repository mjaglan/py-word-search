# -*- coding: utf-8 -*-


"""
Approach:
- Build trie using words.txt file. This is our valid dictionary.
- Generate ROW X COL size grid using python lists. Assign random characters from (a-z) to each cell in this grid.
  - display the grid on terminal.
- From any location (i,j) in this grid, words can be formed in any of 8 directions by going to east, west, north,
  south, north-east, north-west, south-east, south-west.
  - for each string made check if it exists in the trie, i.e., if it is valid.
  - valid string will be added to result set, containing unique words.
  - display the result on terminal.
"""


import sys
import random
import datetime


class TrieNode(object):
    """
    Prefix trie implementation.
    """

    def __init__(self, char):
        """
        Initialize TrieNode object.
        :param char:
        """
        self.char = char
        self.children = []
        self.word_finished = False


class WordSearch(object):
    """
    Class that searches a grid of letters (a-z only) for valid English words. Words can be found along any diagonal,
    forwards, upwards, downwards or backwards and must not ‘wrap’ between edges.
    """

    def __init__(self, cols, rows):
        """
        Initialize WordSearch object.
        :param cols:
        :param rows:
        """
        self.cols = cols
        self.rows = rows
        self.cut_off = None
        self.wordSet = None
        self.board = None

    def add_word(self, word):
        """
        Adding a word in the trie structure
        """
        node = self.wordSet
        for char in word:
            found_in_child = False
            # Search for the character in the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # And point the node to the child that contains this char
                    node = child
                    found_in_child = True
                    break
            # We did not find it so add a new chlid
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                # And then point node to the new child
                node = new_node
        # Everything finished. Mark it as the end of a word.
        node.word_finished = True

    def buildSet(self, filename):
        """
        Pre-process input word list using simple TRIE.
        :param filename:
        :return:
        """
        self.cut_off = 0
        self.wordSet = TrieNode('*')
        # Read a Text File Line by Line Using an Iterator in Python
        fileObj = open(filename)
        for line in fileObj:
            line_cleaned = line.strip().lower()
            self.add_word(line_cleaned)
            n_line = len(line_cleaned)
            if n_line > self.cut_off:
                self.cut_off = n_line
        fileObj.close()

    def generateBoard(self):
        """
        Generate a board of random letters.
        :return:
        """
        print ("\n\n")
        print ("Board Size: %d X %d" % (self.rows, self.cols))
        alphabets="abcdefghijklmnopqrstuvwxyz"
        self.board = list()
        for i in xrange(self.rows):
            a_row = list()
            for j in xrange(self.cols):
                a_row.append(random.choice(alphabets))
            self.board.append(a_row)
            print (a_row)

    def isValid(self, word):
        """
        Check if a word exists in wordSet.
        :param word:
        :return:
        """
        prev = None
        node = self.wordSet
        # If the root node has no children, then return False.
        # Because it means we are trying to search in an empty trie
        if not node:
            return False
        for char in word:
            # Search through all the children of the present `node`
            if len(node.children) != 0:
                foundChar = False
                for child in node.children:
                    prev = child
                    if child.char == char:
                        # Assign node as the child containing the char and break
                        node = child
                        foundChar = True
                        break
                if not foundChar:
                    return False
            else:
                return False
        # Well, we are here means we have found the prefix. Return true to indicate that
        if word[-1] == prev.char and prev.word_finished == True:
            return True
        else:
            return False

    def getValidWords(self):
        """
        Identify all valid words in the board.
        :return:
        """
        result_set = set()
        for i in xrange(self.rows):
            for j in xrange(self.cols):
                # (i, j) new start point

                # East
                kC=j
                nC = min(self.cols, kC+self.cut_off)
                while(kC < nC):
                    # word = board[i][kC:nC]
                    q=kC
                    word = list()
                    while(q < nC):
                        word.append(self.board[i][q])
                        q+=1
                    word = "".join(word)
                    if (self.isValid(word)):
                        result_set.add(word)
                    nC -= 1

                # West
                kC=j
                nC = max(-1, kC-self.cut_off)
                while(kC > nC):
                    # word = board[i][kC:nC]
                    q=kC
                    word = list()
                    while(q > nC):
                        word.append(self.board[i][q])
                        q-=1
                    word = "".join(word)
                    if (self.isValid(word)):
                        result_set.add(word)
                    nC += 1

                # North
                kR=i
                nR = max(-1, kR-self.cut_off)
                while(kR > nR):
                    # word = board[kR:nR][j]
                    p=kR
                    word = list()
                    while(p > nR):
                        word.append(self.board[p][j])
                        p-=1
                    word = "".join(word)
                    if (self.isValid(word)):
                        result_set.add(word)
                    nR += 1

                # South
                kR=i
                nR = min(self.rows, kR+self.cut_off)
                while(kR < nR):
                    # word = board[kR:nR][j]
                    p=kR
                    word = list()
                    while(p < nR):
                        word.append(self.board[p][j])
                        p+=1
                    word = "".join(word)
                    if (self.isValid(word)):
                        result_set.add(word)
                    nR -= 1

                # North East
                kR=i
                kC=j
                nR = max(-1, kR-self.cut_off)
                nC = min(self.cols, kC+self.cut_off)
                while(kR > nR and kC < nC):
                    # word = board[kR:nR][kC:nC]
                    p=kR
                    q=kC
                    word = list()
                    while(p > nR and q < nC):
                        word.append(self.board[p][q])
                        p-=1
                        q+=1
                    word = "".join(word)
                    if (self.isValid(word)):
                        result_set.add(word)
                    nC -= 1
                    nR += 1

                # North West
                kR=i
                kC=j
                nR = max(-1, kR-self.cut_off)
                nC = max(-1, kC-self.cut_off)
                while(kR > nR and kC > nC):
                    # word = board[kR:nR][kC:nC]
                    p=kR
                    q=kC
                    word = list()
                    while(p > nR and q > nC):
                        word.append(self.board[p][q])
                        p-=1
                        q-=1
                    word = "".join(word)
                    if (self.isValid(word)):
                        result_set.add(word)
                    nC += 1
                    nR += 1

                # South East
                kR=i
                kC=j
                nR = min(self.rows, kR+self.cut_off)
                nC = min(self.cols, kC+self.cut_off)
                while(kR < nR and kC < nC):
                    # word = board[kR:nR][kC:nC]
                    p=kR
                    q=kC
                    word = list()
                    while(p < nR and q < nC):
                        word.append(self.board[p][q])
                        p+=1
                        q+=1
                    word = "".join(word)
                    if (self.isValid(word)):
                        result_set.add(word)
                    nC -= 1
                    nR -= 1

                # South West
                kR=i
                kC=j
                nR = min(self.rows, kR+self.cut_off)
                nC = max(-1, kC-self.cut_off)
                while(kR < nR and kC > nC):
                    # word = board[kR:nR][kC:nC]
                    p=kR
                    q=kC
                    word = list()
                    while(p < nR and q > nC):
                        word.append(self.board[p][q])
                        p+=1
                        q-=1
                    word = "".join(word)
                    if (self.isValid(word)):
                        result_set.add(word)
                    nC += 1
                    nR -= 1

        return result_set

    def display(self):
        """
        Print list of valid Words.
        :return:
        """
        result_set = self.getValidWords()
        print ("\n\n")
        print ("RESULT: total %d words found" % (len(result_set)))
        for word in result_set:
            print(word)


def printUsage():
    """
    Print program usage information.
    :return:
    """
    print("USAGE:")
    print("python   wordsearch.py   <word-list-file>   <cols>   <rows>")


def entryPoint():
    """
    Program Entry Point.
    :return:
    """
    start = datetime.datetime.now()
    fileName = cols = rows = None
    try:
        if len(sys.argv) == 4:
            fileName = sys.argv[1]
            cols = int(sys.argv[2])
            rows = int(sys.argv[3])
        elif len(sys.argv) >= 2 and sys.argv[1] == "--help":
            printUsage()
    except Exception as e:
        print(e)
        printUsage()

    tws = WordSearch(cols, rows)
    tws.buildSet(fileName)
    tws.generateBoard()
    tws.display()
    end = datetime.datetime.now()
    print("\n")
    print ("Execution Time (HH:MM:SS): %s" % (end - start))


if __name__ == '__main__':
    entryPoint()
