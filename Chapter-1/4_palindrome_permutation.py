# Given a string, write a function to check if it is a permutation of a palindrome.
import unittest

# Helper functions
def get_char_number(char):
    a = ord("a")
    z = ord("z")
    val = ord(char)
    if val >= a and val <= z:  # check for letter characters
        return val - a
    return -1


def check_max_one_odd(chars):
    found_odd = False
    for char, count in chars.items():
        if count % 2 != 0:
            if found_odd:
                return False
            else:
                found_odd = True
    return True


def toggle_bit(bit_vector, index):
    if index < 0:
        return bit_vector
    mask = 1 << index
    if mask & bit_vector == 0:  # Bit was Off
        bit_vector |= mask  # On
    else:
        bit_vector &= ~mask  # Off
    return bit_vector


def check_exactly_one_bit_set(bit_vector):
    return (bit_vector & (bit_vector - 1)) == 0


# Solution 1
def is_palindrome_permutation_hash_table(string):
    """
    This solution uses hash table.

    Time Complexity: O(n)
    Space Complexity: O(c) # number of characters
    """
    chars = dict()
    for char in string:
        key = get_char_number(char)
        if key != -1:  # Ignoring non letter characters
            chars[key] = chars.get(key, 0) + 1

    return check_max_one_odd(chars)


# Solution 2
def is_palindrome_permutation_bit_vector(string):
    """
    This solution uses bit vector and toggles the 
    bit at index of characters to count.
        
    Time Complexity: O(n)
    Space Complexity: O(c)
    """

    bit_vector = 0
    for char in string:
        index = get_char_number(char)
        bit_vector = toggle_bit(bit_vector, index)
    return bit_vector == 0 or check_exactly_one_bit_set(bit_vector)


class TestPallindromePermutation(unittest.TestCase):
    def setUp(self):
        self.true_input = "tact coa"
        self.false_input = "python"

    def test_bit_vector(self):
        self.assertTrue(is_palindrome_permutation_bit_vector(self.true_input))
        self.assertFalse(is_palindrome_permutation_bit_vector(self.false_input))

    def test_hash_table(self):
        self.assertTrue(is_palindrome_permutation_hash_table(self.true_input))
        self.assertFalse(is_palindrome_permutation_hash_table(self.false_input))


if __name__ == "__main__":
    unittest.main()
