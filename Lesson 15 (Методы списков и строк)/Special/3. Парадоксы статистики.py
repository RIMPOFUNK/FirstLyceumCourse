def mediana(value: list):
    val = sorted(value)
    if len(val) % 2 == 0:
        tmp = len(val) // 2
        return average(val[tmp:tmp + 2])
    else:
        return val[len(val) // 2]


def moda(value: list):
    _map = {}
    for i in value:
        if i not in _map:
            _map[i] = 1
        else:
            _map[i] += 1
    maxx = max(_map.values())

    for key, val in _map.items():
        if maxx == val:
            return key


size = int(input())
data = []

for i in range(size):
    data.append(input().split())

medians = []
mods = []
all = []

for i in data:
    for j in i:
        all.append(int(j))

for i in data:
    medians.append(mediana(i))
    print(mediana(i), end=' ')

print()
for i in data:
    mods.append(moda(i))
    print(moda(i), end=' ')

print()
print(mediana(medians), moda(mods), sep='\n')
print(mediana(all), moda(all), sep='\n')

