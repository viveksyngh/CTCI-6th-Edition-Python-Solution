"""
A magic index is an array A[0...n-1] is defined to be index such that A[i] = i. Given a sorted array of distinct
integers, write a method to find a magic index, if one exists, in array A.

FOLLOW UP

What if the values are not distinct ?
"""

def magic_index(arr):
    low, high = 0, len(arr)-1
    while low <= high: 
        mid = (low + high)//2
        if arr[mid] == mid:
            return mid
        
        if arr[mid] > mid:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1


def magic_index_followup(arr):
    if len(arr) == 0:
        return -1

def magic_index_followup_helper(arr, low, high):
    if low > high:
        return -1
    mid = (low + high)//2
    midValue = arr[mid]

    if midValue == mid:
        return mid
    
    left_index = min(mid-1, midValue)
    left_value = magic_index_followup_helper(arr, low, left_index)
    if  left_value >= 0:
        return left_value
    
    right_index = max(mid+1, midValue)
    right_value = magic_index_followup_helper(arr, right_index, high)
    if right_value >= 0:
        return right_value
    
    return -1