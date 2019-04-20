num = int(input())

flag = 0
for i in range(1, num + 1, 1):
    if num % i == 0:
        print(i, end=' ')
        flag += 1
print("")    
print("ПРОСТОЕ" if flag == 2 else "НЕТ")