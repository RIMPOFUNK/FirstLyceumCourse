size = int(input())

lst = sorted([int(input()) for _ in range(size)], reverse=True)
for i in lst:
    print(i)