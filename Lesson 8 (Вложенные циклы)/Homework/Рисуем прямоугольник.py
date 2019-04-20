n = int(input())
m = int(input())
sign = input()

for i in range(n):
    for j in range(m):
        if j == 0 or j == m - 1:
            print(sign, end='')
        elif i == 0 or i == n - 1:
            print(sign, end='')
        else:
            print(' ', end='')
    print()
