import random

place = "fork"
sword = False

while True:
    if place == "fork":
        print("You are in front of a", place)
        print("Choose between the right, left and front way.")

        way = input()
        if way == "right":
            place = "impassable cliff"
        elif way == "left":
            place = "Naglfar"
        elif way == "front":
            place = "dragon's lair"
        else:
            print("Bad input! Try again")
            continue
    elif place == "impassable cliff":
        print("Now you are in front of an", place)
        print("Do you want to try to jump over it or just go back?")

        answer = input()
        if "back" in answer or answer == "no":
            place = "fork"
        elif answer == "yes":
            if random.randint(0, 1):
                print("You jumped over a cliff, but there is big frog here")
                if sword:
                    print("With the sword of Hephaestus, you killed the frog and escaped from the labyrinth")
                    break
                print("You've been eaten by it")
            else:
                print("You jumped off from the cliff and dead")
            break
        else:
            print("Bad input! Try again")
            continue
    elif place == "Naglfar":
        print("Oh, god. Ragnarök came. A Naglfar is here! Do you want to join the battle or just go back?")
        answer = input()

        if "back" in answer or answer == "no":
            place = "fork"
        elif answer == "yes":
            if sword:
                print("With the sword of Hephaestus, you and the Gods stopped Ragnarok")
                print("You escaped from the labyrinth")
                break
            else:
                print("You've been killed, but you fought like a hero.")
                place = "Valhalla"
        else:
            print("Bad input! Try again")
            continue
    elif place == "Valhalla":
        print("You got to the Valhalla")
        print("Hephaestus gives you best of the world sword")

        sword = True

        print("Odin gives you a chance to fix all. You've been return to the Earth")
        place = "fork"

    elif place == "dragon's lair":
        print("You've come to dragon's lair. The Great Dragon is very angry")
        print("It attacks you")

        if sword:
            print("You killed the Great Dragon by the Hephaestus's sword")
            print("Do you want to go further or go back?")

            answer = input()

            if "back" in answer or answer == "no":
                place = "fork"
            else:
                print("After a very long way you came to Dragon's treasure")
                print("You escaped from the labyrinth")
                break
        else:
            print("The Great Dragon killed you, because you was unarmed")
            break
