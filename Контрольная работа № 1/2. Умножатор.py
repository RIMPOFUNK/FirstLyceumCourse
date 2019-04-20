lst = input().split()

_range = input().split()
left, right = int(_range[0]), int(_range[1])

value = 1

for i in lst:
    if left <= int(i) <= right:
        pass
    else:
        value *= int(i)
print(value)