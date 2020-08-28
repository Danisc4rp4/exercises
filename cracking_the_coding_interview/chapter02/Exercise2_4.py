# -*- coding: utf-8 -*-
import unittest
from Exercise2_1 import LinkedList, LinkedNode
            
        
def partition(linkedList, x):
    """
    @param x: the value for partition (int).
    @param linkedList: the linked list.
    @return: returns a list of values (int in this case). 
    """
    head = linkedList.head
    lower = []
    greaterEq = []
    while head:
        if head.val < x:
            lower.append(head.val)
        else:
            greaterEq.append(head.val)
        head = head.next
    return lower + greaterEq
    
    

class partitionTest(unittest.TestCase):
        
    def testPartition(self):
        """
            Test partition with value 2:
            1 -> 3 -> 1 -> 9 -> 3 -> 2 -> 1 -> 3 -> 5
            the list will become:
            1 -> 1 -> 1 -> 3 -> 9 -> 3 -> 2 -> 3 -> 5
            
        """
        head = LinkedNode(1)
        linkedList = LinkedList(head)
        linkedList.insert(3)
        linkedList.insert(1)
        linkedList.insert(9)
        linkedList.insert(3)
        linkedList.insert(2)
        linkedList.insert(1)
        linkedList.insert(3)
        linkedList.insert(5)
        
        self.assertEqual(partition(linkedList, 2), [ 1, 1, 1, 3, 9, 3, 2, 3, 5 ])
        

if __name__ == '__main__':
   unittest.main()
