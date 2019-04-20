from PIL import Image as im
import numpy as np


def bw_convert(inp="image.jpg", out="res.jpg"):
    image = np.asarray(im.open(inp))
    r, g, b = image[:, :, 0], image[:, :, 1], image[:, :, 2]

    im.fromarray(np.uint8(np.round(r * 0.2989) + np.round(g * 0.5870) + np.round(b * 0.1140))).save(out)
