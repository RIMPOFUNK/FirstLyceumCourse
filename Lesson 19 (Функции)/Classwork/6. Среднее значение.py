def print_average(arr):
    avg = 0
    for i in arr:
        avg += i
    print(0) if len(arr) == 0 else print(avg / len(arr))