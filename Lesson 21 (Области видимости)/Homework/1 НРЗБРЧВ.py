translatedText = ""


def translate(text):
    if not text:
        return

    global translatedText

    for i in text:
        if i not in "ЁУЕЫАОЭЯЮИуеёыаоэяию:;.,?!-–":
            translatedText += i

    tmp = translatedText.split()
    translatedText = ""

    for i in range(len(tmp) - 1):
        translatedText += tmp[i] + ' '
    translatedText += tmp[-1]
