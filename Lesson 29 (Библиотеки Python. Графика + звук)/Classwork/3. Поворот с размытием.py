from PIL import Image as im
from PIL import ImageFilter as iF


def motion_blur(n):
    ret = im.open("image.jpg")
    ret = ret.transpose(im.ROTATE_270)
    ret = ret.filter(iF.GaussianBlur(n))
    
    ret.save("res.jpg")
    
