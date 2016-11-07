# Implement an algorithm to determine if a string has all unique charachters.
# What if you can not use additional data structure?
import unittest

# Solutions without using additional data structure

def is_unique_chars_compare(string):
    """This solution compares every character of string to 
        every other character of string.

        Time Complexity: O(n^2)
        Space Complexity: O(1)
    """

    for i, char in enumerate(string):
        for j, other_chars in enumerate(string):
            if i != j and char == other_chars:
                return False
    return True


def is_unique_chars_sort(string):
    """This solution first sorts the string
        and then compares two consecutive charachters.

        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """

    sorted_string = "".join(sorted(string)) # Sort is not in place
    for i in range(len(sorted_string) - 1):
        if sorted_string[i] == sorted_string[i+1]:
            return False
    return True

# Solutions which uses additional data structures

def is_unique_chars_map(string):
    """This solution assumes that character set of string is ASCII.
        It uses an list to keep track 
        of apperance of charachters in string.

        Time Complexity: O(n)
        Space Complexity: O(1)
    """

    if len(string) > 128 :
        return False

    chars_list = [False] * 128
    for char in string:
        if chars_list[ord(char)]:
            return False
        chars_list[ord(char)] = True
    return True


def is_unique_chars_bit_vector(string):
    """This solution assumes that string is made of only 
        lowecase charachters from a to z.

        Time Complexity: O(n)
        Space Complexity: O(1)
    """

    checker = 0
    for char in string:
        val = ord(char) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True


class TestUnique(unittest.TestCase):

    def setUp(self):
        self.positive_data = ["python", "django", ""]
        self.negative_data = ["javascript", "hello"]

    def test_is_unique_chars_compare(self):
        print "Started testing 'test_is_unique_chars_compare' "
        
        print "Running test case for positive data"
        for string in self.positive_data:
            self.assertTrue(is_unique_chars_compare(string))

        print "Running test case for negative data"
        for string in self.negative_data:
            self.assertFalse(is_unique_chars_compare(string))


    def test_is_unique_chars_sort(self):
        print "Started testing 'is_unique_chars_sort' "
        
        print "Running test case for positive data"
        for string in self.positive_data:
            self.assertTrue(is_unique_chars_sort(string))

        print "Running test case for negative data"
        for string in self.negative_data:
            self.assertFalse(is_unique_chars_sort(string))

    def test_is_unique_chars_map(self):
        print "Started testing 'is_unique_chars_map' "
        
        print "Running test case for positive data"
        for string in self.positive_data:
            self.assertTrue(is_unique_chars_map(string))

        print "Running test case for negative data"
        for string in self.negative_data:
            self.assertFalse(is_unique_chars_map(string))

    def test_is_unique_chars_bit_vector(self):
        print "Started testing 'is_unique_chars_bit_vector' "
        
        print "Running test case for positive data"
        for string in self.positive_data:
            self.assertTrue(is_unique_chars_bit_vector(string))

        print "Running test case for negative data"
        for string in self.negative_data:
            self.assertFalse(is_unique_chars_bit_vector(string))


if __name__ == '__main___':
    unittest.main()



