"""Implement a function to check if a binary tree is balanced."""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_height(root):
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1


def check_balanced(root):
    if root is None:
        return True
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    if abs(left_height - right_height) > 1:
        return False
    return check_balanced(root.left) and check_balanced(root.right)


def check_height(root):
    if root is None:
        return 0
    left_height = check_height(root.left)
    if left_height == -1:
        return -1
    
    right_height = check_height(root.right)
    if right_height == -1:
        return -1
    
    if abs(right_height - left_height) > 1:
        return -1
    return max(left_height, right_height) + 1


def check_balanced_1(root):
    return check_height(root) != -1


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(7)
    print check_balanced(root)
    print check_balanced_1(root)
