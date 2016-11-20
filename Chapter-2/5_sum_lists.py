# You have two numbers repersented by a single linked list, 
# where each node contains a single digit. The digits are in
# reverse order, such that the 1's digit is ate the head of the
# list, Write a function that adds the two numbers and returns
# the sum as linked list.
import unittest

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def sum_list(list1, list2):
    """This solution sum two numbers repersented by linked list,
       where each node in linked list repersent digits of numbers.
       
       Time Complexity: O(n)
       Space Complexity: O(n)
    """

    node1, node2  = list1, list2
    result, tail = None, None
    carry = 0
    while node1 or node2:
        val = carry
        if node1:
            val += node1.data
        if node2:
            val += node2.data
        node = Node(val%10)
        
        if result is None:
            result = node
            tail = result
        else:
            tail.next = node
            tail = node
        carry = val/10
        node1 = node1.next
        node2 = node2.next
    
    if carry:
        node = Node(carry)
        tail.next = node
        tail = node
    return result


def sum_list_recursive(list1, list2, carry):
    """This solution uses recursion to add two linked list.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    if list1 == None and list2 == None and carry == 0:
        return None
    val = carry
    if list1:
        val += list1.data
    if list2:
        val += list2.data

    result = Node(val%10)

    if list1 is not None or list2 is not None:
        if list1 is not None:
            list1 = list1.next
        if list2 is not None:
            list2 = list2.next
        more = sum_list_recursive(list1, list2, val/10)
        result.next = more
    return result

# Suppose digits are stored in forward order, Repeat the above problem
# Input : (6 -> 1 -> 7) + ( 2 -> 9 -> 5)
# Output: (9 -> 1 -> 2)

def sum_lists_reverse(list1, list2):
    """This solution some two numbers whose digits,
        are stored in forward order. 
        
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    l1 = get_length(list1)
    l2 = get_length(list2)

    if l1 > l2:
        list2 = pad_list(list2, l1 - l2)
    elif l2 > l1:
        list1 = pad_list(list1, l2 - l1)

    result, carry = sum_lists_reverse_helper(list1, list2)

    if carry != 0:
        result = insert_before(result, carry)
    return result

# Helper functions
def sum_lists_reverse_helper(list1, list2):
    """ Helper functions to sum reversed list."""
    if list1 is None and list2 is None:
        return None, 0
    result, carry = sum_lists_reverse_helper(list1.next, list2.next)
    val = list1.data + list2.data + carry
    final_result = insert_before(result, val%10)
    return final_result, val/10


def insert_before(result, val):
    """Helper function to insert a node at begining of linked list."""
    node = Node(val)
    node.next = result
    result = node
    return result


def get_length(list1):
    """Helper function to get length of linked list."""
    count = 0
    node = list1
    while node:
        node = node.next
        count += 1
    return count


def pad_list(list1, count):
    """Helper function to pad the list with zero in the begining."""
    node = list1
    for i in range(count):
        node = insert_before(node, 0)
    return node


class TestSumList(unittest.TestCase):

    def setUp(self):
        self.list1 = self.create_input_linked_list([7, 1, 6])
        self.list2 = self.create_input_linked_list([5, 9, 4])

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

    def print_node(self, head):
        node = head
        while node is not None:
            print str(node.data) + " ",
            node = node.next
        print ''

    def test_sum_list_1(self):
        self.print_node(self.list1)
        self.print_node(self.list2)
        sum_l = sum_list_recursive(self.list1, self.list2, 0)
        self.print_node(sum_l)

    def test_sum_list_reverse(self):
        self.print_node(self.list1)
        self.print_node(self.list2)
        sum_l = sum_lists_reverse(self.list1, self.list2)
        self.print_node(sum_l)




