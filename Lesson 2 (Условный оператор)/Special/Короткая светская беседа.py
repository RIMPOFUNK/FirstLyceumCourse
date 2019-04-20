print("Как ваше настрение?")
answ = input()

if "не" in answ or "?" in answ:
    print("Я вас не понимаю")
elif "хорош" in answ or "прекрас" in answ:
    print("Вот и отлично!")
elif "ужас" in answ:
    print("Ничего! Выход есть всегда")
else:
    print("Я вас не понимаю")