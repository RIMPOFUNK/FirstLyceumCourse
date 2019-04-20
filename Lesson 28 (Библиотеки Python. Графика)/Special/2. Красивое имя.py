from PIL import Image as im
from PIL import ImageDraw as draw


def image_filter(pix, i, j):
    """ Adulting photography """
    return pix[i, j][1] // 2 + 30, pix[i, j][2] // 2 + 10, pix[i, j][0] // 2


name = im.new("RGB", (795, 200), (100, 255, 100))
draw_name = draw.Draw(name)

draw_name.line((25, 0, 25, 200), fill=(255, 0, 200), width=20)
draw_name.line((35, 100, 110, 0), fill=(150, 80, 100), width=10)
draw_name.line((35, 100, 110, 200), fill=(100, 100, 200), width=8)

draw_name.line((140, 0, 140, 200), fill=(255, 200, 255), width=15)
draw_name.line((150, 200, 200, 100), fill=(0, 0, 0), width=3)
draw_name.line((212, 0, 212, 200), fill=(0, 0, 255), width=22)

draw_name.ellipse((250, 0, 380, 100), fill=(255, 255, 255))
draw_name.line((250, 0, 250, 200), fill=(0, 0, 0), width=10)
draw_name.ellipse((263, 15, 370, 83), fill=(100, 255, 100))

draw_name.line((400, 0, 400, 50), fill=(117, 93, 153), width=15)
draw_name.line((400, 50, 400, 150), fill=(0, 191, 255), width=5)
draw_name.line((400, 150, 400, 200), fill=(150, 0, 24), width=15)
draw_name.line((415, 200, 475, 100), fill=(255, 248, 231), width=15)
draw_name.line((477, 0, 477, 100), fill=(254, 40, 162), width=8)
draw_name.line((477, 100, 477, 200), fill=(237, 255, 33), width=8)

draw_name.line((500, 200, 530, 100), fill=(28, 28, 28), width=14)
draw_name.line((530, 100, 560, 0), fill=(255, 255, 255), width=14)
draw_name.line((560, 0, 590, 100), fill=(28, 28, 28), width=14)
draw_name.line((590, 100, 620, 200), fill=(255, 255, 255), width=14)

draw_name.line((650, 200, 680, 100), fill=(255, 71, 202), width=14)
draw_name.line((680, 100, 710, 0), fill=(0, 71, 171), width=14)
draw_name.line((710, 0, 740, 100), fill=(255, 71, 202), width=14)
draw_name.line((740, 100, 770, 200), fill=(0, 71, 171), width=14)

pixels = name.load()

for i in range(795):
    for j in range(200):
        r, g, b = pixels[i, j]
        pixels[i, j] = 255 - r, 255 - g, 255 - b
        pixels[i, j] = image_filter(pixels, i, j)

name.save("name.png", "PNG")