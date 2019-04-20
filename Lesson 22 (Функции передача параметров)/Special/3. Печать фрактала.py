def fractal_print(obj):
    print(f"[{obj[0]}, ", end='')
    print(*obj[1:], sep=', ', end=']')


