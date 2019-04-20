def del_defis(string: str):
    for i in range(len(string) - 2):
        if string[i] == string[i + 1] == '-':
            string = string[:i] + string[i + 1:]

    return string


size = int(input())
tituls = []

string = ""
count = 0

while True:
    string += input() + '-'

    if '*' in string:
        string = string[:len(string) - 3]
        tituls.append('-'.join(string[0:].split()))

        count += 1
        string = ""

    if count == size:
        break

for _ in range(len(tituls) - 1):
    print(del_defis(tituls.pop()), end=', ')

print(del_defis(tituls.pop()))
