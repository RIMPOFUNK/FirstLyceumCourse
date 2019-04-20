def mirror(arr):
    tmp = arr[:]
    arr.extend(tmp[::-1])
    