# Write an algorithm to return kth to the last of singly linked list

import unittest


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def get_size(head):
    """Helper function to get size of linked list."""
    length = 0
    current = head
    while current:
        current = current.next
        length += 1
    return length


def kth_to_last_size(head, k):
    """This solution find size of the linked list,
        then find (size - k)th node from the begining.

        Time Complexity: O(n)
        Space Complexity: O(1) 
    """

    n = get_size(head)
    if n < k :
        return None
    counter, current = 0, head
    while current and counter < n - k:
        current = current.next 
        counter += 1
    return current


def kth_to_last_without_size(head, k):
    """This solution find kth to last node,
        without knowing size of the linked list.

        Time Complexity: O(n)
        Space Complexity: O(1)
    """

    counter, first_ptr = 0, head
    while counter < k and first_ptr:
        counter += 1
        first_ptr = first_ptr.next
    
    if first_ptr is None:
        return None

    second_ptr = head
    while first_ptr:
        second_ptr = second_ptr.next
        first_ptr = first_ptr.next
    return second_ptr


def kth_to_last_helper(head, k):
    """Helper function to get kth to last node recursively."""
    if head is None:
        return None, 0
    node, i = kth_to_last_helper(head.next, k) 
    i += 1
    if k == i:
        return head, i
    return node, i


def kth_to_last_recursive(head, k):
    """This solution finds kth to the last node recursively."""
    node, index = kth_to_last_helper(head, k)
    return node


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
        print "Solution 1 : ",
        node = kth_to_last_size(head, 1)
        print node.data
        print "Solution 2 : ",
        node =  kth_to_last_without_size(head, 1)
        print node.data
        print "Solution 3 : ",
        node =  kth_to_last_recursive(head, 1)
        print node.data

    def test_case_2(self):
        first_node = Node(1)
        second_node = Node(2)
        third_node = Node(3)
        fourth_node = Node(4)
        head = first_node
        first_node.next = second_node
        second_node.next = third_node
        third_node.next = fourth_node
        print "Solution 1 : ",
        node = kth_to_last_size(head, 2)
        print node.data
        print "Solution 2 : ",
        node =  kth_to_last_without_size(head, 2)
        print node.data
        print "Solution 3 : ",
        node =  kth_to_last_recursive(head, 2)
        print node.data

    def test_case_3(self):
        first_node = Node(1)
        second_node = Node(2)
        third_node = Node(3)
        fourth_node = Node(4)
        head = first_node
        first_node.next = second_node
        second_node.next = third_node
        third_node.next = fourth_node
        print "Solution 1 : ",
        node = kth_to_last_size(head, 3)
        print node.data
        print "Solution 2 : ",
        node =  kth_to_last_without_size(head, 3)
        print node.data
        print "Solution 3 : ",
        node =  kth_to_last_recursive(head, 3)
        print node.data



