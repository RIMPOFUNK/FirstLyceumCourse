def recursive_reverse(some_list):
    if not some_list:
        return []
    else:
        return recursive_reverse(some_list[1:]) + [some_list[0]]
    
