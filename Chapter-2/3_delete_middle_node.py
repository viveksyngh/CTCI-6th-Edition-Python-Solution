# Implement an algorithm to delete a node in middle (i.e any node but the first and last node,
# not necessarily in the exact middle) of a singly linked list, given only access to that node
import unittest


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def delete_middle_node(node):
    if node == None or node.next == None:
        return False
    node.data = node.next.data
    node.next = node.next.next
    return True


class TestKthToLast(unittest.TestCase):

    def test_case_1(self):
        first_node = Node(1)
        second_node = Node(2)
        third_node = Node(3)
        fourth_node = Node(4)
        head = first_node
        first_node.next = second_node
        second_node.next = third_node
        third_node.next = fourth_node
        self.print_node(head)
        delete_middle_node(second_node)
        self.print_node(head)

    def test_case_2(self):
        first_node = Node(1)
        second_node = Node(2)
        third_node = Node(3)
        fourth_node = Node(4)
        head = first_node
        first_node.next = second_node
        second_node.next = third_node
        third_node.next = fourth_node
        self.print_node(head)
        delete_middle_node(third_node)
        self.print_node(head)

    def print_node(self, head):
        node = head
        while node is not None:
            print str(node.data) + " ",
            node = node.next
        print ''

    def print_node(self, head):
        node = head
        while node is not None:
            print str(node.data) + " ",
            node = node.next
        print ''



 