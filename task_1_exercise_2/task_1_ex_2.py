"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse
import operator
import math
from inspect import signature

def calculate(args):
    # Your code
    try:
        numbers = [int(i) for i in args.user_input]
    except ValueError:
        raise NotImplementedError
    if args.operation in dir(operator):
        function = getattr(operator, args.operation)
        if len(signature(function).parameters) > 0:
            return function(numbers[0])
        elif len(signature(function).parameters) > 1:
            return function(numbers[0], numbers[1])
    elif args.operation in dir(math):
        function = getattr(math, args.operation)
        if len(signature(function).parameters) > 0:
            return function(numbers[0])
        elif len(signature(function).parameters) > 1:
            return function(numbers[0], numbers[1])
    else:
        raise NotImplementedError

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('operation')
    parser.add_argument('user_input', type=str, nargs='+')
    args = parser.parse_args()
    print(calculate(args))


if __name__ == '__main__':
    main()