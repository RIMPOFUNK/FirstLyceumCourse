def sorted2(data, key=None):
    ret = []
    for i in data:
        if key is None:
            ret += [list(sorted(i, reverse=True))]
        else:
            ret += [list(sorted(i, key=key))]
    if key:
        ret = sorted(ret, key=lambda x: key(x[-1]), reverse=True)
    return ret


data = [[1], [3, 2], [6, 5, 4]]
key = lambda x: x

print(sorted2(data, key))