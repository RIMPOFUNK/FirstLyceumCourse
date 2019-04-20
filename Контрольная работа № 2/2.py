def sorted2(data, key=None):
    ret = []
    for i in data:
        if key is None:
            ret += [list(sorted(i, reverse=True))]
        else:
            ret += [list(sorted(i, key=key))]
    if key:
        ret = sorted(ret, key=lambda x: x[-1], reverse=True)
    print(ret)

    
sorted2([[1], [2, 3], [4, 5, 6]])
sorted2([[1], [3, 2], [6, 5, 4]], lambda x: x)