number = int(input())

while int(str(number)[0]) != 1 and number < 1000000000:
    number *= int(str(number)[0])
print(number)