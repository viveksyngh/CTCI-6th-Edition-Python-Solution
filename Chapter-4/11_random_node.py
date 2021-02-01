"""
You are implementing a binary tree class from scratch, which, in addition to insert, find, and delete
has a method getRandomNode() which returns a random node from the tree. All nodes should be equally likely
to be chosen. Design and implement an algorithm form getRandomNode(), and explain how you would implemnets
the rest of the methods.
"""
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.size = 1

class Tree:
    def __init__(self):
        self.root  = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        self.insert_helper(self.root, data)
    
    def insert_helper(self, root, data):
        if data <= root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self.insert_helper(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self.insert_helper(root.right, data)
        root.size += 1
    
    def find(self, data):
        return self.find_helper(self.root, data)

    def find_helper(self, root, data):
        if root is None:
            return None

        if root.data == data:
            return root
        
        if data < root.data:
            return self.find_helper(root.left, data)
        else:
            return self.find_helper(root.right, data)

    def get_random_node(self):
        return self.get_random_node_helper(self.root)
    
    def get_random_node_helper(self, root):
        left_size = root.left.size if root.left else 0
        rand_value = random.randint(0, root.size)
        if rand_value < left_size:
            return self.get_random_node_helper(root.left)
        elif rand_value == left_size:
            return root
        else:
            return self.get_random_node_helper(root.ight)
        





    
