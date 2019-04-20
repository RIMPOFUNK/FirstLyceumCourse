size = int(input())
lst = []

for i in range(size):
    money = int(input())
    lst.append(money)

for i in lst:
    print(i)

print()

for i in lst:
    print(i * 3)
