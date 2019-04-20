def divSum(num: int):
    summ = 0
    for i in range(1, num):
        if num % i == 0:
            summ += i
    return summ


for i in range(1, 10000):
    ds = divSum(i)
    for j in range(i, 10000):
        if ds == j and divSum(j) == i and i != j:
            print(i, j)
