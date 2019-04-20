leftBorder = 1
rightBorder = 1000
tryingCount = 0
sign = ' '

while sign != '=' and tryingCount <= 10:
    print((rightBorder + leftBorder) // 2)
    sign = input()
    
    if sign == '>':
        leftBorder = (rightBorder + leftBorder) // 2
    elif sign == '<':
        rightBorder = (rightBorder + leftBorder) // 2
    tryingCount += 1
