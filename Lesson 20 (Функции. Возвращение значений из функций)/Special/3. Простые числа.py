def prime(num):
    for i in range(2, num):
        if num % i == 0 and i != num:
            return "Составное число"
    return "Простое число"
