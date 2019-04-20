string1 = input()
string2 = input()

equal = 0
non_equal = 0

for i in range(len(string1)):
    if string1[i] == string2[i] and string1[i] in string2:
        equal += 1
    elif string1[i] != string2[i] and string1[i] in string2:
        non_equal += 1

print(equal, non_equal)
