from functools import reduce
from sys import stdin
from math import gcd


print(reduce(lambda x, y: gcd(x, y),
             map(lambda t: int(t), stdin.readlines()),
             0))

