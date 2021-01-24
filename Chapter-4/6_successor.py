"""Write an algorithm to find next node (i.e inorder successor) of a given node 
in binary search tree. """

import unittest
class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
    

def find_left_most_node(root):
    node = root
    while node.left:
        node = node.left
    return node


def find_successor(root, node):
    if root is None:
        return None
    # If node has right subtree then find the leftmost element in right subtree
    if node.right :
        return find_left_most_node(node.right)
    # if node is left of parent then return it 
    # Else find the parent which has unexplored right subtree and return it
    else:
        x = node
        n = node.parent
        while n and n.left != x:
            x = n
            n = n.parent
        return n


class TestInOrder(unittest.TestCase):
    def setUp(self):
        self.root = Node(4)
        self.two = Node(2, parent=self.root)
        self.root.left = self.two
        self.one = Node(1, parent=self.two)
        self.root.left.left = self.one
        self.three = Node(3, parent=self.two)
        self.root.left.right = self.three
        self.root.right = Node(6, parent=self.root)
        self.root.right.left = Node(5, parent=self.root.right)
        self.seven = Node(7, parent=self.root.right)
        self.root.right.right = self.seven

    def test_positive(self):
        self.assertEqual(find_successor(self.root, self.two), self.three)
        self.assertEqual(find_successor(self.root, self.one), self.two)
        self.assertEqual(find_successor(self.root, self.three), self.root)
        self.assertEqual(find_successor(self.root, self.seven), None)


if __name__ == "__main__":
    unittest.main()