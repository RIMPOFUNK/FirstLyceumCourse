import sys


length = list(map(lambda x: int(x), sys.stdin.readlines()))
print(sum(length) / len(length)) if length else print(-1)
