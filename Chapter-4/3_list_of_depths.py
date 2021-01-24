"""Given a binary tree, design an algorithm which creates linked list 
of all the nodes at each depth."""


class ListNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, node):
        node.next = self.head
        self.head = node
    
    def print_list(self):
        node = self.head
        while node:
            print(node.data, ' -> ')
            node = node.next
        print('null')
        

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

level_list_map = {}

def list_of_depths(root, level):
    if root == None:
        return 
    if not level_list_map.get(level):
        level_list_map[level] = LinkedList()
    level_list_map[level].add_node(root)
    list_of_depths(root.left, level + 1)
    list_of_depths(root.right, level + 1)


if __name__ == '__main__':
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    list_of_depths(root, 1)
    for key, data in level_list_map.items():
        data.print_list()

    