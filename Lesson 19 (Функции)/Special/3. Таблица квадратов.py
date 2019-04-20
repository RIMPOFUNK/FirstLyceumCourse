def squared():
    matrix = []
    num = 11
    for _ in range(90):
        if num % 10 != 0:
            matrix.append(num**2)
        num += 1

    while matrix:
        for _ in range(8):
            print(str(matrix.pop(0)).ljust(5, ' '), end='') if matrix else ...

        print(matrix.pop(0)) if matrix else ...
