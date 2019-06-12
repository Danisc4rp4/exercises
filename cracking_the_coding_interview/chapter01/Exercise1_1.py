# -*- coding: utf-8 -*-
import unittest

def getVal(ch):
    return ord(ch)

def isUnique(s):
    """
    Implement an algorithm to determine if a string has all unique characters.
    This method is able to check unicode strings.
    """
    # First I create a integer (32 bit) zero (32 zero bits).
    checker = 0
    for ch in s:
        # for each character i shift the 1 as many times as the value of
        # the char, calculated as for the getVal method.
        check = (1 << getVal(ch))
        # if checker and check > 0 means that that the one has been
        # shfted already the same positions, that means that the 
        # same letter has been found previously. In this case the 
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
        self.assertEqual(isUnique('thisłopn'), True)
        self.assertEqual(isUnique('1jehwkua764392'), True)
        self.assertEqual(isUnique('1jehwkua76439211'), False)

if __name__ == '__main__':
    unittest.main()
