import numpy as np


def snake(rows, cols):
    val = np.arange(1, rows * cols + 1).reshape(rows, cols)
    val[1::2, ::-1].sort()
    return val
