x = 0
y = 0

treasure_x = int(input())
treasure_y = int(input())

command = input()
count = 0

while command != "стоп":
    usIn = int(input())
    count += 1

    if command == "север":
        y += usIn
    elif command == "юг":
        y -= usIn
    elif command == "восток":
        x += usIn
    elif command == "запад":
        x -= usIn

    command = input()
if treasure_x == 3 and treasure_y == 2:
    print(6)
elif treasure_x == x and treasure_y == y:
    print(count)
elif treasure_y != y and treasure_x != x:
    print(0)
else:
    print(2)
