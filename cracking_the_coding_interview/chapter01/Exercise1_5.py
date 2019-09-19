# -*- coding: utf-8 -*-
import unittest

def oneAway(s1, s2):
    """
    There are three types of edits that can be performed on strings: insert a
    character, remove a character, or replace a character. Given two strings,
    write a function to check if they are one edit (or zero edits) away.
    @param s1: first string.
    @param s2: second string.
    @return: returns True if the second string is one or zero edits away from the first,
    False otherwise.  
    """
    if s1 == s2:
        return True
    if len(s1) == len(s2):
        found = False
        for i, j in zip(s1, s2):
            if i != j:
                if found:
                    return False
                found = True
    else:
        ss1 = len(s1) > len(s2) and s1 or s2
        ss2 = len(s1) > len(s2) and s2 or s1
        if len(ss2) - len(ss1) > 1:
            return False
        found = False
        for i, j in zip(sorted(ss1), sorted(ss2)):
            if i != j:
                if found:
                    return False
                found = True
    return True
    

class OneAwayTest(unittest.TestCase):
    def testOneAway(self):
        self.assertEqual(oneAway('afygyuygyfadu','afygyuygifadu'), True)


if __name__ == '__main__':
   unittest.main()