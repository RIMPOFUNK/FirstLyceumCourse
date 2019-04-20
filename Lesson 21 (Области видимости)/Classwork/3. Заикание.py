mes = ""


def print_without_duplicates(message):
    global mes
    if mes == message:
        return
    mes = message
    print(mes)
