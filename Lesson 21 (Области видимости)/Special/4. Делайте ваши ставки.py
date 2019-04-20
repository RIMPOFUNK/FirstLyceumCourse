num_to_money = {}


def do_bet(number, count):
    if number in num_to_money or 10 < number or number <= 0 or count <= 0:
        print("Что-то пошло не так, попробуйте еще раз")
    else:
        num_to_money[number] = count
        print(f"Ваша ставка в размере {count} на лошадь {number} принята")
