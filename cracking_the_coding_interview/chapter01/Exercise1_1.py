# -*- coding: utf-8 -*-
import unittest
import sys

def getVal(ch):
    return ord(ch)

def isUnique(s):
    """
    O(n)
    @param s: unicode string.
    @return: boolean value, true if the unicode string does not contain 
    any repeated char. 
    """
    # First I create a bit array. The max length of a bit array in a 32bit
    # architecture is (2^32-1)/2.
    checker = 0
    for ch in s:
        # for each character i shift the 1 as many times as the value of
        # the char, calculated as for the getVal method.
        check = (1 << getVal(ch))
        # if checker && check > 0 means that the char has been
        # shifted already in the same position, and that means that the 
        # same letter occurred previously. In this case the 
        # string is not unique (return False).
        if (checker & check) > 0:
            return False
        # I update the checker with the new 1 in the position check 
        # (found using getVal).
        checker = checker | check

    return True


class isUniqueTest(unittest.TestCase):
    def testIsUnique(self):
        self.assertEqual(isUnique('thisisfalse'), False)
        self.assertEqual(isUnique('this��opn'), True)
        self.assertEqual(isUnique('1jehwkua764392'), True)
        self.assertEqual(isUnique('1jehwkua76439211'), False)


if __name__ == '__main__':
    unittest.main()
