flag = False
n = int(input())

for i in range(n):
    string = input()
    if "кот" in string or "Кот" in string:
        flag = True
    if "пёс" in string or "Пёс" in string:
        flag = False
print("МЯУ" if flag else "НЕТ")