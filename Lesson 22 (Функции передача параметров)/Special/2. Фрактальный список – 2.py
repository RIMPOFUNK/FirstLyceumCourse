def defractalize(fractal):
    tmp = fractal[:]
    fractal.clear()
    
    fractal.extend([i for i in tmp if i not in fractal and str(i).isdigit()])
