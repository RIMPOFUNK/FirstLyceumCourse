size = int(input())
strings = []

for i in range(size):
    string = input()
    strings.append(string)

number = int(input())
number -= 1

for i in strings:
    if number >= len(i):
        print(end='')
    else:
        print(i[number], end='')
