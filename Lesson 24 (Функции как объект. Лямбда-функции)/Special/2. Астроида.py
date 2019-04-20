import math


def points(vals):
    return map(lambda t: (math.cos(t)**3, math.sin(t)**3), vals)


def result(vals):
    return min(map(lambda t: math.hypot(0.75 - t[0], 0 - t[1]), points(vals)))


print(result(range(int(2 * math.pi))))
# 0.25
