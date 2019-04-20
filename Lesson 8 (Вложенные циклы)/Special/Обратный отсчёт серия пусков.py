startCount = int(input())

for i in range(1, startCount + 1):
    for j in range(i - 1, -1, -1):
        print("Осталось секунд:", j)
    print("Пуск", i)