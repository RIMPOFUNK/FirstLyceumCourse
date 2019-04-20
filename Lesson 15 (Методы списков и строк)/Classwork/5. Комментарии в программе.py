size = int(input().split('#')[1])
out = []

for i in range(size):
    string = input()
    out.append(string[0:string.index('#')].rstrip() if '#' in string else string.rstrip())

print(*out, sep='\n')
