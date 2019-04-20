commands = list(input())
tape = [0] * 30000

index = 0
i = 0
for _ in range(len(commands)):
    index = 0 if index == len(tape) - 1 else index
    index += 1 if commands[i] == '>' else 0
    index -= 1 if commands[i] == '<' else 0

    if commands[i] == '[':
        if tape[index] == 0:
            i += 2
        else:
            if commands[i + 1] == '-':
                tape[index] = 0
            elif commands[i + 1] == '+':
                tape[index] = 255
        continue
    elif commands[i] == '+':
        if tape[index] == 255:
            tape[index] = 0
        else:
            tape[index] += 1
    elif commands[i] == '-':
        if tape[index] == 0:
            tape[index] = 255
        else:
            tape[index] -= 1
    elif commands[i] == '.':
        print(tape[index])
    i += 1
