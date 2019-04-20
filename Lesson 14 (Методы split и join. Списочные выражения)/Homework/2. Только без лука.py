size = int(input())

lst = [input() for i in range(size)]

for i in range(len(lst)):
    if i < len(lst) and "лук" in lst[i]:
        del lst[i]

for i in range(len(lst)):
    if "лук" not in lst[i]:
        print(lst[i], end='')
        print(', ' if i < len(lst) - 1 else '', end='')
