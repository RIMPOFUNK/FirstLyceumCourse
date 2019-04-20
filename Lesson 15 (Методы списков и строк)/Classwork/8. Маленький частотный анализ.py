string = input()

letter_to_count = {}

for i in string:
    if i == ' ':
        continue
    if i.lower() not in letter_to_count:
        letter_to_count[i.lower()] = 1
    else:
        letter_to_count[i.lower()] += 1

maxx = max(letter_to_count.values())
letter = []

for key, value in letter_to_count.items():
    if value >= maxx:
        maxx = value
        letter.append(key)
print(sorted(letter)[0])
