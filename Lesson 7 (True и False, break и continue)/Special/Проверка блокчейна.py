def _hash(m, r, h_prev):
    return 37 * (m + r + h_prev) % 256


n = int(input())

h_previous = 0
BadBlockNumber = -1

for i in range(n):
    b = int(input())

    h = b % 256
    r = (b // 256) % 256
    m = b // 256**2

    if (h != _hash(m, r, h_previous) or h > 100) and BadBlockNumber == -1:
        BadBlockNumber = i

    h_previous = h

print(BadBlockNumber)