size = int(input())
coast = [[]]

for i in range(size - 1):
    coast.append([int(j) for j in input().split()])

stations = input().split()
point1, point2 = int(stations[0]), int(stations[1])

lcoast = coast[max(point1, point2)][min(point1, point2)]
result = -1

for i in range(size):
    if i != point1 and i != point2:
        if (lcoast > coast[max(point1, i)][min(point1, i)] +
                coast[max(i, point2)][min(i, point2)]):
            lcoast = coast[max(i, point2)][min(i, point2)] + coast[max(i, point2)][min(i, point2)]
            result = i

print(result if result != -1 else point1)
