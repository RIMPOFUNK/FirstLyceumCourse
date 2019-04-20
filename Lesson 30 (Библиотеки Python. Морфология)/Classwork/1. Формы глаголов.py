import pymorphy2
import sys


morph = pymorphy2.MorphAnalyzer()

get = ''.join(sys.stdin.readlines()).lower().replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ')
get = get.replace('–', ' ').replace('-', ' ').replace(':', ' ').replace(';', ' ').split()

count = 0
for i in filter(lambda x: 'INFN' in morph.parse(x)[0][1] or 'VERB' in morph.parse(x)[0][1],
                map(lambda x: morph.parse(x)[0].normal_form, get)):
    if "видеть" in i or "увидеть" in i or "глядеть" in i or "примечать" in i or "узреть" in i:
        count += 1

print(count)