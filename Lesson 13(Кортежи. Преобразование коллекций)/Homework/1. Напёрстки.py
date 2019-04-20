size = int(input())

thimbles = [input() for i in range(size)]
action = []

for i in range(int(input())):
    for j in range(int(input())):
        action.append(thimbles[int(input()) - 1])
    thimbles = list(action)
    action.clear()
print(*thimbles, sep='\n')