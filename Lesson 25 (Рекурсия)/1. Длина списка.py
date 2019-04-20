count = 0


def recursive_len(lst):
    global count
    if lst:
        recursive_len(lst[1:])
        count += 1
    return count
    
