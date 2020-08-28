# -*- coding: utf-8 -*-
import unittest
from Exercise2_1 import LinkedList, LinkedNode
            
        
def getListValue(linkedList):
    """
    @param linkedList: the linked list.
    @return: returns the value int (reverse order). 
    """
    head = linkedList.head
    power = 0
    sum = 0
    while head:
        sum += head.val * (10**power)
        power += 1
        head = head.next
    return sum

def getDiv(currentVal, power):
    return int(currentVal / (10 ** power))

def getListFromValue(value):
    power = 0
    currentVal = value
    div = getDiv(currentVal, power)
    while div > 0:
        power += 1
        div = getDiv(currentVal, power)
    power -= 1
    last = head = LinkedNode(getDiv(currentVal, power))
    while power > 0:
        currentVal = currentVal % (10 ** power)
        power -= 1
        last = head
        head = LinkedNode(getDiv(currentVal, power))
        head.next = last
    res = LinkedList(head)
    return res

def sumList(linkedList1, linkedList2):
    """
    @param linkedList1: the linked list to sum.
    @param linkedList2: the second linked list to sum.
    @return: returns the list representing value int of the sum.
    """
    totalSum = getListValue(linkedList1) + getListValue(linkedList2)
    res = getListFromValue(totalSum)
    return res

    
class sumListTest(unittest.TestCase):
        
    def testSumList(self):
        """
            Test sumList with reverse order:
            1 -> 3 -> 1 -> 9 -> 3 -> 2 -> 1 -> 3 -> 5
            the list will become:
            1 -> 1 -> 1 -> 3 -> 9 -> 3 -> 2 -> 3 -> 5
            
        """
        head = LinkedNode(7)
        linkedList1 = LinkedList(head)
        linkedList1.insert(1)
        linkedList1.insert(6)

        head = LinkedNode(5)
        linkedList2 = LinkedList(head)
        linkedList2.insert(9)
        linkedList2.insert(2)
        
        self.assertEqual(str(sumList(linkedList1, linkedList2)), '219')
        

if __name__ == '__main__':
   unittest.main()
