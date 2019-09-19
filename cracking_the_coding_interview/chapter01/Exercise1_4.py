# -*- coding: utf-8 -*-
import unittest

def isPermutationOfPalindrome(word):
    """
    Given a string, write a function to check if it is a permutation of
    a palindrome. A palindrome is a word or phrase that is the same
    forwards and backwards. A permutation is a rwearrangement of letters.
    A palindrome does not need to be limited to just dictionary words.
    @param s: string.
    @return: returns True if the string is a permutation of a palindrome,
    False otherwise.  
    """
    word = sorted(word)
    map = {}
    for ch in word:
        if map.get(ch):
            map[ch] = 0
        else:
            map[ch] = 1
    if len(word)%2:
        return len([map[k] for k in map if map[k]]) == 1
    return not [map[k] for k in map if map[k]]
    

class IsPermutationOfPalindromeTest(unittest.TestCase):
    def testIsPermutationOfPalindrome(self):
        self.assertEqual(isPermutationOfPalindrome('afygyuygyfadu'), True)


if __name__ == '__main__':
   unittest.main()