from sys import stdin


matrix = [list(map(int, i.replace('\n', '').split())) for i in stdin.readlines()]
summ = zip(*matrix)

m_sum, z_sum = set(), set()

for i in range(len(matrix)):
    m_sum.add(sum(matrix[i]))

for i in summ:
    z_sum.add(sum(i))

if len(m_sum) == len(z_sum) == 1 and m_sum == z_sum:
    print("YES")
else:
    print("NO")

