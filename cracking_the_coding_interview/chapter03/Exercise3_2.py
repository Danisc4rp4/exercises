# -*- coding: utf-8 -*-
import unittest

from Stack import Stack

class StackMin(Stack):

    class StackNode(Stack.StackNode):

        def __init__(self, data):
            super().__init__(data)
            self.min = data


    def push(self, data):
        super().push(data)
        if self.top.next and self.top.next.min < self.top.data:
            self.top.min = self.top.next.min

    def min(self):
        return self.top.min


class StackMinTest(unittest.TestCase):
    def testStackMin(self):
        """
            Test stack min:
            1, 2, 5, 4, 8, 6
            result should be:
            min = 1
            
        """
        stack = StackMin()
        stack.push(1)
        stack.push(2)
        stack.push(5)
        stack.push(4)
        stack.push(8)
        stack.push(6)

        self.assertEqual(stack.min(), 1)
        

if __name__ == '__main__':
   unittest.main() 
