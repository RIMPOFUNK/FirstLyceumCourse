from PIL import Image as im
from PIL import ImageDraw as draw


image = im.new("RGB", (1920, 1080), (255, 0, 0))
desk = draw.Draw(image)
desk.polygon((0, 0, 100, 250), fill=(0, 0, 80))
image.show()
