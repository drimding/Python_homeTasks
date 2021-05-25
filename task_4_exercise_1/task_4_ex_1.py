"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""


def swap_quotes(txt):
    for i in range(len(txt)):
        if txt[i] == '"':
            txt = txt[:i] + '\'' + txt[i + 1:]
        elif txt[i] == '\'':
            txt = txt[:i] + '\"' + txt[i + 1:]
    return txt