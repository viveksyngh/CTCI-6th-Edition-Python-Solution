# Given two strings, write a method to decide if one is permutation of the other.
import unittest

# Solution - 1
def check_premutation_sort(string1, string2):
    """
    This solution sorts both string and checks 
    if two strings are equal or not after sorting.

    Time Complexity: O(n log(n))
    Space Complexity: O(n)
    """

    if len(string1) != len(string2):
        return False
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    return sorted_string1 == sorted_string2


# Solution - 2
def check_permutation_list(string1, string2):
    """
    This solution uses an array to keep count of characters.
    First traverse through one string and count the characters,
    then traverse through second string to match counts of characters.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    if len(string1) != len(string2):
        return False

    letters = [0] * 128
    for char in string1:
        letters[ord(char)] += 1

    for char in string2:
        letters[ord(char)] -= 1
        if letters[ord(char)] < 0:
            return False
    return True


# Test Case
class TestCheckPermutation(unittest.TestCase):
    def setUp(self):
        self.true_data = [("dear", "read"), ("lame", "male"), ("team", "mate")]
        self.false_data = [("near", "rear"), ("hello", "allo")]

    def test_check_premutation_sort(self):
        # Testing for True data set
        for data in self.true_data:
            self.assertTrue(check_premutation_sort(data[0], data[1]))

        # Testing for False data set
        for data in self.false_data:
            self.assertFalse(check_premutation_sort(data[0], data[1]))

    def test_check_permutation_list(self):
        # Testing for True data set
        for data in self.true_data:
            self.assertTrue(check_permutation_list(data[0], data[1]))

        # Testing for False data set
        for data in self.false_data:
            self.assertFalse(check_permutation_list(data[0], data[1]))


if __name__ == "__main__":
    unittest.main()
