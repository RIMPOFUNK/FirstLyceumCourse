string = input()
count = 1

for i in range(1, len(string)):
    if string[i - 1] != string[i]:
        print(count, string[i - 1])
        count = 1
    else:
        count += 1

print(count, string[-1])
