def count(word):
    return len([i for i in word if i.lower() in "ёуеыаоэяию"])


def is_ritm(phrase):
    phrase = phrase.split()

    if list(map(lambda x: count(x) == count(phrase[0]), phrase)).count(True) == len(phrase):
        print("Парам пам-пам")
    else:
        print("Пам парам")


is_ritm(input())
