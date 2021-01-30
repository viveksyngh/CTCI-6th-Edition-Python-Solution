"""
Design an algorithm and write code to find first common ancestor of two nodes in 
a binary tree. Avoid storing additionals nodes in a data structure.

NOTE: This is not necessarily a binary search tree.
"""

def first_common_ancestor(root, p, q):
    if not covers(root, p) or not covers(root, q):
        return None

def first_common_ancestor_helper(root, p, q):
    if root is None or root == p or root == q:
        return root
    
    pleft = covers(root.left, p)
    qleft = covers(root.left, q)
    if pleft != qleft:
        return root
    child = root.left if pleft else root.right
    return  first_common_ancestor_helper(child, p, q)

def covers(root, p):
    if root is None:
        return False
    if root == p:
        return True
    return covers(root.left, p) or covers(root.right, q)