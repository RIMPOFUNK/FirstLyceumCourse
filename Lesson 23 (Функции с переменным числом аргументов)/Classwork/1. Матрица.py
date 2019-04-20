def matrix(n=1, m=None, a=0):
    return [[a for _ in range(n)] for _ in range(n)] if not m else\
        [[a for _ in range(n)] for _ in range(m)]
