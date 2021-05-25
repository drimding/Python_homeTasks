"""
Task 2_3

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""
import argparse

def bounded_knapsack(args):
    result = 0
    for i in sorted(args.w, reverse=True):
        if result + i <= args.W:
            result += i
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-W",  type=int, help="capacity")
    parser.add_argument("-w", nargs="*", type=float, help="weight")
    parser.add_argument("-n",  type=int, help="bars_number")
    args = parser.parse_args()
    if not all ([args.W, args.w, args.n]) or args.W<0 or  any(i < 0 for i in args.w) or args.n<0:
        raise ValueError
    print(bounded_knapsack(args))


if __name__ == '__main__':
    main()
