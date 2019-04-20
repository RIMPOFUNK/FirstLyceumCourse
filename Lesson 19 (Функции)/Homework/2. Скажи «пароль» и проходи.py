def ask_password():
    flg = False
    for _ in range(3):
        flg = True if input() == "password" else flg
    
    print("В доступе отказано") if not flg else print("Пароль принят")