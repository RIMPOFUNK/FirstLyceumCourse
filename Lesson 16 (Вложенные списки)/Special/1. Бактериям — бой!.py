size = int(input())
lst = []

for i in range(size):
    lst.append([0] * size)
    for j in range(size):
        lst[i][j] = int(input())
count = int(input())

for i in range(count):
    x, y = int(input()), int(input())
    for _x in range(-1, 2):
        for _y in range(-1, 2):
            if not _x and not _y:
                lst[y][x] -= 8
                lst[y][x] = 0 if lst[y][x] < 0 else lst[y][x]
            elif 0 <= x + _x < size and 0 <= y + _y < size:
                lst[y + _y][x + _x] -= 4
                lst[y + _y][x + _x] = 0 if lst[y + _y][x + _x] < 0 else lst[y + _y][x + _x]

for i in lst:
    print(*i, end=' ')
    print()
