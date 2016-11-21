# Given two (singly) linked list, determine if two linked list intersect.
# Return intersecting node.

import unittest


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def intersection(list1, list2):
    list1_len = get_length(list1)
    list2_len = get_length(list2)

    if list1_len > list2_len:
        smaller = list2
        larger = list1
    else:
        smaller = list1
        larger = list2

    smaller_ptr = smaller
    larger_ptr = larger
    for i in range(abs(list1_len - list2_len)):
        larger_ptr = larger_ptr.next

    while smaller_ptr and larger_ptr:
        if smaller_ptr and larger_ptr and (smaller_ptr == larger_ptr):
            return True, smaller_ptr
        smaller_ptr = smaller_ptr.next
        larger_ptr = larger_ptr.next
    return False, None


def get_length(list1):
    """Helper function to get length of linked list."""
    count = 0
    node = list1
    while node:
        node = node.next
        count += 1
    return count

