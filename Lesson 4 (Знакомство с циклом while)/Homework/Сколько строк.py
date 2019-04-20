string = input()
count = 1

while "Спасибо." not in string:
    string = input()
    count += 1
print(count)