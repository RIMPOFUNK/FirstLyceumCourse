print("Do you like cats?")
answer1 = input()

print("Do you want to break free?")
answer2 = input()

if answer1 == "yes" and answer2 == "yes":
    print("You are positive and free person")
elif answer1 == "yes" and answer2 == "no":
    print("You are slave")
elif answer1 == "no" and answer2 == "yes":
    print("You have a serious mental problems")
elif answer1 == "no" and answer2 == "no":
    print("You are negative person")
else:
    print("Error: bad input")