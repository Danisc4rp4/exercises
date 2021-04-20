# -*- coding: utf-8 -*-
import unittest

STACKTYPE_FIRST = 1
STACKTYPE_SECOND = 2
STACKTYPE_THIRD = 3

def threeInOne():
    """
    Use a single array to implement three stacks
    @return: returns the array.
    """
    stackArray = []

    # Length of the stacks
    firstStack = 0
    secondStack = 0
    thirdStack = 0

    def AddToStack(stack, item, stackArray, firstStack, secondStack, thirdStack):
        firstArray = firstStack and stackArray[:firstStack] or []
        secondArray = secondStack and stackArray[firstStack:firstStack + secondStack] or []
        thirdArray = thirdStack and stackArray[firstStack + secondStack:firstStack + secondStack + thirdStack] or []

        if stack == STACKTYPE_FIRST:
            firstArray.append(item)
            firstStack += 1
        elif stack == STACKTYPE_SECOND:
            secondArray.append(item)
            secondStack += 1
        else:
            thirdArray.append(item)
            thirdStack += 1

        stackArray = firstArray + secondArray + thirdArray

        return (stackArray, firstStack, secondStack, thirdStack)

    (stackArray, firstStack, secondStack, thirdStack) = AddToStack(STACKTYPE_FIRST, 0, stackArray, firstStack, secondStack, thirdStack)
    (stackArray, firstStack, secondStack, thirdStack) = AddToStack(STACKTYPE_SECOND, 1, stackArray, firstStack, secondStack, thirdStack)
    (stackArray, firstStack, secondStack, thirdStack) = AddToStack(STACKTYPE_FIRST, 1, stackArray, firstStack, secondStack, thirdStack)

    return (stackArray, firstStack, secondStack, thirdStack)


class ThreeInOneTest(unittest.TestCase):
    def testThreeInOne(self):
        """
            Test three stacks in one array:
            [0, 1] [1] []
            result should be:
            ( [0, 1, 1 ], 2, 1, 0 )
            
        """        
        self.assertEqual(threeInOne(), ( [0, 1, 1 ], 2, 1, 0 ))
        

if __name__ == '__main__':
   unittest.main() 
