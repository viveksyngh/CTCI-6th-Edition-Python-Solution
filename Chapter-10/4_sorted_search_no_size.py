"""
You are given an array-like data structure Listy which lacks a size method. It does, however, have an elementAt(i)
method that returns the element at index i in O(1) time. If i is beyond the bounds of the data structure, it returns
-1. (For this reason, the data structure only supports positive integers). Given a Listy which contains sorted, 
positive integers, find he index at which an element x occurs. If x occurs multiple times, you may return any index.
"""
import unittest

class Listy:
    def __init__(self, items):
        self.items = items
    
    def elementAt(self, i):
        if i >= len(self.items):
            return -1
        return self.items[i]

def sorted_search(items, value):
    end = 1
    while items.elementAt(end) != -1 and items.elementAt(end) < value:
        end = end * 2
    return binary_search(items, value, 0, end)

def binary_search(items, value, low, high):
    while low <= high:
        mid = (low + high)//2
        mid_value = items.elementAt(mid)
        if mid_value == -1 or mid_value > value:
            high = mid - 1
        elif mid_value < value:
            low = mid + 1
        else:
            return mid
    return -1


class TestSortedSearch(unittest.TestCase):
    def setUp(self):
        pass

    def test_positive(self):
        self.assertEqual(sorted_search(Listy([2, 4, 6, 8, 13]), 8), 3)
    
    def test_negative(self):
        self.assertEqual(sorted_search(Listy([2, 4, 6, 8, 13]), 12), -1)
    
    def test_higher_limit(self):
        self.assertEqual(sorted_search(Listy([2, 4, 6, 8, 13]), 20), -1)
    
    def test_lower_limit(self):
        self.assertEqual(sorted_search(Listy([2, 4, 6, 8, 13]), 1), -1)
    
    def test_higher_edge(self):
        self.assertEqual(sorted_search(Listy([2, 4, 6, 8, 13]), 13), 4)

    def test_lower_edge(self):
        self.assertEqual(sorted_search(Listy([2, 4, 6, 8, 13]), 2), 0)


if __name__ == "__main__":
    unittest.main()