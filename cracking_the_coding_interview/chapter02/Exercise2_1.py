# -*- coding: utf-8 -*-
import unittest


class LinkedNode(object):
    def __init__(self, val=None):
        self.next = None
        self.val = val
        

class LinkedList(object):
    """
    The class Linked List can be empty.
    """
    def __init__(self, head=None):
        self.head = head
        self.length = 1
        
    def insert(self, element):
        node = LinkedNode(element)
        if not self.head:
            self.head = node
        else:
            head = self.head
            while head.next:
                head = head.next
            head.next = node
        self.length += 1

        
    def remove(self, element, head=None, prev=None):
        """
        Removes a node from the linked list if the node has the value 'element'.
        if head is specified, the function starts from that node, otherwise from list head.
        """
        head = not head and self.head or head
        while head:
            if head.val == element:
                if prev:
                    prev.next = head.next
                    head = head.next
                else:
                    head = head.next
                    self.head = head
                self.length -= 1
            else:
                prev = head
                head = head.next
        
    def __str__(self, *args, **kwargs):
        head = self.head
        res = ""
        while head:
            res += head.val and str(head.val) or ""
            head = head.next
        return res
            
        
def removeDups(linkedList):
    """
    Write code to remove duplicates from an unsorted linked list.
    @param linkedList: the linked list.
    @return: returns the linked list without duplicates
    """
    head = linkedList.head
    while head and head.next:
        linkedList.remove(head.val, head.next, head)
        head = head.next
    return linkedList
    

class RemoveDupsTest(unittest.TestCase):
    def testNodeInsert(self):
        """
        Test node insert.
        """
        pass
        
    def testremoveDups(self):
        """
            Test remove duplicates with these values:
            1 -> 3 -> 1 -> 9 -> 3 -> 2 -> 1 -> 3 -> 5
            result should be:
            1 -> 3 -> 9 -> 2 -> 5
            
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
        
        self.assertEqual(str(removeDups(linkedList)), "13925")
        

if __name__ == '__main__':
   unittest.main() 
