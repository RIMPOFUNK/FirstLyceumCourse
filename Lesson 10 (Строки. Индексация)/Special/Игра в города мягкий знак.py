city1 = input()
city2 = input()

index = -1

if city1[index] == 'ь':
    index = -2

if city1[index] == city2[0]:
    print("ВЕРНО")
else:
    print("НЕВЕРНО")