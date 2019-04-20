num1 = float(input())
num2 = float(input())
sign = str(input())

if sign == '+':
    print(num1 + num2)
elif sign == '-':
    print(num1 - num2)
elif sign == '*':
    print(num1 * num2)
elif sign == '/' and num2 != 0:
    print(num1 / num2)
else:
    print("888888")