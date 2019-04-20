logins = input().split(',')
bad = []
maxx = 0

for i in logins:
    Flag = False
    for j in i:
        if not j.isalnum() and j != '_':
            Flag = True
    if Flag:
        bad.append(i)
        maxx = len(i) if maxx < len(i) else maxx

bad.sort()

for i in bad:
    print(" " * (maxx - len(i)), i, sep='')