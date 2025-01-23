#!/usr/bin/env python3
from itertools import product

def imply(p, q):
    return not p or q

def tabular(arr):
    return ' \\\\\n'.join(
        ' & '.join(str(int(cell)) for cell in row)
        for row in arr)

# 问题 2.3.21
# (1)
print(tabular(map(
    lambda ps: (ps[0],
                ps[1],
                imply(*ps),
                ps[0] and imply(*ps),
                imply(ps[0] and imply(*ps), ps[1])),
    product([True, False], repeat=2)
)))

# (2)
print(tabular(map(
    lambda ps: (ps[0],
                ps[1],
                imply(*ps),
                imply(imply(*ps), ps[0]),
                not ps[0],
                imply(imply(*ps), ps[0]) and not ps[0]),
    product([True, False], repeat=2)
)))
