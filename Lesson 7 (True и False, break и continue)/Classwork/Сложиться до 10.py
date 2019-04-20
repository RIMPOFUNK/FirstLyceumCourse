num = int(input())
count = 0
summ = 0

while num != 0:
    count += 1
    summ += num
    
    if summ == 10:
        print(count)
        break
    
    num = int(input())