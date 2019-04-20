number = int(input())
count = 0

while number >= 2:
    number /= 2
    count += 1
if number > 1:
    print("НЕТ")
else:
    print(count)