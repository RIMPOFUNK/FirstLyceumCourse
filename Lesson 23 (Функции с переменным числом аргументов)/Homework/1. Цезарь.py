alphabet = ['А',
            'Б',
            'В',
            'Г',
            'Д',
            'Е',
            'Ж',
            'З',
            'И',
            'Й',
            'К',
            'Л',
            'М',
            'Н',
            'О',
            'П',
            'Р',
            'С',
            'Т',
            'У',
            'Ф',
            'Х',
            'Ц',
            'Ч',
            'Ш',
            'Щ',
            'Ъ',
            'Ы',
            'Ь',
            'Э',
            'Ю',
            'Я']


def encrypt_caesar(msg, shift=3):
    global alphabet
    ret = ""

    for i in msg:
        if not i.isalnum() or i.upper() not in alphabet:
            ret += i
        else:
            if i.islower():
                index = alphabet.index(i.upper()) + shift
                index = -(32 - index) if index >= 32 else index

                ret += alphabet[index].lower()
            if i.isupper():
                index = alphabet.index(i.upper()) + shift
                index = -(32 - index) if index >= 32 else index

                ret += alphabet[index]
    return ret


def decrypt_caesar(msg, shift):
    return encrypt_caesar(msg, -shift)

