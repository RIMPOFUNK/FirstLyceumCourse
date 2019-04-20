maximal = int(input())

count = int(input())
strings = []

for i in range(count):
    string = input()
    strings.append(string)

for i in range(count):
    if len(strings[i]) > maximal:
        print(strings[i][:maximal - 3] + "...")
    else:
        print(strings[i])
