import sys


print(len(list(filter(lambda x: x.lstrip().startswith('#'), sys.stdin.readlines()))))