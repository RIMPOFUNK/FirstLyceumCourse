romanian = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

one, two, three = 5, 4, 0


def to_romain(number):
    if number <= 0:
        return ''

    ret = ''
    for key, val in romanian.items():
        while number >= key:
            ret += val
            number -= key

    return ret


def roman():
    global one, two, three
    three = one + two
    print(f"{to_romain(one)} + {to_romain(two)} = {to_romain(three)}")
