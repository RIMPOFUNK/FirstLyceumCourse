from sys import stdin


def replace(val):
    return ''.join(filter(lambda x: x not in '!?.,:;', val))


val = filter(lambda t: t[1][0].isupper(),
             sorted(enumerate(map(lambda z: replace(z), stdin.read().split())), key=lambda i: i[1]))
even = []

for i in val:
    if i[1] in even:
        continue
    even.append(i[1])
    print(f"{i[0]} - {i[1]}")