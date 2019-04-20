from sys import stdin


book_names = list(filter(lambda x: len(x) > 1, input().split('\t')))

lst = [i.replace('\n', '') for i in stdin.readlines()]

data = {i.split('\t')[0]: i.split('\t')[1:] for i in lst}
best = min(data, key=lambda x: sum(map(lambda x: int(x), data[x])))

print(best)
for i in enumerate(data[best]):
    print(f"{book_names[i[0]]}\t{i[1]}")
