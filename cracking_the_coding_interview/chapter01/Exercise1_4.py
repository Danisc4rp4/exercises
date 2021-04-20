# -*- coding: utf-8 -*-
import unittest

def isPermutationOfPalindrome(word):
    """
    O(n)
    @param s: string.
    @return: returns True if the string is a permutation of a palindrome,
    False otherwise.  
    """
    chmap = {}
    for ch in word:
        if ch in chmap:
            chmap[ch] += 1
        else:
            chmap[ch] = 1
    print(chmap)
    return len([chmap[el] for el in chmap if chmap[el]%2 > 0]) == len(word)%2
    

class IsPermutationOfPalindromeTest(unittest.TestCase):
    def testIsPermutationOfPalindrome(self):
        self.assertEqual(isPermutationOfPalindrome('aaaaffffddddc'), True)


if __name__ == '__main__':
   unittest.main()