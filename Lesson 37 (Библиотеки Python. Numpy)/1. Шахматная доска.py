import numpy as np


def make_field(size):
    val = np.zeros(size * size, dtype=np.int8).reshape(size, size)
    val[::2, ::2] = 1
    val[1::2, 1::2] = 1
    return val
