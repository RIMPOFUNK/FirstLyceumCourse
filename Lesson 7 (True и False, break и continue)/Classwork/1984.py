n = int(input())

war = "Евразия"
peace = "Остазия"

for i in range(n):
    string = input()
    if string == "С кем война?":
        print(war)
    elif string == "С кем мир?":
        print(peace)
    elif string == "Меняем":
        war, peace = peace, war