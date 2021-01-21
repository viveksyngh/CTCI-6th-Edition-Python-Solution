"""
Imagine you are reading in a stream of integers. Periodically, you wish to be able to look up the
rank of a number x (the number of values less than or equal to x). Implement the data structures and algorithms
 to support these operations. That is, implement the method track(int x), which is called when each number is generated,
 and the method getRankOfNumber(int x), which returns the number of values less than or equal to x (not including x itself).

 EXAMPLE:
 Stream (in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
 getRankOfNumber(1) = 0
 getRankOfNumber(3) = 1
 getRankOfNumber(4) = 3
"""

import unittest

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.left_size = 0

class RankTree:

    def __init__(self):
        self.tree = None
    
    def insert(self, val):
        self.tree = self.track(self.tree, val)
    
    def rank(self, val):
        return self.getRankOfNumber(self.tree, val)
    
    @staticmethod
    def track(tree, val):
        if tree is None:
            return Node(val)

        if val <= tree.val:
            tree.left_size += 1
            tree.left = RankTree.track(tree.left, val)
        else:
            tree.right = RankTree.track(tree.right, val)
        return tree

    @staticmethod
    def getRankOfNumber(tree, val):
        if tree.val == val:
            return tree.left_size
        
        if val < tree.val:
            if tree.left is None:
                return -1
            return RankTree.getRankOfNumber(tree.left, val)

        if tree.right is None:
            return -1

        right_rank = RankTree.getRankOfNumber(tree.right, val)
        if right_rank == -1:
            return -1
        return right_rank + tree.left_size + 1


class TestRankFromStream(unittest.TestCase):
    def setup(self):
        pass
    
    def prepare_stream(self):
        input = [5, 1, 4, 4, 5, 9, 7, 13, 3]
        rt = RankTree()
        for i in input:
            rt.insert(i)
        return rt

    def test_first_element(self):
        rt = self.prepare_stream()
        self.assertEqual(rt.rank(1), 0)
    
    def test_middle_elements(self):
        rt = self.prepare_stream()
        self.assertEqual(rt.rank(3), 1)
        self.assertEqual(rt.rank(4), 3)
    
    def test_last_element(self):
        rt = self.prepare_stream()
        self.assertEqual(rt.rank(13), 8)


        

if __name__ == "__main__":
    unittest.main()
