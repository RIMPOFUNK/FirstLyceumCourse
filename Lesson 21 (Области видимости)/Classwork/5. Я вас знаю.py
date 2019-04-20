name = ""


def polite_input(question):
    global name
    if not name:
        print("Как вас зовут?")
        name = input()
    print(f"{name}, {question}")
    return input()
