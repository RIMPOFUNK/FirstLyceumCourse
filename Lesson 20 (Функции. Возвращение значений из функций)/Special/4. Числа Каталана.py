arr = [1]


def catalan(num):
    global arr

    while len(arr) != num + 1:
        arr.append(int(arr[-1]) * (4 * len(arr) - 2) // (len(arr) + 1))

    return arr[num]
