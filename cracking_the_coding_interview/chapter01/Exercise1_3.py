# -*- coding: utf-8 -*-
import unittest

def URLify(s, l):
    """
    Complexity is O(n)
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