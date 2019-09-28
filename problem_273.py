"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.

"""

# Similar to binary search:
# Time Complexity: O(log n)
# Space Complexity: O(1)
def has_fixed_point(arr: List) -> bool:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid:
            return True
        if arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return False
