def image_filter(pix, i, j):
    """ Adulting photography """
    return pix[i, j][1] // 2 + 30, pix[i, j][2] // 2 + 10, pix[i, j][0] // 2
