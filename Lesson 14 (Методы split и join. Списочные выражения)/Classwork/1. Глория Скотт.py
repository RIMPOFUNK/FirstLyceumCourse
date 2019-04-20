string = input()

words = string.split()
lst = []

for i in range(2, len(words), 3):
    lst.append(words[i])

while lst:
    print(lst.pop(0), end=' ')
