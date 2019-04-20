def print_operation_table(op, rows=9, col=9):
    for i in range(1, rows + 1):
        for j in range(1, col + 1):
            print(str(op(i, j)).ljust(5, ' '), end='')
        print()
