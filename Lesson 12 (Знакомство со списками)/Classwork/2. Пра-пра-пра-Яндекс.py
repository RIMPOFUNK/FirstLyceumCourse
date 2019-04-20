size = int(input())
strings = []

for i in range(size):
    string = input()
    strings.append(string)

search = input()

for i in strings:
    if search in i:
        print(i)