StoneCount = int(input())

while StoneCount > 0:
    if StoneCount % 4 == 0:
        StoneCount -= 3
        got = 3

    else:
        got = StoneCount % 4
        StoneCount -= StoneCount % 4

    print("The computer got", got)
    print("Rest =", StoneCount)

    if StoneCount == 0:
        print("The computer won")
        break

    userIn = int(input())
    while userIn > 3 or userIn > StoneCount or userIn < 1:
        print("Bad input! Try again!")
        userIn = int(input())

    StoneCount -= userIn

    print("The user got", userIn)
    print("Rest =", StoneCount)
   
    if StoneCount == 0:
        print("The user won")
        break
