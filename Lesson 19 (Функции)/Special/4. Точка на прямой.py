def line(s: str, t: str):
    t = t.split(';')
    if '+' in s:
        equation = float(s[:s.find('x')]) * float(t[0]) + float(s[s.find('+'):])
    else:
        after = s[s.find('x'):]
        equation = float(s[:s.find('x')]) * float(t[0]) + float(after[after.find('-'):])

    print(True) if float(t[1]) == equation else print(False)

