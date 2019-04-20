size = int(input())
strings = []

for i in range(size):
    string = input()
    strings.append(string)

size_srch = int(input())
search = []

for i in range(size_srch):
    word = input()
    search.append(word)

for i in strings:
    Flag = True
    for j in search:
        if j not in i:
            Flag = False
    if Flag:
        print(i)
