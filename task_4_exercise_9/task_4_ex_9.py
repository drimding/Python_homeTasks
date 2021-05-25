"""
For a positive integer n calculate the result value, which is equal to the sum
of the odd numbers of n.

Example,
n = 1234 result = 4
n = 246 result = 0

Write it as function.

Note:
Raise TypeError in case of wrong data type or negative integer;
Use of 'functools' module is prohibited, you just need simple for loop.
"""


def sum_odd_numbers(n: int) -> int:
    # Your code
    if not isinstance(n, int) or n <=0 or isinstance(n, bool):
        raise TypeError
    result = 0
    n = str(n)
    for i in range(len(n)):
        if int(n[i]) % 2 != 0:
            result = result + int(n[i])
    return result
