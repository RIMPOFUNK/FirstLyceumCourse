login = input()
adress = input()

if "@" not in login and "@" in adress:
    print("OK")
elif "@" in login:
    print("Некорректный логин")
elif "@" not in adress:
    print("Некорректный адрес")