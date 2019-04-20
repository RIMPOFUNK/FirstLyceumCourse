from sys import stdin


def range(val):
    ret = (val - val % 100000) // 1000
    return f"{ret} - {ret + 100}"


vals = {}
for i in map(lambda x: x.split()[0] + '\t' + range(int(x.split()[2])), stdin.readlines()):
    tmp = i.split('\t')

    if tmp[1] in vals:
        vals[tmp[1]] += [tmp[0]]
    else:
        vals[tmp[1]] = [tmp[0]]


for key in sorted(vals.keys(), key=lambda x: int(x.split()[0])):
    print(f"{key}: {', '.join(sorted(vals[key]))}")

