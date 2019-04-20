from random import sample


def make_bingo():
    tmp = [[sample(range(1, 75), 25).pop() for i in range(5)] for _ in range(5)]
    tmp[2][2] = 0
    return tuple([tuple(i) for i in tmp])