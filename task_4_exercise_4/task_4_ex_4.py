"""
Implement a function `split_by_index(string: str, indexes: List[int]) -> List[str]`
which splits the `string` by indexes specified in `indexes`. 
Only positive index, larger than previous in list is considered valid.
Invalid indexes must be ignored.

Examples:
```python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
```
"""


def split_by_index(str_to_split, indexes):
    # Your code
    result = []
    marker = 0
    str_to_split_lent = len(str_to_split)
    indexes_lent = len(indexes)
    if not indexes:
        result.append(str_to_split)
    for i in range(indexes_lent):
        try:
            if marker < indexes[i] < str_to_split_lent and i < indexes_lent:
                result.append(str_to_split[marker:indexes[i]])
                marker = indexes[i]
        except TypeError:
            continue
        if i == indexes_lent - 1:
            result.append(str_to_split[marker:])
    return result
