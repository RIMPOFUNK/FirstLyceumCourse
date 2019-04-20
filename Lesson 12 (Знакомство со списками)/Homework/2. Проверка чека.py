inp = input().split()

size = int(inp[0])
summ = int(inp[1])

lst = [input().split() for i in range(size)]

price = 0
for i in range(size):
    price += int(lst[i][0]) * int(lst[i][1][1:])

print(summ - price)

if summ - price != 0:
    count = 1
    for i in lst:
        if int(i[0]) * int(i[1][1:]) != int(i[2][1:]):
            print(count, end=' ')

        count += 1
