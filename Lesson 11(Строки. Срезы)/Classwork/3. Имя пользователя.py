username = input()

Flag = False
for i in username:
    if i not in "_abcdefghijklmnopqrstuvwxyz" and i not in "1234567890" and not Flag:
        print("Неверный символ:", i)
        Flag = True
if not Flag:
    print("OK")