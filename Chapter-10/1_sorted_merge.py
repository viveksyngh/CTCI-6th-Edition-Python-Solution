"""
You are given two sorted arrays, A and B, where A has large enough buffer at 
the end to hold B. Write a method to merge B into A in sorted order.
"""

import unittest

def sorted_merge(A : [int], B : [int], lastA : int, lastB : int):
    """Solution: merge the elements from back side."""
    indexA = lastA - 1
    indexB = lastB - 1
    mergeIndex = lastA + lastB - 1
    while indexA >= 0 and indexB >= 0:
        if A[indexA] > B[indexB]:
            A[mergeIndex] = A[indexA]
            indexA -= 1
        else:
            A[mergeIndex] = B[indexB]
            indexB -= 1
        mergeIndex -= 1
    
    while indexA >= 0:
        A[mergeIndex] = A[indexA]
        indexA -= 1
        mergeIndex -= 1
    
    while indexB >= 0:
        A[mergeIndex] = B[indexB]
        indexB -= 1
        mergeIndex -= 1
    
    return A

    
class TestSortedMerge(unittest.TestCase):
    def setup(self):
        pass

    def test_empty(self):
        self.assertEqual(sorted_merge([], [], 0, 0), [])
    
    def test_single_item(self):
        self.assertEqual(sorted_merge([1, 0, 0], [2], 1, 1), [1, 2, 0])
    
    def test_case_2(self):
        self.assertEqual(sorted_merge([2, 5, 8, 0, 0, 0], [1, 7, 9], 3, 3), [1, 2, 5, 7, 8, 9])
    
    def test_case_3(self):
        self.assertEqual(sorted_merge([1, 2, 5, 0, 0, 0, 0], [7, 8, 9, 0], 3, 3), [1, 2, 5, 7, 8, 9, 0])

if __name__ == "__main__":
    unittest.main()