size = int(input())
strings = [input() for _ in range(size)]

for i in range(size):
    Slash = False
    Inquotes = False

    StartSpace = True
    FirstSpace = True

    for j in strings[i]:
        if j == " ":
            if StartSpace or Inquotes:
                print(j, end="")
            elif FirstSpace:
                print(j, end="")
                FirstSpace = False
        else:
            StartSpace = False
            FirstSpace = True

            if j == '#' and not Inquotes:
                break
            if j == '\\':
                Slash = False if Slash else True
            if j == "'":
                Inquotes = False if Inquotes and not Slash else True

            Slash = False if j != '\\' else Slash
            print(j, end='')
    print()
