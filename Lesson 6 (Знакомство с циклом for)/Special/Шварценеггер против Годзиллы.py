def gcd(a: int, b: int):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


n = int(input())

numerator = int(input())
denominator = int(input())

for i in range(n - 1):
    inp_numerator = int(input())
    inp_denominator = int(input())

    tmp = lcm(denominator, inp_denominator)
    x = tmp // denominator
    y = tmp // inp_denominator

    denominator = lcm(inp_denominator, tmp)
    numerator = numerator * x + inp_numerator * y


print(numerator // gcd(numerator, denominator),
      denominator // gcd(denominator, numerator),
      sep='/')