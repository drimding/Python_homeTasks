"""
Create a function sum_binary_1 that for a positive integer n
calculates the result value, which is equal to the sum of the
“1” in the binary representation of n otherwise, returns None.

Example,
n = 14 = 1110 result = 3
n = 128 = 10000000 result = 1
"""


def sum_binary_1(n: int):
    # Your code
    if not (isinstance(n, int)) or n <= 0:
        return None
    n = list(str(bin(n)[2:]))
    result = 0
    for digit in n:
        result = result + int(digit)
    return result