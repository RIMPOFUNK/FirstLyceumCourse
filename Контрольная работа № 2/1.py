from sys import stdin
from numpy import median


num = int(input())
for i in stdin.readlines():
    val = list(sorted(filter(lambda t: not t % num, map(int, i.split()))))
    print(median(val)) if val else print(-1)
        

    

