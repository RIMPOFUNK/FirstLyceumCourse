from PIL import Image, ImageDraw


def gradient(color):
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))

    draw = ImageDraw.Draw(new_image)

    for i in range(512):
        if color.upper() == "R":
            draw.line((i, 0, i, 200), fill=(i // 2, 0, 0), width=2)
        elif color.upper() == "G":
            draw.line((i, 0, i, 200), fill=(0, i // 2, 0), width=2)
        else:
            draw.line((i, 0, i, 200), fill=(0, 0, i // 2), width=2)

    new_image.save("res.png", "PNG")

