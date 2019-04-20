price = float(input())
summ = 0

while price >= 0:
    if price > 1000:
        price -= price * 0.05
    summ += price
    price = float(input())
    
print(summ)
