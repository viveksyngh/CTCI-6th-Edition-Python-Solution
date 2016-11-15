# Write a code to remove duplicates from an unsorted linked list.
import unittest

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    """This solution uses has table to track duplicates.

        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    if head is None:
        return head
    
    node = head
    already_seen_values = {}
    already_seen_values[node.data] = True
    
    while node.next != None:
        if node.next.data in already_seen_values:
            node.next = node.next.next
        else:
            already_seen_values[node.next.data] = True
            node = node.next
    return head


def remove_duplicates_without_buffer(head):
    """ This solutions track duplicates without using any extra space.

        Time Complexity: O(n^2)
        Space Complexity: O(1)
    """

    if head is None:
        return head
    first_ptr = head

    while first_ptr != None:
        second_ptr = first_ptr
        while second_ptr.next != None:
            if second_ptr.next.data == first_ptr.data:
                second_ptr.next = second_ptr.next.next
            else:
                second_ptr = second_ptr.next
        first_ptr = first_ptr.next
    return head

# Testcases
class TestRemoveDups(unittest.TestCase):

    def test_case_1(self):
        first_node = Node(1)
        second_node = Node(2)
        third_node = Node(3)
        fourth_node = Node(4)
        head = first_node
        first_node.next = second_node
        second_node.next = third_node
        third_node.next = fourth_node 
        print "Input : ",
        self.print_node(head)
        head = remove_duplicates_without_buffer(head)
        print "Output : ",
        self.print_node(head)
        print ''

    def test_case_2(self):
        first_node = Node(2)
        second_node = Node(2)
        third_node = Node(3)
        fourth_node = Node(2)
        head = first_node
        first_node.next = second_node
        second_node.next = third_node
        third_node.next = fourth_node 
        print "Input : ",
        self.print_node(head)
        head = remove_duplicates_without_buffer(head)
        print "Output : ",
        self.print_node(head)
        print ''

    def test_case_3(self):
        first_node = Node(2)
        second_node = Node(2)
        third_node = Node(2)
        fourth_node = Node(2)
        head = first_node
        first_node.next = second_node
        second_node.next = third_node
        third_node.next = fourth_node 
        print "Input : ",
        self.print_node(head)
        head = remove_duplicates_without_buffer(head)
        print "Output : ",
        self.print_node(head)
        print ''

    def print_node(self, head):
        node = head
        while node is not None:
            print str(node.data) + " ",
            node = node.next
        print ''
