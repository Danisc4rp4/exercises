# -*- coding: utf-8 -*-
import unittest
from Exercise2_1 import LinkedList, LinkedNode
            
        
def deleteMiddleNode(linkedList):
    """
    @param linkedList: the linked list.
    """
    head = linkedList.head
    prev = None
    next = None
    if not head.next or not head.next.next:
        return
    while head.next and head.next.next:
        prev = head
        next = head.next.next
        head = head.next
    prev.next = next
    
    

class DeleteMiddleNodeTest(unittest.TestCase):
        
    def testDeleteMiddleNode(self):
        """
            Test delete node in the middle, not first or last:
            1 -> 3 -> 1 -> 9 -> 3 -> 2 -> 1 -> 3 -> 5
            the list will become:
            1 -> 3 -> 1 -> 9 -> 3 -> 2 -> 1 -> 5
            
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

        deleteMiddleNode(linkedList)
        
        self.assertEqual(str(linkedList), '13193215')
        

if __name__ == '__main__':
   unittest.main()
