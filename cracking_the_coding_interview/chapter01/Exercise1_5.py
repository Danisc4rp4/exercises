# -*- coding: utf-8 -*-
import unittest

def firstOneAdd(w1, w2):
    """
    Determines wheter the first of the two strings has only one add compared
    to the second.
    """
    if len(w2) > len(w1):
        raise Exception("Wrong way to use this method!!!")
    found = False
    for index2 in range(len(w2)):
        gap = found and 1 or 0
        if w2[index2] != w1[index2 + gap]:
            if found:
                return False
            found = True
    return True


def oneAway(s1, s2):
    """
    O(n)
    @param s1: first string.
    @param s2: second string.
    @return: returns True if the second string is one or zero edits away from the first,
    False otherwise.  O(n)
    """
    n = len(s1)
    m = len(s2)
    lendiff = abs(n-m)
    if lendiff > 1:
        return False

    if not lendiff and s1 != s2:
        return False

    if lendiff:
        longer = n > m and s1 or s2
        shorter = n < m and s2 or s1
        return firstOneAdd(longer, shorter)

    return True
    

class OneAwayTest(unittest.TestCase):
    def testOneAway(self):
        self.assertEqual(oneAway('daniscarpa','daniscarpa'), True)
        self.assertEqual(oneAway('danisarpa','daniscarpa'), True)
        self.assertEqual(oneAway('daniiscarpa','daniscarpa'), True)
        self.assertEqual(oneAway('daniscarpa','daniscarpa'), True)


if __name__ == '__main__':
   unittest.main()