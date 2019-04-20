import sys


def summ(val):
    return sum([ord(i.upper()) - ord('A') + 1 for i in val])


print(*sorted(sorted(sys.stdin.read().split()), key=lambda x: summ(x)), sep='\n')
