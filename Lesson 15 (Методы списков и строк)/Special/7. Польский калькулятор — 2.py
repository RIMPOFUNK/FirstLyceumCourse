stack = []

operations = input().split()

for i in operations:
    if i not in "+-*/~!#@":
        stack.append(int(i))
    else:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '-':
            first, second = stack.pop(), stack.pop()
            stack.append(second - first)
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == '/':
            first, second = stack.pop(), stack.pop()
            stack.append(second // first)
        elif i == '~':
            stack.append(-stack.pop())
        elif i == '!':
            C = 1
            for t in range(1, stack.pop() + 1):
                C *= t
            stack.append(C)
        elif i == '#':
            value = stack.pop()

            stack.append(value)
            stack.append(value)
        elif i == '@':
            third = stack.pop()
            second = stack.pop()
            first = stack.pop()

            stack.append(second)
            stack.append(third)
            stack.append(first)

print(*stack, sep='\n')
