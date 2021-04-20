# -*- coding: utf-8 -*-
import unittest

def matrixLineRotate(rotate, mline):
    for i in range(len(mline)):
        rotate[i] = [mline[i]] + rotate[i]

def rotateMatrix(matrixToRotate):
    """
    O(n) n matrix dimension
    @return: returns the matrix rotated by 90 degrees.
    """
    rotate = [[] for _ in range(len(matrixToRotate[0]))]
    for mline in matrixToRotate:
        matrixLineRotate(rotate, mline)
    return rotate

class MatrixTestCase():

    def __init__(self, matrix, expectedResult):
        self.matrix = matrix
        self.expectedResult = expectedResult

class RotateMatrixTest(unittest.TestCase):

    @staticmethod
    def _getIntMatrix(n, m):
        return [[1 + i*m + j for j in range(m)] for i in range(n)]

    def testRotateMatrix(self):
        testCases = {
            0: MatrixTestCase(self._getIntMatrix(3, 4), [ [9, 5, 1], [10, 6, 2], [11, 7, 3], [12, 8, 4] ]),
            1: MatrixTestCase(self._getIntMatrix(3, 3), [ [7, 4, 1], [8, 5, 2], [9, 6, 3] ])
        }

        testcase1 = testCases.get(0)
        res1 = rotateMatrix(testcase1.matrix)
        self.assertEqual(res1, testcase1.expectedResult)

        testcase2 = testCases.get(1)
        res2 = rotateMatrix(testcase2.matrix)
        self.assertEqual(res2, testcase2.expectedResult)


if __name__ == '__main__':
   unittest.main() 
