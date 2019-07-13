# Assume you have a method is_substring which checks,
# if one word is a substring of another. Given two string,
# s1 and s2, write code to check if s2 is a rotation of s1
# using only one call to  is_substring

import unittest


def is_string_rotation(string1, string2):
    if len(string1) != len(string2) or len(string1) == 0:
        return False

    large_string = string1 + string1
    return is_substring(large_string, string2)


def is_substring(string1, string2):
    if string1.find(string2) == -1:
        return False
    return True


class TestStringRotation(unittest.TestCase):
    def setUp(self):
        self.true_input = ("waterbottle", "erbottlewat")
        self.false_input = ("hello", "alloh")

    def test_is_string_rotation(self):
        self.assertTrue(is_string_rotation(self.true_input[0], self.true_input[1]))
        self.assertFalse(is_string_rotation(self.false_input[0], self.false_input[1]))


if __name__ == "__main__":
    unittest.main()
