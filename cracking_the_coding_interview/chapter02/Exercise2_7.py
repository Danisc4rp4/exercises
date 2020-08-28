# -*- coding: utf-8 -*-
import unittest
from Exercise2_1 import LinkedList, LinkedNode
            
        
def intersection(linkedList1, linkedList2):
    """
    @param linkedList1: the linked list.
    @param linkedList2: the second linked list.
    @return: returns true if there is an intersection.
    """
    longestList = linkedList1.length >= linkedList2.length and linkedList1 or linkedList2
    shortestList = linkedList1.length < linkedList2.length and linkedList2 or linkedList2
    lenDiff = longestList.length - shortestList.length

    head1 = longestList.head
    for _ in range(lenDiff):
        head1 = head1.next
    head2 = shortestList.head
    while head1 and head1 != head2:
        head1 = head1.next
        head2 = head2.next
    return head1
    
class intersectionTest(unittest.TestCase):
        
    def testIntersection(self):
        """
            Test intersection:
            1 -> 3 -> 1 -> 9*** -> 3 -> 9 -> 1 -> 3 -> 1
                      2 -> 
            9*** is the intersection
        """
        head1 = LinkedNode(1)
        linkedList1 = LinkedList(head1)
        linkedList1.insert(3)
        linkedList1.insert(1)
        linkedList1.insert(9)
        linkedList1.insert(3)
        linkedList1.insert(9)
        linkedList1.insert(1)
        linkedList1.insert(3)
        linkedList1.insert(1)

        intersect = head1.next.next.next

        head2 = LinkedNode(2)
        linkedList2 = LinkedList(head2)
        head2.next = intersect
        linkedList2.length = 7

        self.assertEqual(intersection(linkedList1, linkedList2), intersect) 


if __name__ == '__main__':
   unittest.main()
