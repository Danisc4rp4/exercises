# -*- coding: utf-8 -*-
import unittest

from Stack import Stack
from StackExceptions import StackEmptyException

DEFAULT_THRESHOLD = 10
class CapacityStack(Stack):

    def __init__(self):
        super().__init__()
        self.capacity = 0

    def pop(self):
        data  = super().pop()
        self.capacity -= 1
        return data

    def push(self, data):
        super().push(data)
        self.capacity += 1


class StackOfPlates():

    def __init__(self, threshold = DEFAULT_THRESHOLD):
        self.threshold = threshold
        self.stacks = []

    def pop(self):
        if not len(self.stacks):
            raise StackEmptyException()
        topStack = self.stacks[-1]
        data = topStack.pop()
        if not len(topStack):
            self.stacks = self.stacks[:-1]
        return data

    def push(self, data):
        currentStack = None
        if not len(self.stacks) or self.stacks[-1].capacity == self.threshold:
            currentStack = CapacityStack()
            self.stacks.append(currentStack)
        if not currentStack:
            currentStack = self.stacks[-1]
        currentStack.push(data)

    def popAt(self, index):
        if len(self.stacks) <= index:
            raise Exception("Wrong usage of popAt, list index out of range.")
        currentStack = self.stacks[index]
        data = currentStack.pop()
        if not len(currentStack):
            self.stacks = self.stacks[:index] + self.stacks[index + 1:len(self.stacks)]
        return data


class StackOfPlatesTest(unittest.TestCase):
    def testStackOfPlates(self):
        """
            Test stack of plates:
            1, 2, 5, 4, 8, 6
            result should be:
            min = 1
            
        """
        stack = StackOfPlates(5)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.push(6)

        self.assertEqual(len(stack.stacks), 2)

        stack.push(7)
        stack.push(8)
        stack.push(9)
        stack.push(10)
        stack.push(11)

        self.assertEqual(len(stack.stacks), 3)
        

if __name__ == '__main__':
   unittest.main() 
