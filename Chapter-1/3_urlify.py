# Write a method to replace all spaces in a string with "%20",
# You may assume that the string has sufficeint space at the end,
# to hold the additional characters and you are given true lengths of string.
import unittest

def urlify_concatenate(string, true_length):
    """This solution traverse through original string and 
       create a new string by appending characters if it is space then,
       it appends "%20".

       Time Complexity: O(n^2), because string is immutable
       Space Complexity: O(n)

    """

    result_string = ""
    for i in range(true_length):
        if string[i] == " ":
            result_string += "%20"
        else:
            result_string += string[i]
    return result_string


def urlify_list(string, true_length):
    """This solution converts the sting into list and then 
        edits the string in backward direction by replacing 
        space with "%20".

        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    char_list = list(string)
    index = len(string)
    for i in range(true_length -1 , -1 , -1):
        if string[i] == " ":
            char_list[index - 1] = '0'
            char_list[index - 2] = "2"
            char_list[index - 3] = "%"
            index -= 3
        else:
            char_list[index - 1] = string[i]
            index -= 1
    return "".join(char_list)


class TestURLify(unittest.TestCase):

    def setUp(self):
        self.input = ("Mr Jhon Smith    ", 13)
        self.result = "Mr%20Jhon%20Smith"

    def test_urlify_concatenate(self):
        self.assertEqual(urlify_concatenate(*self.input), self.result)

    def test_urlify_list(self):
        self.assertEqual(urlify_list(*self.input), self.result)


if __name__ == '__main__':
    unittest.main()