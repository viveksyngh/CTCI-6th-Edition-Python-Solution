# Write an algorithm such that if an element in MxN matrix is 0,
# it's entire row and column are set to 0

import unittest


def zero_matrix(matrix):
    """
    It uses two sets to store rows and columns which has 0,
    then iterates through matrix and sets value to 0 
    if that row or column is present in the corresponding set.

    Time Complexity: O(M x N)
    Space Complexity: O(M + N)
    """
    rows = set()
    columns = set()
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                columns.add(j)

    for i in range(m):
        for j in range(n):
            if i in rows or j in columns:
                matrix[i][j] = 0
    return matrix


class TestZeroMatrix(unittest.TestCase):
    def setUp(self):
        self.input = [[1, 2, 0], [3, 0, 5], [0, 4, 6]]
        self.output = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def test_zero_matrix(self):
        self.assertEqual(zero_matrix(self.input), self.output)


if __name__ == "__main__":
    unittest.main()
