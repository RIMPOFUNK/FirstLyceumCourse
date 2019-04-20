def who_are_you_and_hello():
    name = input()
    while name != name.capitalize() or not name.isalpha() or\
            len(name.split()) != 1:
        name = input()
    print(f"Привет, {name}!")
