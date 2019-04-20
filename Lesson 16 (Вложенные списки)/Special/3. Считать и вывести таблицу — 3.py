n, m = int(input()), int(input())

table = [[input() for _ in range(m)] for _ in range(n)]

for i in table:
    print(*i, sep='\t')
