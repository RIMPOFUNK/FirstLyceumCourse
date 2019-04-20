def palindrome(s):
    s = s.lower()
    pal = s[::-1]

    if s == pal:
        return True
    return False


def is_simple(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0 and num != i:
            return False
    return True


def check_pin(val):
    val = val.split('-')
    if is_simple(int(val[0])) and palindrome(val[1]) and int(val[2]) % 2 == 0:
        return "Корректен"
    return "Некорректен"