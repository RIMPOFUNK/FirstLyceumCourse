StoneCount = int(input())

while StoneCount > 0:
    if StoneCount % 3 == 0:
        StoneCount -= 2
        print("The computer got", 2)
        print("Rest =", StoneCount)

    else:
        print("The computer got", 1)
        StoneCount -= 1
        print("Rest =", StoneCount)

    if StoneCount == 0:
        winner = "user"
        break

    userIn = int(input())
    while userIn > 3 or userIn > StoneCount or userIn < 1:
        print("Bad input! Try again!")
        userIn = int(input())

    print("The user got", userIn)
    StoneCount -= userIn
    print("Rest =", StoneCount)

    if StoneCount == 0:
        winner = "computer"
        break
print("The", winner, "won")