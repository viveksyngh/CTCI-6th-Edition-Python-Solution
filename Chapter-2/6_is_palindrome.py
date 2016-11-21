# Check whether a linked list is palindrome or or not.
import unittest


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def is_palindrome(linked_list):
    """This solution reverses the original linked list and 
        then compares the linked_list.

        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    reverse_list = reverse(linked_list)
    node1 = linked_list
    node2 = reverse_list
    while node1 and node2:
        if node1.data != node2.data:
            return False
        node1 = node1.next
        node2 = node2.next
    if node1 != None or node2 != None:
        return False
    return True


def reverse(linked_list):
    """Reverse a linked list"""
    head = None
    node = linked_list
    while node:
        if head is None:
            head = Node(node.data)
        else:
            new_node = Node(node.data)
            new_node.next = head
            head = new_node
        node = node.next
    return head


def is_palindrome_stack(linked_list):
    """This solution uses a stack data structure."""
    stack = []
    fast = linked_list
    slow = linked_list

    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next
        fast = fast.next

    if fast is not None:
        slow = slow.next

    while slow:
        item = stack.pop()
        if item != slow.data:
            return False
        slow = slow.next
    return True


class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.input = self.create_input_linked_list([0, 1, 1, 2, 2, 1, 1, 0])
        self.input = self.create_input_linked_list([1, 2])
        self.input = self.create_input_linked_list([1])

    def create_input_linked_list(self, input_list):
        head, end = None, None
        for data in input_list:
            node = Node(data)
            if head is None:
                head = node
                end = head
            else:
                end.next = node
                end = node
        return head

    def print_list(self, head):
        node = head
        while node is not None:
            print str(node.data) + " ",
            node = node.next
        print ''

    def test_is_palindrome(self):
        self.print_list(self.input)
        self.print_list(reverse(self.input))
        print is_palindrome(self.input)
    
    def test_is_palindrome_stack(self):
        self.print_list(self.input)
        self.print_list(reverse(self.input))
        print is_palindrome_stack(self.input)


