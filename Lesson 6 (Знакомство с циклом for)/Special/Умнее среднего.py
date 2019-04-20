n = int(input())

summ = 0
avg = 0

for i in range(1, n + 1, 1):
    IQ = int(input())

    if summ == 0 or IQ == avg:
        print("0")
    elif IQ < avg:
        print('<')
    elif IQ > avg:
        print('>')

    summ += IQ
    avg = summ / i
