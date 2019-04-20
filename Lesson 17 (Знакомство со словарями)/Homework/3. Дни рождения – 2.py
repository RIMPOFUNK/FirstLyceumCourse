birthdays = {}
size = int(input())

for i in range(size):
    inp = input().split()

    if inp[2] not in birthdays:
        birthdays[inp[2]] = [[inp[0], inp[1]]]
    else:
        birthdays[inp[2]].append([inp[0], inp[1]])

size = int(input())
month = [input() for _ in range(size)]

for i in month:
    if i in birthdays:
        month = sorted(birthdays[i], key=lambda t: (int(t[1]), t[0]))
        st = ''
        for x in month:
            st += ' '.join(x) + ' '
        print(st.rstrip())
    if i not in birthdays:
        print()
