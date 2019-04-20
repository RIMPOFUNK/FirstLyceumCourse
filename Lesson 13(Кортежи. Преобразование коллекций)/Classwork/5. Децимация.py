size = int(input())

surnames = [(input(), False) for _ in range(size)]
step, repeat = int(input()), int(input())

for i in range(repeat):
    count = 0
    for j in range(size):
        if not surnames[j][1]:
            count += 1
            count = 1 if count > step else count

        if count == step:
            surnames[j] = (surnames[j][0], True)

for i in surnames:
    print(i[0]) if not i[1] else ""
