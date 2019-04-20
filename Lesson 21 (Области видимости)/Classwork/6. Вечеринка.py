friends = {}


def add_friends(name, lst):
    if name not in friends:
        friends[name] = lst
    else:
        friends[name] += lst


def is_friends(name1, name2):
    if name2 in friends[name1]:
        return True
    return False


def print_friends(name):
    print(*sorted(friends[name]))

