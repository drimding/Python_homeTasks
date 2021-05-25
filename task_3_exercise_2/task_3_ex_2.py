"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""
import re
import argparse

def from_roman_numerals(args):
    roman_library = {'I' : 1, 'II' : 2, 'III' : 3, 'IV' : 4, 'V' : 5, 'VI' : 6, 'VII' : 7, 'VIII' : 8, 'IX' : 9, 'X' : 10,
             'XI' : 11, 'XX' : 20, 'XXX' : 30, 'XL' : 40, 'L' : 50, 'LX' : 60, 'LXX' : 70, 'LXXX' : 80, 'XC' : 90, 'C' : 100}

    result = re.findall('^(C{0,3})(L?X{0,3}|X[LC])(V?I{0,3}|I[VX])$', args.user_input)

    if result :
        arabic = 0
        result = result[0]
        for value in result:
            if value:
                arabic += roman_library.get(value)
        return arabic
    else:
        raise ValueError


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('user_input', type=str)
    args = parser.parse_args()
    print(from_roman_numerals(args))


if __name__ == "__main__":
    main()
