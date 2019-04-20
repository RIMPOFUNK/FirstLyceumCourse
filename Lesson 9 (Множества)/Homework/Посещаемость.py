def is_have(students: list, value):
    for i in students:
        if value not in i:
            return False
    return True


m = int(input())

s_gen = []
went = set()

for i in range(m):
    went.clear()
    n = int(input())
    for j in range(n):
        surname = input()
        went.add(surname)
    s_gen.append(sorted(set(went)))

best = set()
for i in s_gen:
    for j in i:
        if is_have(s_gen, j) and j not in best:
            best.add(j)

for i in best:
    print(i)
