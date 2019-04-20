def quarter(xcoord, ycoord):
    answer = ["I", "IV"] if xcoord > 0 else ["II", "III"]
    out = answer[0] if ycoord > 0 else answer[1]
    
    print(f"{out} четверть")
