StoneCount = int(input())

while StoneCount != 0:
    removeCount = int(input())
    if removeCount > 3 or removeCount > StoneCount or removeCount < 1:
        print(StoneCount)
    else:
        StoneCount -= removeCount
        print(StoneCount)
