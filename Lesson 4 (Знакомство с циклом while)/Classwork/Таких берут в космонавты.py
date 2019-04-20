height = input()
count = 0
maxHeight = 0
minHeight = 300

while height != '!':
    if int(height) <= 190 and int(height) >= 150:
        count += 1
        if int(height) > maxHeight:
            maxHeight = int(height)
        if int(height) < minHeight:
            minHeight = int(height)
    height = input()
        
print(count)
print(minHeight, maxHeight)