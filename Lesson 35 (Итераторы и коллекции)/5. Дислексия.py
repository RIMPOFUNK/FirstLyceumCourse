from functools import reduce


def set_key(val: str):
    return ''.join(sorted(val))


def func(dictionary, val):
    return set_key(val) in dictionary and \
           val in dictionary[set_key(val)] and len(dictionary[set_key(val)]) == 1 \
           or set_key(val) not in dictionary


tmp = input().lower().split()
text = input().lower().split()

dic = {}
for i in tmp:
    if set_key(i) in dic:
        dic[set_key(i)] += [i]
    else:
        dic[set_key(i)] = [i]

print(reduce(lambda res, val: res + val + ' ' if func(dic, val) else res + '#' * len(val) + ' ',
             text, '').strip())
