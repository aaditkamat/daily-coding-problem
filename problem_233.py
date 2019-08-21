"""
This problem was asked by Apple.

Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
"""

def fib(n: int) -> int:
    if n <= 0:
        raise ValueError(f"The value of function argument must be greater than or equal to 1")
    first, second = 0, 1
    for i in range(3, n + 1, 2):
        first += second
        second += first
    return first if n % 2 == 1 else second

if __name__ == '__main__':
    assert fib(1) == 0
    assert fib(2) == 1
    assert fib(5) == 3 
    assert fib(8) == 13
    
