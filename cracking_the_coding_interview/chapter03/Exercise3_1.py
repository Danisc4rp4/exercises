# -*- coding: utf-8 -*-
import unittest


def getEmptyThreeStackArray():
    return [ 0, 0, 0]

def getStack(threeStacksArray, stackNum):
    stack1Index = 0
    stack1Len = threeStacksArray[stack1Index]
    stack1 = stack1Len == 0 and [] or threeStacksArray[1:1+stack1Len]

    stack2Index = 1 + stack1Len
    stack2Len = threeStacksArray[stack2Index]
    stack2 = stack2Len == 0 and [] or threeStacksArray[stack2Index+1:stack2Index+1+stack2Len]

    stack3Index = stack2Index + 1 + stack2Len
    stack3Len = threeStacksArray[stack3Index]
    stack3 = stack3Len == 0 and [] or threeStacksArray[stack3Index+1:]
    stackSwitcher = {
        1: stack1,
        2: stack2,
        3: stack3
    }
    return stackSwitcher.get(stackNum)

def getStackWithAdd(valToAdd, currentStack):
    return [valToAdd] + currentStack

def addTothreeStacksArray(threeStackArray, valToAdd, stackNum):
    stack1 = getStack(threeStackArray, 1)
    stack2 = getStack(threeStackArray, 2)
    stack3 = getStack(threeStackArray, 3)
    if stackNum == 1:
        stack1 = getStackWithAdd(valToAdd, stack1)
    if stackNum == 2:
        stack2 = getStackWithAdd(valToAdd, stack2)
    if stackNum == 3:
        stack3 = getStackWithAdd(valToAdd, stack3)
    return [len(stack1)] + stack1 + [len(stack2)] + stack2 + [len(stack3)] + stack3


class ThreeInOneTest(unittest.TestCase):
    def testThreeInOne(self):
        """
            Test three stacks in one array:
            [1, 10, 2, 11, 12, 1, 13]
            result should be:
            [ [10], [11, 12], [13] ]
            
        """
        threeStacksArray = getEmptyThreeStackArray()
        threeStacksArray = addTothreeStacksArray(threeStacksArray, 10, 1)       
        threeStacksArray = addTothreeStacksArray(threeStacksArray, 11, 2)       
        threeStacksArray = addTothreeStacksArray(threeStacksArray, 12, 2)
        threeStacksArray = addTothreeStacksArray(threeStacksArray, 13, 3)    

        listOfStacks = []
        listOfStacks.append(getStack(threeStacksArray, 1))
        listOfStacks.append(getStack(threeStacksArray, 2))
        listOfStacks.append(getStack(threeStacksArray, 3))   
       
        self.assertEqual(listOfStacks, [ [10], [12, 11], [13] ])

        # TODO: Implement pop()
        

if __name__ == '__main__':
   unittest.main() 
