import sys


print(any(filter(lambda x: '0' in x.split(), sys.stdin.readlines())))
