size = int(input())
lst = []

for i in range(size):
    name = input()
    count = input()
    lst.append(name + ' ' + count)

for i in range(size):
    print(lst.pop())