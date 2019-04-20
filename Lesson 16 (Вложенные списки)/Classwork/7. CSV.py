size = int(input())
table = [input().split(',') for _ in range(size)]

size = int(input())
index = [input().split(',') for _ in range(size)]

for i in range(len(index)):
    for j in range(1):
        print(table[int(index[i][j])][int(index[i][j + 1])])
