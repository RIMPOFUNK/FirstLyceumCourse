eng = int(input())
ger = int(input())
fr = int(input())

s_eng = set()
s_ger = set()
s_fr = set()

for i in range(ger + eng + fr):
    surname = input()
    if surname in s_eng and surname not in s_ger:
        s_ger.add(surname)
    elif surname in s_ger and surname not in s_fr:
        s_fr.add(surname)
    elif surname in s_fr and surname not in s_eng:
        s_eng.add(surname)
    else:
        s_ger.add(surname)

s_gen = s_eng ^ s_ger & s_ger ^ s_fr & s_eng ^ s_fr & s_fr ^ s_ger ^ s_eng
print(len(s_gen) if len(s_gen) != 0 else "NO")