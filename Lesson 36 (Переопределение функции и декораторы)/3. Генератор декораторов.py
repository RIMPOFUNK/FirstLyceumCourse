def check_password(func, password):
    def decor(input_pass):
        if input_pass != password:
            print("Access denied")
            return

        def new_func(*args, **kwargs):
            return func(*args, **kwargs)

        return new_func
    return decor
