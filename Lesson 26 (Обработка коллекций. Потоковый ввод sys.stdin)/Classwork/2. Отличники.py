lst = []

for i in range(int(input())):
    clas = []
    
    for j in range(int(input())):
        clas.append(int(input().split()[1]))
    
    lst.append(any(map(lambda x: x == 5, clas)))
    
print("ДА") if all(lst) else print("НЕТ")       