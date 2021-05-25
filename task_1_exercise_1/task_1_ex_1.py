"""01-Task1-Task1
Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and
data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py 1 * 2

Notes:
For other operations need to raise NotImplementedError.
Do not dynamically execute your code (for example, using exec()).
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse

def calculate(args):
    # Your code
    # Addition function
    def add(a, b):
        val = a + b
        return val

    # Subtraction function
    def sub(a, b):
        val = a - b
        return val

    # Division function
    def div(a, b):
        val = a / b
        return val

    # Multiplication function
    def multi(a, b):
        val = a * b
        return val

    parser = argparse.ArgumentParser()
    parser.add_argument('digit_1', type=float)
    parser.add_argument('operation', type=str)
    parser.add_argument('digit_2', type=float)
    args = parser.parse_args()
    if args.operation == '+':
        return add(args.digit_1, args.digit_2)
    elif args.operation == '-':
        return sub(args.digit_1, args.digit_2)
    elif args.operation == '/':
        return div(args.digit_1, args.digit_2)
    elif args.operation == '*':
        return multi(args.digit_1, args.digit_2)
    else:
        raise NotImplementedError
    pass


def main():
    args = None
    print(calculate(args))


if __name__ == '__main__':
    main()
