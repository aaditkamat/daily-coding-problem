"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
from typing import List
def twoSum(lst: List[int], k: int) -> bool:
    mapping = {}
    for num in lst:
        if num in mapping:
            return True
        mapping[k - num] = num
    return False

if __name__== '__main__':
    assert twoSum([10, 5, 3, 7], 17)
    assert not twoSum([4, 6, 3, 7], 8)
    assert twoSum([2, 2, 5, 6, 9], 4)
    assert not twoSum([], 2)
    assert not twoSum([1], 5)
    assert twoSum([3, 5, 9, 2, 5, 6, 12], 15)
