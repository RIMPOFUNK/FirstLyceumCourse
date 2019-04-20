height, width = int(input()), int(input())

lst = [list(input()) for _ in range(height)]

del lst[1::2]

for i in range(len(lst)):
    del lst[i][1::2]

for i in lst:
    print(*i, sep='')
