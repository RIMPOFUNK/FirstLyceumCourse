size = int(input())
table = []
table.append([0] * size)

for i in range(1, size):
    table.append([0] * size)
    count = 0
    for j in input().split():
        table[i][count] = int(j)
        table[count][i] = int(j)
        count += 1
for i in table:
    print(*i, sep=' ')
