from random import sample
import string


chars = string.ascii_uppercase.replace('O', '').replace('I', '') \
          + string.ascii_lowercase.replace('o', '').replace('l', '') \
          + string.digits.replace('1', '').replace('0', '')


def generate_password(size):
    return ''.join(sample(chars, size))


def main(n, m):
    if m == 1:
        return list(chars[:n])

    tmp = set()
    while len(tmp) < n:
        tmp.add(generate_password(m))
    return tmp