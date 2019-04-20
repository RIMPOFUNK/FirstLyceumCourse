from sys import stdin
from functools import reduce


def lex_sum(val: str):
    return sum(ord(i) for i in val[:3])


val = [i.replace('\n', '') for i in stdin.readlines()]
print(reduce(lambda x, y: x if (lex_sum(x) < lex_sum(y)) else y, val, val[0]))

