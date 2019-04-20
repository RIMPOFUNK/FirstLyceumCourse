def choose_coffee(val):
    global ingredients
    
    for i in val:
        if i == "Эспрессо" and ingredients[0] >= 1:
            ingredients[0] -= 1
            return "Эспрессо"
        if i == "Капучино" and ingredients[0] >= 1 and ingredients[1] >= 3:
            ingredients[0] -= 1
            ingredients[1] -= 3
            return "Капучино"
        if i == "Маккиато" and ingredients[0] >= 2 and ingredients[1] >= 1:
            ingredients[0] -= 2
            ingredients[1] -= 1
            return "Маккиато"
        if i == "Кофе по-венски" and ingredients[0] >= 1 and\
           ingredients[2] >= 2:
            ingredients[0] -= 1
            ingredients[2] -= 2
            return "Кофе по-венски"
        if i == "Латте Маккиато" and ingredients[0] >= 1 and\
           ingredients[1] >= 2 and ingredients[2] >= 1:
            ingredients[0] -= 1
            ingredients[1] -= 2
            ingredients[2] -= 1
            return "Латте Маккиато"
        if i == "Кон Панна" and ingredients[0] >= 1 and ingredients[2] >= 1:
            ingredients[0] -= 1
            ingredients[2] -= 1
            return "Кон Панна"
    return "К сожалению, не можем предложить Вам напиток"

