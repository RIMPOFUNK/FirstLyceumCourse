from pymorphy2 import MorphAnalyzer
from sys import stdin


morph = MorphAnalyzer()


def set_gender(word):
    lexem = morph.parse(word)[0]
    if 'masc' in lexem.tag.gender:
        return "ой"
    elif 'femn' in lexem.tag.gender:
        return "ая"
    return "ое"


def set_form(word):
    lexem = morph.parse(word)[0]
    if lexem.tag.number == 'plur':
        return "Живые"
    return "Жив" + set_gender(word)


for i in stdin.read().split():
    lexem = morph.parse(i)
    if 'NOUN' not in lexem[0][1]:
        print("Не существительное")
    elif 'anim' in lexem[0][1]:
        print(set_form(i))
    else:
        print(f"Не {set_form(i)}".capitalize())