# -*- coding: utf-8 -*-
import unittest

def rotateMatrix(matrixToRotate):
    """
    Given an image represented by an NxN matrix, where each pixel in the image is 4
    bytes, write a method to rotatethe image by 90 degrees. Can you do this in place?
    @param matrixToRotate: the matrix to rotate by 90 degrees.
    @return: returns the matrix rotated by 90 degrees.
    """
    matrixDimension = len(matrixToRotate)
    # Note: it's impossible to initialise rotatedMatrix to the value of matrixToRotate
    # (rotatedMatrix = matrixToRotate). Doing that equals to point to the same object, 
    # and the value of matrixToRotate would be overridden.
    rotatedMatrix = [[0 for _ in range(matrixDimension)] for _ in range(matrixDimension)]
    for matrixIndex in range(matrixDimension):
        for layerIndex in range(matrixDimension):
            rotatedMatrix[layerIndex][matrixDimension - 1 - matrixIndex] = matrixToRotate[matrixIndex][layerIndex]
    return rotatedMatrix


class RotateMatrixTest(unittest.TestCase):
    def testRotateMatrix(self):
        self.assertEqual(rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])


if __name__ == '__main__':
   unittest.main() 
