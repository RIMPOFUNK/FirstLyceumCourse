old = set()


def print_only_new(message):
    if message not in old:
        print(message)
        old.add(message)
