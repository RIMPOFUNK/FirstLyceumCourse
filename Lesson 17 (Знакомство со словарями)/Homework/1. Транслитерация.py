transliteration = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "Zh",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "Kh",
    "Ц": "Tc",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Shch",
    "Ы": "Y",
    "Э": "E",
    "Ю": "Iu",
    "Я": "Ia"
}

message = input().split()

for i in range(len(message)):
    for j in message[i]:
        if j in transliteration:
            print(transliteration[j], end='')
        elif j.upper() in transliteration:
            print(transliteration[j.upper()].lower(), end='')

    print(message[i][-1] if message[i][-1] in ",.:-–_|!?;" else "", end='')
    if i < len(message) - 1:
        print(end=' ')
