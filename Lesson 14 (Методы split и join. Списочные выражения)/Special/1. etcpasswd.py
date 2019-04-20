inf = []
add = input().split(':')

while '' not in add:
    inf.append(add)
    add = input().split(':')

simple = input().split(';')

for i in inf:
    if i[1] in simple:
        print("To: ", i[0], '\n', i[4].split(',')[0],
              ", ваш пароль слишком простой, смените его.", sep='')
