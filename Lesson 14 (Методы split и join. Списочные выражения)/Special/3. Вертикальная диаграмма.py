counts = input().split()
height = max([int(i) for i in counts])

out = "*" * (len(counts) + 2)
out += '\n' + '*' + (len(counts) * ' ') + '*' + '\n'

for i in range(height, 0, -1):
    for j in range(len(counts) + 2):
        if j == 0 or j >= len(counts) + 1:
            out += '*'
        elif i <= int(counts[j - 1]):
            out += '*'
        else:
            out += ' '
    out += '\n'

print(out)
