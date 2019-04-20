combinations = input()
lst = []

count = 0
for i in range(len(combinations)):
    if combinations[i] == 'o' or combinations[i] == 'о':
        count += 1
    else:
        count = 0

    lst.append(count)

print(max(lst))
