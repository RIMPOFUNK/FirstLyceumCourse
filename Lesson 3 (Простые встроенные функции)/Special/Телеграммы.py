string = input()

rubls = len(string) * 40 // 100
cent = len(string) * 40 % 100
print(rubls, "р.", cent, "коп.")