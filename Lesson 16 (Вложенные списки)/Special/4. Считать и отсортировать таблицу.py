def bubble_sort(value: list):
    for i in range(len(value) - 1):
        for j in range(len(value) - i - 1):
            if value[j] > value[j + 1]:
                value[j], value[j + 1] = value[j + 1], value[j]
    return value


n, m = int(input()), int(input())

table = [[input() for i in range(m)] for _ in range(n)]

for i in range(len(table)):
    for j in range(len(table[i])):
        if 0 < i <= n - 2:
            tmp = bubble_sort(table[i])
            print(tmp[j], end='\t')
        else:
            print(table[i][j], end='\t')
    print()
