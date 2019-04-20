num = 1
items = []


def add_item(itemName, itemCost):
    items.append(f"{itemName} - {itemCost}")
    
    
def print_receipt():
    global num, items
    
    if not items:
        return
     
    print(f"Чек {num}. Всего предметов: {len(items)}")
    print(*items, sep='\n')
    print(f"Итого: {sum([int(i.split(' - ')[1]) for i in items])}")
    print('-' * 5)
    
    num += 1
    items = []
    
   