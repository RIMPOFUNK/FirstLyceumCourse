def golden_ratio(num: int):
    fib = [0, 1]
    for i in range(2, num + 2):
        fib.append(fib[i - 1] + fib[i - 2])

    print(fib[num + 1] / fib[num])
