"""Write an algorithm to find next node (i.e inorder successor) of a given node 
in binary search tree. """

class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
    

def find_left_most_node(root):
    node = root
    while node.left:
        node = node.left
    return node


def find_successor(root, node):
    if root is None:
        return None
    if node.right :
        return find_left_most_node(node.right)
    else:
        x = node
        n = node.parent
        while n and n.left != x:
            x = n
            n = n.parent
        return n


