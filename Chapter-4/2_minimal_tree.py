"""Given a sorted(Increasing order) array with unique elements
write an alorithm to create binay search tree with minimal heights"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_minimal_tree(array):
    if not len(array):
        return None
    mid = len(array)/2
    node = Node(array[mid])
    node.left = build_minimal_tree(array[0 : mid - 1])
    node.right = build_minimal_tree(array[mid + 1 : 0])
    return node


if __name__ == '__main__':
    print build_minimal_tree([1])
    print build_minimal_tree([1, 2, 3, 4, 5])
    print build_minimal_tree([1, 2, 3, 4, 5, 6])
