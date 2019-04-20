def find_farthest_orbit(val):
    mm = max([a * b for a, b in val if a != b])
    for a, b in val:
        if a * b == mm:
            return (a, b) 
    