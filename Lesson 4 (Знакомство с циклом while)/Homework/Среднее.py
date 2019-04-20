DaysCount = 0
summ = 0
t = float(input())

while t > -300:
    DaysCount += 1
    summ += t
    t = float(input())
print(summ / DaysCount)