# -*- coding: utf-8 -*-
import unittest
from utils.LinkedNode import LinkedNode
        
def removeDups(head):
    """
    ...
    @param linkedList: the linked list.
    @return: returns the linked list without duplicates
    """
    valMap = set()
    current = head
    prev = None
    while current:
        if head.val in valMap:
            prev.next = current.next
        else:
            valMap.add(head.val)
            prev = current
        current = current.next

def getAsList(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


class RemoveDupsTest(unittest.TestCase):
        
    def testremoveDups(self):
        """
            Test remove duplicates with these values:
            1 -> 3 -> 1 -> 9 -> 3 -> 2 -> 1 -> 3 -> 5
            result should be:
            1 -> 3 -> 9 -> 2 -> 5
            
        """
        n1 = LinkedNode(1)
        n2 = LinkedNode(1)
        n3 = LinkedNode(1)
        n4 = LinkedNode(1)
        n5 = LinkedNode(1)
        n6 = LinkedNode(1)
        n7 = LinkedNode(1)
        n8 = LinkedNode(1)
        n9 = LinkedNode(1)
        
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        n5.next = n6
        n6.next = n7
        n7.next = n8
        n8.next = n9

        removeDups(n1)
        
        self.assertEqual(getAsList(n1), [1])
        

if __name__ == '__main__':
   unittest.main() 
