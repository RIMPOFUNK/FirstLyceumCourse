def roots_of_quadratic_equation(a, b, c):
    if a == b == c == 0:
        return ["all"]
    if a == b == 0:
        return []    
    if a == 0:
        return [-c / b]
    if c == 0:
        return [-b / a, 0]
      
    d = b**2 - 4 * a * c
    if d < 0:
        return []
    if d == 0:
        return [(-b - d**0.5) / (2 * a)]
    
    return [(-b - d**0.5) / (2 * a), (-b + d**0.5) / (2 * a)]
