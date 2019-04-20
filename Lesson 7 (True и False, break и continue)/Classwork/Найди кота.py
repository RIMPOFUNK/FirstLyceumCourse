n = int(input())
flag = False

for i in range(n):
    string = input()
    if "кот" in string or "Кот" in string:
        flag = True
print("МЯУ" if flag else "НЕТ")