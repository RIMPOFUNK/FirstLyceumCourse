# возвращает строку без гласных
def without_violents(val):
    return ''.join(list(filter(lambda x: x.lower() not in "aeiouy", val)))


# количество гласных
def count(word, key="aeiouy"):
    return len([i for i in word if i.lower() in key])


# определяет тип ошибки
def error(login, password):
    wv = without_violents

    if count(password) != 3 and wv(login) != wv(password):
        return "Everything is wrong"
    if count(password) != 3:
        return "Wrong number of vowels"
    return "Wrong consonants"


def success(login):
    print(f"Привет, {login}!")


def failure(login, error):
    print(f"Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {error.upper()}.")


def ask_password(login, password, success, failure):
    login, password, wv = login.lower(), password.lower(), without_violents

    if count(password) == 3 and wv(password) == wv(login):
        success(login)
    else:
        failure(login, error(login, password))


def main(login, password):
    ask_password(login, password, success, failure)


