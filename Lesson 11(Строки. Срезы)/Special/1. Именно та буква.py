word = input()
index = int(input())
letter = input()

if letter[0] not in word or len(letter) > 1 or index - 1 >= len(word):
    print("ОШИБКА")
elif word[index - 1] == letter[0]:
    print("ДА")
else:
    print("НЕТ")
