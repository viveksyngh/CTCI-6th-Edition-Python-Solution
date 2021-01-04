"""
Given a sorted array of n integers that has been rotated an unknown number of times,
write code to find an element in the array. You may assume that the aaray was originally sorted 
in increasing order. 

EXAMPLE
Input Find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
"""

import unittest

def serach_sorted_array(arr, low, high, value):
    if len(arr) == 0:
        return -1

    if low > high :
        return -1

    mid = (low + high)//2
    if arr[mid] == value:
        return mid
    
    if arr[low] < arr[mid]:
        if value >= arr[low] and value < arr[mid]:
            return serach_sorted_array(arr, low, mid - 1, value) # Search in left half
        else:
            return serach_sorted_array(arr, mid + 1, high, value)  # Search in right half
    elif arr[mid] < arr[high]:
        if value > arr[mid] and value <= arr[high]:
            return serach_sorted_array(arr, mid + 1, high, value)
        else:
            return serach_sorted_array(arr, low, mid - 1, value)
    elif arr[low] == arr[mid]:
        if arr[mid] != arr[high]:
            return serach_sorted_array(arr, mid + 1, high,  value)
        else:
            r = serach_sorted_array(arr, low, mid - 1, value)
            if r != -1:
                return r
            return serach_sorted_array(arr, mid + 1, high,  value)
    
    return -1


class TestSortedSearchArray(unittest.TestCase):
    def setUp(self):
        pass

    def test_positive(self):
        self.assertEqual(serach_sorted_array([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 0, 11, 5), 8)
    
    def test_positive_right(self):
        self.assertEqual(serach_sorted_array([10, 15, 20, 0, 5], 0, 4, 5), 4)
    
    def test_positive_left(self):
        self.assertEqual(serach_sorted_array([50, 5, 20, 30, 40], 0, 4, 5), 1)
    
    def test_empty(self):
        self.assertEqual(serach_sorted_array([], 0, 0, 5), -1)
    
    def test_negative_single(self):
        self.assertEqual(serach_sorted_array([1], 0, 0, 5), -1)

    def test_negative(self):
        self.assertEqual(serach_sorted_array([50, 5, 20, 30, 40], 0, 4, 6), -1)
    


if __name__ == "__main__":
    unittest.main()