"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

from typing import List

def prod(lst):
    result = []
    curr = 1
    for num in lst:
       result.append(curr * num)
       curr *= num
    result.reverse()
    result.append(1)
    return result

def get_right_products(lst: List[int]) -> List[int]:
    """Get products of the array element from the right starting with 1 at the 1st position
    e.g. for [1, 2, 3, 4, 5] you will et [1, 5, 20, 60, 120, 120]
    """
    return prod(lst[: : -1])

def prod_without_self(lst: List[int]) -> List[int]:
    """For each element in the list, get the stored products of all the element to th
    right using the get_right_products function and multiply that with the product calculated 
    during the iteration from left""" 
    right_prod = get_right_products(lst)
    curr_prod = 1
    result = []
    for i in range(len(lst)):
        result.append(right_prod[i + 1] * curr_prod)
        curr_prod *= lst[i]
    return result

if __name__ == '__main__':
    assert prod_without_self([]) == []
    assert prod_without_self([3]) == [1]
    assert prod_without_self([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert prod_without_self([3, 2, 1]) == [2, 3, 6]


