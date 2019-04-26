import PIL
from PIL import Image as im
from PIL import ImageDraw as draw


class ImageDrawer(draw.ImageDraw):
    def __init__(self, *args, **kwargs):
        super()
        self.image = im.new(*args, **kwargs)
        self.desk = draw.Draw(self.image)

    def left_triangle(self, xy, fill=None, outline=None):
        avg = abs(xy[1] + xy[3]) / 2
        self.desk.polygon(((xy[0], avg), (xy[2], xy[0]), (xy[2], xy[3])), fill=fill, outline=outline)

    def right_triangle(self, xy, fill=None, outline=None):
        avg = abs(xy[1] + xy[3]) / 2
        self.desk.polygon(((xy[2], avg), (xy[0], xy[1]), (xy[0], xy[3])), fill=fill, outline=outline)

    def __str__(self):
        self.image.show()
        return ''


a = ImageDrawer("RGB", (200, 200), (0, 0, 0))

a.left_triangle((10, 10, 90, 90), 'white', 'red')
a.left_triangle((110, 110, 190, 190), 'white', 'red')

a.right_triangle((10, 110, 90, 190), 'white', 'red')
a.right_triangle((110, 10, 190, 90), 'white', 'red')
print(a)
