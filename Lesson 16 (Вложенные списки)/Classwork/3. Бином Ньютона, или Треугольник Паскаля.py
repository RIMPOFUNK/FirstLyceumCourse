size = int(input())

lst = [1]
print(1)
for i in range(size - 1):
    lst1 = [1]
    for j in range(i):
        lst1.append(lst[j] + lst[j + 1])
    lst1.append(1)
    print(*lst1)
    lst = lst1[:]
    