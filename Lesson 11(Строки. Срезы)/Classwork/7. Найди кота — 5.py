def find(word: str, elem: str):
    if len(elem) > len(word):
        return 0
    index = 0
    while word[index:index + 2] != elem[0:2] and (index + 2) < len(word) - 1:
        index += 1
    if elem in word:
        return index + 1


count = int(input())

indexes = []
numbers = "123456789010"

for i in range(0, count):
    string = input()
    indexes.append(string)

for i in range(1, count + 1):
    if find(indexes[i - 1], "кот") != 0:
        print(i,
              find(indexes[i - 1], "кот")) if str(find(indexes[i - 1],
                                                       "кот")) in numbers else print(end='')
