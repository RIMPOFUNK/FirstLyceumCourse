print("Hi! There is your hero in the grot")
print("To escape here select true door")
print("You have to choose between right, left and forward door")

choice = input()

if choice == "right":
	print("Oops. There is new fork. Choose true door again!")
	choice1 = input()
	if choice1 == "right":
		print("You've been eaten by big frog")
	elif choice1 == "left":
		print("There is the impassable cliff")
	elif choice1 == "forward":
		print("You have left the grot! Excellent!")
	else:
		print("Command is incorrect. Terminate!")
elif choice == "left":
	print("Oh, my god! You came to Yellowstone Supervolcano")
elif choice == "forward":
	print("This door led you into the abyss of nothingness")
else:
	print("Command is incorrect. Terminate!")