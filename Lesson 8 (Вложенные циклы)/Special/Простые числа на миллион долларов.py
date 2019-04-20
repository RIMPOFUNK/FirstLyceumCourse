border = int(input())

for i in range(2, border):
    Flag = True
    for j in range(2, border):
        if i % j == 0 and i != j:
            Flag = False
    if Flag:
        print(i)
