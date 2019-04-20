number = input()

num1 = int(number[0])
num2 = int(number[1])
num3 = int(number[2])

if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
    
if (num1 + num3) / 2 == num2:
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")