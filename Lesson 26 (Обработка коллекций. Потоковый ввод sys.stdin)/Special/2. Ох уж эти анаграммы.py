import sys


def is_equal(lhs, rhs):
    minn, maxx = min(lhs, rhs), max(lhs, rhs)
    return all(map(lambda x: x in minn, maxx))


def find_ann(content):
    ret = {}

    for i in content:
        ret[i] = sorted(list(map(lambda x: x if is_equal(x, i) and x != i else "0", content)),
                        key=lambda x: -ord(x[0]) if x != Ellipsis else "0")
        content.remove(i)

    return ret


size = int(input())
lst = []


lst.extend(sys.stdin.read().lower().split())
lst = sorted(lst)

tmp = find_ann(lst)

for i, j in tmp.items():
    print(i, *list(filter(lambda x: x != Ellipsis and x != '0', j))) if j else ...

