"""Useful binary search functions.
bisect — Array bisection algorithm: 
https://docs.python.org/3/library/bisect.html"""

# find the right most position to insert the element
def bisect_right(array, target):
    left, right = 0, len(array)   # note: right
    while left < right:
        mid = (left + right) // 2
        if target < array[mid]:
            right = mid
        else:
            left = mid + 1
    return left

# find the left most position to insert the element
def bisect_left(array, target):
    left, right = 0, len(array)   # note: right
    while left < right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
