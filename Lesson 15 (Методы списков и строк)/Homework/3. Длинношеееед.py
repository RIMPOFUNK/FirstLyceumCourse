word = input().lower()
maxx = 0

for i in word:
    maxx = word.count(i) if word.count(i) > maxx else maxx

print(maxx)
