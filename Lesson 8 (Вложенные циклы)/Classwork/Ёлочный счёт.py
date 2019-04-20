n = int(input())
count = 1
m = 0

while n >= count:
    m += 1
    for i in range(m): 
        if count > n:
            break
        else:
            print(count, end=' ')
            count += 1
    print()