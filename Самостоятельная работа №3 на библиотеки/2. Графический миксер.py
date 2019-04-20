from PIL import Image as img


def twist_image(input_file_name, output_file_name):
    image = img.open(input_file_name)
    pixels = image.load()

    _i = image.size[0] - 1
    for i in range(image.size[0] // 2):
        _j = image.size[1] // 2 - 1
        for j in range(image.size[1] // 2, image.size[1]):
            pixels[i, j], pixels[_i, _j] = pixels[_i, _j], pixels[i, j]

            _j -= 1
        _i -= 1

    image.save(output_file_name)


lhs = img.open('ret.jpg').load()
size = img.open('need.jpg').size
rhs = img.open('need.jpg').load()


for i in range(size[0]):
    for j in range(size[1]):
        if lhs[i, j] != rhs[i, j]:
            print(lhs[i, j], rhs[i, j])
