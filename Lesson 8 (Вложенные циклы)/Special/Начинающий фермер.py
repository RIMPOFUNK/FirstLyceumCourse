money = int(input())
count = int(input())

for bull in range(1, count + 1):
    for cow in range(count + 1):
        for calf in range(count + 1):
            if bull + cow + calf == count and bull * 20 + cow * 10 + calf * 5 == money:
                print(bull, cow, calf)