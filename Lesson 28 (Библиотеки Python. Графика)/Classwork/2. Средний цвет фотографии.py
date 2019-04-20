from PIL import Image as img


pixels = img.open("image.jpg").load()
x, y = img.open("image.jpg").size

R = sum([sum([pixels[i, j][0] for i in range(x)]) for j in range(y)])
G = sum([sum([pixels[i, j][1] for i in range(x)]) for j in range(y)])
B = sum([sum([pixels[i, j][2] for i in range(x)]) for j in range(y)])

size = x * y
print(R // size, G // size, B // size)
