stack1 = int(input())
stack2 = int(input())

while stack1 != 0 or stack2 != 0:
    if stack1 > stack2:
        removeCount = stack1 - stack2
        stack1 -= removeCount
        print("The computer got", removeCount, "from 1 stone")
        print(stack1, stack2)

    elif stack1 < stack2:
        removeCount = stack2 - stack1
        stack2 -= removeCount
        print("The computer got", removeCount, "from 2 stone")
        print(stack1, stack2)

    else:
        stack1 -= 1
        print("The computer got", 1, "from 1 stone")
        print(stack1, stack2)

    if stack1 == stack2 == 0:
        winner = "computer"
        break

    userStack = int(input())
    userCount = int(input())
    while userStack > 2 or userStack < 1 or userCount < 1:
        print("Bad input! Try again")
        userStack = int(input())
        userCount = int(input()) 
            
    if userStack == 1:
        stack1 -= userCount
        print("The user got", userCount, "from 1 stone")
        print(stack1, stack2)

    elif userStack == 2:
        stack2 -= userCount
        print("The user got", userCount, "from 2 stone")
        print(stack1, stack2)

    if stack1 == stack2 == 0:
        winner = "user"
        break
print("The", winner, "won")