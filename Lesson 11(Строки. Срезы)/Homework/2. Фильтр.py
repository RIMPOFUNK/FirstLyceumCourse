count = int(input())

words = []

for i in range(count):
    word = input()
    words.append(word)

for i in words:
    if i[:2] == "%%":
        print(i[2:])
    elif i[:4] != "####":
        print(i)
