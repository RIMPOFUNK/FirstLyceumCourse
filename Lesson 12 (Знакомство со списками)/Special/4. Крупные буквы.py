f = {'A': [' *   ', '* *  ', '***  ', '* *  ', '* *  '],
     'B': ['**   ', '* *  ', '**   ', '* *  ', '**   '],
     'C': [' *   ', '* *  ', '*    ', '* *  ', ' *   ']}

string = input()
for i in range(5):
    for j in string:
        print(f.get(j)[i], end='')
    print()
