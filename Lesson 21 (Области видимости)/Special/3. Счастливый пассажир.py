def is_lucky(ticket):
    ticket = str(ticket)
    if (sum([int(i) for i in ticket[:3]]) ==
            sum([int(i) for i in ticket[3:]])):
        return True
    return False


def lucky(ticket):
    ticket = str(ticket)
    while len(ticket) < 6:
        ticket = "0" + ticket

    if is_lucky(ticket) and is_lucky(lastTicket):
        return "Счастливый"
    else:
        return "Несчастливый"

