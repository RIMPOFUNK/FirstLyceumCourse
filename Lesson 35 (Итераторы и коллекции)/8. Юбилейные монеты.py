from functools import reduce
from sys import stdin


even, ret = [], 0
for i in [(int(i.split()[0]), ' '.join(i.split()[1:])) for i in stdin.readlines()]:
    if i not in even:
        even.append(i)
    else:
        ret += i[0]
print(ret)