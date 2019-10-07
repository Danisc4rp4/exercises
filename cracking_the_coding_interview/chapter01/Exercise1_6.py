# -*- coding: utf-8 -*-
import unittest

def stringCompression(stringToCompress=[]):
    """
    Implement a method to perform basic string compression using the counts of
    repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.
    If the "compressed" string would not become smaller than the original string,
    your method shold return the original string. You can assume the string has only 
    uppercase and lowercase letters (a - z).
    @param aString: first string.
    @return: returns the compressed string.
    """
    previouslyChecked = None
    compressedString = ""
    seenTimes = 0
    for charToCheck in stringToCompress:
        if charToCheck != previouslyChecked:
            compressedString += (seenTimes > 1 and str(seenTimes) or '') + charToCheck
            seenTimes = 1
        else:
            seenTimes += 1
        previouslyChecked = charToCheck
    compressedString += seenTimes > 1 and str(seenTimes) or ''
    return len(compressedString) < len(stringToCompress) and compressedString or stringToCompress


class StringCompressionTest(unittest.TestCase):
    def testStringCompression(self):
        self.assertEqual(stringCompression('aaabbbccc'),'a3b3c3')
        self.assertEqual(stringCompression('aabbcc'), 'aabbcc')
        self.assertEqual(stringCompression('aabbc'), 'aabbc')


if __name__ == '__main__':
   unittest.main() 
