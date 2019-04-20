numbers = input().split()
_range = input().split()
summ = 0

for i in range(len(numbers)):
    if int(_range[0]) <= i <= int(_range[1]):
        summ += int(numbers[i])**2
print(summ)