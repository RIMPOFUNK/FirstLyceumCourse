size = int(input())

words = {}
for i in range(size):
    tmp = input().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    tmp = tmp.replace(':', '').replace(';', '').split()

    for j in tmp:
        letter = j.capitalize()

        if letter not in words:
            words[letter] = 1
        else:
            words[letter] += 1

for key, value in sorted(words.items(), key=lambda val: (-val[1], val[0])):
    print(key, sep='\n')
