"""
T1 and T2 are two very large binary trees, with T1 much larger than T2. Create an algorithm to determine
if T2 is a subtree of T1.

A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
"""
import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def simeple_solution(t1, t2):
    t1_builder, t2_builder = [], []
    preorder(t1, t1_builder)
    preorder(t2, t2_builder)
    
    return "".join(t2_builder) in "".join(t1_builder) 

def preorder(root, items):
    if root is None:
        items.append('X')
        return 
    
    items.append(str(root.data))
    preorder(root.left, items)
    preorder(root.right, items)


def alternate_solution(t1, t2):
    if t2 is None:
        return True
    return subtree(t1, t2)


def subtree(t1, t2):
    if t1 is None:
        return False
    elif t1.data == t2.data and match_tree(t1, t2):
        return True
    else:
        return subtree(t1.left, t2) or subtree(t1.right, t2)

def match_tree(t1, t2):
    if t1 is None and t2 is None:
        return True
    
    if t1 is None or t2 is None:
        return False
    
    if t1.data != t2.data:
        return False
    
    return match_tree(t1.left, t2.left) and match_tree(t1.right, t2.right)


class TestSutree(unittest.TestCase):
    def setUp(self):
        self.t1 = Node(6)
        self.t1.left = Node(2)
        self.t1.right = Node(7)
        self.t1.left.right = Node(4)
        self.t1.left.left = Node(1)
        self.t1.left.right.left = Node(3)
        self.t1.left.right.right = Node(5)

        self.t2 = Node(2)
        self.t2.left = Node(1)
        self.t2.right = Node(4)
        self.t2.right.left = Node(3)
        self.t2.right.right = Node(5)


    def test_simple_solution(self):
        self.assertEqual(simeple_solution(self.t1, self.t2), True)

    def test_alternate_solution(self):
        self.assertEqual(simeple_solution(self.t1, self.t2), True)

if __name__ == "__main__":
    unittest.main()