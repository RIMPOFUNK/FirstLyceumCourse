def to_seconds(val):
    if ':' not in str(val):
        return int(val) * 60
    val = val.split(':')
    return int(val[0]) * 3600 + int(val[1]) * 60


def constuctor(seconds):
    return f"{seconds // 3600}:{seconds % 3600 // 60 if seconds % 3600 // 60 != 0  else '00'}"


def sum_time(first, second):
    return constuctor(to_seconds(first) + to_seconds(second))


def late(now, classes, bus):
    if to_seconds(max(bus)) + to_seconds(now) + 300 < to_seconds(classes):
        return f"Выйти через {max(bus) - 5} минут"

    for i in reversed(bus):
        if to_seconds(i) - 300 + to_seconds(now) + to_seconds(20) <= to_seconds(classes):
            return f"Выйти через {i - 5} минут" if i - 5 >= 0 else "Опоздание"
    return "Опоздание"


# print(late('12:00', '12:40', [0, 1, 4, 6, 25]))
# 20
# print(late('9:20', '9:35', [4, 25, 30]))
# опоздание
# print(late('13:50', '14:30', [7, 17, 35, 48]))
# 12
# print(late('12:59', '13:45', [3, 35, 46, 55]))
# опоздание
