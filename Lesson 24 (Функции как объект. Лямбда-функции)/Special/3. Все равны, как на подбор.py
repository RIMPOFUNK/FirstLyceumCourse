def same_by(val, objects):
    return not list(filter(lambda x: x != list(map(val, objects))[0], map(val, objects)))
