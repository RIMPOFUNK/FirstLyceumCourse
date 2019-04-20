import pymorphy2


morph = pymorphy2.MorphAnalyzer()

print("В холодильнике 99 бутылок кваса.")
print("Возьмём одну и выпьем.")

word = morph.parse('бутылка')[0]

for i in range(98, 0, -1):
    num = word.make_agree_with_number(i).word

    if str(i)[-1] == '1' and i != 11:
        print(f"Осталась {i}", num, "кваса.")
    else:
        print(f"Осталось {i}", num, "кваса.")
    print(f"В холодильнике {i}", num, "кваса.")
    print("Возьмём одну и выпьем.")
print("Осталось 0 бутылок кваса.")
