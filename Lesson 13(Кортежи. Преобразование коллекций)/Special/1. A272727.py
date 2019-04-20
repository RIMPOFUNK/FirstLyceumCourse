def consilience_count(lst: list):
    count = 0
    copy = lst[:]

    rev = [copy.pop() for _ in range(len(copy))]

    for i in range(len(lst)):
        if lst[i] == rev[i]:
            count += 1
    return count


count = int(input())
lst = [0]

for i in range(count):
    lst.append(consilience_count(lst))

lst.pop()

for i in range(len(lst)):
    print(lst[i])
