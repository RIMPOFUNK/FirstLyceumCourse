def repeat_count(string: str):
    count = 0
    for i in string:
        if i == '\n':
            count = 0
        else:
            count += 1
    return count


command = input()

sign = command[0]
command = command[1:]

gaps_count = 0
string = sign
left_count = 0

for i in command:
    if i == '>':
        string += sign
        gaps_count += 1
    elif i == 'V':
        left_count = 0

        string += '\n'
        string += (' ' * gaps_count) + sign
    elif i == '<':
        left_count += 1
        gaps_count -= 1

        string = string[0:-repeat_count(string)]

        string += ' ' * gaps_count +\
                  sign * (left_count + 1)

print(string)
