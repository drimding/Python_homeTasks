"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(str_to_split: str, delimiter=-1) -> list:
    result = []
    marker = 0
    lent = len(str_to_split)
    try:
        if delimiter == -1:
            raise TypeError
        delimiter = str(delimiter)
        for i in range(lent):
            if str_to_split[i] == delimiter:
                result.append(str_to_split[marker:i])
                marker = i + 1
            if i == lent - 1:
                result.append(str_to_split[marker:i + 1])
    except TypeError:
         raise ValueError
    return result