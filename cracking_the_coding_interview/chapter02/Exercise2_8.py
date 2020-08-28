# -*- coding: utf-8 -*-
import unittest
from Exercise2_1 import LinkedList, LinkedNode
            
        
def loopDetect(linkedList):
    """
    @param linkedList: the linked list.
    @return: returns the node where the loop starts.
    """
    head = linkedList.head
    seen = []
    while head:
        seen.append(head)
        if head.next in seen:
            return head.next
        head = head.next
    return None
    
class loopDetectTest(unittest.TestCase):
        
    def testLoopDetect(self):
        """
            Test loop detection:
            1 -> 3 -> 1 -> 9*** -> 3 -> 9 -> 1 -> 3 -> 1 -> 9*** ...
            9*** is the loop starting node
        """
        head = last = LinkedNode(1)
        linkedList = LinkedList(head)
        linkedList.insert(3)
        linkedList.insert(1)
        linkedList.insert(9)
        linkedList.insert(3)
        linkedList.insert(9)
        linkedList.insert(1)
        linkedList.insert(3)
        linkedList.insert(1)

        while last.next:
            last = last.next
        
        last.next = head.next

        self.assertEqual(loopDetect(linkedList), head.next) 


if __name__ == '__main__':
   unittest.main()
