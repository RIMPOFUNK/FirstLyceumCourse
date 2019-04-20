def get_period(numerator: int, denominator: int):
    ans = ''
    lst = dict()
    index = 0

    numerator = numerator % denominator
    lst[numerator] = index
    index += 1

    if numerator == 0:
        return 0

    while True:
        digit, numerator = divmod(numerator * 10, denominator)
        ans += str(digit)

        if numerator not in lst:
            lst[numerator] = index
            index += 1
        else:
            return ans[lst[numerator]:]


print(get_period(1, int(input())))
