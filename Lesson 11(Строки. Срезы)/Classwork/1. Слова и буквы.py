def find_min(lst: list):
    value = lst[0]
    lenght = len(value)
    for i in range(len(lst)):
        value = lst[i] if len(lst[i]) < lenght else value
        lenght = len(value)
    return value


def find_max(lst: list):
    value = lst[-1]
    lenght = len(value)
    for i in range(len(lst)):
        value = lst[i] if len(lst[i]) > lenght else value
        lenght = len(value)
    return value


string = input()
list = []

while string != "стоп":
    if string != "стоп":
        list.append(string)
    string = input()

minimal = find_min(list)
maximal = find_max(list)

Flag = True
for i in range(len(minimal)):
    if minimal[i] not in maximal:
        Flag = False

print("ДА" if Flag else "НЕТ")
