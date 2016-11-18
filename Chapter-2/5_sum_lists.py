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
        sum_l = sum_list(self.list1, self.list2)
        self.print_node(sum_l)




