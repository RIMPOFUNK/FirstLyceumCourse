value = int(input())
trib = []

trib.extend([1, 1, 1, 3, 5, 9])
index = 1

fib1 = 3
fib2 = 5
fib3 = 9
fib = 17

while index < value:
    trib.append(fib)

    fib1 = fib2
    fib2 = fib3
    fib3 = fib
    fib = fib1 + fib2 + fib3

    index += 1

for i in range(index):
    print(trib[i], end=' ')
