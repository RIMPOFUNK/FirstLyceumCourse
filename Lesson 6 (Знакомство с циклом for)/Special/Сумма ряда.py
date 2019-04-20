n = int(input())

summ = 0
for i in range(1, n + 1, 1):
    num = int(input())
    if i % 2 == 0:
        summ -= num
    else:
        summ += num
print(summ)