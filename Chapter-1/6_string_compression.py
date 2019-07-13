# Implement a method to perform basic string compression,
# using counts of repeated characters

import unittest


def compress_string_concatenation(string):
    """
    It creates a new string and traverse through original string, 
    concatenate the characters and its count to new string.
    String concatenation is very expensive, as strings are immutable.

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """

    count = 0
    compressed_string = ""
    for i in range(len(string)):
        count += 1
        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compressed_string += string[i] + str(count)
            count = 0
    return string if len(compressed_string) >= len(string) else compressed_string


def compress_string_list(string):
    """
    This solution uses a list to store characters and its count,
    So that it does not have to concatenate string each time.
         
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """

    compressed_string = []
    count = 0
    for i in range(len(string)):
        count += 1
        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compressed_string.append(string[i])
            compressed_string.append(str(count))
            count = 0
    return (
        string if len(compressed_string) >= len(string) else "".join(compressed_string)
    )


class TestCompressString(unittest.TestCase):
    def setUp(self):
        self.data_set = [("aabcccccaaa", "a2b1c5a3"), ("a", "a"), ("", "")]

    def test_compress_string_concatenation(self):
        for data in self.data_set:
            input_data = data[0]
            output_data = data[1]
            self.assertEqual(compress_string_concatenation(input_data), output_data)

    def test_compress_string_list(self):
        for data in self.data_set:
            input_data = data[0]
            output_data = data[1]
            self.assertEqual(compress_string_list(input_data), output_data)


if __name__ == "__main__":
    unittest.main()
