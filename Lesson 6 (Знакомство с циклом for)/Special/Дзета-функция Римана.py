n = int(input())

summ = 0
for i in range(1, n + 1, 1):
    summ += 1 / i**2
print(3.141592653589793**2 / summ)