size = int(input())
lst = []

sum = []
pair = 0

for i in range(size):
    num = int(input())
    lst.append(num)

for i in range(size - 1):
    pair = 0
    if i >= len(lst):
        break
    else:
        pair = lst[i] + lst[i + 1]
        sum.append(pair)

for i in sum:
    print(i)