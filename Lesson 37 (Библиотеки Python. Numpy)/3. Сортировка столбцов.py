import numpy as np


def super_sort(rows, cols):
    first = np.random.randint(1, 100, (rows, cols))
    second = first.copy()

    second = np.rot90(second)

    if len(second) % 2:
        second[1::2, ::-1].sort()
        second[::2, :].sort()
    else:
        second[1::2, :].sort()
        second[::2, ::-1].sort()

    return first, np.rot90(second, -1)


# print(*super_sort(4, 4), sep='\n\n')