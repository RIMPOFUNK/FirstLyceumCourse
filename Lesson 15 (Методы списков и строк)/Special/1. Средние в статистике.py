def average(value: list):
    avg = 0
    for i in value:
        avg += float(i)

    return avg / len(value)


def mediana(value: list):
    val = sorted(value)
    if len(val) % 2 == 0:
        tmp = len(val) // 2 - 1
        return average(val[tmp:tmp + 2])
    else:
        return float(val[len(val) // 2])


numbers = input().split()

print(average(numbers), mediana(numbers))
