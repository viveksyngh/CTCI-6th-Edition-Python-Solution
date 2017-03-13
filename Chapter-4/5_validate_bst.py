"""Implement a function to check if a binary tree in binary search tree."""

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


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(7)
    print is_bst(root)
    print is_bst_better(root, None, None)
