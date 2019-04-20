def coincidence_count(lhs: list, rhs: list):
    count = 0
    for i in range(len(lhs)):
        if lhs[i] == rhs[i]:
            count += 1
    return count


size = int(input())

first = [int(input()) for _ in range(size)]
second = first[:]

trainingCount = int(input())

for i in range(trainingCount):
    if int(input()) == 1:
        first[int(input())] += int(input())
    else:
        second[int(input())] += int(input())

print(*first, sep=' ')
print(*second, sep=' ')

print(coincidence_count(first, second))
