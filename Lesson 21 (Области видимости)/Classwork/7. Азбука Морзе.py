eng = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--.."
}

digits = {
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "−−−−−"}

rus = {
    "А": ".-", "Б": "-...", "Ц": "-.-.", "Д": "-..", "Е": ".", "Я": ".−.−", "Ф": "..-.", "Г": "--.",
    "Х": "....", "И": "..", "Й": ".---", "К": "-.-", "Л": ".-..", "М": "--", "Н": "-.", "О": "---",
    "П": ".--.", "Щ": "--.-", "Р": ".-.", "С": "...", "Т": "-", "У": "..-", "Ж": "...-", "В": ".--",
    "Ь": "-..-", "Ы": "-.--", "З": "--..", "Ч": "−−−.", "Ш": "−−−−", "Ъ": "−..−", "Э": "..−..",
    "Ю": "..−−"
}

language = None


# Определяет, на каком языке написан текст
def lang_str(text: str):
    if len([True for i in text if i.isalpha() and i.lower() in [x.lower() for x in rus.keys()]]) >\
            len([True for i in text if i.isalpha() and i.lower() in [x.lower() for x in eng.keys()]]):
        return "rus"
    return "eng"


def encode_to_morse(text: str):
    global language
    language = "rus" if lang_str(text) == "rus" else "eng"

    morse = rus if lang_str(text) == "rus" else eng
    morse = digits if text.isdigit() else morse
    ret = ""

    for i in text:
        if i == " ":
            ret += "\t"
        elif i.upper() not in morse and i.isalpha():
            print(f"Fatal error! The symbol {i} is not in Morse alphabet")
        elif i.isalnum():
            if i in digits:
                ret += digits[i] + ' '
            else:
                ret += morse[i.upper()] + ' '
    return ret


def decode_from_morse(code):
    morse = rus if language == "rus" else eng
    code_to_letter = {val: key for key, val in morse.items()}
    code_to_digits = {val: key for key, val in digits.items()}
    ret = ""

    if all(map(lambda x: x not in code_to_letter and x not in code_to_digits, code.split())):
        return "FAIL"

    for i in code.split('\t'):
        for j in i.split():
            if j in code_to_digits:
                ret += code_to_digits[j]
            else:
                ret += code_to_letter[j]
        ret += ' '
    return ret.capitalize()


def menu():
    print("1. Ввести строку")
    print("2. Закодировать")
    print("3. Раскодировать")
    print("4. Выйти")


def main():
    string = ""
    while True:
        print(" " * 5, string) if string else ...
        menu()
        choose = int(input())

        if choose == 1:
            print("Вводите: ", end='')
            string = input()
        elif choose == 2:
            string = encode_to_morse(string)
        elif choose == 3:
            string = decode_from_morse(string)
        elif choose == 4:
            return
