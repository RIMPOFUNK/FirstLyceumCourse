import pymorphy2
import sys


def replace_all(value, key='!@#"$%^&*?/;:.,+-=*/[]–-|\/'):
    return ''.join(list(map(lambda x: ' ' if x in key else x, value)))


morph = pymorphy2.MorphAnalyzer()
text = ''.join(sys.stdin.readlines()).lower()

text = replace_all(text)

frequency = {}
for i in map(lambda x: morph.parse(x)[0].normal_form,
             filter(lambda i: 'NOUN' in morph.parse(i)[0][1] and morph.parse(i)[0][3] > 0.5, text.split())):
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

frequency = dict(sorted(frequency.items(), key=lambda x: (x, frequency[x[0]])[0], reverse=True))
frequency = dict(sorted(frequency.items(), key=lambda x: (x, frequency[x[0]])[1], reverse=True))

print(' '.join(list(frequency)[:10]))
