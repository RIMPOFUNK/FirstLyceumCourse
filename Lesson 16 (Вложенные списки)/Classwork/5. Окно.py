size = int(input())
values = [int(input()) for _ in range(size)]

minn = int(input())
maxx = int(input())

for i in values:
    if minn <= i <= maxx:
        print(i)
