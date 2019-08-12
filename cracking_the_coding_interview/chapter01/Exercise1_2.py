# -*- coding: utf-8 -*-
import unittest

def checkPermutation(first, second):
    """
    Given two strings, write a method to decide if one is a permutation 
    of the other.
    @param first: string.
    @param second: the second string to compare.
    @return: boolean, true if the second string is a permutation of the first.  
    """
    # if the strings have different lenght, than for sure one is not the
    # permutation of the other.
    if len(first)!=len(second):
        return False
    # If one string is the permutation of the other, then the 
    # sorted strings are identical. Complexity is O(nlogn) as
    # the complexity of sorted().
    return sorted(first) == sorted(second)

class IsUniqueTest(unittest.TestCase):
    def testIsUnique(self):
        self.assertEqual(checkPermutation('aaabbbccc', 'abcabcabc'), True)
        self.assertEqual(checkPermutation('aaabbbccc', 'abcabcabcz'), False)


if __name__ == '__main__':
   unittest.main()