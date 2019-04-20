size = int(input())
teams = [(input(), int(input())) for _ in range(size)]

teams = sorted([(teams[i][1], teams[i][0]) for i in range(len(teams))], reverse=True)

top = sorted([teams[i][1]
              for i in range(len(teams) // 2 if len(teams) % 2 == 0 else len(teams) // 2 + 1)])
teams = sorted(teams[i][1] for i in range(len(top), len(teams)))

print(*top, sep='\n')
print(*teams, sep='\n')
