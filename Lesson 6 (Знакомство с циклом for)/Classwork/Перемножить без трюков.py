mult = 1
for i in range(6):
    num = int(input())
    if num == 0 or num == 1:
        continue
    mult *= num
print(mult)