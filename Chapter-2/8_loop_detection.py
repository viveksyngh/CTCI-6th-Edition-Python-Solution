# Given a circular linked lits, implement an algorithm that returns the node at the begining of the loop.

import unittest


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def loop_detection(head):
    slow_ptr = head
    fast_ptr = head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            break
    # if there is no circle
    if fast_ptr is None or fast_ptr.next is None:
        return None

    slow_ptr = head
    while slow_ptr != fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    return slow_ptr




