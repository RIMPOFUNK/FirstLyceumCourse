def take_large_banknotes(val):
    res = []
    
    for i in val:
        if i > 10:
            res.append(i)
    return res