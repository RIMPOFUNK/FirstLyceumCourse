m = int(input())
n = int(input())

have = []
to_read = []

for i in range(m):
    book = input()
    have.append(book)
for i in range(n):
    book = input()
    to_read.append(book)
for i in to_read:
    if i in have:
        print("YES")
    else:
        print("NO")