word = input()
count = 0

for i in word:
    count += 1
    print(ord(i), end='')
    if count < (len(word)):
        print(", ", end='')