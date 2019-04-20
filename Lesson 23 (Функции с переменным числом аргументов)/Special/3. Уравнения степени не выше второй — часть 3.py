def roots_of_quadratic_equation(a, b, c):
    if a == b == c == 0:
        return ["all"]
    if a == b == 0:
        return []
    if a == 0:
        return [-c / b]
    if c == 0:
        return [-b / a, 0]

    d = b ** 2 - 4 * a * c
    if d < 0:
        return []
    if d == 0:
        return [(-b - d ** 0.5) / (2 * a)]

    return [(-b - d ** 0.5) / (2 * a), (-b + d ** 0.5) / (2 * a)]


def solve(*cof):
    if len(cof) > 3 or len(cof) == 0:
        return

    if len(cof) == 3:
        a, b, c = float(cof[0]), float(cof[1]), float(cof[2])
        return roots_of_quadratic_equation(a, b, c)
    if len(cof) == 2:
        return roots_of_quadratic_equation(0, float(cof[0]), float(cof[1]))

    return roots_of_quadratic_equation(0, 0, float(cof[0]))


coeff = [float(i) for i in input().split()]

print(*solve(*coeff))

