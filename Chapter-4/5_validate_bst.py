"""Implement a function to check if a binary tree in binary search tree."""

import unittest
import math
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_bst(root):
    if root is None:
        return True
    if (root.right and root.data >= root.right.data) or (root.left and root.data < root.left.data):
        return False
    return is_bst(root.left) and is_bst(root.right)


def is_bst_better(root, Min, Max):
    if root is None:
        return True
    if (Max != None and root.data > Max) or (Min != None and root.data <= Min):
        return False
    return is_bst_better(root.left, Min, root.data) and is_bst_better(root.right, root.data, Max)



class TestIsBST(unittest.TestCase):
    def setUp(self):
        self.root = Node(4)
        self.root.left = Node(2)
        self.root.left.left = Node(1)
        self.root.left.right = Node(3)
        self.root.right = Node(6)
        self.root.right.left = Node(5)
        self.root.right.right = Node(7)

    def test_positive(self):
        self.assertEqual(is_bst_better(self.root, -1 * math.inf, math.inf), True)


if __name__ == "__main__":
    unittest.main()