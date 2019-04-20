size = int(input())
allow = [input() for _ in range(size)]

size = int(input())
for i in range(size):
    trying = input()
    flag = True

    for j in allow:
        if trying.find(j) == 0 and (trying == j or trying[len(j):][0] == '/'):
            print("YES")
            flag = False
            break
    if flag:
        print("NO")
