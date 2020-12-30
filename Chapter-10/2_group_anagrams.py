"""
Write a method to sort an array of strings so that all the anagrams are next to each other.
"""

import unittest
from collections import defaultdict

# Solution 1 : Using regular sorting alogrithms with custom compare method
def group_anagram_1(strings):
    """ 
    Runtime Complexity: O(nLog(n))
    """

    def cmp_str(str1, str2):
        s1 = sorted(str1)
        s2 = sorted(str2)
        if s1 == s2:
            return 0
        if s1 > s2:
            return 1
        if s1 < s2:
            return -1

    strings.sort(cmp=cmp_str)
    return strings

# Solution 2 : We don't need to sort array of strings, we can just rearrange them to group anagrams together using hash table
def group_anagram(strings):
    hash_map = defaultdict(list)
    for s in strings:
        hash_map["".join(sorted(s))].append(s)
    
    i = 0 
    for _, values in hash_map.items():
        for value in values:
            strings[i] = value
            i += 1
    
    return strings
    

class TestGroupAnagram(unittest.TestCase):
    def setup(self):
        pass

    def test_empty(self):
        self.assertEqual(group_anagram([]), [])
    
    def test_single(self):
        self.assertEqual(group_anagram(["car"]), ["car"])
    
    def test_single_anagram(self):
        self.assertEqual(group_anagram(["car", "arc", "rac"]), ["car", "arc", "rac"])
    
    def test_multiple_anagram(self):
        self.assertIn(group_anagram(["car", "act", "rac", "cat", "arc"]), [["car", "rac", "arc", "act", "cat"], ["act", "cat", "car", "rac", "arc"]])


if __name__ == "__main__":
    unittest.main()