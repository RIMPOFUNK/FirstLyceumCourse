data = {}
count = {}


def get_transactions(transaction):
    if "print_it" in transaction:
        for key, val in data.items():
            print(f"{count[key]} {key} {val}")
        return

    transaction = transaction.replace('-', ":").split(':')
    if transaction[1] in data:
        data[transaction[1]] += int(transaction[2])
        count[transaction[1]] += 1
    else:
        data[transaction[1]] = int(transaction[2])
        count[transaction[1]] = 1

