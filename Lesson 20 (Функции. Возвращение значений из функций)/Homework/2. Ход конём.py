def t2c(key):
    return 'ABCDEFGH'.find(key[0]) + 1, int(key[1])


def c2t(key):
    return 'ABCDEFGH'[key[0] - 1] + str(key[1])


def possible_turns(val):
    letter, number = t2c(val)
    tmp = []

    tmp.append((letter + 2, number + 1))
    tmp.append((letter + 2, number - 1))

    tmp.append((letter - 2, number + 1))
    tmp.append((letter - 2, number - 1))

    tmp.append((letter + 1, number + 2))
    tmp.append((letter + 1, number - 2))

    tmp.append((letter - 1, number + 2))
    tmp.append((letter - 1, number - 2))

    res = []

    for a, b in tmp:
        if 0 < a <= 8 and 0 < b <= 8:
            res += [c2t((a, b))]

    return sorted(res)
