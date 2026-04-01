from PIL import Image

path = "images/car.png"
chars = "@%#&-=+_:.,$!*"
row = ""

with Image.open(path) as im:
    im = im.convert("L")
    width, height = im.size
    print(width, height)
    print(im.mode)
    new_width = 50
    new_height = int((height / width) * new_width * 0.5)
    im = im.resize((new_width, new_height))
    print(im.size)

for y in range(new_height):
    row = ""
    for x in range(new_width):
        pixel = im.getpixel((x, y))
        index = int(pixel * (len(chars) - 1) // 255)
        row += chars[index]
    print(row)
