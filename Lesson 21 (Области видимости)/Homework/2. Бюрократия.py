name = ""
holidays = ""
swapper = ""
money = ""


def setup_profile(Name, Holidays):
    global name, holidays, swapper, money
    name, holidays = Name, Holidays
    swapper, money = "", ""


def print_application_for_leave():
    print(f"Заявление на отпуск в период {holidays}. {name}")


def print_holiday_money_claim(Money):
    global money
    money = Money

    print(f"Прошу выплатить {money} отпускных денег. {name}")


def print_attorney_letter(swap):
    global swapper
    swapper = swap

    print(f"На время отпуска в период {holidays} моим заместителем назначается {swapper}. {name}")


