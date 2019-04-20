from PIL import Image as im
from PIL import ImageDraw as draw


def board(num, size):
    ret = im.new("RGB", (num * size, num * size), (255, 255, 255))
    desk = draw.Draw(ret)

    for i in range(0, num, 2):
        for j in range(0, num, 2):
            desk.rectangle((size * j, size * i, size * (j + 1) - 1, size * (i + 1) - 1), fill=(0, 0, 0))

    for i in range(1, num, 2):
        for j in range(1, num, 2):
            desk.rectangle((size * j, size * i, size * (j + 1) - 1, size * (i + 1) - 1), fill=(0, 0, 0))

    ret.save("res.png", "PNG")

# board(8, 50)

# get = im.open("res.png").load()
# need = im.open("image.jpg").load()
# for i in range(50):
# for j in range(50):
# print(get[i, j], need[i, j])