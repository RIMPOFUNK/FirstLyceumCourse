size = int(input())
coast = [[]]

for i in range(size - 1):
    coast.append([int(j) for j in input().split()])

for i in range(size - 1):
    for j in range(i + 1, size):
        for t in range(size):
            if t != i and t != j:
                if (coast[max(i, j)][min(i, j)] > coast[max(i, t)][min(i, t)] +
                        coast[max(j, t)][min(j, t)]):
                    print(i, j)
                    break
