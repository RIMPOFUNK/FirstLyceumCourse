from PIL import Image as img


def makeanagliph(name, move):
    pic = img.open(name)
    pixels = pic.load()

    ret = img.new('RGB', (pic.size[0], pic.size[1]), (0, 0, 0))
    ret_pixels = ret.load()

    for i in range(pic.size[0]):
        for j in range(pic.size[1]):
            if i < move:
                ret_pixels[i, j] = 0, *pixels[i, j][1:]
            else:
                g, b = pixels[i, j][1:]
                ret_pixels[i, j] = pixels[i  - (move ), j][0], g, b
    ret.save("res.jpg")

