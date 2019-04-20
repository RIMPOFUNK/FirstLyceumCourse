def find(collection, value):
    """ Возвращает индекс искомого элемента value в collection,
        если элемента не существует – порождает исключение KeyError
    """
    if value not in collection:
        raise KeyError

    index = 0
    for i in collection:
        if i == value:
            return index
        index += 1


upper_case = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
lower_case = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

step = int(input())
message = input()

for i in message:
    symbol = i
    if i in upper_case:
        index = find(upper_case, i) + step
        symbol = upper_case[index if index < len(upper_case) else abs(len(upper_case) - index)]
    elif i in lower_case:
        index = find(lower_case, i) + step
        symbol = lower_case[index if index < len(lower_case) else abs(len(lower_case) - index)]
    print(symbol, end='')
