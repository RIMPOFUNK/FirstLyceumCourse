n = int(input())
errorsCount = 0
goodCount = 0

while errorsCount < n:
    str1 = input()
    if str1 == "раз":
        goodCount += 1
    else:
        print("Правильных отсчётов было ",
              goodCount,
              ", но теперь вы ошиблись.", sep='')
        goodCount = 0
        errorsCount += 1
        continue
    
    str2 = input()
    if str2 == "два":
        goodCount += 1
    else:
        print("Правильных отсчётов было ",
              goodCount,
              ", но теперь вы ошиблись.", sep='')
        goodCount = 0
        errorsCount += 1
        continue
    
    str3 = input()
    if str3 == "три":
        goodCount += 1
    else:
        print("Правильных отсчётов было ",
              goodCount,
              ", но теперь вы ошиблись.", sep='')
        goodCount = 0
        errorsCount += 1
        continue
    
    str4 = input()
    if str4 == "четыре":
        goodCount += 1
    else:
        print("Правильных отсчётов было ",
              goodCount,
              ", но теперь вы ошиблись.", sep='')
        goodCount = 0
        errorsCount += 1
        continue
    
print("На сегодня хватит.")