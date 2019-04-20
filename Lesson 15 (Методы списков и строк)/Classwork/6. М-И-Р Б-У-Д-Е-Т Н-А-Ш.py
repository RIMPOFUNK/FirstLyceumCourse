words = input().split()

for i in words:
    for j in range(len(i)):
        print(i[j].upper(), end='-' if j < len(i) - 1 else "")
    print(end=' ')
