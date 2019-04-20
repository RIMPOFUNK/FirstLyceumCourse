from pymorphy2 import MorphAnalyzer


morph = MorphAnalyzer()
tags = ['nomn', 'gent', 'datv', 'accs', 'ablt', 'loct']
cases = ["Именительный", "Родительный", "Дательный", "Винительный", "Творительный", "Предложный"]

word = morph.parse(morph.parse(input())[0].normal_form)[0]

if 'NOUN' in word.tag:
    print("Единственное число:")
    for i in range(6):
        print(f"{cases[i]} падеж: {word.inflect({tags[i]}).word}")

    print("Множественное число:")
    for i in range(6):
        print(f"{cases[i]} падеж: {word.inflect({'plur', tags[i]}).word}")
else:
    print("Не существительное")
