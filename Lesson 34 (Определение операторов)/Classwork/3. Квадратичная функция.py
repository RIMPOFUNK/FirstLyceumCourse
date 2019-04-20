class SquareFunction:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def __call__(self, val):
        return val**2 * self.a + self.b * val + self.c
