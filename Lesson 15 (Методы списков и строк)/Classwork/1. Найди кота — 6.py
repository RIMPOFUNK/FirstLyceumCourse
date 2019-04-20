size = int(input())

cat = [input() for _ in range(size)]

for i in range(len(cat)):
    print(i + 1, cat[i].index("кот") + 1) if "кот" in cat[i] else ...
