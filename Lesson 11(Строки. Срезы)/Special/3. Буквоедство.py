string = input()
print(string)

while len(string) > 1:
    string = string[1:len(string) - 1]
    print(string)
