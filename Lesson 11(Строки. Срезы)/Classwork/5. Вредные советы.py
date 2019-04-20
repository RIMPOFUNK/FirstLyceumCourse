count = int(input())

advice = []

for i in range(count):
    string = input()
    advice.append(string)

for i in range(len(advice)):
    if (advice[i][0:2] == "не" or advice[i][0:2] == "Не") and advice[i][2] == " ":
        print(advice[i][3:])
    elif advice[i][0] == " ":
        print(advice[i][1:])
    else:
        print(advice[i])
