size = int(input())
strings = {}

for i in range(size):
    string = input().split()
    strings[string[0]] = ' '.join(string[1:])

size = int(input())

for i in range(size):
    val = input()
    if val in strings:
        print(strings[val])
    else:
        print("Нет в словаре")