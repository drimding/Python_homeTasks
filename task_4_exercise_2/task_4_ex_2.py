"""
Task04_1_2
Write `is_palindrome` function that checks whether a string is a palindrome or not
Returns 'True' if it is palindrome, else 'False'

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

Note:
Usage of any reversing functions is prohibited.
The function has to ignore special characters, whitespaces and different cases
Raise ValueError in case of wrong data type
"""
import re

def is_palindrome(text):
    is_pal = True
    try:
        text = re.sub('\W+','',text).lower()
        print(text)
    except TypeError:
        raise ValueError
    if text.isdigit():
        comparator = int(text)
        rev = 0
        num = comparator
        while num > 0:
            dig = num % 10
            rev = rev * 10 + dig
            num = num // 10
            if comparator == rev:
                is_pal = True
            else:
                is_pal = False
    else :
        letters = list(text)
        for letter in letters:
            if letter == letters[-1]:
                letters.pop(-1)
            else:
                is_pal = False
                break
    return is_pal