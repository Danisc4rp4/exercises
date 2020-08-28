# -*- coding: utf-8 -*-
import unittest
from Exercise2_1 import LinkedList, LinkedNode
            
        
def palindrome(linkedList):
    """
    @param linkedList: the linked list.
    @return: returns true if the list is palindrome, false otherwise.
    """
    head = linkedList.head
    listValues = []
    while head:
        listValues.append(head.val)
        head = head.next
    lenList = len(listValues)
    med = int(lenList / 2)
    return listValues[:med] == [listValues[i] for i in range(lenList - 1, med, -1)]
    
class palindromeTest(unittest.TestCase):
        
    def testPalindrome(self):
        """
            Test palindrome list:
            1 -> 3 -> 1 -> 9 -> 3 -> 9 -> 1 -> 3 -> 1
            will return true.
        """
        head = LinkedNode(1)
        linkedList = LinkedList(head)
        linkedList.insert(3)
        linkedList.insert(1)
        linkedList.insert(9)
        linkedList.insert(3)
        linkedList.insert(9)
        linkedList.insert(1)
        linkedList.insert(3)
        linkedList.insert(1)

        self.assertEqual(palindrome(linkedList), True) 


if __name__ == '__main__':
   unittest.main()
