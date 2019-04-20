number = int(input())
base = 8

while number >= 8:
    number /= base

print(int(number))