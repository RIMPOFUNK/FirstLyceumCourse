size = int(input())
phone_book = {}

for i in range(size):
    inp = input().split()
    if inp[1] not in phone_book:
        phone_book[inp[1]] = [inp[0]]
    else:
        phone_book[inp[1]].append(inp[0])

size = int(input())
surnames = [input() for _ in range(size)]

for i in surnames:
    if i in phone_book:
        print(*phone_book[i], sep=' ')
    else:
        print("Нет в телефонной книге")
