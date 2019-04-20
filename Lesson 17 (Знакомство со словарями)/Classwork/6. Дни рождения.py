size = int(input())
birthdays = {}

for i in range(size):
    inp = input().split()
    if inp[2] not in birthdays:
        birthdays[inp[2]] = [inp[0]]
    else:
        birthdays[inp[2]].append(inp[0])

size = int(input())
month = [input() for _ in range(size)]

for i in month:
    if i in birthdays:
        print(*sorted(birthdays[i]), sep=' ')
    else:
        print()
