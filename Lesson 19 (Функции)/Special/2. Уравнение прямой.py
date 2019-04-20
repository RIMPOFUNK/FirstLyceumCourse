def equation(a, b):
    a, b = a.split(';'), b.split(';')

    xa, ya = float(a[0]), float(a[1])
    xb, yb = float(b[0]), float(b[1])

    if xa == xb:
        print(xa)
    elif ya == yb:
        print(ya)
    else:
        k = (ya - yb) / (xa - xb)
        print(k, yb - k * xb)


