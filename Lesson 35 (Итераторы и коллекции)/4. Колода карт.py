import itertools


names = ["пик", "треф", "бубен", "червей"]
names.remove(input())
for i in itertools.product(list(range(2, 11)) + ["валет", "дама", "король", "туз"], names):
    print(*i)