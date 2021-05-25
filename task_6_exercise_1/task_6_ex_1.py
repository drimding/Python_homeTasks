"""
Implement function combine_dicts, which receives a changeable
number of dictionaries (keys - letters, values - integers)
and combines them into one dictionary.

Dict values should be summarized in case of identical keys.

Example:
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

combine_dicts(dict_1, dict_2)
Result: {'a': 300, 'b': 200, 'c': 300}

combine_dicts(dict_1, dict_2, dict_3)
Result: {'a': 600, 'b': 200, 'c': 300, 'd': 100}
"""
from string import ascii_lowercase


def combine_dicts(*args: dict):
    result = {}
    for arg in args:
        for k, v in arg.items():
            if not str(k).isalpha() or len(k) > 1:
                raise KeyError
            if not isinstance(v, int):
                raise ValueError
            if k in result:
                result[k] += v
            else:
                result.update({k: v})
    return result

