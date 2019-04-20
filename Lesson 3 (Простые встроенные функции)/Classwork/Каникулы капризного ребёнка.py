town1 = input()
town2 = input()

towns = ["Пенза", "Тула"]

if town1 not in towns and town2 not in towns or town1 == town2\
   or town1 in towns and town2 in towns and town1 != town2\
        or town2 == "Тула" or town1 == "Пенза":
    print("НЕТ")
elif town1 == "Пенза" or town1 == "Тула" or town2 == "Тула" or town2 == "Пенза":
    print("ДА")