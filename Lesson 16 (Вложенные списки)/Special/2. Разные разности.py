def Differences(value: list):
    res = [0]

    for i in value:
        for j in value:
            if i - j not in res:
                res += [i - j]
    return res


size = int(input())

print(*sorted(Differences([int(input()) for _ in range(size)])), sep='\n')
