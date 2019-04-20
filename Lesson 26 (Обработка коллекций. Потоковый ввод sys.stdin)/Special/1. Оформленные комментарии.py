import sys


tmp = sys.stdin.read().split('\n')
lst = {i + 1: tmp[i] for i in range(len(tmp))}

for i in filter(lambda x: '#' in lst[x].lstrip(), lst):
    print(f"Line {i}: {lst[i].replace('#', '').lstrip()}")
