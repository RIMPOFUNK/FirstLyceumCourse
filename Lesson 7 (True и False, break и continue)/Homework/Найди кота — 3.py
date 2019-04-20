string = input()

flag = True
count = 0
strNum = -1
strCount = 0

while "СТОП" not in string:
    count += 1

    if ("кот" in string or "Кот" in string) and flag:
        flag = False
        strNum = count
        
    if "кот" in string or "Кот" in string:
        strCount += 1
    
    string = input()
    
print(strCount, strNum)  