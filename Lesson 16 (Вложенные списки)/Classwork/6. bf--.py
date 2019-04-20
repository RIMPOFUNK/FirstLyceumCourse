commands = list(input())
tape = [0] * 30000

index = 0
for i in commands:
    index = 0 if index == len(tape) - 1 else index
    index += 1 if i == '>' else 0
    index -= 1 if i == '<' else 0

    if i == '+':
        if tape[index] == 255:
            tape[index] = 0
        else:
            tape[index] += 1
    elif i == '-':
        if tape[index] == 0:
            tape[index] = 255
        else:
            tape[index] -= 1
    elif i == '.':
        print(tape[index])
