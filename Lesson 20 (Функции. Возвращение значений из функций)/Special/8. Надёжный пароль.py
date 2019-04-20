def password_level(pas: str):
    if len(pas) < 6:
        return "Недопустимый пароль"
    if pas.isdigit():
        return "Ненадежный пароль"

    f1 = f2 = f3 = False
    for i in pas:
        if i.isupper():
            f1 = True
        elif i.islower():
            f2 = True
        elif i in "0123456789":
            f3 = True

    if f1 * f2 * f3:
        return "Надежный пароль"
    if f1 ^ f2 and not f3:
        return "Ненадежный пароль"

    return "Слабый пароль"
