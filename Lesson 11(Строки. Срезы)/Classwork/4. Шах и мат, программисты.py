count = int(input())

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if count <= 9:
    for i in range(count, 0, -1):
        symbol = 0
        for j in range(count, 0, -1):
            print(alphabet[symbol], end='')
            print(i, ' ', sep='', end='')
            symbol += 1

        print()
