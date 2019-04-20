def palindrome(word):
    if ''.join(word.lower().split()) == ''.join(word.lower()[::-1].split()):
        return "Палиндром"
    return "Не палиндром"
