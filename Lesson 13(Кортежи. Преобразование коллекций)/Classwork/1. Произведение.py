size = int(input())
nums = [int(input()) for _ in range(size)]
mult = int(input())

Flag = False
for i in range(size):
    for j in range(size):
        if nums[i] * nums[j] == mult:
            Flag = True
            break

print("ДА" if Flag else "НЕТ")