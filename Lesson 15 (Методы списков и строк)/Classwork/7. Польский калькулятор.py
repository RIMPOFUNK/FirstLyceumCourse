stack = []

operations = input().split()

for i in operations:
    if i not in "+-*/":
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
            stack.append(stack.pop() / stack.pop())
print(*stack, sep='\n')
