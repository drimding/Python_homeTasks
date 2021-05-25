"""Implement a function `most_common_words(file_path: str, top_words: int) -> list`
which returns most common words in the file.
<file_path> - system path to the text file
<top_words> - number of most common words to be returned

Example:

print(most_common_words(file_path, 3))
>>> ['donec', 'etiam', 'aliquam']
> NOTE: Remember about dots, commas, capital letters etc.
"""
import re
from collections import Counter


def most_common_words(file_path: str, top_words: int):
    words_list = []
    result = []
    # read file and filter only [a-z|A-Z] words
    words_list += re.findall(r"[a-z|A-Z]+", open(file_path).read().lower())

    # Use collections Counter for count words in words_list
    words_counter = Counter(words_list).most_common(top_words)
    for word in words_counter:
        result.append(word[0])
    return result
