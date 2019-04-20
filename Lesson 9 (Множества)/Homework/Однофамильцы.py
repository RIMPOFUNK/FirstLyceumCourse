n = int(input())

set1 = set()
set2 = set()
count = 0

for i in range(n):
    surname = input()
    if surname not in set1:
        set1.add(surname)
    else:
        set2.add(surname)
        count += 1

for i in set2:
    if i in set1:
        count += 1
print(count)