val = input().split(';')
out = ""

for i in val:
    for j in i.split(','):
        if out == "":
            out = str(int(j)) if int(j) >= 1000000000 else ""
        elif out[-1] == '\n':
            out += j if int(j) >= 1000000000 else ''
        else:
            out += ',' + j if int(j) >= 1000000000 else ''
    out += '\n'
print(out)