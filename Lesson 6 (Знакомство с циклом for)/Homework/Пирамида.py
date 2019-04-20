n = int(input())

for i in range(1, n + 1, 1):
    print((n - i) * ' ', end='')
    for j in range(i * 2 - 1):
        print('*', end='')
    print('')