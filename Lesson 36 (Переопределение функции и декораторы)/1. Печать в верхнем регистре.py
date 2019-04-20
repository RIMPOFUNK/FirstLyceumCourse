def upper_print(func):
    def upper(*words):
        func(*[i.upper() for i in words])
    return upper


print = upper_print(print)
