"""Task 1
For a given integer n calculate the value which is equal to a:
- squared number, if its value is strictly positive;
- modulus of a number, if its value is strictly negative;
- zero, if the integer n is zero.

Example,
n = 4 result = 16
n = -5 result = 5
n = 0 result = 0

Example of how the task should be called:
python3 task_3_ex_1.py 4

Note: use argparse module for parsing arguments from CLI
"""
import argparse

def calculate(n):
    # Your code
    if n > 0:
        n = n * n
    elif n < 0:
        n = abs(n)

    return n


def main():
    parser = argparse.ArgumentParser(description="Please enter integer number for the calculate ")
    parser.add_argument('n', type=int, )
    args = parser.parse_args()
    print(calculate(args.n))


if __name__ == '__main__':
    main()
