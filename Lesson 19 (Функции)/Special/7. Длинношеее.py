def count(word: str):
    count = 0
    for i in word:
        if i.lower() in "аоэиуыеёюяeaiouy":
            count += 1
    return count


def print_long_words(text: str):
    text = list(text)

    for i in range(len(text)):
        if not text[i].isalpha():
            text[i] = ' '

    txt = ""
    for i in text:
        txt += i
    text = txt

    text = text.split()

    for i in text:
        if count(i) >= 4:
            print(i.lower())
