"""
A binary search tree was created by traversing through an array from left to right and inserting 
each element. Given binary search tree with distinct elements, print all possible arrays that could have
lef to this tree.
"""

from collections import deque
import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bst_sequence(root):
    result = all_sequence(root)
    return [list(res) for res in result]
    
def all_sequence(root):
    result = []
    if root is None:
        result.append([])
        return result
    
    prefix = deque()
    prefix.append(root.data)
    # Recurse on left and right subtree
    left_seq = all_sequence(root.left)
    right_seq = all_sequence(root.right)

    
    # weave left each list from the left and right sides together
    for left in left_seq:
        for right in right_seq:
            weaved = []
            weave(left, right, weaved, prefix)
            result.extend(weaved)
    return result


def weave(first_list, second_list, results, prefix):
    if len(first_list) == 0 or len(second_list) == 0:
        result = deque()
        result.extend(prefix)
        result.extend(first_list)
        result.extend(second_list)
        results.append(result)
        return 
    
    headFirst = first_list.popleft()
    prefix.append(headFirst)
    weave(first_list, second_list, results, prefix)
    prefix.pop()
    first_list.appendleft(headFirst)

    headSecond = second_list.popleft()
    prefix.append(headSecond)
    weave(first_list, second_list, results, prefix)
    prefix.pop()
    second_list.appendleft(headSecond)


class TestBSTSequence(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        self.root = Node(2)
        self.root.left = Node(1)
        self.root.right = Node(3)
        self.assertEqual(bst_sequence(self.root), [[2, 1, 3], [2, 3, 1]])

if __name__ == "__main__":
    unittest.main()