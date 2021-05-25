"""
Task 3

Implement a decorator `call_once` which runs `sum_of_numbers` function once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments.

Example:
@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))

>>> 55

print(sum_of_numbers(999, 100))

>>> 55

print(sum_of_numbers(134, 412))

>>> 55
"""
caches_result = None


def call_once(fn):
    def wrapper(a, b):
        global caches_result
        if caches_result is None:
            caches_result = fn(a, b)
        return caches_result
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b



