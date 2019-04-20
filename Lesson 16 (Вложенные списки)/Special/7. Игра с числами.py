from statistics import median

num, name, steps = int(input()), input(), int(input())
lst = []

for _ in range(steps):
    if name == "Петя":
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        num += 11
        name = "Маша"
    elif name == "Маша":
        num = num * 3 - 2
        name = "Петя"

    lst.append(num)
lst.sort()

print(median(lst))
