# Given an image repersented by NxN matrix, where each image is 4 bytes,
# Write a method to image by 90 degrees


import unittest


def rotate_matrix(matrix):
    """This solution rotates the matrix by 90 degree, 
        without using any extra space.
    """

    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)
    for layer in range(n/2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - layer
            top = matrix[first][i]

            matrix[first][i] = matrix[last - offset][first]

            matrix[last - offset][first] = matrix[last][last - offset]

            matrix[last][last - offset] = matrix[i][last]

            matrix[i][last] = top
    return True


class TestRotateMatrix(unittest.TestCase):

    def setUp(self):
        self.input = [[1, 2, 3, 4], 
                      [5, 6, 7, 8], 
                      [9, 10, 11, 12], 
                      [13, 14, 15, 16]]
        self.output = [[13, 9, 5, 1], 
                       [14, 10, 6, 2], 
                       [15, 11, 7, 3], 
                       [16, 12, 8, 4]]

    def test_rotate_matrix(self):
        self.assertTrue(rotate_matrix(self.input))

