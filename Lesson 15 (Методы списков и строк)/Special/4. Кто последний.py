queue = []

count = int(input())

for i in range(count):
    event = input()

    if "Кто последний" in event:
        queue.append(event.split(' - ')[1][0:-1])
    elif "Я только спросить" in event:
        queue.insert(0, event.split(' - ')[1][0:-1])
    elif "Следующий" in event:
        if not queue:
            print("В очереди никого нет.")
        else:
            print("Заходит ", queue[0], '!', sep='')
            del queue[0]
