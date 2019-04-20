num = int(input())
lst = [i**2 for i in range(num)]

for i in range(len(lst)):
    print(lst[i], end=' ')
