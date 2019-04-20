from PIL import Image as img


def mirror():
    image = img.open("image.jpg")
    image = image.transpose(img.FLIP_LEFT_RIGHT)

    image.save("res.jpg")
