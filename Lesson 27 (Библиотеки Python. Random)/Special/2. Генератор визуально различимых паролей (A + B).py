from random import choice, shuffle
import string


digits = string.digits.replace('1', '').replace('0', '')
uppercase = string.ascii_uppercase.replace('O', '').replace('I', '')
lowercase = string.ascii_lowercase.replace('o', '').replace('l', '')

chars = digits + lowercase + uppercase
three = choice(lowercase) + choice(uppercase) + choice(digits)


def generate_password(size):
    if size == 1:
        return choice(digits)
    if size == 2:
        return choice(digits) + choice(lowercase)
    if size == 3:
        ret = list(choice(digits) + choice(lowercase) + choice(uppercase))
        shuffle(ret)
        return ''.join(ret)

    ret = set(three)
    while len(ret) < size:
        ret.add(choice(chars))

    return ''.join(ret)


def main(n, m):
    if m == 1:
        return list(chars[:n])

    tmp = set()
    while len(tmp) < n:
        tmp.add(generate_password(m))
    return tmp
