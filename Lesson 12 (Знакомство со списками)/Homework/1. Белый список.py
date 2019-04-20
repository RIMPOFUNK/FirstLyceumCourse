white_size = int(input())
white = []

for i in range(white_size):
    value = input()
    white.append(value)

list_size = int(input())
lst = []

for i in range(list_size):
    value = input()
    lst.append(value)

for i in lst:
    if i in white:
        print(i)