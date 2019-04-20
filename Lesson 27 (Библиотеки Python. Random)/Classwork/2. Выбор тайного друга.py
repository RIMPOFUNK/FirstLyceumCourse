import sys
from random import choice, shuffle


names = [i.strip() for i in sys.stdin.readlines()]
tmp = names[:]
shuffle(tmp)

while names:
    i = 0
    while i < len(tmp) and tmp[i] == names[0]:
        i += 1
    print(f"{names.pop(0)} - {tmp.pop(i)}")

