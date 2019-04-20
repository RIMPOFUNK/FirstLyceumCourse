def check_password(func, password):
    if password.lower() != "посчитай число фиббоначчи, пожалуйста":
        print("В доступе отказано")
        return

    def new_func(num):
        return func(num)
    return new_func


def fib(num):
    num = int(num)
    val = [0, 1]
    for i in range(2, num + 1):
        val.append(val[i - 1] + val[i - 2])
    return val[-1]


fib = check_password(fib, input("Enter the password: "))
print(fib(input("Enter fib number: "))) if fib else ...


