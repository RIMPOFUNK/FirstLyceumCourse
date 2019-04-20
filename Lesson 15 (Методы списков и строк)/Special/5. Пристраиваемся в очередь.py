queue = []

size = int(input())

for i in range(size):
    event = input()

    if "встал" in event or "встала" in event:
        queue.append(event.split(" вста")[0])
    if "Привет" in event:
        name = event[event.index(' ') + 1:event.index('!')]
        last = event[event.index('!') + 2:event.index(" будет")]
        queue.insert(queue.index(name) + 1, last)
    if "хватит" in event:
        name = event[:event.index("хватит") - 2]
        queue.remove(name)
print(*queue, sep='\n')
