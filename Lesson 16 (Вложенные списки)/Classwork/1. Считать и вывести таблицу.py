first = int(input())
second = int(input())

lst = [[0] * second for _ in range(first)]

for i in range(first):
    for j in range(second):
        lst[i][j] = input()
        
for i in range(first):
    for j in range(second):
        print(lst[i][j], end='\t')
    print()