size = int(input())
data = [int(input()) for _ in range(size)]

first_param, second_param = data[0], data[-1]
print(*list(filter(lambda x: x**2 % first_param and not x % second_param, data[1:-1])), sep='\n')
