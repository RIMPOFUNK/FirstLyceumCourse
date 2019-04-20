size = int(input())
legion = [input() for _ in range(size)]
step = int(input())
number = 0

print(legion[0])
del legion[0]

for i in range(size):
    if len(legion) > number + step - 1:
        number += step - 1
        print(legion[number])
        del legion[number]
    else:
        number = 0
        if len(legion) > number:
            print(legion[number])
            del legion[number]

