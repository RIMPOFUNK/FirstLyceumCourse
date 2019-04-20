import numpy as np


# превращение вводимой стоки в матрицу
def divide_str(val):
    return [[i for i in j] for j in val.split()]


# печать
def print_field(val):
    for i in val:
        print(''.join(i))
    print()


# транспонирование
def trans(matrix):
    return [[str(i) for i in list(j)] for j in list(np.array(matrix).transpose())]


# вертикальное отрадение
def vertical_reflection(val):
    return [val.pop() for _ in range(len(val))]


# горизонтальное отражение
def horizontal_reflection(val):
    return [list(reversed(i)) for i in val]


# отражение вдоль горизонтали и вертикали одновременно
def horizontal_vertical(val):
    return vertical_reflection(horizontal_reflection(val))


# горизонтальное отражение, затем транспонирование
def horizontal_trans(val):
    return trans(horizontal_reflection(val))


# вертикальное отражение, затем транспонирование
def vertical_trans(val):
    return trans(vertical_reflection(val))


# транспонирование, затем два отражения
def trans_two_reflection(val):
    return horizontal_reflection(vertical_reflection(trans(val)))


source = divide_str("""xxx.  
....  
x.xx  
x...  """)

print_field(source)