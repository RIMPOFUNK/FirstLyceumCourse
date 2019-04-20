print("Do you believe in horoscopes?")
answer1 = input()

if answer1 == "yes" or answer1 == "no":
    print("What is your favorite season?")
    answer2 = input()

    if answer2 == "winter" or answer2 == "spring" or answer2 == "summer" or answer2 == "autumn":
        print("Do you like cats?")
        answer3 = input()

        if answer3 == "yes" or answer3 == "no":
            if answer1 == "yes" and (answer2 == "spring" or answer2 == "summer")\
                    and answer3 == "yes":
                print("You are positive person")
            elif answer1 == "yes" and (answer2 == "spring" or answer2 == "summer")\
                    and answer3 == "no":
                print("You are ambiguous person")
            elif answer1 == "yes" and (answer2 == "winter" or answer2 == "autumn")\
                    and answer3 == "yes":
                print("You don't have a mental disorder")
            elif answer1 == "yes" and (answer2 == "winter" or answer2 == "autumn")\
                    and answer3 == "no":
                print("You have a tendency to depression")
            elif answer1 == "no" and answer3 == "no":
                print("You have a few friends")
            elif answer1 == "no" and answer3 == "yes":
                print("You are diverse person")
        else:
            print("Error: bad input")
    else:
        print("Error: bad input")
else:
    print("Error: bad input")