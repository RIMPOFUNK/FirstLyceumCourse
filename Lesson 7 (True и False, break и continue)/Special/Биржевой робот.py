price = int(input())
upFlag = False
downFlag = False

buyCost = 0
saleCost = 0
previous = price

while price != 0:
    price = int(input())
    if price > previous and not upFlag:
        upFlag = True
        buyCost = price
    if price < previous and not downFlag and upFlag:
        downFlag = True
        saleCost = price

    previous = price

print(buyCost, saleCost, saleCost - buyCost)