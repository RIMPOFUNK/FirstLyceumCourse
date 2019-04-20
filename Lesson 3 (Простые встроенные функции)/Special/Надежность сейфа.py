number = int(input())

num1 = number // 100 % 10
num2 = number // 10 % 10
num3 = number % 10

if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2

if num1 == num2 == num3:
    print("В числе все цифры одинаковые")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("В числе две одинаковые цифры")
else:
    print("ОК")