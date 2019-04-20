from pymorphy2 import MorphAnalyzer
from sys import stdin


morph = MorphAnalyzer()

word = morph.parse(morph.parse(input())[0].normal_form)[0]

if 'VERB' in word.tag or 'INFN' in word.tag:
    print("Прошедшее время:")
    print(word.inflect({'past', 'masc'}).word)
    print(word.inflect({'past', 'femn'}).word)
    print(word.inflect({'past', 'neut'}).word)
    print(word.inflect({'past', 'plur'}).word)

    print("Настоящее время:")
    print(word.inflect({'pres'}).word)
    print(word.inflect({'pres', 'plur'}).word)
    print(word.inflect({'pres', '2per'}).word)
    print(word.inflect({'2per', 'plur'}).word)
    print(word.inflect({'3per'}).word)
    print(word.inflect({'3per', 'plur'}).word)
else:
    print("Не глагол")
