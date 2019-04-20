def average(value: list):
    avg = 0
    for i in value:
        avg += float(i)

    return avg / len(value)


def mediana(value: list):
    value = sorted(value)
    if len(value) % 2 == 0:
        tmp = len(value) // 2
        return average(value[tmp:tmp + 2])
    else:
        return value[len(value) // 2]


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


numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(mediana(numbers), moda(numbers))
