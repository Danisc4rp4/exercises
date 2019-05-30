# -*- coding: utf-8 -*-

def isUnique(s):
    """
    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?
    """
    visited = {}
    for ch in s:
        if not visited.get(ch):
            visited[ch] = True
        else:
            return False
    return True

if __name__ == '__main__':
    print isUnique('łlo')