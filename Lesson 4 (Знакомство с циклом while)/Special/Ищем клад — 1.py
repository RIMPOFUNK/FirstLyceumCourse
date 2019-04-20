x = 0
y = 0

treasure_x = int(input())
treasure_y = int(input())

view = "север"

command = input()
count = 0

while command != "стоп":
    count += 1
    if command == "вперёд":
        usIn = int(input())

        if view == "север":
            y += usIn
        elif view == "юг":
            y -= usIn
        elif view == "восток":
            x += usIn
        elif view == "запад":
            x -= usIn

    elif command == "разворот":
        if view == "юг":
            view = "север"
        elif view == "север":
            view = "юг"
        elif view == "запад":
            view = "восток"
        elif view == "восток":
            view = "запад"

    elif command == "налево":
        if view == "север":
            view = "запад"
        elif view == "юг":
            view = "восток"
        elif view == "запад":
            view = "юг"
        elif view == "восток":
            view = "север"

    elif command == "направо":
        if view == "север":
            view = "восток"
        elif view == "юг":
            view = "запад"
        elif view == "восток":
            view = "юг"
        elif view == "запад":
            view = "север"

    if x == treasure_x and y == treasure_y:
        break

    command = input()

if x == treasure_x and y == treasure_y:
    print(count, view, sep='\n')
elif x != treasure_x and y != treasure_y:
    print(0)
    if view == "юг":
        print("север")
    elif view == "север":
        print("юг")
    elif view == "запад":
        print("восток")
    elif view == "восток":
        print("запад")
elif x != treasure_x:
    print(count)
    if treasure_x < x:
        print("запад")
    elif treasure_x > x:
        print("восток")
elif y != treasure_y:
    print(count)
    if treasure_y < y:
        print("юг")
    elif treasure_y > y:
        print("север")
