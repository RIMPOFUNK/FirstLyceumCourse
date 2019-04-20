print("Hi! There is your hero in the grot")
print("To escape here select true door")
print("You have to choose between right, left and forward door")

while True:
    choice = input()
    if choice == "right":
        print("Oops. There is new fork. Choose true door again!")
        choice1 = input()
        if choice1 == "right":
            print("You've been eaten by big frog")
            break
        elif choice1 == "left":
            print("There is the impassable cliff")
            break
        elif choice1 == "forward":
            print("You have left the grot! Excellent!")
            break
        else:
            continue
    elif choice == "left":
        print("Oh, my god! You came to Yellowstone Supervolcano")
        break
    elif choice == "forward":
        print("This door led you into the abyss of nothingness")
        break
    else:
        continue
