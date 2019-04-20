def swap(first, second):
    if first is second:
        return
    tmp1 = first.copy()
    tmp2 = second.copy()
    
    first.clear()
    second.clear()
    
    first.extend(tmp2)
    second.extend(tmp1)
