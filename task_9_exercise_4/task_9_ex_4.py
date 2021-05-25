"""
Implement a bunch of functions which receive a changeable number of strings and return next
parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
  Note: raise ValueError if there are less than two strings
4) characters of alphabet, that were not used in any string
  Note: use `string.ascii_lowercase` for list of alphabet letters

Note: raise TypeError in case of wrong data type

Examples,
```python
test_strings = ["hello", "world", "python", ]
print(chars_in_all(*test_strings))
>>> {'o'}
print(chars_in_one(*test_strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(chars_in_two(*test_strings))
>>> {'h', 'l', 'o'}
print(not_used_chars(*test_strings))
>>> {'q', 'k', 'g', 'f', 'j', 'u', 'a', 'c', 'x', 'm', 'v', 's', 'b', 'z', 'i'}
"""
import string


def chars_in_all(*strings):
    result = None
    for word in strings:
        if result is None:
            result = chars_in_one(word)
        else:
            result = result & chars_in_one(word)
    return result


def chars_in_one(*strings):
    return set(''.join(strings))


def chars_in_two(*strings):
    if len(strings) < 2:
        raise ValueError
    result = set()
    for i in range(len(strings)):
        for j in range(i, len(strings)-1):
            result |= chars_in_one(strings[j+1]) & chars_in_one(strings[i])
    return result


def not_used_chars(*strings):
    result = set(string.ascii_lowercase)
    for word in strings:
        result -= chars_in_one(word)
    return result
