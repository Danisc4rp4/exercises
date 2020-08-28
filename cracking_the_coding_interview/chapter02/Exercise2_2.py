# -*- coding: utf-8 -*-
import unittest
from Exercise2_1 import LinkedList, LinkedNode
            
        
def getKtoLast(linkedList, k):
    """
    @param linkedList: the linked list.
    @param k: integer, index of the first element to return.
    @return: returns a list of values (int in this case). 
    """
    head = linkedList.head
    ind = 1
    res = []
    while head:
        if ind >= k:
            res.append(head.val)
        ind += 1
        head = head.next
    return res
    

class GetKtoLastTest(unittest.TestCase):
        
    def testGetKtoLast(self):
        """
            Test get kth element of the single linked list to last:
            1 -> 3 -> 1 -> 9 -> 3 -> 2 -> 1 -> 3 -> 5 with k = 4
            result should be:
            9 -> 3 -> 2 -> 1 -> 3 -> 5
            
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
        
        self.assertEqual(getKtoLast(linkedList, 4), [ 9, 3, 2, 1, 3, 5 ])
        

if __name__ == '__main__':
   unittest.main()
