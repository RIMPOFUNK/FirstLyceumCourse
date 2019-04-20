while True:
    num1 = int(input())
    sign = input()
    
    if sign == 'x':
        print(num1)
        break
    elif sign == '!':
        if num1 < 0:
            continue
        factorial = 1
        for i in range(1, num1 + 1):
            factorial *= i
        print(factorial)
        continue
    
    num2 = int(input())
    
    if sign == '+':
        print(num1 + num2)
    elif sign == '-':
        print(num1 - num2)
    elif sign == '*':
        print(num1 * num2)
    elif sign == '/':
        if num2 == 0:
            continue
        print(num1 // num2)
    elif sign == '%':
        if num2 == 0:
            continue        
        print(num1 % num2)