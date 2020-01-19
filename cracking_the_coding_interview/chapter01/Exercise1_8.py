# -*- coding: utf-8 -*-
import unittest

ROW_KEY = 'rows'
COL_KEY = 'columns'

def zeroMatrix(matrix):
    """
    Write an algorithm such that if an element in a MxN matrix is 0, its entire
    row and column are set to 0.
    @param matrix: the matrix.
    @return: returns the matrix with zeros set.
    """
    matrixMap = {
        ROW_KEY: [],
        COL_KEY: []
    }
    matrixRows = len(matrix)
    matrixColumns = len(matrix[0])
    for matrixRowIndex in range(matrixRows):
        for matrixColumnIndex in range(matrixColumns):
            if not matrix[matrixRowIndex][matrixColumnIndex]:
                matrixMap[ROW_KEY].append(matrixRowIndex)
                matrixMap[COL_KEY].append(matrixColumnIndex)
    for zeroRowIndex in matrixMap[ROW_KEY]:
        for matrixColumnIndex in range(matrixColumns):
            matrix[zeroRowIndex][matrixColumnIndex] = 0
    for zeroColumnIndex in matrixMap[COL_KEY]:
        for matrixRowIndex in range(matrixRows):
            matrix[matrixRowIndex][zeroColumnIndex] = 0
    return matrix


class ZeroMatrixTest(unittest.TestCase):
    def testZeroMatrix(self):
        self.assertEqual(zeroMatrix([[1, 2, 0], [0, 5, 6], [7, 8, 9]]), [[0, 0, 0], [0, 0, 0], [0, 8, 0]])

if __name__ == '__main__':
   unittest.main() 
