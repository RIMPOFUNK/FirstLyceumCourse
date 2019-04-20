import numpy as np


table = np.genfromtxt('ABBREV.csv', delimiter=';', dtype=None, names=True, encoding="utf8")
print(table)
