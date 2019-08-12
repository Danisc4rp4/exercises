# -*- coding: utf-8 -*-
import unittest

def URLify(s, l):
    """
    Write a method to replace all spaces in a string with '%20'. You may assume that 
    the string has sufficient space at the end to hold the additional characters, and
    that you are given the "true" length of the string.
    @param s: string.
    @param l: length of the string.
    @return: the string with spaces replaced by '%20'.  
    """
    if l==0:
        return ''
    if s[0] == ' ':
        return '%20' + URLify(s[1:], l-1)
    return s[0] + URLify(s[1:], l-1)


class URLifyTest(unittest.TestCase):
    def testURLify(self):
        self.assertEqual(URLify('test this one  ', 13), 'test%20this%20one')


if __name__ == '__main__':
   unittest.main()