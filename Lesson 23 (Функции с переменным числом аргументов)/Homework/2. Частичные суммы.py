def partial_sums(*val):
    if len(val) == 0:
        return [0]
    if len(val) <= 1:
        return [0, val[0]]
    ret = [0, val[0]]
    for i in range(len(val) - 1):
        ret.append(sum(val[:i]) + val[i] + val[i + 1])
    return ret