# There are three types of edits that can be performed on a string
# insert a character, remove a character, and replace a character
# Given two strings write a function to check if they are one edit
# (zero edit away).

import unittest

# Helper functions
def is_inserted(string1, string2):
    i, j = 0, 0
    insert_found = False
    while i < len(string1) and j < len(string2):
        if string1[i] != string2[j]:
            if insert_found:
                return False
            else:
                insert_found = True
        else:
            i += 1
        j += 1
    return True


def is_replaced(string1, string2):
    j = 0
    replace_found = False
    for i in range(len(string1)):
        if string1[i] != string2[j]:
            if replace_found:
                return False
            else:
                replace_found = True
        j = j + 1
    return True


# Solution 1
def is_one_away(string1, string2):
    """This solution checks for each operation individually."""
    if len(string1) + 1 == len(string2):
        return is_inserted(string1, string2)
    elif len(string1) - 1 == len(string2):
        return is_inserted(string2, string1)
    elif len(string1) == len(string2):
        return is_replaced(string1, string2)
    return False


def is_one_away_compact(string1, string2):
    """
    This solution is more compact and checks for all operation 
        in single traversal of string.
    """
    if abs(len(string1) - len(string2)) > 1:
        return False
    i, j = 0, 0
    found_difference = False
    while i < len(string1) and j < len(string2):
        if string1[i] != string2[j]:
            if found_difference:
                return False
            else:
                found_difference = True

            if len(string1) == len(string2):
                j = j + 1
        else:
            j = j + 1
        i = i + 1
    return True


class TestCaseOneAway(unittest.TestCase):
    def setUp(self):
        self.positive_input = [("pale", "ple"), ("pales", "pale"), ("pale", "bale")]
        self.negative_input = [("pale", "bake")]

    def test_is_one_away(self):
        for data in self.positive_input:
            self.assertTrue(is_one_away(data[0], data[1]))

        for data in self.negative_input:
            self.assertFalse(is_one_away(data[0], data[1]))

    def test_is_one_away_compact(self):
        for data in self.positive_input:
            self.assertTrue(is_one_away_compact(data[0], data[1]))

        for data in self.negative_input:
            self.assertFalse(is_one_away_compact(data[0], data[1]))


if __name__ == "__main__":
    unittest.main()
