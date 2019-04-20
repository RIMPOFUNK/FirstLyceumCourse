def coeff(i, k):
    return i * k + 1


def make_shades(val, k):
    alley = list(reversed(val)) if k <= -1 else val

    count = 0
    ret = []
    if k == 0:
        return list(map(lambda x: x != 0, alley))

    for i in alley:
        if not i:
            if count > 0:
                count -= 1
                ret.append(True)

            else:
                ret.append(False)
        else:
            if count != 0 and i == 1:
                count -= 1
            else:
                count += coeff(i, -k if k <= -1 else k) - 1
            ret.append(True)

    if k < 0:
        return list(reversed(ret))
    return ret


def calculate_sunny_length(shades):
    return shades.count(False)


def main():
    k = int(input())
    dark = [int(i) for i in input().split()]

    if calculate_sunny_length(make_shades(dark, k)) >= 10:
        print("Обгорел")
    else:
        print("Тени достаточно")
