# -*- coding: utf-8 -*-
import unittest

def stringCompression(stringToCompress):
    """
    O(n)
    @param aString: first string.
    @return: returns the compressed string.
    """
    if not len(stringToCompress):
        return ""
    firstChar = stringToCompress[0]
    last = 0
    while last < len(stringToCompress) and stringToCompress[last] == firstChar:
        last += 1 
    return firstChar + str(last) + stringCompression(stringToCompress[last:])
    

class StringCompressionTest(unittest.TestCase):
    def testStringCompression(self):
        self.assertEqual(stringCompression('aaabbbccc'),'a3b3c3')
        self.assertEqual(stringCompression('aabbcc'), 'a2b2c2')
        self.assertEqual(stringCompression('aabbc'), 'a2b2c1')


if __name__ == '__main__':
   unittest.main() 
