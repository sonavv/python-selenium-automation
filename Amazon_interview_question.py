import timeit

def unique_letter(string: str):
    string = string.lower()
    for l in string:
        if string.count(l) == 1:
            return l

print(unique_letter('google'))

def unique_letter_optimal(string: str):
    string = string.lower()
    d = {}
    for l in string:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    for k, v in d.items():
        if v == 1:
            return k
print(unique_letter_optimal('googe'))

setup_code_1 = """
from __main__ import unique_letter
string = 'llajhgjvjidnnfnm n llajhgjvjidnnfnm '
"""
setup_code_2 = """
from __main__ import unique_letter_optimal
string = 'llajhgjvjidnnfnm n llajhgjvjidnnfnm '"""

print(timeit.timeit(stmt="unique_letter(string)", setup=setup_code_1, number=10000))
print(timeit.timeit(stmt="unique_letter_optimal(string)", setup=setup_code_2, number=10000))