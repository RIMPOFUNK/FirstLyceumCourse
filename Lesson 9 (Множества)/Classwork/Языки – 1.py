eng = int(input())
ger = int(input())

s_eng = set()
s_ger = set()

for i in range(ger + eng):
    surname = input()
    if surname in s_eng:
        s_ger.add(surname)
    else:
        s_eng.add(surname)
print(len(s_eng ^ s_ger) if len(s_eng ^ s_ger) != 0 else "NO")