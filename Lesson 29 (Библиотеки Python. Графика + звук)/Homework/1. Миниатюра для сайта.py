from PIL import Image as img


def make_preview(size, n_colors):
    pic = img.open("image.jpg")
    
    pic = pic.resize(size)
    pic = pic.quantize(n_colors)
    
    pic.save("res.bmp", "BMP")
    
