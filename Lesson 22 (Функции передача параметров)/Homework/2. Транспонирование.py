import numpy as np


def transpose(matrix):
    tmp = np.array(matrix)
    tmp = tmp.transpose()

    matrix.clear()
    matrix.extend(tmp)
