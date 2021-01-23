"""
In an array of integers, a "peak" is an element which is greater than or eual to the adjacent integers and a "valley"
is an element which is less than or equal to the adjacent integers, For example, in the array [5, 8, 6, 2, 3, 4, 6],
[8, 6] are peaks and [5, 2] are valleys. Given an array of integers, sort the array into an altering sequence of peaks
and valleys.

EXAMPLE:
Input: {5, 3, 1, 2, 3}
Ouput: {5, 1, 3, 2, 3}
"""
import math, unittest

def suboptimal_solution(array):
    # sort the array in increasing order
    array.sort()

    # convert SMALL < MEDIUM < LARGE  to  MEDIUM < SMALL < LARGE
    # This will set peaks at 1, 3, 5 .... 
    # Even {2, 4, 6, ... } indexes will be automatically become valley 
    for i in range(1, len(array), 2):
        array[i], array[i-1] = array[i-1], array[i]
    return array

def optimal_solution(array):
    # take any three element and if you put largest one in the middle 
    # then it will have alternate peak and valleys
    for i in range(1, len(array), 2):
        max_index = find_max_index(array, i-1, i, i+1)
        if max_index != i:
            array[max_index], array[i] = array[i], array[max_index]
    return array


def find_max_index(array, a, b, c):
    INT_MIN = -math.inf
    a_value = array[a] if a >= 0 and a < len(array) else INT_MIN
    b_value = array[b] if b >= 0 and b < len(array) else INT_MIN
    c_value = array[c] if c >= 0 and c < len(array) else INT_MIN
    max_value = max(a_value, b_value, c_value)
    if max_value == a_value:
        return a
    elif max_value == b_value:
        return b
    else:
        return c

class TestSubOptimal(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        self.assertEqual(suboptimal_solution([5, 3, 1, 2, 3]), [2, 1, 3, 3, 5])

class TestOptimal(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        self.assertEqual(suboptimal_solution([5, 3, 1, 2, 3]), [2, 1, 3, 3, 5])

if __name__ == "__main__":
    unittest.main()