StoneCount1 = int(input())
StoneCount2 = int(input())

while StoneCount1 > 0 or StoneCount2 > 0:
    stackNumber = int(input())
    removeCount = int(input())

    if stackNumber == 1:
        StoneCount1 -= removeCount
    elif stackNumber == 2:
        StoneCount2 -= removeCount
    print(StoneCount1, StoneCount2)