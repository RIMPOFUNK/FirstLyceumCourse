size = int(input())

value = {}
tmp = {}

for i in range(size):
    string = input().split()
    value[string[0]] = int(string[-1])

    if i > 0:
        tmp[string[0]] = string[4][:-1]
        while string[0] != start:
            value[tmp[string[0]]] += int(string[-1])
            string[0] = tmp[string[0]]
    else:
        start = string[0]
print(*value.values(), sep='\n')
