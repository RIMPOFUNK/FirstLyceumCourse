from PIL import Image as im


def transparency(filename1, filename2):
    lhs, rhs = im.open(filename1), im.open(filename2)
    lhs_pixels, rhs_pixels = lhs.load(), rhs.load()
    
    ret = im.new("RGB", (lhs.size[0], lhs.size[1]), (0, 0, 0))
    ret_pixels = ret.load()
    
    for i in range(lhs.size[0]):
        for j in range(lhs.size[1]):
            r = int(lhs_pixels[i, j][0] * 0.5 + rhs_pixels[i, j][0] * 0.5)
            g = int(lhs_pixels[i, j][1] * 0.5 + rhs_pixels[i, j][1] * 0.5)
            b = int(lhs_pixels[i, j][2] * 0.5 + rhs_pixels[i, j][2] * 0.5)
            ret_pixels[i, j] = r, g, b
            
    ret.save("res.jpg")
