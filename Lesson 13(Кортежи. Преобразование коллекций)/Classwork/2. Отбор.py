size = int(input())

lst = [input() for _ in range(size)]

for i in lst:
    print(i)

print()

for i in lst:
    if int(i[-1]) == 5 or int(i[-1]) == 4:
        print(i)