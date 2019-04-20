stack1 = int(input())
stack2 = int(input())
stack3 = int(input())

nim = stack1 ^ stack2 ^ stack3

if nim > 0:
    if stack1 ^ nim < stack1:
        removeCount = stack1 - (stack1 ^ nim)
        stack1 -= removeCount
        stackNumber = 1
    elif stack2 ^ nim < stack2:
        removeCount = stack2 - (stack2 ^ nim)
        stack2 -= removeCount
        stackNumber = 2
    else:
        removeCount = stack3 - (stack3 ^ nim)
        stack3 -= removeCount
        stackNumber = 3
else:
    stack1 -= 1
    removeCount = 1
    stackNumber = 1

print("The computer got", removeCount, "from", stackNumber)
print(stack1, stack2, stack3)

while stack1 + stack2 + stack3 > 0:
    winner = "user"

    print("Enter stack stack number: ", end='')
    stackNumber = int(input())

    while stackNumber < 1 or stackNumber > 3:
        print("Invalid stack number. Try again!")
        if stackNumber == 1 and stack1 == 0\
                or stackNumber == 2 and stack2 == 0\
                or stackNumber == 3 and stack3 == 0:
            print("This stack is empty")
            stackNumber = -1

    while True:
        if stackNumber == 1:
            get = stack1
        elif stackNumber == 2:
            get = stack2
        else:
            get = stack3

        print("Enter stone count: ", end='')
        removeCount = int(input())

        if 0 < removeCount <= get:
            if stackNumber == 1:
                stack1 -= removeCount
                get = stack1
            elif stackNumber == 2:
                stack2 -= removeCount
                get = stack2
            else:
                stack3 -= removeCount
                get = stack3
            print("The user got", removeCount, "from ", stackNumber)
            print(stack1, stack2, stack3)

            break

    if stack1 + stack2 + stack3 > 0:
        winner = "computer"
        nim = stack1 ^ stack2 ^ stack3

        if nim > 0:
            if stack1 ^ nim < stack1:
                removeCount = stack1 - (stack1 ^ nim)
                stack1 -= removeCount
                get = stack1
                stackNumber = 1
            elif stack2 ^ nim < stack2:
                removeCount = stack2 - (stack2 ^ nim)
                stack2 -= removeCount
                get = stack2
                stackNumber = 2
            else:
                removeCount = stack3 - (stack3 ^ nim)
                stack3 -= removeCount
                get = stack3
                stackNumber = 3
        else:
            if stack1 > 0:
                stack1 -= 1
                stackNumber = 1
                get = stack1
            elif stack2 > 0:
                stack2 -= 1
                stackNumber = 2
                get = stack2
            else:
                stack3 -= 1
                stackNumber = 3
                get = stack3
            removeCount = 1
        print("The computer got", removeCount, "from", stackNumber)
        print(stack1, stack2, stack3)

print("The", winner, "won")