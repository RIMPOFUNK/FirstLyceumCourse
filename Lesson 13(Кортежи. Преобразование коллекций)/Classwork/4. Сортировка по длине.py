def bubble_sort(value: list):
    for i in range(len(value) - 1):
        for j in range(len(value) - i - 1):
            if len(value[j]) > len(value[j + 1]):
                value[j], value[j + 1] = value[j + 1], value[j]
            elif len(value[j]) == len(value[j + 1]):
                if value[j] > value[j + 1]:
                    value[j], value[j + 1] = value[j + 1], value[j]
    return value


size = int(input())

lst = bubble_sort([input() for _ in range(size)])

print(*lst, sep='\n')