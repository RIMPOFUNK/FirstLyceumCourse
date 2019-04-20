from PIL import Image as img


def mirror():
    image = img.open("image.jpg")
    pixels = image.load()

    ret = image.copy()
    ret_pixels = ret.load()

    _i = 0
    for i in range(image.size[0] - 1, -1, -1):
        _j = 0
        for j in range(image.size[1] - 1, -1, -1):
            ret_pixels[_i, _j] = pixels[j, i]
            _j += 1
        _i += 1

    ret.save("res.jpg")

