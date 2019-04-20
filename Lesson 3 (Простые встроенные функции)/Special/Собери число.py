number = int(input())

num1 = number // 100 % 10
num2 = number // 10 % 10
num3 = number % 10

sum1 = num1 + num2
sum2 = num2 + num3

print(str(max(sum1, sum2)) + str(min(sum1, sum2)))