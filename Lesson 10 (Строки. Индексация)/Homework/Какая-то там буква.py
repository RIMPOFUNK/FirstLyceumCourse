word = input()
number = int(input())

if number > len(word) or number <= 0:
    print("ОШИБКА")
else:
    print(word[number - 1])