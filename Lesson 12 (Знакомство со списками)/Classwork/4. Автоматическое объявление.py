strings_size = int(input())
strings = []

for i in range(strings_size):
    string = input()
    strings.append(string)

indexes_size = int(input())
indexes = []

for i in range(indexes_size):
    index = int(input())
    index -= 1
    indexes.append(index)

for i in indexes:
    if i >= len(strings):
        print(end='')
    else:
        print(strings[i])