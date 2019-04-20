value = input()

words = value.split()

_map = {i: 0 for i in value if i in "QWERTYUIOPASDFGHJKLZXCVBNM"}

for i in words:
    if i[0] in _map:
        _map[i[0]] += 1
           
print(_map)