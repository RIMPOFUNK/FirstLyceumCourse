def discriminant(a, b, c):
    return b**2 - 4 * a * c


def larger_root(p, q):
    return max((-p + discriminant(1, p, q)**0.5) / 2,
               (-p - discriminant(1, p, q)**0.5) / 2)


def smaller_root(p, q):
    return min((-p + discriminant(1, p, q)**0.5) / 2,
               (-p - discriminant(1, p, q)**0.5) / 2)


def main():
    p, q = float(input()), float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))
    