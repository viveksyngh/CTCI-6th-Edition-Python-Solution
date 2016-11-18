# Write a code to partition a linked list around a value x, 
# such that all nodes less than x come before all nodes
# greater than or equal to x. if x is contained within the list,
# the value of x only need to be after the elements less than x.
# The partition element x can appear anywhere in the "right partition";
# It does not need to appear between the left and right partitions.
import unittest


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None



def partition(head, x):
    """This solution creates two linked list 
        one with value smaller than x, 
        other with value greater than equal to x.
        then combines both linked list.

        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    
    lowHead = None
    lowEnd = None
    highHead = None
    highEnd = None
    node = head
    while node:
        next_node = node.next
        if node.data < x:
            if lowHead is None:
                lowHead = node
                lowEnd = lowHead
            else:
                lowEnd.next = node
                lowEnd = node
        else:
            if highHead is None:
                highHead = node
                highEnd = highHead
            else:
                highEnd.next = node
                highEnd = node
        node = next_node
    lowEnd.next = highHead
    highEnd.next = None
    return lowHead


def partition_1(head, x):
    """This solution uses only two variables as 
        compared to four variables used by above solution.

        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    
    start = head
    end = head
    node = head
    while node:
        node_next = node.next
        if node.data < x:
            node.next = start
            start = node
        else:
            end.next = node
            end = node
        node = node_next
    end.next = None
    return start

class TestPartition(unittest.TestCase):

    def setUp(self):
        self.input = None
        self.end = None

    def test_case_partition(self):
        self.create_input_linked_list([3, 5, 8, 5, 10, 2, 1])
        self.print_node(self.input)
        self.output = partition(self.input, 5)
        self.print_node(self.output)

    def test_case_partition_1(self):
        self.create_input_linked_list([3, 5, 8, 5, 10, 2, 1])
        self.print_node(self.input)
        self.output = partition_1(self.input, 5)
        self.print_node(self.output)

    def create_input_linked_list(self, input_list):
        # input_list = [3, 5, 8, 5, 10, 2, 1]
        for data in input_list:
            node = Node(data)
            if self.input is None:
                self.input = node
                self.end = self.input
            else:
                self.end.next = node
                self.end = node

    def print_node(self, head):
        node = head
        while node is not None:
            print str(node.data) + " ",
            node = node.next
        print ''

