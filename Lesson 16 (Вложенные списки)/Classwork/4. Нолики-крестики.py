size = int(input())
lst = [list(input()) for _ in range(size)]

winner = ""

for i in lst:
    for j in range(len(i) - 2):
        if i[j] == i[j + 1] == i[j + 2] == 'x' and not winner:
            winner = 'x'
            break
        if i[j] == i[j + 1] == i[j + 2] == 'o' and not winner:
            winner = 'o'
            break

for i in range(len(lst) - 2):
    for j in range(len(lst[i])):
        if lst[i][j] == lst[i + 1][j] == lst[i + 2][j] == 'x' and not winner:
            winner = 'x'
        elif lst[i][j] == lst[i + 1][j] == lst[i + 2][j] == 'o' and not winner:
            winner = 'o'

print(winner if winner else '-')
