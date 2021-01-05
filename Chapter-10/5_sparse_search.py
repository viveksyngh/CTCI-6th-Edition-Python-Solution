"""
Given a sorted aaray of strings that is interspersed with empty strings, write a method to find the location of a given string.

EXAMPLE

Input: ball, {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}
Ouput: 4
"""
import unittest

def search(strings, s, first, last):
    if first > last:
        return -1
    
    mid = (first + last)//2
    if strings[mid] == "":
        left = mid - 1
        right = mid + 1

        while True:
            if left < first or right > last:
                return -1
            elif left >= first and strings[left] != "":
                mid = left
                break
            elif right <= last and strings[right] != "":
                mid = right
                break
                
            left -= 1
            right += 1
    
    if strings[mid] == s:
        return mid
    elif strings[mid] < s:
        return search(strings, s, mid + 1, last)
    else:
        return search(strings, s, first, mid - 1)

def search_sparse(strings, s):
    if len(strings) == 0 or s == "":
        return -1
    return search(strings, s, 0, len(strings)-1)


class TestSearchSparse(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_array(self):
        self.assertEqual(search_sparse([], "abc"), -1)
    
    def test_empty_string(self):
        self.assertEqual(search_sparse(["abc", "", ""], ""), -1)
    
    def test_positive(self):
        self.assertEqual(search_sparse(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "ball"), 4) 

    def test_negative(self):
        self.assertEqual(search_sparse(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "pad"), -1) 

if __name__ == "__main__":
    unittest.main()