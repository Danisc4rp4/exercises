# -*- coding: utf-8 -*-
import unittest

def stringRotation(string1, string2):
    """
    ..
    @param string1: the first string.
    @param string1: the second string, rotation of the first string or not.
    @return: returns true if the second string is a rotation, false otherwise.
    """
    string2Len = len(string2)
    if len(string1) != string2Len:
        return False
    for string2Index in range(string2Len):
        if string1 == string2[string2Index:] + (string2Index and string2[:string2Index] or ""):
            return True
    return False

class StringRotationTest(unittest.TestCase):
    def testStringRotation(self):
        self.assertEqual(stringRotation("Daniela", "laDanie"), True)
        self.assertEqual(stringRotation("Daniela", "laDani"), False)
        self.assertEqual(stringRotation("Daniela", "laDanii"), False)
        

if __name__ == '__main__':
   unittest.main() 
